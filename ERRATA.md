# Errata - SPE Monograph 20, *Phase Behavior* (Whitson & Brule, 2000)

Corrections to the **First Printing** (Henry L. Doherty Memorial Fund of AIME / SPE, Richardson, Texas, 2000). Every numbered equation, table, worked-example number, figure caption and cross-reference in Chapters 1 to 9 and Appendices A to D was audited: equations against their canonical published forms and for dimensional consistency, worked examples by reproducing the arithmetic from the stated inputs, and tables for internal consistency. Only errors that survived an independent adversarial re-check are listed here. **34 confirmed errors**: 3 high, 15 medium, 16 low.

Page references give the printed book page first and the PDF page in parentheses (PDF page = book page + 7). Equations are written in plain ASCII/Unicode; "Book prints" transcribes the source verbatim, "Correction" gives the intended form.

## The three that matter most

If you carry only three corrections forward, carry these; each changes a computed result, not just a label.

1. **Eq. 4.23 (Ch 4, p.50)** - the Peng-Robinson fugacity-coefficient log argument has a sign error in the denominator: printed `Z - (1-√2)B`, should be `Z + (1-√2)B`. Affects both the pure-component and mixture forms.
2. **Eq. 9.18 (Ch 9, p.147)** - the brine formation-volume-factor exponent is the wrong sign; as printed, brine FVF increases with pressure.
3. **Table C-7 (App C, p.196)** - the N2 and CO2 rows have their component properties (M, Tc, pc, ω, vc, Zc, γ, Tb, s) transposed.

## Coverage and error count by section

| Section | Items audited | Confirmed errors |
|---|---|---|
| Chapter 1 - Introduction | 2 | 1 |
| Chapter 2 - Volumetric and Phase Behaviour of Oil and Gas Systems | 12 | 0 |
| Chapter 3 - Gas and Oil Properties and Correlations | 185 | 3 |
| Chapter 4 - Equation-of-State Calculations | 106 | 2 |
| Chapter 5 - Heptanes-Plus Characterisation | 106 | 3 |
| Chapter 6 - Conventional PVT Measurements | 95 | 4 |
| Chapter 7 - Black-Oil PVT Formulations | 59 | 9 |
| Chapter 8 - Gas-Injection Processes | 7 | 0 |
| Chapter 9 - Water/Hydrocarbon Systems | 52 | 1 |
| Appendix A - Property Tables and Units | 340 | 0 |
| Appendix B - Example Problems | 95 | 5 |
| Appendix C - Equation-of-State Applications | 46 | 2 |
| Appendix D - Understanding Laboratory Oil PVT Reports | 34 | 4 |
| **Total** | **1139** | **34** |

Sections with no confirmed errors (Chapters 1, 2, 8 and Appendix A) are almost entirely qualitative text, figures, or verbatim property tables; the audited-item counts above show they were examined, not skipped.

## Chapter 1 - Introduction

### E1. Reference 91 (Peng & Robinson)  
*p.4 (PDF 11) - cross-reference - LOW*

- **Book prints:** Peng, D.Y. and Robinson, D.B.: "A New-Constant EOS," Ind. & Eng. Chem. Fund. (1976) 15, No. 1, 59.
- **Issue:** The title of the seminal Peng-Robinson paper is "A New Two-Constant Equation of State." The book's abbreviated citation drops the word "Two," printing "A New-Constant EOS," which is not a valid rendering of the title (a two-constant EOS is the defining feature of the paper).
- **Correction:** Peng, D.Y. and Robinson, D.B.: "A New Two-Constant EOS," Ind. & Eng. Chem. Fund. (1976) 15, No. 1, 59.

## Chapter 3 - Gas and Oil Properties and Correlations

### E2. Eq. 3.102f (Alani-Kennedy a_i for i != C7+)  
*p.34 (PDF 41) - equation - MEDIUM*

- **Book prints:** a_i = a1i/T + log a2i ; i != C7+
- **Issue:** The printed form is dimensionally/physically broken for the van der Waals attraction term. Using Table 3.1 constants it yields a_i ~ 5 to 18 (e.g. C1 70-300F at 560R: 9160.64/560 + log(61.89) = 18.15), which makes the a/v^2 term negligible (a few psia) so the EOS (Eq 3.102a) cannot produce liquid densities. The Alani-Kennedy relation is a = K exp(n/T); with a1=K, a2=n the correct form a_i = a1i*exp(a2i/T) gives physically sound values (~4,300-153,000) that are continuous across the two C1 temperature ranges (C1 at 300F: 9938 from low-range vs 10585 from high-range). Both image and pdftotext confirm the LHS is 'a_i =' (not 'log a_i =') and the trailing '+ log a2i' term.
- **Correction:** a_i = a1i · exp(a2i/T) ; i ≠ C7+ (Alani-Kennedy a = K·exp(n/T), with a1=K, a2=n from Table 3.1)

