# DFT Study of Silicon Band Structure using Quantum ESPRESSO

## Aim
To calculate the electronic band structure and density of states of crystalline silicon using density functional theory, and to compare the computed band gap with published values.

## Tools
Quantum ESPRESSO, BURAI, VESTA, and Python with NumPy and Matplotlib.

## Planned Steps
First, convergence tests for cutoff energy and k-points. Second, self-consistent calculation. Third, band structure and density of states. Fourth, comparison with literature.

## Status
SCF calculation is completed, converged in six iterations. Convergence tests, band structure and density of states calculation is also completed.

## Author
Rizwan Haider, BS Physics, Thal University Bhakkar

## Results

Settings (from convergence tests): plane-wave cutoff 40 Ry, k-point grid 6x6x6. Total energy changes by less than 1 mRy between neighbouring cutoffs from 40 Ry, and between neighbouring grids from 4x4x4.

Band structure: path L-Gamma-X-W-K-Gamma.

![Silicon band structure](si_bands.png)

| Quantity | Value |

| Indirect band gap (LDA) | 0.52 eV |
| Valence band maximum | at Gamma |
| Conduction band minimum | along Gamma-X |
| Minimum direct gap | 2.56 eV |
| Experimental indirect gap | 1.12 eV |

##Note: the calculated gap is about half the experimental value. This is the known underestimation of band gaps by LDA, not an error in the setup.

## Files
- `si.ec*.in/out`: cutoff convergence test
- `si.k*.in/out`: k-point convergence test
- `si.scf.final.in/out`: final self-consistent calculation
- `si.bands.in/out`: band structure calculation
- `gap.py`, `plot_bands.py`: scripts for the gap and the plot

  ## Density of states:
  non-self-consistent run on a 12x12x12 grid with the tetrahedron method, then dos.x.

![Silicon density of states](si_dos.png)

The zero-DOS window is 0.54 eV wide, consistent with the 0.52 eV indirect gap from the band structure (the difference is about one DOS energy step of 0.02 eV).
