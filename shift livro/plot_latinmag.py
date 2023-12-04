from matplotlib.pyplot import subplots,show
from numpy import array,diag,sqrt
from linregrobust import linregrobust,model
from tempo import relogio

horas,horas2,minutes = relogio()


def plotmag(livro,maggram):

    p1_robust,plot1_maggram_robust,plot1_livros,cov_robust,goodIndexes,goodTargets,horasGoodIndex = linregrobust(livro,maggram)

    

    maggram = maggram + abs(min(maggram))
    plot1_maggram_model_robust = model(goodTargets,*p1_robust)
    plot2_robust = model(maggram,*p1_robust) 

    cov_robust = sqrt(diag(cov_robust))

    goodIndexesMin = array(goodIndexes) * 3600

    fig, (ax1) = subplots(1,1)

    ax1.plot(minutes, plot2_robust, '-m', linewidth = 1)
    ax1.scatter(horas2,plot1_livros)
    ax1.grid()
    #ax1.title.set_text(f' magenta: y = {p1_robust[0]:.2f}x + {p1_robust[1]:.2f}, stddev(m) = {cov_robust[0]:.2f}, stddev(b) = {cov_robust[1]:.2f} / azul: médias horárias registradas')
    ax1.title.set_text(f'Z(x) = {p1_robust[0]:.2f}x + {p1_robust[1]:.2f}')
                           
    show()