### E3. Eq. 3.113b  
*p.36 (PDF 43) - equation - MEDIUM*

- **Book prints:** Bob = 1 + (4.67 x 10^-4)Rs + (0.11 x 10^-4)(T-60)(gAPI/ggc) - (0.1337 x 10^-7)Rs(T-60)(gAPI/ggc)
- **Issue:** Vazquez-Beggs Bob cross-term coefficient (C3) for gAPI>30 is wrong in both sign and magnitude. The canonical Vazquez-Beggs (1980) value is C3 = +1.337 x 10^-9 (positive, order 10^-9). The book prints -(0.1337 x 10^-7) = -1.337 x 10^-8, i.e. wrong sign and 10x too large. Internal check: the gAPI<=30 form (Eq 3.113a) correctly reproduces C3 = -1.8106 x 10^-8; the >30 cross-term should be a small POSITIVE 1.337e-9, not a larger negative value. At gAPI=40, ggc=0.8, T=200F, Rs=800 the erroneous term shifts Bo by ~0.08 (about 5%).
- **Correction:** Bob = 1 + (4.67×10^-4)Rs + (0.11×10^-4)(T-60)(γAPI/γgc) + (0.1337×10^-8)Rs(T-60)(γAPI/γgc), for γAPI>30 [i.e. C3 = +1.337×10^-9]

### E4. Eq. 3.134b (definition of xi_Ti)  
*p.38 (PDF 45) - equation - MEDIUM*

- **Book prints:** xi_Ti = 5.35(Tci Mi^3 / pci^4)^(1/6)
- **Issue:** The Stiel-Thodos viscosity-reducing parameter must have molecular weight in the DENOMINATOR: xi = Tc^(1/6)/(M^(1/2) pc^(2/3)) = (Tc/(M^3 pc^4))^(1/6), so xi ~ M^-1/2. As printed, Mi^3 is in the numerator (xi ~ M^+1/2), inverting the M dependence. Both the rendered image and the pdftotext extraction ('Tci Mi^3 / pci^4', slash after Mi^3) agree. This contradicts the parallel mixture form Eq 3.133b (xi_T = 5.35(Tpc/(M^3 ppc^4))^(1/6)), the Lucas Eq 3.67, and the Fig 3.12 caption, all of which correctly place M^3 in the denominator.
- **Correction:** ξ_Ti = 5.35(T_ci / (M_i^3 p_ci^4))^(1/6)

## Chapter 4 - Equation-of-State Calculations

### E5. Eq. 4.23 (both the unnumbered pure-component fugacity above it and the numbered mixture form)  
*p.50 (PDF 57) - equation - HIGH*

- **Book prints:** ln f/p = ln phi = Z - 1 - ln(Z-B) - [A/(2*sqrt2*B)] ln{ [Z + (1+sqrt2)B] / [Z - (1-sqrt2)B] } ; and ln fi/(yi*p) = ln phi_i = (Bi/B)(Z-1) - ln(Z-B) + [A/(2*sqrt2*B)]( Bi/B - (2/A) sum_j yj Aij ) ln{ [Z + (1+sqrt2)B] / [Z - (1-sqrt2)B] }
- **Issue:** Denominator of the log argument is printed as Z - (1-sqrt2)B. Since (1-sqrt2) = -0.4142, this evaluates to Z + 0.4142B, whereas the correct Peng-Robinson fugacity denominator is Z + (1-sqrt2)B = Z - (sqrt2-1)B = Z - 0.4142B. Verified numerically: integrating (Z-1)/p dp along an isotherm for methane (T=300K, p=5MPa) gives ln phi = -0.10397, which matches the closed form with denominator Z+(1-sqrt2)B (-0.10397) and NOT the printed form Z-(1-sqrt2)B (-0.05113). The sign of the term inside the denominator bracket is wrong. Error is consistent across both the pure and mixture expressions.
- **Correction:** ln f/p = ln phi = Z - 1 - ln(Z - B) - [A/(2 sqrt2 B)] ln{ [Z + (1+sqrt2)B] / [Z + (1-sqrt2)B] } (equivalently denominator Z - (sqrt2-1)B). Mixture form Eq. 4.23: ln fi/(yi p) = ln phi_i = (Bi/B)(Z-1) - ln(Z-B) + [A/(2 sqrt2 B)]( Bi/B - (2/A) sum_j yj Aij ) ln{ [Z + (1+sqrt2)B] / [Z + (1-sqrt2)B] }. Only the denominator sign changes; numerator and all other terms are as printed.

### E6. Fig. 4.2 caption  
*p.50 (PDF 57) - figure - LOW*

