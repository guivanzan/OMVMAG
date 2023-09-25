import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit    

#import scipy as sp EXISTE O LEAST SQUARES DO SCIPY

linhaD = np.load('linhas/declinacao.npy')
linhaH = np.load('linhas/forca horizontal.npy')
linhaZ = np.load('linhas/forca vertical.npy')

linha1 = np.load('linhas/Linha 1.npy')
linha2 = np.load('linhas/Linha 2.npy')
linha3 = np.load('linhas/Linha 3.npy')

horas = []
for i in range(24):
    horas.append(i+1)
horas = np.array(horas).reshape(24,1)

#definindo médias horárias (x) pra least squares

linha1_shift = linha1[0] + abs(np.min(linha1[0])) + 1
linha1_medias_horarias = []

for i in range(11):
    center = 60 + 60*i
    hour_centered_mean = np.mean(linha1_shift[center-30:center+30])
    linha1_medias_horarias.append(hour_centered_mean)

for j in range(11):
    center = 780 + 60*j
    hour_centered_mean = np.mean(linha1_shift[center-30:center+30])
    linha1_medias_horarias.append(hour_centered_mean)

rows = len(linha1_medias_horarias)
linha1_medias_horarias = np.array(linha1_medias_horarias).reshape(rows,1)

#definindo alvos (y) para least squares

target = np.ndarray.tolist(linhaZ[16])
del target[12]
del target[0]
for k in range(len(target)):
    target[k] = float(target[k])
target = np.array(target).reshape(22,1)


#calculando least squares

#lincoef = np.linalg.lstsq(linha1_medias_horarias,target, rcond=None)[0]

#

def model(x,m,b):
    return m*x+b
target_robust = np.ndarray.flatten(target)
linha1_medias_horarias_robust = np.ndarray.flatten(linha1_medias_horarias)

#p0 = lincoef = np.linalg.lstsq(linha1_medias_horarias[0],target[0], rcond=None)[0]


p1,cov  = curve_fit(model,linha1_medias_horarias_robust,target_robust,p0=[linha1_medias_horarias[0],target[0]])

#definindo timeseries a plottar

horas_alt = np.ndarray.tolist(horas)
del horas_alt[12]
del horas_alt[0]
horas_alt = np.array(horas_alt).reshape(22,1)

scatter1 = model(linha1_medias_horarias,*p1)

plot4 = linha1[0] - np.min(linha1[0]) + 1
plot4 = model(plot4,*p1)
plot4 = plot4.reshape(1440,1)

plot6 = abs(target-scatter1)

#plot

fig, (ax1, ax2, ax3, ax4, ax5) = plt.subplots(5,1) 

ax1.scatter(horas_alt, scatter1)
ax1.grid()
ax1.title.set_text('Médias horárias do magnetograma * coef. angular (calculado usando valores dentro da média) (valores com shift)')
#
ax2.scatter(horas, linhaZ[0])
ax2.grid()
ax2.title.set_text('Livro de médias horárias')
#
ax3.scatter(horas_alt, target)
ax3.scatter(horas_alt, scatter1)
ax3.grid()
ax3.title.set_text('Laranja: médias calculadas (gráfico 1) / Azul: Médias registradas (gráfico 2)')
#
ax4.plot(linha1[1], plot4, '-g', linewidth = 1)
ax4.grid()
ax4.title.set_text('Magnetograma digitalizado * coef. angular (valores com shift)')
#
ax5.scatter(horas_alt, plot6)
ax5.grid()
ax5.title.set_text('Diferença absoluta entre médias registradas e médias calculadas')
#
fig.set_size_inches(18,26)

plt.show()

