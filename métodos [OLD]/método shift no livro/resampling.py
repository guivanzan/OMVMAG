from numpy import array,ndarray
from pandas import read_csv
from scipy.signal import resample_poly
from fractions import Fraction
from tkinter import Tk
from tkinter.filedialog import askopenfilename

cabecalho = ['Horario','Componente']

def rat(n, denom_max = 1000):  
        x = Fraction(n).limit_denominator(denom_max) 
        return (x.numerator, x.denominator)

def resampling():
    
    Tk().withdraw()
    line = askopenfilename(title = 'Selecione um magnetograma digitalizado (.csv)')
    line = read_csv(line, names = cabecalho, header = None, on_bad_lines='skip')
    line = array(line['Componente'])

    n = len(line)
    [P,Q] = rat(1440/n)
    line = resample_poly(line,P,Q,padtype='mean')
#     line = ndarray.tolist(line)
#     del line[-1]
    line = array(line).reshape(1,1440)

    return line[0]
