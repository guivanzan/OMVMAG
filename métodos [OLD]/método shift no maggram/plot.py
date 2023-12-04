import matplotlib.pyplot as plt
import numpy as np
from linreg import linreg

horas = []
for i in range(24):
    horas.append(i)
horas = np.array(horas).reshape(24,1)

minutes = []
for i in range(1440):
    minutes.append(60*i)
minutes = np.array(minutes)

def model(x,m,b):
        return m*x+b

def plotmag(livro,maggram):

    p1,plot1_maggram,plot1_livros = linreg(livro,maggram)
    plot1_maggram = model(plot1_maggram,*p1)
    plot2 = model(maggram,*p1)

    fig, (ax1, ax2, ax3) = plt.subplots(3,1) 

    ax1.scatter(horas, plot1_livros)
    ax1.scatter(horas, plot1_maggram)
    ax1.grid()
    ax1.title.set_text('Laranja: médias calculadas / Azul: Médias registradas')

    ax2.plot(minutes, plot2, '-g', linewidth = 1)
    ax2.grid()
    ax2.title.set_text('Magnetograma digitalizado * coef. angular (valores com shift)')

    ax3.scatter(horas, abs(plot1_livros-plot1_maggram))
    ax3.grid()
    ax3.title.set_text('Diferença absoluta entre médias registradas e médias calculadas')

    fig.set_size_inches(18,26)

    plt.show()