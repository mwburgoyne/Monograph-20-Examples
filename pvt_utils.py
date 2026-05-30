"""
pvt_utils.py -- shared helpers for the Monograph 20 worked examples.

This module pulls together the bits of code that were previously copy-pasted
across the notebooks:

    * the component property library (Tables A-1A / 4.3),
    * the Hall-Yarborough Z-factor,
    * Wilson (and modified Wilson) K-value correlations,
    * the Peng-Robinson EOS primitives,
    * a robust Rachford-Rice solver (Nielsen & Lia, 2022), and
    * a two-phase PR flash with a Michelsen stability test.

It is deliberately written to be *read*, not to be production grade.  Every
function takes what it needs as arguments (no hidden globals), so the notebooks
can import a piece and see exactly what goes in and out.

Oilfield units throughout (psia, degR, ft3, lbm-mol).
"""

import math
import numpy as np
from scipy.optimize import fsolve

R = 10.73146           # universal gas constant, psia-ft3 / (degR * lbm-mol)
SQRT2 = math.sqrt(2.0)


# ---------------------------------------------------------------------------
# Component library
# ---------------------------------------------------------------------------
class Component:
    """A single component and its pure-component EOS properties.

    ``bip`` holds the binary interaction parameters of this component against
    [N2, CO2, H2S, C1] respectively; all other pairs default to zero.  ``s`` is
    the dimensionless Peneloux volume-shift (c / b).
    """

    def __init__(self, name, M, gamma, rhosc, Pc, Tc, vc, w, tb, L, H, s, bip):
        self.name = name      # component name
        self.M = M            # molecular weight
        self.gamma = gamma    # specific gravity
        self.rhosc = rhosc    # liquid density at standard conditions, lbm/ft3
        self.Pc = Pc          # critical pressure, psia
        self.Tc = Tc          # critical temperature, degR
        self.vc = vc          # critical volume, ft3/lbm-mol
        self.w = w            # acentric factor
        self.tb = tb          # normal boiling point, degR
        self.L = L            # net heating value placeholder
        self.H = H            # gross heating value, Btu/scf
        self.s = s            # Peneloux volume-shift parameter (c/b)
        self.bip = bip        # [k_N2, k_CO2, k_H2S, k_C1]

    def zc(self):
        """Critical compressibility factor."""
        return self.Pc * self.vc / (R * self.Tc)

    def __repr__(self):
        return f"Component({self.name})"


