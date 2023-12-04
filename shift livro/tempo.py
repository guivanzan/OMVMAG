from numpy import array

def relogio():
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

    return horas,horas2,minutes