- **Book prints:** Fig. 4.2-Temperature and component-dependent EOS terms Omega^o_a alpha(T_r,omega) and Omega^o_a alpha(T_r,omega) for the ZJRK EOS (from Yarborough).
- **Issue:** The second term is printed identically to the first (Omega^o_a alpha). The figure has two panels: the top y-axis is labelled 'EOS Constant Omega_b' and the bottom 'EOS Constant Omega_a'. Per Eq. 4.18 the b-constant uses the beta correction, not alpha, and its coefficient is Omega^o_b, not Omega^o_a. The caption's second term should describe the b-constant.
- **Correction:** Fig. 4.2 - Temperature and component-dependent EOS terms Ω°_a α(T_r,ω) and Ω°_b β(T_r,ω) for the ZJRK EOS (from Yarborough).

## Chapter 5 - Heptanes-Plus Characterisation

### E7. Eq. 5.15  
*p.73 (PDF 80) - equation - MEDIUM*

- **Book prints:** eta ~= 110 / [1 - (1 + 4/alpha^0.7)]
- **Issue:** As printed the denominator 1 - (1 + 4/alpha^0.7) = -4/alpha^0.7, so the equation yields a NEGATIVE eta for all alpha (e.g. alpha=2.273 gives eta = -49). eta is the minimum C7+ molecular weight and must be positive (0 to 110). The inner term is missing its exponent -1 (and the relation is a product, not a simple 110-over-denominator fraction). The correct form reproduces the fitted values shown in Fig 5.7: alpha=2.273 -> eta~76 (fig 75.7) and alpha=0.817 -> eta~90 (fig 93.2).
- **Correction:** eta ~= 110*[1 - (1 + 4/alpha^0.7)^-1], equivalently eta ~= 110/(1 + 0.25*alpha^0.7) = 440/(4 + alpha^0.7)

### E8. Table 5.7 (COEFFICIENTS FOR YARBOROUGH AROMATICITY FACTOR CORRELATION), column headers  
*p.79 (PDF 86) - table - LOW*

- **Book prints:** Y_a | A_0 | A_1 | A_2 | A_2 (fifth/last column header printed as A_2)
- **Issue:** Eq. 5.43 is gamma_i = exp[A_0 + A_1*i^-1 + A_2*i + A_3*ln(i)], i.e. four coefficients A_0..A_3. Table 5.7 supplies four coefficient columns but the last one is mislabelled A_2 (duplicating the 4th column). The last column holds the A_3 values.
- **Correction:** Last column header should read A_3, giving columns: Y_a, A_0, A_1, A_2, A_3.

### E9. Eq. 5.82  
*p.84 (PDF 91) - equation - MEDIUM*

- **Book prints:** M_I = M_C7 (M_N / M_C7)^(1/N_H)
- **Issue:** The exponent numerator is printed as the numeral 1 (confirmed: text-layer glyph code '1', width matching digits, distinct from the italic 'I' in M_I). With a constant exponent 1/N_H every group boundary M_I would be identical, which contradicts the surrounding text (I = 1,...,N_H defined; M_I are the per-group upper boundaries, and at I=N_H the boundary must equal the heaviest MW M_N). The exponent must be the running index I/N_H so that I=N_H gives M_I = M_N and boundaries are log-spaced between M_C7 and M_N.
- **Correction:** M_I = M_C7 (M_N / M_C7)^(I/N_H), I = 1,...,N_H

## Chapter 6 - Conventional PVT Measurements

### E10. Eq. 6.21  
*p.94 (PDF 101) - equation - MEDIUM*

- **Book prints:** c = (1/V_rt)(∂V_rt/∂p)_T = (1/V_ro)(∂V_ro/∂p)_T ; p > p_b (book uses partial derivatives ∂; no negative sign printed)
- **Issue:** Missing the negative sign of the isothermal-compressibility definition. Above the bubblepoint dV/dp < 0, so as printed c would be negative; the undersaturated-oil compressibilities tabulated in Table 6.9 (13.48, 15.88, 18.75 x10^-6 vol/vol-psi) are positive. Standard definition is c = -(1/V)(dV/dp)_T.
- **Correction:** c = -(1/V_rt)(∂V_rt/∂p)_T = -(1/V_ro)(∂V_ro/∂p)_T ; p > p_b

### E11. Eq. 6.49  
*p.100 (PDF 107) - numerical - LOW*

- **Book prints:** r_s = r_p = 1/R_p = 1/(21,580 scf/STB) = 4.58x10^-5 STB/scf
- **Issue:** The denominator 21,580 is a digit transposition of R_p = 21,850 scf/STB computed one line earlier in Eq. 6.48. 1/21,580 = 4.634x10^-5, which does NOT equal the printed 4.58x10^-5; whereas 1/21,850 = 4.577x10^-5 = 4.58x10^-5. The result is right, the denominator is mistyped.
- **Correction:** r_s = r_p = 1/R_p = 1/(21,850 scf/STB) = 4.58x10^-5 STB/scf

