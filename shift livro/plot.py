from matplotlib.pyplot import subplots,show
from numpy import array,diag,sqrt
from linregrobust import linregrobust,model
from tempo import relogio

horas,horas2,minutes = relogio()


def plotmag(livro,maggram):
    #p1_robust,plot1_maggram_robust,plot1_livros,cov_robust,goodIndexes,goodTargets,horasGoodIndex = linregrobust(livro,maggram)
    p1_robust,plot1_maggram_robust,plot1_livros,cov_robust = linregrobust(livro,maggram)

    maggram = maggram + abs(min(maggram))
    #plot1_maggram_model_robust = model(goodTargets,*p1_robust)
    plot1_maggram_model_robust = model(plot1_maggram_robust,*p1_robust)
    plot2_robust = model(maggram,*p1_robust) 

    cov_robust = sqrt(diag(cov_robust))

    #goodIndexesMin = array(goodIndexes) * 3600
    horas3 = array(horas) * 3600

    #fig, (ax1, ax2, ax3) = subplots(3,1)
    fig, (ax1, ax2, ax3) = subplots(3,1)


    ax1.scatter(horas, plot1_livros)
    #ax1.scatter(goodIndexes, goodTargets)
    ax1.scatter(horas, plot1_maggram_model_robust)
    ax1.grid()
    #ax1.title.set_text('Azul: médias registradas / Laranja: médias com média robusta')
    ax1.title.set_text('''Blue: means from the report book
                       Orange: means obtained after the analysis''')

    ax2.plot(minutes, plot2_robust, '-m', linewidth = 1)
    #ax2.scatter(goodIndexesMin,goodTargets)
    ax2.scatter(horas3, plot1_livros)
    ax2.grid()
    ax2.title.set_text(f' magenta: y = {p1_robust[0]:.2f}x + {p1_robust[1]:.2f}, stddev(m) = {cov_robust[0]:.2f}, stddev(b) = {cov_robust[1]:.2f} / azul: médias horárias registradas')
    #ax2.title.set_text(f'Z(x) = {p1_robust[0]:.2f}x + {p1_robust[1]:.2f}')

    ax3.scatter(horas,plot1_maggram_robust)
                           
    # ax3.plot(minutes, plot2_robust, '-m', linewidth = 1)
    # ax3.grid()
    # #ax3.title.set_text(f' magenta: y = {p1_robust[0]:.2f}x + {p1_robust[1]:.2f}, stddev(m) = {cov_robust[0]:.2f}, stddev(b) = {cov_robust[1]:.2f} / azul: médias horárias registradas')

    show()
