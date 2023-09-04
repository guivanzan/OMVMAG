import numpy as np

def formating(array):
    formatedArray = []
    for i in range(len(array)):
        formatedArray.append(str(array[i]-1))
    
    for j in range(len(formatedArray)):
        if formatedArray[j] == '-1':
            formatedArray[j] = ' '
            
    return formatedArray