### E12. Eq. 6.49 (final units)  
*p.100 (PDF 107) - nomenclature - LOW*

- **Book prints:** = 4.58x10^-5 STB/scf = 45.8 STB/scf
- **Issue:** Unit label off by a factor of 1e6. 4.58x10^-5 STB/scf equals 45.8 STB/MMscf, not 45.8 STB/scf. Compare the parallel dewpoint result Eq. 6.46, which correctly writes 154.4 STB/MMscf.
- **Correction:** r_s = r_p = 1/R_p = 1/(21,580 scf/STB) = 4.58×10^-5 STB/scf = 45.8 STB/MMscf

### E13. Table 6.12, component row between n-C5 and C7+ (values 1.79 / 1.79 / 1.60 / 1.52 / 1.03 / 0.73 / 0.80)  
*p.106 (PDF 113) - table - MEDIUM*

- **Book prints:** C7 1.79 1.79 1.60 1.52 1.03 0.73 0.80 (row immediately above the C7+ row 6.85 ...)
- **Issue:** Row is mislabeled 'C7'. This is the hexane (C6) row: the plus fraction is the separate C7+ row directly below, the dewpoint value 1.79 mol% equals the C6 (Hexanes) wellstream value in Table 6.5, and Eq. 6.55 uses this 0.0179 with M=86.17 and rho=41.43 (n-hexane properties). There is no C6 row otherwise, and splitting a discrete C7 from C7+ is nonsensical.
- **Correction:** The row label should be C6 (Hexanes), not C7. Corrected sequence: ... n-C5, C6 (1.79 1.79 1.60 1.52 1.03 0.73 0.80), C7+ (6.85 ...), Total.

## Chapter 7 - Black-Oil PVT Formulations

### E14. Eq. 7.19 (third sub-equation, m_o-bar-g)  
*p.114 (PDF 121) - equation - MEDIUM*

- **Book prints:** m_o-bar-g = 350 V_o-bar ( R_p - R_s F_o-bar-o ) gamma_o-bar-g
- **Issue:** m_o-bar-g is the mass of condensate (stock-tank oil from reservoir gas). Its volume is V_o-bar-g = r_s * V_g-bar-g = r_s * V_o-bar(R_p - R_s F_o-bar-o), so its mass is 350 * gamma_o-bar-g * r_s * V_o-bar(R_p - R_s F_o-bar-o). The r_s factor is missing. This is confirmed by Eq. 7.20 immediately below, where m_g = V_o-bar(R_p - R_s F_o-bar-o)(350 gamma_o-bar-g r_s + 0.076 gamma_g-bar-g) correctly contains 350 gamma_o-bar-g r_s.
- **Correction:** m_ōg = 350 V_ō (R_p - R_s F_ōo) r_s γ_ōg

### E15. Eq. 7.17 (second sub-equation, V_g)  
*p.114 (PDF 121) - typo - MEDIUM*

- **Book prints:** V_g = V_o B_gd ( R_p - R_s F_o-bar-o )
- **Issue:** The leading volume is printed as V_o (reservoir-oil volume, ft3, defined in the line above) with no overbar. On the stated V_o-bar (total stock-tank oil, STB) basis, the reservoir gas volume is V_g = B_gd * V_g-bar-g = B_gd * V_o-bar(R_p - R_s F_o-bar-o). Using V_o makes the expression dimensionally ft^6/STB. Every parallel relation (Eqs. 7.19-7.23) uses V_o-bar(R_p - R_s F_o-bar-o); the overbar was dropped here.
- **Correction:** V_g = V̄_o B_gd (R_p - R_s F̄_oo) [leading V̄_o = total stock-tank oil, STB, carrying the overbar]

### E16. Sec 7.3.4, text just below Eq. 7.17  
*p.114 (PDF 121) - cross-reference - LOW*

- **Book prints:** F_o-bar-o is the fraction of total stock-tank oil that comes from the reservoir oil (Eq. 7.4).
- **Issue:** F_o-bar-o (fraction of total stock-tank oil from reservoir oil) is defined in Eq. 7.6. Eq. 7.4 defines F_g-bar-g (fraction of total surface gas from reservoir gas). The cross-reference points to the wrong equation; the correct citation (Eq. 7.6) is used later in the text below Eq. 7.37.
- **Correction:** F_ōo is the fraction of total stock-tank oil that comes from the reservoir oil (Eq. 7.6).

### E17. Sec 7.3.4, text just below Eq. 7.30  
*p.116 (PDF 123) - cross-reference - LOW*

- **Book prints:** where F_g is given by Eq. 7.25 in terms of producing GOR, R_p (through the quantity F_o-bar-o).
- **Issue:** F_g (mole fraction of wellstream from reservoir gas) is defined in Eq. 7.27. Eq. 7.25 defines the surface-component mole fractions x_o-bar and x_g-bar of the reservoir oil. The reference should be to Eq. 7.27.
- **Correction:** where F_g is given by Eq. 7.27 in terms of producing GOR, R_p (through the quantity F_ōo).

