from numpy import array,mean,ndarray
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

horas = []
for i in range(24):
    horas.append(i)

horas1 = horas[:12]
horas2 = horas[12:]
horas1 = array(horas1).reshape(12,1)
horas2 = array(horas2).reshape(12,1)

def model(x,m,b):
        return m*x+b

def linreg(medias1,medias2,maggram1,maggram2):
    #maggram = maggram + abs(min(maggram)) + 1
    maggram_medias_horarias1 = []

    for i in range(12):
        center = 0 + 60*i
        if i == 0:
             
             hour_centered_mean = mean(maggram1[center:center+30])
             maggram_medias_horarias1.append(hour_centered_mean)
        elif i == 11:
             
             hour_centered_mean = mean(maggram1[center-30:center])
             maggram_medias_horarias1.append(hour_centered_mean)
        else:

            hour_centered_mean = mean(maggram1[center-30:center+30])
            maggram_medias_horarias1.append(hour_centered_mean)
    
    maggram_medias_horarias1 = array(maggram_medias_horarias1).reshape(12,1)
    
    
    target1 = array(medias1).reshape(12,1)
    target_flat = ndarray.flatten(target1)

    maggram_medias_horarias_flat1 = ndarray.flatten(maggram_medias_horarias1)

    p1,cov  = curve_fit(model,maggram_medias_horarias_flat1,target_flat)

    maggram_medias_horarias2 = []

    for i in range(12):
        center = 0 + 60*i
        if i == 0:

            hour_centered_mean = mean(maggram2[center:center+30])
            maggram_medias_horarias2.append(hour_centered_mean)
        elif i == 0:

            hour_centered_mean = mean(maggram2[center-30:center])
            maggram_medias_horarias2.append(hour_centered_mean)
        else:

            hour_centered_mean = mean(maggram2[center-30:center+30])
            maggram_medias_horarias2.append(hour_centered_mean)
    
    maggram_medias_horarias2 = array(maggram_medias_horarias2).reshape(12,1)
    
    
    target2 = array(medias2).reshape(12,1)
    target_flat = ndarray.flatten(target2)

    maggram_medias_horarias_flat2 = ndarray.flatten(maggram_medias_horarias2)

    p2,cov  = curve_fit(model,maggram_medias_horarias_flat2,target_flat)

    return p1,maggram_medias_horarias1,target2,p2,maggram_medias_horarias2,target2

    