"""Plotting the health of harmonisation matchups
"""

import argparse
from .. import common
def parse_cmdline():
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser = common.add_to_argparse(parser,
        include_period=False,
        include_sat=0,
        include_channels=False,
        include_temperatures=False)

    parser.add_argument("file",
        action="store",
        type=str,
        help="Path to file containing enhanced matchups")

    return parser.parse_args()
p = parse_cmdline()

import logging
logging.basicConfig(
    format=("%(levelname)-8s %(asctime)s %(module)s.%(funcName)s:"
            "%(lineno)s: %(message)s"),
    filename=p.log,
    level=logging.DEBUG if p.verbose else logging.INFO)

import sys
import pathlib

import numpy
import matplotlib.pyplot
import xarray
import scipy.stats

import pyatmlab.graphics

from typhon.physics.units.tools import UnitsAwareDataArray as UADA
from typhon.physics.units.common import radiance_units as rad_u
import typhon.physics.units.em

from .. import matchups
from .. import fcdr

def plot_ds_summary_stats(ds, lab="", Ldb=None):
    """Plot single file with summary stats for specific label

    Label can me empty, then it plots the standard, or it can contain a
    string corresponding to what is generated by
    combine_hirs_hirs_matchups run with the --debug option, such as
    'neighbours_delta_cm·mW m^-2 sr^-1'
    """

    if lab:
        # extra cruft added to string by combine_hirs_hirs_matchups
        lab = f"other_{lab:s}_"
    
    (f, ax_all) = matplotlib.pyplot.subplots(2, 4, figsize=(25, 10))

    g = ax_all.flat

    cbs = []
    
    chan = ds["channel"].item()
    # for unit conversions
    srf1 = typhon.physics.units.em.SRF.fromArtsXML(
            typhon.datasets.tovs.norm_tovs_name(ds.sensor_1_name).upper(),
            "hirs", ds["channel"].item())
    srf2 = typhon.physics.units.em.SRF.fromArtsXML(
            typhon.datasets.tovs.norm_tovs_name(ds.sensor_2_name).upper(),
            "hirs", ds["channel"].item())

    y1 = UADA(ds["nominal_measurand1"]).to(
            ds[f"K_{lab:s}forward"].units, "radiance", srf=srf1)
    y2 = UADA(ds["nominal_measurand2"]).to(
            ds[f"K_{lab:s}forward"].units, "radiance", srf=srf2)
    yb = [y1, y2]

    kxrange = scipy.stats.scoreatpercentile(ds[f"K_{lab:s}forward"], [1, 99])
    kyrange = scipy.stats.scoreatpercentile(ds[f"K_{lab:s}backward"], [1, 99])
    kΔrange = scipy.stats.scoreatpercentile(ds[f"K_{lab:s}forward"]+ds[f"K_{lab:s}backward"], [1, 99])
    Lxrange = scipy.stats.scoreatpercentile(y1, [1, 99])
    Lyrange = scipy.stats.scoreatpercentile(y2, [1, 99])
    Lmax = max(Lxrange[1], Lyrange[1])
    Lmin = min(Lxrange[0], Lyrange[0])
    LΔrange = scipy.stats.scoreatpercentile(
        y2 - y1,
        [1, 99])

    # radiance comparison
    a = next(g)
    pc = a.hexbin(
        y1,
        y2,
        extent=(Lmin, Lmax, Lmin, Lmax),
        mincnt=1)
    a.plot([Lmin, Lmax], [Lmin, Lmax], 'k--')
    a.set_xlabel("Radiance {sensor_1_name:s}".format(**ds.attrs)
        + f"[{y1.units:s}]")
    a.set_ylabel("Radiance {sensor_2_name:s}".format(**ds.attrs)
        + f"[{y2.units:s}]")
    a.set_title("Radiance comparison")
    a.set_xlim(Lmin, Lmax)
    a.set_ylim(Lmin, Lmax)
    cbs.append(f.colorbar(pc, ax=a))

    # histograms for real and simulated measurements
    a = next(g)
    sensor_names = [ds.sensor_1_name, ds.sensor_2_name]
    for i in range(2):
        (cnts, bins, patches) = a.hist(
            yb[i],
            label=f"{sensor_names[i]:s} (measured)",
            histtype="step",
            range=(Lmin, Lmax),
            density=True,
            stacked=False,
            bins=100)
    for nm in Ldb.data_vars.keys():
        (cnts, bins, patches) = a.hist(
            Ldb[nm].sel(chan=chan),
            label=f"{nm:s} (IASI-simulated)",
            histtype="step",
            range=(Lmin, Lmax),
            density=True,
            stacked=False,
            bins=100)
    a.legend()
    a.set_xlabel("Radiance " + f"[{y1.units:s}]")
    a.set_ylabel("Density per bin")
    a.set_title("Histograms of radiances")

    # K forward vs. K backward
    a = next(g)
    pc = a.hexbin(
        ds[f"K_{lab:s}forward"],
        ds[f"K_{lab:s}backward"],
       extent=numpy.concatenate([kxrange, kyrange]),
       mincnt=1)
    a.plot(kxrange, -kxrange, 'k--')
    a.set_xlabel("K forward\n[{units:s}]".format(**ds[f"K_{lab:s}forward"].attrs))  
    a.set_ylabel("K backward\n[{units:s}]".format(**ds[f"K_{lab:s}backward"].attrs))  
    a.set_title("Estimating K forward or backward, comparison")
    a.set_xlim(kxrange)
    a.set_ylim(kyrange)
    cbs.append(f.colorbar(pc, ax=a))

    # histogram of K forward / backward differences
    a = next(g)
    (cnts, bins, patches) = a.hist(
        ds[f"K_{lab:s}forward"]+ds[f"K_{lab:s}backward"],
        histtype="step",
        bins=100,
        range=kΔrange)
    a.plot([0, 0], [0, cnts.max()], 'k--')
    a.set_xlabel("Sum of K estimates [{units:s}]".format(**ds[f"K_{lab:s}forward"].attrs))
    a.set_ylabel("No. matchups in bin")
    a.set_title("Distribution of sum of K estimates")
    a.set_xlim(kΔrange)

    # Ks vs. Kforward
    a = next(g)
    pc = a.hexbin(
        ds[f"K_{lab:s}forward"],
        ds[f"K_{lab:s}forward"]+ds[f"K_{lab:s}backward"],
        extent=numpy.concatenate([kxrange, kΔrange]),
        mincnt=1)
    a.plot(kxrange, [0, 0], 'k--')
    a.set_xlabel("K forward\n[{units:s}]".format(**ds[f"K_{lab:s}forward"].attrs))  
    a.set_ylabel("Sum of K estimates [{units:s}]".format(**ds[f"K_{lab:s}forward"].attrs))
    a.set_title("K difference vs. K forward")
    a.set_xlim(kxrange)
    a.set_ylim(kΔrange)
    cbs.append(f.colorbar(pc, ax=a))

    # K vs. radiance
    a = next(g)
    pc = a.hexbin(y1,
        ds[f"K_{lab:s}forward"],
        extent=numpy.concatenate([Lxrange, kxrange]),
        mincnt=1)
    a.set_xlabel("Radiance {sensor_1_name:s}".format(**ds.attrs)
        + f"[{y1.units:s}]")
    a.set_ylabel("K forward\n[{units:s}]".format(**ds[f"K_{lab:s}forward"].attrs))  
    a.set_title("K vs. measurement")
    a.set_xlim(Lxrange)
    a.set_ylim(kxrange)
    cbs.append(f.colorbar(pc, ax=a))

    # K vs. ΔL
    a = next(g)
    extremes = [min([LΔrange[0], kxrange[0]]), max([LΔrange[1], kxrange[1]])]
    pc = a.hexbin(y2-y1,
        ds[f"K_{lab:s}forward"],
        extent=numpy.concatenate([LΔrange, kxrange]),
        mincnt=1)
    a.plot(extremes, extremes, 'k--')
    a.set_xlabel("Radiance {sensor_2_name:s} - {sensor_1_name:s}".format(**ds.attrs)
        + f"[{y1.units:s}]")
    a.set_ylabel("K forward\n[{units:s}]".format(**ds[f"K_{lab:s}forward"].attrs))  
    a.set_title("K vs. measurement difference")
    a.set_xlim(LΔrange)
    a.set_ylim(kxrange)
    cbs.append(f.colorbar(pc, ax=a))

    # K - ΔL vs. radiance
    a = next(g)
    pc = a.hexbin(y1,
        ds[f"K_{lab:s}forward"] - (y2-y1),
        extent=numpy.concatenate([[Lmin, Lmax], kxrange-LΔrange]),
        mincnt=1)
    a.plot([0, Lmax], [0, 0], 'k--')
    a.set_xlabel("Radiance {sensor_1_name:s}".format(**ds.attrs)
        + f"[{y1.units:s}]")
    a.set_ylabel(f"K - ΔL [{y1.units:s}]".format(**ds.attrs))
    a.set_xlim(Lmin, Lmax)
    a.set_ylim(kxrange-LΔrange)
    a.set_title('K "wrongness" per radiance')
    cbs.append(f.colorbar(pc, ax=a))

    for cb in cbs:
        cb.set_label("No. matchups in bin")

    for a in ax_all.flat:
        a.grid(axis="both")

    f.suptitle("K stats for pair {sensor_1_name:s}, {sensor_2_name:s}, {time_coverage:s}".format(**ds.attrs)
        + ", channel " + str(ds["channel"].item()) + "\nchannels used to predict: " +
        ", ".join(str(c) for c in numpy.atleast_1d(ds[f"K_{lab:s}forward"].attrs["channels_prediction"])))
    f.subplots_adjust(hspace=0.35, wspace=0.3)

    pyatmlab.graphics.print_or_show(f, False,
        "harmstats/{sensor_1_name:s}_{sensor_2_name:s}/ch{channel:d}/harmonisation_K_stats_{sensor_1_name:s}-{sensor_2_name:s}_ch{channel:d}_{time_coverage:s}_{lab:s}.".format(
            channel=ds["channel"].item(), lab=lab, **ds.attrs))
    