# From Tables A-1A, 4.3 & A-3 (oilfield units).  bip = [N2, CO2, H2S, C1].
_LIBRARY = [
    Component('N2',  28.02, 1.026,  29.31,  493.0,  227.3, 1.443, 0.0450, 139.3, 0,    0,     -0.1927, [0,     0,     0,    0]),
    Component('CO2', 44.01, 1.101,  31.18, 1070.6,  547.6, 1.505, 0.2310, 350.4, 0,    0,     -0.0817, [0,     0,     0,    0]),
    Component('H2S', 34.08, 1.1895, 31.18, 1306.0,  672.4, 1.564, 0.1000, 383.1, 0,    672.0, -0.1288, [0.13,  0.135, 0,    0]),
    Component('C1',  16.04, 0.415,  20.58,  667.8,  343.0, 1.590, 0.0115, 201.0, 0,    1012.0, -0.1595, [0.025, 0.105, 0.07, 0]),
    Component('C2',  30.07, 0.546,  28.06,  707.8,  549.8, 2.370, 0.0908, 332.2, 0,    1783.0, -0.1134, [0.01,  0.13,  0.085, 0]),
    Component('C3',  44.09, 0.585,  31.66,  616.3,  665.7, 3.250, 0.1454, 416.0, 27.4, 2557.0, -0.0863, [0.09,  0.125, 0.08, 0]),
    Component('iC4', 58.12, 0.60,   35.01,  529.1,  734.7, 4.208, 0.1756, 470.6, 32.7, 3354.0, -0.0844, [0.095, 0.12,  0.075, 0]),
    Component('nC4', 58.12, 0.60,   36.45,  550.7,  765.3, 4.080, 0.1928, 490.8, 31.4, 3369.0, -0.0675, [0.095, 0.115, 0.075, 0]),
    Component('iC5', 72.15, 0.621,  39.13,  490.4,  828.8, 4.899, 0.2273, 541.8, 36.3, 4001.0, -0.0608, [0.1,   0.115, 0.07, 0]),
    Component('nC5', 72.15, 0.630,  39.30,  488.6,  845.4, 4.870, 0.2510, 556.6, 36.2, 4009.0, -0.0390, [0.11,  0.115, 0.07, 0]),
    Component('C6',  86.17, 0.664,  41.19,  436.9,  913.4, 5.929, 0.2957, 615.4, 41.2, 4756.0, -0.0080, [0.11,  0.115, 0.055, 0]),
    Component('C7',  100.2, 0.688,  42.58,  396.8,  972.5, 6.924, 0.3506, 668.8, 46.3, 5503.0,  0.0033, [0.11,  0.115, 0.05, 0]),
    Component('C8',  114.2, 0.703,  44.19,  360.6, 1023.9, 7.882, 0.3978, 717.9, 50.9, 6250.0,  0.0314, [0.11,  0.115, 0.048, 0]),
    Component('C9',  128.3, 0.718,  45.35,  332.0, 1070.3, 8.773, 0.4437, 763.1, 55.7, 6996.0,  0.0408, [0.11,  0.115, 0.046, 0]),
    Component('C10', 142.29, 0.73,  45.68,  304.0, 1111.8, 9.661, 0.4902, 805.2, 61.4, 7743.0,  0.0655, [0.11,  0.115, 0.045, 0]),
    Component('Air', 28.97, 1.0,    29.31,  547.0,  239.0, 1.364, 0.0400, 141.9, 0,    0,     -0.45037, [0,     0,     0,    0]),
    Component('H2O', 18.02, 1.00,   62.37, 3206.0, 1165.0, 0.916, 0.3440, 671.6, 0,    0,      0,       [0,     0,     0,    0]),
    Component('O2',  32.0,  0.50,   31.18,  732.0,  278.0, 1.174, 0.0250, 162.2, 0,    0,      0,       [0,     0,     0,    0]),
]

# Look up components by name, e.g. COMP_LIB['C1']
COMP_LIB = {c.name: c for c in _LIBRARY}


def get_components(names):
    """Return a list of Component objects for the given names, in order."""
    return [COMP_LIB[n] for n in names]


def build_bips(comps):
    """Build the lower-triangular binary-interaction-parameter matrix.

    Only pairs involving N2, CO2, H2S or C1 are non-zero; each component carries
    those four values in ``comp.bip``.
    """
    inorganic_col = {'N2': 0, 'CO2': 1, 'H2S': 2, 'C1': 3}
    bip_list = []
    for i, row_comp in enumerate(comps):
        row = []
        for j, col_comp in enumerate(comps):
            if j > i:                      # lower-triangular only
                continue
            col = inorganic_col.get(col_comp.name)
            row.append(row_comp.bip[col] if col is not None else 0.0)
        bip_list.append(row)
    return bip_list


def _bip(bip_list, i, j):
    """Symmetric access into the ragged lower-triangular bip matrix."""
    return bip_list[i][j] if i >= j else bip_list[j][i]


# ---------------------------------------------------------------------------
# Hall-Yarborough Z-factor (Section 3.3.2)
# ---------------------------------------------------------------------------
def zfactor(Tpr, Ppr):
    """Gas Z-factor from the Hall-Yarborough correlation."""
    t = 1.0 / Tpr
    alpha = 0.06125 * t * math.exp(-1.2 * (1 - t) ** 2)

    def fy(y):
        return (-alpha * Ppr
                + (y + y ** 2 + y ** 3 - y ** 4) / (1 - y) ** 3
                - (14.76 * t - 9.76 * t ** 2 + 4.58 * t ** 3) * y ** 2
                + (90.7 * t - 242.2 * t ** 2 + 42.4 * t ** 3) * y ** (2.18 + 2.82 * t))

    y = fsolve(fy, 0.001)[0]
    return alpha * Ppr / y