### E18. Eq. 7.39 (middle member of the equality chain)  
*p.117 (PDF 124) - equation - LOW*

- **Book prints:** q_o/(q_o + q_g) = q_o-bar B_o / ( q_o-bar B_o + q_g-bar B_gd ) = [ 1 + (R_p - R_s F_o-bar-o) B_gd / (5.615 F_o-bar-o B_o) ]^-1
- **Issue:** The left member (q_o/(q_o+q_g) with q_o=q_o-bar F_o-bar-o B_o and q_g=q_o-bar(R_p-R_s F_o-bar-o)B_gd from Eq. 7.37) and the right member are correct and equal. The middle member is not: q_o-bar B_o is a reservoir-barrel rate (bbl/D) while q_g-bar B_gd is ft3/D, and they are summed without the 5.615 ft3/bbl conversion that appears in the right member; it also omits the F_o-bar-o weighting and uses total surface gas q_g-bar (= q_o-bar R_p) rather than the vapour surface-gas rate. As written the middle member reduces to B_o/(B_o + R_p B_gd), which does not equal the right member.
- **Correction:** Middle member should read q_ō F_ōo B_o / ( q_ō F_ōo B_o + q_ō(R_p - R_s F_ōo) B_gd / 5.615 ), which equals both the left member q_o/(q_o+q_g) and the right member [1 + (R_p - R_s F_ōo) B_gd/(5.615 F_ōo B_o)]^-1.

### E19. Eq. 7.44  
*p.118 (PDF 125) - equation - MEDIUM*

- **Book prints:** (S_o)_k = [ (A_o)_{k-1} - (dN_p)_k - [ phi(1 - S_wi) r_s gamma*_o-bar / B_gd ]_k ] / [ phi( 1/B_o - r_s gamma*_o-bar / B_gd ) ]_k
- **Issue:** Eq. 7.44 is the algebraic solution for So obtained by combining the material balance (Eq. 7.40) with the definition of A_o (Eq. 7.41). A_o in Eq. 7.41 contains the term 5.615(1 - Sw - So) r_s gamma*_o/B_gd (with B_gd in ft3/scf, r_s in STB/scf), so the 5.615 ft3->bbl conversion must carry through. Both the r_s*gamma*_o/B_gd term in the numerator and in the denominator are missing the factor 5.615. The E_o/E_g factors in Eq. 7.43 also carry 5.615 with B_gd, confirming the ft3/scf convention. As printed, Eq. 7.44 is dimensionally inconsistent with its own source equations and gives a wrong So whenever r_s is non-negligible.
- **Correction:** (S_o)_k = [ (A_o)_{k-1} - (dN_p)_k - [ 5.615 phi(1 - S_wi) r_s gamma*_o-bar / B_gd ]_k ] / [ phi( 1/B_o - 5.615 r_s gamma*_o-bar / B_gd ) ]_k

### E20. Eq. 7.46  
*p.118 (PDF 125) - equation - MEDIUM*

- **Book prints:** (S_o)_k = [ (A_g)_{k-1} - (ΔG_p)_k - [ φ(1 - S_wi)/B_gd ]_k ] / [ φ( R_s γ*_g / B_o - 1/B_gd ) ]_k (γ*_g is the star-g gravity ratio of Eq. 7.42, not 'g-bar')
- **Issue:** Same defect as Eq. 7.44 but for the gas-condensate branch. Solving the gas material balance (Eq. 7.40) together with A_g (Eq. 7.41, which contains 5.615(1 - Sw - So)/B_gd) requires the 5.615 factor on every 1/B_gd term. The numerator phi(1 - S_wi)/B_gd term and the denominator 1/B_gd term both drop the 5.615, making 7.46 inconsistent with 7.41/7.43 (B_gd stated in ft3/scf throughout).
- **Correction:** (S_o)_k = [ (A_g)_{k-1} - (ΔG_p)_k - [ 5.615 φ(1 - S_wi)/B_gd ]_k ] / [ φ( R_s γ*_g / B_o - 5.615/B_gd ) ]_k

### E21. Sec 7.4.3, Oil Reservoir step 3 and Gas-Condensate step 3  
*p.118 (PDF 125) - cross-reference - LOW*

