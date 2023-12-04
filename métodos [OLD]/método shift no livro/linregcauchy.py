from numpy import mean,array,ndarray
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit,least_squares


horas = []
for i in range(24):
    horas.append(i)
horas = array(horas).reshape(24,1)

def model(x,m,b):
        return m*x+b

def linregcauchy(medias,maggram):
    maggram = maggram + abs(min(maggram))
    maggram_medias_horarias = []

    for i in range(24):
        #center = 30 + 60*i
        start = 0 + 60*i
        stop = 60 + 60*i
        hour_centered_mean = mean(maggram[start:stop])
        maggram_medias_horarias.append(hour_centered_mean)

        # if i == 0:
             
        #      hour_centered_mean = mean(maggram[0:30])
        #      maggram_medias_horarias.append(hour_centered_mean)
        # elif i == 23:

        #     hour_centered_mean = mean(maggram[start:start+60])
        #     maggram_medias_horarias.append(hour_centered_mean)
        # else:
            
        #     hour_centered_mean = mean(maggram[1410:1440])
        #     maggram_medias_horarias.append(hour_centered_mean)
    
    maggram_medias_horarias = array(maggram_medias_horarias).reshape(24,1)
    
    maggram_medias_horarias = array(maggram_medias_horarias).reshape(24,1)
    
    target = array(medias).reshape(24,1)
    target_flat = ndarray.flatten(target)

    maggram_medias_horarias_flat = ndarray.flatten(maggram_medias_horarias)

    p1,cov  = curve_fit(model,maggram_medias_horarias_flat,target_flat,method='trf',loss = 'cauchy')
    
    return p1,maggram_medias_horarias,target,cov

    