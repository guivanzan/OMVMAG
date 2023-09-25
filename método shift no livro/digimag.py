from plot import plotmag
from numpy import load,hstack
from resampling import resampling
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# PRIMEIRO SELECIONA O LIVRO DE MEDIA E DEPOIS O MAGNETOGRAMA

Tk().withdraw()
linhaZ = load(askopenfilename(title='Selecione uma tabela de médias horárias (.npy)'))
medias = hstack((linhaZ[15][12:],linhaZ[16][:12]))
maggram = resampling()

plotmag(medias,maggram)