# ---------------------------------------------------------------------------
# K-value correlations
# ---------------------------------------------------------------------------
def k_wilson(comps, t, p):
    """Wilson K-value estimate (Eq 4.42).  t in degR, p in psia."""
    return [math.exp(5.37 * (1 + c.w) * (1 - 1 / (t / c.Tc))) / (p / c.Pc)
            for c in comps]


def k_modified_wilson(w, tc, pc, t, p, pk, A2):
    """Modified Wilson K-value with convergence pressure (Eqs 3.159-3.160).

    t in degR, pressures in psia, pk = convergence pressure.
    """
    A1 = 1 - ((p - 14.7) / (pk - 14.7)) ** A2
    return (pc / pk) ** (A1 - 1) * math.exp(5.37 * A1 * (1 + w) * (1 - 1 / (t / tc))) / (p / pc)


# ---------------------------------------------------------------------------
# Peng-Robinson EOS primitives
# ---------------------------------------------------------------------------
def pr_a(w, Tc, Pc, t):
    """PR attraction parameter a(T) for one component (Eqs 4.20-4.22)."""
    if w <= 0.49:
        m = 0.37464 + 1.54226 * w - 0.26992 * w ** 2          # Eq 4.21
    else:
        m = 0.3796 + 1.485 * w - 0.1644 * w ** 2 + 0.01667 * w ** 3   # Eq 4.22
    alpha = (1 + m * (1 - (t / Tc) ** 0.5)) ** 2
    return 0.45724 * R ** 2 * Tc ** 2 * alpha / Pc


def pr_b(Tc, Pc):
    """PR co-volume parameter b for one component."""
    return 0.07780 * R * Tc / Pc


def aij_matrix(ai, bips):
    """Cross attraction terms a_ij = sqrt(a_i a_j)(1 - k_ij).

    These depend only on temperature (through a_i) and the BIPs, *not* on
    composition, so they are computed once per flash rather than every
    iteration.
    """
    n = len(ai)
    return [[(ai[i] * ai[j]) ** 0.5 * (1 - _bip(bips, i, j)) for j in range(n)]
            for i in range(n)]


def mix_ab(frac, aij, bi):
    """Mixture a and b from composition (van der Waals mixing rules)."""
    n = len(frac)
    a_mix = sum(frac[i] * frac[j] * aij[i][j] for i in range(n) for j in range(n))
    b_mix = sum(frac[i] * bi[i] for i in range(n))
    return a_mix, b_mix


def z_roots(a_mix, b_mix, p, t):
    """Real roots of the PR cubic in Z, with the (unphysical) middle root
    dropped when three real roots exist (Eq 4.19)."""
    A = a_mix * p / (R * t) ** 2
    B = b_mix * p / (R * t)
    coeffs = [1.0, B - 1.0, A - 3 * B ** 2 - 2 * B, -(A * B - B ** 2 - B ** 3)]
    roots = [r.real for r in np.roots(coeffs) if abs(r.imag) < 1e-12]
    roots.sort()
    if len(roots) == 3:
        roots.pop(1)
    return roots


