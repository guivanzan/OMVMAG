from plot import plotmag
from numpy import load
from resampling import resampling
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# PRIMEIRO SELECIONA O LIVRO DE MEDIA E DEPOIS O MAGNETOGRAMA

Tk().withdraw()
linhaZ = load(askopenfilename(title='Selecione uma tabela de médias horárias (.npy)'))
#medias = hstack((linhaZ[15][9:],linhaZ[16][:9]))
medias1 = linhaZ[16][:12]
medias2 = linhaZ[16][12:]

maggram1,maggram2 = resampling()

plotmag(medias1,medias2,maggram1,maggram2)

### curve fit com as metades separadas e juntar depois