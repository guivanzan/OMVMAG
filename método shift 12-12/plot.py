import matplotlib.pyplot as plt
from numpy import array,hstack
from linreg import linreg,model

horas = []
for i in range(24):
    horas.append(i)
horas = array(horas).reshape(24,1)

minutes1 = []
minutes2 = []

for i in range(720):
    minutes1.append(60*i)
minutes1 = array(minutes1)

for i in range(720):
    minutes2.append(720*60 + 60*i)
minutes2 = array(minutes2)

def plotmag(livro1,livro2,maggram1,maggram2):

    p1,plot1_maggram1,plot1_livro1,p2,plot1_maggram2,plot1_livro2 = linreg(livro1,livro2,maggram1,maggram2)
    plot1_maggram1 = model(plot1_maggram1,*p1)
    plot1_maggram2 = model(plot1_maggram2,*p2)
    plot2_1 = model(maggram1,*p1)
    plot2_2 = model(maggram2,*p2)

    shift = abs(plot2_1[-1] - plot2_2[0])
    plot2_2 = plot2_2 + shift

    plot1_livros = hstack((plot1_livro1,plot1_livro2))
    plot1_maggram = hstack((plot1_maggram1,plot1_maggram2))

    fig, (ax1, ax2, ax3) = plt.subplots(3,1) 

    ax1.scatter(horas, plot1_livros)
    ax1.scatter(horas, plot1_maggram)
    ax1.grid()
    ax1.title.set_text('Laranja: médias calculadas / Azul: Médias registradas')

    ax2.plot(minutes1, plot2_1, '-g', linewidth = 1)
    ax2.plot(minutes2, plot2_2, '-g', linewidth = 1)    
    ax2.grid()
    ax2.title.set_text('Magnetograma digitalizado * coef. angular')

    ax3.scatter(horas, abs(plot1_livros-plot1_maggram))
    ax3.grid()
    ax3.title.set_text('Diferença absoluta entre médias registradas e médias calculadas')

    fig.set_size_inches(18,26)

    plt.show()