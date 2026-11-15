import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
d = np.loadtxt('si.dos')
E, g = d[:, 0], d[:, 1]
vbm = 6.0448
x = E - vbm
plt.plot(x, g, color='navy', lw=1.2)
plt.fill_between(x, g, color='navy', alpha=0.2)
plt.axvline(0, color='red', ls='--', lw=0.8)
plt.xlim(-13, 8)
plt.ylim(bottom=0)
plt.xlabel('Energy - VBM (eV)')
plt.ylabel('DOS (states/eV)')
plt.title('Silicon density of states (LDA)')
plt.savefig('si_dos.png', dpi=200, bbox_inches='tight')
mask = (g < 1e-3) & (x > -0.5) & (x < 1.5)
if mask.any():
    print('Zero-DOS window (eV): %.2f to %.2f, width %.2f' % (x[mask].min(), x[mask].max(), x[mask].max() - x[mask].min()))
print('saved si_dos.png')
