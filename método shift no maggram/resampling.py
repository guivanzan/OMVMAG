from numpy import array,hstack,ndarray
from pandas import read_csv
from scipy.signal import resample_poly
from fractions import Fraction
from tkinter import Tk
from tkinter.filedialog import askopenfilename

cabecalho = ['Horário','Componente']

def rat(n, denom_max = 1000):  
        x = Fraction(n).limit_denominator(denom_max) 
        return (x.numerator, x.denominator)

def resampling():
    
    Tk().withdraw()
    line_1 = askopenfilename(title = 'Selecione o magnetograma do dia anterior a ser trabalhado (.csv)')
    line_1 = read_csv(line_1, names = cabecalho, header = None, on_bad_lines='skip')
    line_1 = line_1[line_1['Horário'] < 0]
    line_1 = array(line_1['Componente'])

    n = len(line_1)
    [P,Q] = rat(720/n)
    line_1 = resample_poly(line_1,P,Q,padtype='mean')
    line_1 = ndarray.tolist(line_1)


    Tk().withdraw()
    line_2 = askopenfilename(title = 'Selecione um magnetograma do dia a ser trabalhado (.csv)')
    line_2 = read_csv(line_2, names = cabecalho, header = None, on_bad_lines='skip')
    line_2 = line_2[line_2['Horário'] < 0]
    line_2 = array(line_2['Componente'])

    n = len(line_2)
    [P,Q] = rat(720/n)
    line_2 = resample_poly(line_2,P,Q,padtype='mean')
    line_2 = ndarray.tolist(line_2)
    
    # for i in range(4):
    #       del line_1[0]
    # for i in range(4):
    #       del line_1[-1]
    # for i in range(4):
    #       del line_2[0]
    # for i in range(4):
    #       del line_2[-1]
          
    line_1 = array(line_1)
    line_2 = array(line_2)

    shift = abs(line_1[-1] - line_2[0])
    if line_2[0] > line_1[-1]:
          line_2 = line_2 - shift
    else:
          line_2 = line_2 + shift
    
    line = hstack((line_1,line_2)).reshape(1,1440)

    return line[0]

# resampling()
