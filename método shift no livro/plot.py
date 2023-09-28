from matplotlib.pyplot import subplots,show
from numpy import array,diag,sqrt
from linreg import linreg,model
from linregcauchy import linregcauchy
from linregrobust import linregrobust

horas = []
for i in range(24):
    horas.append(i)
horas = array(horas).reshape(24,1)

horas2 = []
for i in range(24):
    horas2.append(horas[i]*3600)
horas2 = array(horas2).reshape(24,1)


minutes = []
for i in range(1440):
    minutes.append(60*i)
minutes = array(minutes)

def plotmag(livro,maggram):

    p1,plot1_maggram,plot1_livros,cov = linreg(livro,maggram)
    plot1_maggram_model = model(plot1_maggram,*p1)
    maggram = maggram + abs(min(maggram))
    plot2 = model(maggram,*p1)

    p1_cauchy,plot1_maggram_cauchy,lixo,cov_cauchy = linregcauchy(livro,maggram)
    plot1_maggram_model_cauchy = model(plot1_maggram_cauchy,*p1_cauchy)
    plot2_cauchy = model(maggram,*p1_cauchy)

    p1_robust,plot1_maggram_robust,lixo,cov_robust = linregrobust(livro,maggram)
    plot1_maggram_model_robust = model(plot1_maggram_robust,*p1_robust)
    plot2_robust = model(maggram,*p1_robust) 

    cov_robust = sqrt(diag(cov_robust))
    cov_cauchy = sqrt(diag(cov_cauchy))
    cov = sqrt(diag(cov))

    fig, (ax1, ax2, ax3) = subplots(3,1) 

    ax1.scatter(horas, plot1_livros)
    ax1.scatter(horas, plot1_maggram_model)
    ax1.scatter(horas, plot1_maggram_model_cauchy)
    ax1.scatter(horas, plot1_maggram_model_robust)
    ax1.grid()
    ax1.title.set_text('Laranja: médias calculadas / Azul: médias registradas / Verde: médias com redução de erro / Vermelho: médias com média robusta')

    ax2.plot(minutes, plot2, '-g', linewidth = 1)
    ax2.plot(minutes, plot2_cauchy,'-r', linewidth = 1)
    ax2.plot(minutes, plot2_robust, '-m', linewidth = 1)
    ax2.scatter(horas2,plot1_livros)
    ax2.grid()
    ax2.title.set_text(f'''         verde: y = {p1[0]:.2f}x + {p1[1]:.2f}, stddev(m) = {cov[0]:.2f}, stddev(b) = {cov[1]:.2f}
                        vermelho: y = {p1_cauchy[0]:.2f}x + {p1_cauchy[1]:.2f}, stddev(m) = {cov_cauchy[0]:.2f}, stddev(b) = {cov_cauchy[1]:.2f}
                        magenta: y = {p1_robust[0]:.2f}x + {p1_robust[1]:.2f}, stddev(m) = {cov_robust[0]:.2f}, stddev(b) = {cov_robust[1]:.2f}
                        azul: médias horárias registradas''')

    ax3.scatter(horas, abs(plot1_livros-plot1_maggram_model))
    ax3.scatter(horas, abs(plot1_livros-plot1_maggram_model_cauchy))
    ax3.scatter(horas, abs(plot1_livros-plot1_maggram_model_robust))
    ax3.grid()
    ax3.title.set_text('Diferença absoluta entre médias registradas e médias calculadas. Azul: ajuste linear, Laranja: ajuste com redução de erro, Verde: ajuste com média robusta')

    #fig.set_size_inches(18,26)

    show()
    # defasagem nas médias?