def _ln_phi(i, Z, frac, a_mix, b_mix, aij, bi, p, t):
    """ln of the fugacity coefficient of component i (corrected Eq 4.23).

    Note the monograph misprints the last log argument; the denominator should
    be Z - (sqrt(2) - 1) B, as used here.
    """
    A = a_mix * p / (R * t) ** 2
    B = b_mix * p / (R * t)
    sum_aij = sum(frac[j] * aij[i][j] for j in range(len(frac)))
    c1 = (bi[i] / b_mix) * (Z - 1) - math.log(Z - B)
    c2 = (A / (2 * SQRT2 * B)) * (bi[i] / b_mix - 2 * sum_aij / a_mix)
    c3 = math.log((Z + (1 + SQRT2) * B) / (Z - (SQRT2 - 1) * B))
    return c1 + c2 * c3


def fugacities(frac, a_mix, b_mix, aij, bi, p, t):
    """Component fugacities for the phase, choosing the Z-root with the lowest
    normalised Gibbs energy.  Returns (fugacity_list, Z)."""
    n = len(frac)
    best = None
    for Z in z_roots(a_mix, b_mix, p, t):
        f = [math.exp(_ln_phi(i, Z, frac, a_mix, b_mix, aij, bi, p, t)) * frac[i] * p
             for i in range(n)]
        gibbs = sum(frac[i] * math.log(f[i]) for i in range(n))
        if best is None or gibbs < best[0]:
            best = (gibbs, f, Z)
    return best[1], best[2]


# ---------------------------------------------------------------------------
# Rachford-Rice -- robust solver of Nielsen & Lia (2022)
# ---------------------------------------------------------------------------
def rr_solver(zi, ki, tol=1e-15, max_iter=100):
    """Solve Rachford-Rice with the transformed-variable method of Nielsen &
    Lia (2022), Fluid Phase Equilibria, which avoids the catastrophic roundoff
    of the naive form.  Mirrors the implementation in pyResToolbox.

    Returns (n_iter, yi, xi, V, L).
    """
    zi = np.asarray(zi, dtype=float)
    ki = np.asarray(ki, dtype=float)
    zi = zi / zi.sum()
    # Perturb K's exactly equal to 1 to avoid the c_i = 1/(1-K) singularity.
    ki = np.where(np.abs(ki - 1.0) < 1e-12, 1.0 + 1e-12, ki)

    def rr(V):
        return np.dot(zi, (ki - 1) / (1 + V * (ki - 1)))

    near_vapor = rr(0.5) > 0
    ki_hat = 1.0 / ki if near_vapor else ki.copy()
    ci = 1.0 / (1.0 - ki_hat)                          # Eq 10

    phi_max = min(1.0 / (1.0 - ki_hat.min()), 0.5)     # Eq 11a
    phi_min = 1.0 / (1.0 - ki_hat.max())               # Eq 11b
    b_min = 1.0 / (phi_max - phi_min)                  # Eq 15
    b_max = np.inf
    b = 1.0 / (0.25 - phi_min)

    def h(b):
        return np.sum(zi * b / (1.0 + b * (phi_min - ci)))        # Eq 12b

    def dh(b):
        return np.sum(zi / (1.0 + b * (phi_min - ci)) ** 2)       # Eq 16b

    n_it, h_b = 0, np.inf
    while abs(h_b) > tol:
        n_it += 1
        h_b, dh_b = h(b), dh(b)
        if h_b > 0:
            b_max = b
        else:
            b_min = b
        b = b - h_b / dh_b
        if b < b_min or b > b_max:
            b = 0.5 * (b_min + b_max)
        if n_it > max_iter:
            break

    ui = -zi * ci * b / (1.0 + b * (phi_min - ci))     # Eq 27b
    phi = (1.0 + b * phi_min) / b                      # rearranged Eq 14b
    if near_vapor:
        L, V = phi, 1.0 - phi
        yi, xi = ui, ki_hat * ui
    else:
        V, L = phi, 1.0 - phi
        xi, yi = ui, ki_hat * ui
    return n_it, yi, xi, V, L