- **Book prints:** 3. Calculate oil saturation (S_o)_k from Eqs. 7.39 through 7.41.
- **Issue:** The saturation is actually obtained from Eq. 7.44 (oil reservoir) and Eq. 7.46 (gas condensate), derived from the material balance (Eq. 7.40) and the A_o/A_g definitions (Eq. 7.41). Eq. 7.39 is the wellbore fractional-flow relation and is unrelated to the reservoir saturation material balance, so the range 7.39-7.41 is wrong (7.39 should be 7.40, or the step should cite Eq. 7.44/7.46).
- **Correction:** Step 3 should reference the material-balance and definition equations 7.40 and 7.41 (7.42 for the gamma* ratios), not "7.39 through 7.41." The oil saturation is given by Eq. 7.44 (Oil Reservoir) and Eq. 7.46 (Gas-Condensate Reservoir). Suggested wording: "3. Calculate oil saturation (S_o)_k from Eqs. 7.40 and 7.41, giving Eq. 7.44 (oil reservoir) or Eq. 7.46 (gas-condensate reservoir)."

### E22. Sec 7.5, text just below Eq. 7.49  
*p.119 (PDF 126) - cross-reference - LOW*

- **Book prints:** From Eq. 7.47, we see that the variation in surface gravities with pressure is included directly in the definitions of the PVT properties.
- **Issue:** Eq. 7.47 is the gas-condensate material-balance error check (epsilon = (A_o)_k - (A_o)_{k-1} + dN_p) and contains no surface gravities. The surface gravities appear in the partial-density definitions of Eqs. 7.48-7.49. The reference should point to Eq. 7.49 (a 7 vs 9 transposition).
- **Correction:** From Eq. 7.49, we see that the variation in surface gravities with pressure is included directly in the definitions of the PVT properties.

## Chapter 9 - Water/Hydrocarbon Systems

### E23. Eq. 9.18  
*p.147 (PDF 154) - equation - HIGH*

- **Book prints:** B*_w(p,T) = B*_w(psc,T) ( 1 + (A_1/A_0) p )^(1/A_1)
- **Issue:** Exponent sign is wrong. The text says Eq. 9.18 is obtained by 'solving Eq. 9.16 for the FVF.' Eq. 9.16 is ln[B*_w(p,T)/B*_w(psc,T)] = -integral_0^p c*_w dp, and c*_w = (A_0 + A_1 p)^-1. Integrating gives ln(ratio) = -(1/A_1) ln(1 + (A_1/A_0)p), so B*_w = B*_w(psc,T)(1 + (A_1/A_0)p)^(-1/A_1). Since A_0 (~3.1e5) and A_1 (~8) from Eq. 9.17 are both positive, the printed positive exponent makes the brine FVF INCREASE (and density DECREASE) as pressure rises, which is unphysical and contradicts both its own derivation (Eq. 9.16) and the following sentence claiming the equation reproduces Rogers-Pitzer densities to within 0.5%. The exponent must be negative.
- **Correction:** B*_w(p,T) = B*_w(p_sc,T) ( 1 + (A_1/A_0) p )^(-1/A_1)

## Appendix B - Example Problems

### E24. Problem 1, part c (gas specific gravity)  
*p.172 (PDF 179) - numerical - LOW*

- **Book prints:** gamma_g = (24.97)/(28.97) = 0.864 (air = 1).
- **Issue:** Arithmetic slip: 24.97/28.97 = 0.8619, which rounds to 0.862, not 0.864. M_g = 24.97 (Table B-2 total) and 28.97 both come straight from the same page, so this is a self-contained division error (>1 unit off in the 3rd significant figure, beyond last-digit rounding).
- **Correction:** gamma_g = 24.97/28.97 = 0.862 (air = 1)

### E25. Problem 7, definition of zeta_Ti accompanying Eq. 3.134b (LBC individual viscosity-reducing parameter)  
*p.176 (PDF 183) - equation - MEDIUM*

- **Book prints:** where zeta_Ti = 5.35(T_ci M_i^3 / p_ci^4)^(1/6).
- **Issue:** M_i^3 is placed in the numerator. The correct Stiel-Thodos/LBC individual reducing parameter has M_i^3 in the denominator, i.e. zeta_Ti = 5.35 T_ci^(1/6)/(M_i^(1/2) p_ci^(2/3)) = 5.35[T_ci/(M_i^3 p_ci^4)]^(1/6). This is confirmed two ways on the same page: the mixture form printed just above is zeta_T = 5.35[T_pc/(M^3 p_pc^4)]^(1/6) (M^3 in denominator), and Table B-12's xi_i column reproduces only with M_i^3 in the denominator (e.g. C1: 5.35[343.0/(16.04^3 x 667.8^4)]^(1/6) = 0.0463, matching the table; the printed numerator form gives 0.74).
- **Correction:** zeta_Ti = 5.35[T_ci/(M_i^3 p_ci^4)]^(1/6), equivalently 5.35 T_ci^(1/6)/(M_i^(1/2) p_ci^(2/3)). (M_i^3 belongs in the denominator, not the numerator as printed.)

### E26. Problem 10, pressure-correction substitution into Eq. 3.98  
*p.180 (PDF 187) - numerical - MEDIUM*

