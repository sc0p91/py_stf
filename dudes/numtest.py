# Package: Pillow
import numpy as np

gcht = [0.05, 0.22, 0.22, 0.15, 0.14, 0.22]
colr = ['red', 'blue', 'green', 'yellow', 'black', 'orange']
colr2 = ['red', 'blue', 'green']
rand = np.random.choice(colr, size=100000, p=gcht)
rand2 = np.random.choice(colr, size=1, p=gcht)
rand3 = np.random.choice(colr, size=1, p=gcht)

out = "img/"+str(rand2[0]+rand3[0])+".png"
print(out)

stats = []
stats2 = []

for c in colr:
    stats.append(f"{c}:{list(rand).count(c)}")
for c in colr2:
    stats2.append(f"{c}:{list(rand2).count(c)}")

#print(f'd gwichtig: {gcht}')
#print(f'aui farbe: {colr}')
#print(f'us hunderdusig heimer: {stats}')
#
#print(f'und: {stats2}')