def solve_rachford_rice(z, K):
    """Flash-friendly wrapper: detect single-phase feeds, otherwise call the
    robust solver.  Returns (V, x, y) as plain lists."""
    z = np.asarray(z, dtype=float)
    K = np.asarray(K, dtype=float)
    z = z / z.sum()
    Km1 = K - 1.0

    if np.sum(z * Km1) <= 0:                    # all liquid
        return 0.0, [float(v) for v in z], [float(v) for v in (K * z) / np.sum(K * z)]
    if np.sum(z * Km1 / K) >= 0:                # all vapour
        return 1.0, [float(v) for v in (z / K) / np.sum(z / K)], [float(v) for v in z]

    _, yi, xi, V, _ = rr_solver(z, K)
    return float(V), [float(v) for v in xi], [float(v) for v in yi]


# ---------------------------------------------------------------------------
# Two-phase PR flash
# ---------------------------------------------------------------------------
class FlashResult:
    """Container for flash outputs (attribute access for readability)."""

    def __init__(self, Fv, x, y, K, fl, fv, Zl, Zv, iterations, single_phase):
        self.Fv = Fv                  # vapour mole fraction
        self.x = x                    # liquid composition
        self.y = y                    # vapour composition
        self.K = K                    # converged K-values
        self.fl = fl                  # liquid fugacities
        self.fv = fv                  # vapour fugacities
        self.Zl = Zl                  # liquid Z-factor
        self.Zv = Zv                  # vapour Z-factor
        self.iterations = iterations
        self.single_phase = single_phase


def flash(comps, z, p, t, bips=None, K=None, tol=1e-12, maxiter=200):
    """Isothermal two-phase Peng-Robinson flash by successive substitution
    with periodic GDEM acceleration (Eq 4.72).

    Returns a FlashResult.  ``single_phase`` is True when the feed flashes to a
    single phase at (p, t).
    """
    n = len(comps)
    if bips is None:
        bips = build_bips(comps)
    if K is None:
        K = k_wilson(comps, t, p)
    K = list(K)

    ai = [pr_a(c.w, c.Tc, c.Pc, t) for c in comps]
    bi = [pr_b(c.Tc, c.Pc) for c in comps]
    aij = aij_matrix(ai, bips)        # composition-independent -> compute once

    Rr_prev = None
    Fv, x, y = z, list(z), list(z)
    fl = fv = [float('nan')] * n
    Zl = Zv = float('nan')

    for it in range(1, maxiter + 1):
        Fv, x, y = solve_rachford_rice(z, K)

        a_l, b_l = mix_ab(x, aij, bi)
        a_v, b_v = mix_ab(y, aij, bi)
        fl, Zl = fugacities(x, a_l, b_l, aij, bi, p, t)
        fv, Zv = fugacities(y, a_v, b_v, aij, bi, p, t)

        Rr = [fl[i] / fv[i] for i in range(n)]
        err = sum((r - 1.0) ** 2 for r in Rr)
        if err < tol or Fv <= 0.0 or Fv >= 1.0:
            break

        lam = 1.0
        if it % 4 == 0 and Rr_prev is not None:        # GDEM acceleration
            b11 = sum(math.log(Rr_prev[i]) ** 2 for i in range(n))
            b01 = sum(math.log(Rr_prev[i]) * math.log(Rr[i]) for i in range(n))
            if b11 - b01 != 0:
                lam = abs(b11 / (b11 - b01))
        Rr_prev = Rr
        K = [K[i] * Rr[i] ** lam for i in range(n)]

    single_phase = Fv <= 0.0 or Fv >= 1.0
    return FlashResult(Fv, x, y, K, fl, fv, Zl, Zv, it, single_phase)


