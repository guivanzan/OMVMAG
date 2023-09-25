import numpy as np
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

horas = []
for i in range(24):
    horas.append(i)
horas = np.array(horas).reshape(24,1)

def model(x,m,b):
        return m*x+b

def linreg(medias,maggram):
    #maggram = maggram + abs(np.min(maggram)) + 1
    maggram_medias_horarias = []

    for i in range(24):
        center = 0 + 60*i
        if i == 0:
             
             hour_centered_mean = np.mean(maggram[center:center+30])
             maggram_medias_horarias.append(hour_centered_mean)
        elif i == 23:
            hour_centered_mean = np.mean(maggram[center-30:center])
            maggram_medias_horarias.append(hour_centered_mean)
        else:
            hour_centered_mean = np.mean(maggram[center-30:center+30])
            maggram_medias_horarias.append(hour_centered_mean)
    
    maggram_medias_horarias = np.array(maggram_medias_horarias).reshape(24,1)

    # target = np.ndarray.tolist(medias)
    # del target[-1]
    # del target[0]
    # for k in range(len(target)):
    #     target[k] = float(target[k])
    
    target = np.array(medias).reshape(24,1)
    target_flat = np.ndarray.flatten(target)

    # target = np.array(medias)
    # target_flat = np.ndarray.flatten(target)

    maggram_medias_horarias_flat = np.ndarray.flatten(maggram_medias_horarias)

    p1,cov  = curve_fit(model,maggram_medias_horarias_flat,target_flat)
    
    return p1,maggram_medias_horarias,target

    