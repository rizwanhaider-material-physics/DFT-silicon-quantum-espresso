import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
t = open('si.bands.out').read()
t = t.split('End of band structure calculation')[-1]
parts = re.split(r'bands \(ev\):', t)[1:]
bands = []
for p in parts:
    p = re.split(r'k =|Writing|highest|JOB|init_run', p)[0]
    e = [float(x) for x in re.findall(r'-?\d+\.\d{4}', p)][:8]
    if len(e) == 8:
        bands.append(e)
vbm = max(b[3] for b in bands)
x = range(len(bands))
for n in range(8):
    plt.plot(x, [b[n] - vbm for b in bands], color='navy', lw=1.2)
ticks = [0, 20, 50, 60, 70, 100]
plt.xticks(ticks, ['L', 'Γ', 'X', 'W', 'K', 'Γ'])
for tk in ticks:
    plt.axvline(tk, color='gray', lw=0.5)
plt.axhline(0, color='red', ls='--', lw=0.8)
plt.ylim(-12, 6)
plt.ylabel('Energy - VBM (eV)')
plt.title('Silicon band structure (LDA), gap = 0.52 eV')
plt.savefig('si_bands.png', dpi=200, bbox_inches='tight')
print('saved si_bands.png')