- **Book prints:** Delta rho_p = 10^-3{0.167+[16.181x10^(-0.0425(41.69))]}(3,500) - 10^-8{0.299+[263x10^(-0.0603(41.69))]}(3,500)^2 = (0.441x10^-3)(3,500) - (1.104x10^-8)(3,500)^2 = 1.26 lbm/ft^3 (four printed occurrences of 3,500).
- **Issue:** The substituted pressure 3,500 is wrong. Problem 10 evaluates density at the bubblepoint, 3,100 psia. With p=3,500 the stated coefficients give (0.441e-3)(3500)-(1.104e-8)(3500)^2 = 1.41, not 1.26. With p=3,100 they give 1.366-0.106 = 1.26, matching the printed result (and the downstream rho_po+Delta_rho_p = 42.95 and final rho_o = 41.69+1.26-5.85 = 37.10). Both occurrences of (3,500) should read (3,100).
- **Correction:** All occurrences of the substituted pressure (3,500) should read (3,100): Delta rho_p = 10^-3{0.167+[16.181x10^(-0.0425(41.69))]}(3,100) - 10^-8{0.299+[263x10^(-0.0603(41.69))]}(3,100)^2 = (0.441x10^-3)(3,100) - (1.104x10^-8)(3,100)^2 = 1.26 lbm/ft^3. (Four printed instances of 3,500 to change, not two.)

### E27. Problem 13, pseudocritical properties via Standing wet-gas correlation Eq. 3.49  
*p.182 (PDF 189) - numerical - MEDIUM*

- **Book prints:** The book input symbol is the overbar (average surface-gas) gravity gamma_gbar, not "gamma_tg". Book prints: "With gamma_gbar = gamma_gHC = 0.80, pseudocritical properties from the Standing 'wet-gas' correlations (Eq. 3.49), T_pcHC = 187 + 330 gamma_gHC - 71.5 gamma_gHC^2 (3.49a) and p_pcHC = 706 - 51.7 gamma_gHC - 11.1 gamma_gHC^2 (3.49b) are T_pc = 426 R and p_pc = 650 psia."
- **Issue:** The input value 0.80 is inconsistent with the reported results and with the reservoir-gas density calculation. gamma=0.80 gives T_pc=405 R and p_pc=658 psia, whereas the printed 426 R and 650 psia (and T_pr=650/426=1.526, and the density rho_g=(3090)(28.97)(0.904)/... = 14.36) all require the wellstream gravity gamma_w=0.904 computed just above via Eq. 3.55. The reservoir gas IS the wellstream, so Eq. 3.49 should use gamma_gHC = gamma_w = 0.904 (cf. Problem 14, which sets gamma_w = gamma_gHC = 0.85). The 0.80 (the assumed surface-gas gravity) is mislabelled as gamma_gHC.
- **Correction:** The Eq. 3.49 input should be the wellstream gravity: gamma_w = gamma_gHC = 0.904 (not gamma_gbar = 0.80). This gives T_pcHC = 426 R and p_pcHC = 650 psia, consistent with the printed results, the T_pr/p_pr and gas-density calculations that follow, and the identical methodology used in Problem 14 (which uses gamma_w for Eq. 3.49). The printed results are correct; the labelled input value 0.80 is the error.

### E28. Table B-27 (Separator Flash Calculation, Problem 17), C1 row, column z_i/(F_v+c_i)  
*p.185 (PDF 192) - typo - LOW*

- **Book prints:** 06116
- **Issue:** Missing decimal point. K_i=287.94 -> c_i=1/(287.94-1)=0.003485; with F_v=0.64241, z_i/(F_v+c_i)=0.3950/0.6459=0.6116. The column also sums to zero only with 0.6116. Printed as '06116'.
- **Correction:** 0.6116

## Appendix C - Equation-of-State Applications

### E29. Table C-7 (Final PR EOS Characterization for Reservoir Gas Condensate), N2 and CO2 rows  
*p.196 (PDF 203) - table - HIGH*

- **Book prints:** N2 | z=0.0018 | M=44.01 | Tc=547.6 | pc=1,070.6 | w=0.2310 | vc=1.505 | Zc=0.2742 | g*=0.5072 | Tb=350.4 | s=-0.0577
CO2 | z=0.0013 | M=28.01 | Tc=227.3 | pc=493.0 | w=0.0450 | vc=1.443 | Zc=0.2916 | g*=0.4700 | Tb=139.3 | s=-0.1752
- **Issue:** The component-property values in the N2 and CO2 rows are interchanged. Nitrogen has M=28.01, Tc=227.3 R, pc=493.0 psia; carbon dioxide has M=44.01, Tc=547.6 R, pc=1,070.6 psia. Table C-7 assigns CO2's molecular weight and criticals to the N2 row and vice versa. The correct (un-swapped) values appear in Tables C-10 and C-12 for the same component library, confirming the transposition. Every property column (M, Tc, pc, omega, vc, Zc, gamma, Tb, s) is swapped between the two rows.
- **Correction:** N2 row: z=0.0018, M=28.01, Tc=227.3, pc=493.0, w=0.0450, vc=1.443, Zc=0.2916, g*=0.4700, Tb=139.3, s=-0.1752. CO2 row: z=0.0013, M=44.01, Tc=547.6, pc=1,070.6, w=0.2310, vc=1.505, Zc=0.2742, g*=0.5072, Tb=350.4, s=-0.0577.

