import re
t = open('si.bands.out').read()
t = t.split('End of band structure calculation')[-1]
parts = re.split(r'bands \(ev\):', t)[1:]
vb, cb = [], []
for p in parts:
    p = re.split(r'k =|Writing|highest|JOB|init_run', p)[0]
    e = [float(x) for x in re.findall(r'-?\d+\.\d{4}', p)][:8]
    if len(e) == 8:
        vb.append(e[3]); cb.append(e[4])
print('k-points read:', len(vb))
v, c = max(vb), min(cb)
print('VBM (eV):', v, ' at k-index', vb.index(v)+1)
print('CBM (eV):', c, ' at k-index', cb.index(c)+1)
print('Indirect gap (eV):', round(c - v, 4))
print('Minimum direct gap (eV):', round(min(a-b for a, b in zip(cb, vb)), 4))