# ---------------------------------------------------------------------------
# Michelsen phase-stability test
# ---------------------------------------------------------------------------
def _trial_phase(comps, z, p, t, bi, aij, fz, kind, conv_lim=1e-10,
                 triv_lim=1e-4, max_iter=100):
    """Grow one incipient phase ('v' vapour-like or 'l' liquid-like) and return
    its tangent-plane sum S and whether it collapsed to the trivial solution."""
    n = len(z)
    K = k_wilson(comps, t, p)
    S, triv_err = 1.0, 1.0
    for _ in range(max_iter):
        if kind == 'v':
            Yi = [z[i] * K[i] for i in range(n)]
        else:
            Yi = [z[i] / K[i] for i in range(n)]
        S = sum(Yi)
        y = [Yi[i] / S for i in range(n)]

        a_mix, b_mix = mix_ab(y, aij, bi)
        fy, _ = fugacities(y, a_mix, b_mix, aij, bi, p, t)

        if kind == 'v':
            Ri = [fz[i] / fy[i] / S for i in range(n)]
        else:
            Ri = [fy[i] / fz[i] * S for i in range(n)]
        K = [K[i] * Ri[i] for i in range(n)]

        conv_err = sum((Ri[i] - 1.0) ** 2 for i in range(n))
        triv_err = sum(math.log(K[i]) ** 2 for i in range(n))
        if conv_err < conv_lim or triv_err < triv_lim:
            break
    return S, y, K, triv_err


class StabilityResult:
    def __init__(self, stable, Sv, Sl, K_init):
        self.stable = stable          # True if the feed is single-phase stable
        self.Sv = Sv                  # vapour-like trial tangent-plane sum
        self.Sl = Sl                  # liquid-like trial tangent-plane sum
        self.K_init = K_init          # K-value guess (yv/yl) to seed a flash


def stability_test(comps, z, p, t, bips=None, tol=1e-4):
    """Michelsen two-sided stability test.

    The feed is unstable (will split) when either trial phase grows to a
    tangent-plane sum S > 1.  Returns a StabilityResult.
    """
    n = len(comps)
    if bips is None:
        bips = build_bips(comps)
    ai = [pr_a(c.w, c.Tc, c.Pc, t) for c in comps]
    bi = [pr_b(c.Tc, c.Pc) for c in comps]
    aij = aij_matrix(ai, bips)

    a_z, b_z = mix_ab(z, aij, bi)
    fz, _ = fugacities(z, a_z, b_z, aij, bi, p, t)

    Sv, yv, _, _ = _trial_phase(comps, z, p, t, bi, aij, fz, 'v')
    Sl, yl, _, _ = _trial_phase(comps, z, p, t, bi, aij, fz, 'l')

    stable = (Sv <= 1.0 + tol) and (Sl <= 1.0 + tol)
    K_init = [yv[i] / yl[i] for i in range(n)]
    return StabilityResult(stable, Sv, Sl, K_init)


# ---------------------------------------------------------------------------
# Self-test: reproduce the published answers from Problem 18 and Appendix C.
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    print("Problem 18 -- ternary C1 / nC4 / C10")
    comps = get_components(['C1', 'nC4', 'C10'])
    z = [0.5, 0.42, 0.08]

    # (a) flash at 500 psia, 280 degF
    res = flash(comps, z, 500, 280 + 460)
    Ml = sum(res.x[i] * comps[i].M for i in range(3))
    Mv = sum(res.y[i] * comps[i].M for i in range(3))
    print(f"  500 psia : Fv={res.Fv:.5f}  Ml={Ml:.2f} (expect ~92.51)  "
          f"Mv={Mv:.2f} (expect ~35.48)")

    # (b) stability + flash at 1500 psia, 280 degF
    st = stability_test(comps, z, 1500, 280 + 460)
    print(f"  1500 psia: Sv={st.Sv:.4f} (expect ~1.0116)  "
          f"Sl={st.Sl:.4f} (expect ~1.0169)  stable={st.stable}")
    res2 = flash(comps, z, 1500, 280 + 460, K=st.K_init)
    print(f"  1500 psia: K={[round(k, 5) for k in res2.K]} "
          f"(expect ~[1.90759, 0.68022, 0.13752])")
    print("\n(Appendix C's full gas-condensate dew-point check, including the "
          "C7+ pseudo-components, lives in that notebook.)")