### E30. Cumulative-compressibility worked example (application of Eq. C-1)  
*p.203 (PDF 210) - equation - LOW*

- **Book prints:** (c̄_o)_meas = [0.059/(5,000 - 2,650)] ln(5,000 - 2,650) = 15.9 × 10⁻⁶ psi⁻¹
- **Issue:** The argument of the logarithm is printed as a subtraction, ln(5,000 - 2,650) = ln(2,350), which contradicts Eq. C-1 (tau_o = A/(p_i - p) * ln(p_i/p)) and does not give the stated result. Evaluating ln(2,350)=7.76 yields 1.95x10^-4, not 15.9x10^-6. The printed answer 15.9x10^-6 is only obtained with ln(5,000/2,650)=0.6349, so the '-' should be '/'. The PR and SRK companion values (18.9 and 19.9 x10^-6) also reproduce only with the ratio form.
- **Correction:** (c̄_o)_meas = [0.059/(5,000 - 2,650)] ln(5,000/2,650) = 15.9 × 10⁻⁶ psi⁻¹

## Appendix D - Understanding Laboratory Oil PVT Reports

### E31. Eq. D-4 (and its application in Eq. D-5)  
*p.210 (PDF 217) - equation - LOW*

- **Book prints:** c_o = (1/V)(dV/dp)_T
- **Issue:** Isothermal compressibility is defined with a leading negative sign; as printed the expression yields a negative number for a physically positive compressibility (dV/dp < 0). In the D-5 example the sign is silently absorbed by taking |0.9781 - 0.9562| = 0.0219 as positive, so the printed definition is inconsistent with the correct positive result. Likely Standing's informal shorthand rather than a deep error.
- **Correction:** c_o = -(1/V)(dV/dp)_T (and correspondingly Eq. D-5: c_o = -(1/V_rel)(ΔV_rel/Δp)_T)

### E32. Fig D-3 in-plot label (upper plateau of differential-liberation curve)  
*p.212 (PDF 219) - figure - LOW*

- **Book prints:** 1517 scf/residual bbl
- **Issue:** The total differential-liberation solution GOR is stated as 1,518 ft3/bbl residual oil in the Page 3 tabular data (Liberated/bbl residual oil column bottom = 1,518), in the cover-letter summary ('1,518 scf gas/bbl residual oil'), and repeatedly in the body text. The figure label reads 1517, one unit low.
- **Correction:** 1,518 scf/residual bbl

### E33. Sec 'Calculation of FVF's From Relative Volumes', last worked line (left column, above Fig D-4 discussion)  
*p.213 (PDF 220) - numerical - LOW*

- **Book prints:** B_o = 1.109(1.674/2.75) = 0.895.
- **Issue:** The denominator 2.75 does not reproduce the stated result. 1.109 x 1.674 / 2.75 = 0.675, not 0.895. The correct denominator is the bubblepoint relative oil volume 2.075 used two lines earlier (B_o = 1.787 x 1.674/2.075 = 1.442). 1.109 x 1.674 / 2.075 = 0.895, which matches. So '2.75' is a dropped-digit typo for '2.075'.
- **Correction:** B_o = 1.109(1.674/2.075) = 0.895 RB/STB.

### E34. Report Page 5 of 11, Separator Tests table, explanatory footnote (unnumbered note below footnotes 1-3)  
*p.218 (PDF 225) - table - MEDIUM*

- **Book prints:** conditions for the first two-stage separator test are (1) p_sp1 = 0 psig and T_sp1 = 75 F and (2) p_sp2 = 0 psig and T_sp2 = 60 F, with total R_sb = 1,206 + 35 = 1,241 scf/STB, B_ob = 1.833, gamma_API = 45.6 API, and gamma_g = 0.942.
- **Issue:** Internal inconsistency with the table it annotates. The footnote's B_ob = 1.833 and gamma_API = 45.6 identify the 0-psig-primary row, whose separator GOR = 1,206 and stock-tank GOR = 0. So the total should be 1,206 + 0 = 1,206. The value 35 is the stock-tank GOR of the 50-psig test row, not the 0-psig row, so 1,206 + 35 = 1,241 mixes rows and contradicts the tabulated 0.
- **Correction:** total R_sb = 1,206 + 0 = 1,206 scf/STB (the stock-tank GOR for the 0-psig-primary test is 0 per its table row; the "35" belongs to the 50-psig row).
