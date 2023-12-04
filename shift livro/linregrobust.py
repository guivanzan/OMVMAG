from numpy import mean,array,ndarray,diag,sqrt
#import matplotlib.pyplot as plt
from scipy.optimize import curve_fit,least_squares


horas = []
for i in range(24):
    horas.append(i)
horas = array(horas).reshape(24,1)

def model(x,m,b):
        return m*x+b

def linregrobust(medias,maggram):
    maggram = maggram + abs(min(maggram))
    maggram_medias_horarias = []

    for i in range(24):
        center = 0 + 60*i
        if i == 0:
            # média centralizada na hora, até meia hora pra frente
            hour_centered_mean = mean(maggram[center:center+30])
            maggram_medias_horarias.append(hour_centered_mean)

        elif i == 23:
            # média centralizada na hora, até meia hora pra trás
            hour_centered_mean = mean(maggram[center-30:center])
            maggram_medias_horarias.append(hour_centered_mean)

        else:
            # média centralizada na hora, meia hora pra frente e pra trás
            hour_centered_mean = mean(maggram[center-30:center+30])
            maggram_medias_horarias.append(hour_centered_mean)
    
    maggram_medias_horarias = array(maggram_medias_horarias).reshape(24,1)
    
    maggram_medias_horarias = array(maggram_medias_horarias).reshape(24,1)
    
    target = array(medias).reshape(24,1)
    target_flat = ndarray.flatten(target)

    maggram_medias_horarias_flat = ndarray.flatten(maggram_medias_horarias)

    p1,cov  = curve_fit(model,maggram_medias_horarias_flat,target_flat,method='trf',loss='cauchy')

    # newTarget = model(maggram_medias_horarias,*p1)

    # absDeviation = abs(newTarget - target)

    # stdDev = sqrt(diag(cov))

    # goodTargets = []
    # goodMeans = []
    # goodIndexes = []
    # horasGoodIndex = ndarray.tolist(horas)
    # for i in range(len(absDeviation)):
    #      if absDeviation[i] < sqrt((stdDev[1]+stdDev[0])/2):
    #         goodIndexes.append(i)
    #         goodTargets.append(target[i])
    #         goodMeans.append(maggram_medias_horarias_flat[i])
    #      else:
    #         None
    # for i in range(len(goodIndexes)):
    #     step = -1-i
    #     del horasGoodIndex[goodIndexes[step]]
    # horasGoodIndex = array(horasGoodIndex)
    # goodTargets = array(goodTargets)
    # goodTargets = ndarray.flatten(goodTargets)

    # goodMeans = array(goodMeans)
    # goodMeans = ndarray.flatten(goodMeans)

    # p1,cov = curve_fit(model,goodMeans,goodTargets)
    
    #return p1,maggram_medias_horarias,target,cov,goodIndexes,goodTargets,horasGoodIndex
    return p1,maggram_medias_horarias,target,cov
    