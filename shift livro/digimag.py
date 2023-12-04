from plot import plotmag
from numpy import load,hstack
from resampling import resampling
from tkinter import Tk
from tkinter.filedialog import askopenfilename
from matplotlib.pyplot import plot,show

# PRIMEIRO SELECIONA O LIVRO DE MEDIA E DEPOIS O MAGNETOGRAMA

Tk().withdraw()
linhaZ = load(askopenfilename(title='Selecione uma tabela de médias horárias (.npy)'))

#medias = hstack((linhaZ[15][13:],linhaZ[16][:13]))
# maggram = resampling()
#plotmag(medias,maggram)

medias2 = hstack((linhaZ[16][13:],linhaZ[17][:13]))
maggram2 = resampling()
plotmag(medias2,maggram2)

# medias2 = hstack((linhaZ[17][13:],linhaZ[18][:13]))
# maggram2 = resampling()
# plotmag(medias2,maggram2)

# medias2 = hstack((linhaZ[18][13:],linhaZ[19][:13]))
# maggram2 = resampling()
# plotmag(medias2,maggram2)

# medias2 = hstack((linhaZ[19][13:],linhaZ[20][:13]))
# maggram2 = resampling()
# plotmag(medias2,maggram2)


# print(linhaZ[15])
# print(linhaZ[16])
# print(linhaZ[17])
# print(linhaZ[18])
# print(linhaZ[19])
# print(linhaZ[20])