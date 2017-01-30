"""Measurement equation and associated functionality
"""

import sympy
from sympy.core.symbol import Symbol

import typhon.physics.metrology

names = ("R_e a_0 a_1 a_2 C_s R_selfIWCT C_IWCT C_E R_selfE R_selfs ε λ "
         "a_3 R_refl d_PRT C_PRT k n K N h c k_b T_PRT T_IWCT B φ "
         "R_IWCT ε O_Re O_TIWCT O_TPRT")

symbols = sym = dict(zip(names.split(), sympy.symbols(names)))

expressions = {}
expressions[sym["R_e"]] = (
    sym["a_0"] + sym["a_1"]*sym["C_E"] + sym["a_2"]*sym["C_E"]**2 - sym["R_selfE"] + sym["O_Re"])
expressions[sym["a_0"]] = (
    -sym["a_2"] * sym["C_s"]**2 - sym["a_1"]*sym["C_s"])
expressions[sym["a_1"]] = (
    sym["R_IWCT"] + sym["R_selfIWCT"] - sym["R_selfs"] -
    sym["a_2"]*(sym["C_IWCT"]**2-sym["C_s"]**2))/(sym["C_IWCT"]-sym["C_s"])
expressions[sym["R_IWCT"]] = (
    (sympy.Integral(((sym["ε"] + sym["a_3"]) * sym["B"] +
    (1+sym["ε"]-sym["a_3"])*sym["R_refl"]) * sym["φ"], sym["λ"])) /
    sympy.Integral(sym["φ"], sym["λ"]))
expressions[sym["B"]] = (
    (2*sym["h"]*sym["c"]**2)/(sym["λ"]**5) *
    1/(sympy.exp((sym["h"]*sym["c"])/(sym["λ"]*sym["k_b"]*sym["T_IWCT"]))-1))
expressions[sym["T_IWCT"]] = (
    sympy.Sum(sympy.IndexedBase(sym["T_PRT"])[sym["n"]], (sym["n"], 0, sym["N"]))/sym["N"] + sym["O_TIWCT"])
expressions[sympy.IndexedBase(sym["T_PRT"])[sym["n"]]] = (
    sympy.Sum(sympy.IndexedBase(sym["d_PRT"])[sym["n"],sym["k"]] *
        sympy.IndexedBase(sym["C_PRT"])[sym["n"]]**sym["k"], (sym["k"], 0, sym["K"]-1))
    + sym["O_TPRT"])
expressions[sym["φ"]] = (sympy.Function("φ")(sym["λ"]))

aliases = {}
aliases[sym["T_PRT"]] = sympy.IndexedBase(sym["T_PRT"])[sym["n"]]
aliases[sym["C_PRT"]] = sympy.IndexedBase(sym["C_PRT"])[sym["n"]]
aliases[sym["d_PRT"]] = sympy.IndexedBase(sym["d_PRT"])[sym["n"],sym["k"]]

functions = {}
for (sn, s) in symbols.items():
    if s in expressions.keys():
        e = expressions[s]
        functions[s] = sympy.Function(sn)(*(aliases.get(sm, sm) for sm in e.free_symbols))

def recursive_substitution(e, stop_at=None, return_intermediates=False):
    """For expression 'e', substitute all the way down.

    Using the dictionary `expressions`, repeatedly substitute all symbols
    into the expression until there is nothing left to substitute.
    """
    o = None
    intermediates = set()
    while o != e:
        o = e
        for sym in typhon.physics.metrology.recursive_args(e):
            if sym != stop_at:
                # subs only works for simple values but is faster
                # replace works for arbitrarily complex expressions but is
                # slower and may yield false positives
                # see http://stackoverflow.com/a/41808652/974555
                e = getattr(e, ("replace" if isinstance(sym, sympy.Indexed) else "subs"))(
                    sym, expressions.get(sym, sym))
                if sym in expressions:
                    intermediates.add(sym)
    return (e, intermediates) if return_intermediates else e
#
#dependencies = {aliases.get(e, e):
#                typhon.physics.metrology.recursive_args(
#                    recursive_substitution(
#                        expressions.get(
#                            aliases.get(e,e),
#                            e)))
#        for e in symbols.values()}

dependencies = {}
for s in symbols.values():
    (e, im) = recursive_substitution(
                expressions.get(aliases.get(s,s),s),
                return_intermediates=True)
    dependencies[aliases.get(s, s)] = typhon.physics.metrology.recursive_args(e) | im

def calc_sensitivity_coefficient(s1, s2):
    """Calculate sensitivity coefficient ∂s1/∂s2

    Arguments:

        s1: Symbol
        s2: Symbol
    """

    if not isinstance(s1, Symbol):
        s1 = symbols[s1]
    if not isinstance(s2, Symbol):
        s2 = symbols[s2]

    if s1 == s2:
        expr = s1
    else:
        expr = expressions[aliases.get(s1, s1)]
    oldexpr = None
    # expand expression until no more sub-expressions and s2 is explicit
    while expr != oldexpr:
        oldexpr = expr
        for sym in expr.free_symbols - {s2}:
            if aliases.get(s2, s2) in dependencies[aliases.get(sym,sym)]:
                here = aliases.get(sym, sym)
                expr = getattr(expr, ("replace" if sym in aliases else
                    "subs"))(here, expressions.get(here, here))
    return expr.diff(aliases.get(s2,s2))