def plot_file_summary_stats(path):
    """Plot various summary statistics for harmonisation file

    Assumes it contains the extra fields that I generate for HIRS using
    combine_hirs_hirs_matchups.
    """

    # TODO:
    #   - get extent from data percentiles
    #   - get axes labels from data-array attributes

    ds = xarray.open_dataset(path)

    # one subplot needs IASI simulations, which I will obtain from kmodel
    kmodel = matchups.KModelSRFIASIDB(
        chan_pairs="single", # not relevant, only using iasi db
        mode="standard", # idem
        units=rad_u["si"],
        debug=True, # will have one of each, makes difference for units
        prim_name=ds.attrs["sensor_1_name"],
        prim_hirs=fcdr.which_hirs_fcdr(ds.attrs["sensor_1_name"], read="L1C"),
        sec_name=ds.attrs["sensor_2_name"],
        sec_hirs=fcdr.which_hirs_fcdr(ds.attrs["sensor_2_name"], read="L1C"))
    kmodel.init_Ldb()

    others = [k.replace("K_other_", "").replace("_forward", "")
            for k in ds.data_vars.keys()
            if k.startswith("K_other_") and k.endswith("_forward")]
    if others:
        for lab in others:
            plot_ds_summary_stats(ds, lab, kmodel.others[lab].Ldb_hirs_simul)
    else:
        plot_ds_summary_stats(ds, kmodel.Ldb_hirs_simul)


def main():
    plot_file_summary_stats(pathlib.Path(p.file))
