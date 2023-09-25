__name__ = '__main__'
from ResNet import identity_block,convolutional_block,ResNet34
import numpy as np
from formatting import formating
import tkinter as tk
from tkinter.filedialog import askopenfilename,askdirectory
 # part of the import if you are not using other tkinter functions

input_shape = (36, 18, 1)

def identify():
    model = ResNet34(input_shape=input_shape)

    weights = askdirectory()
    model.load_weights(weights)

    tk.Tk().withdraw()
    digits = np.load(askopenfilename())
    
    labels = model.predict(digits)
    labels = np.argmax(labels,axis = 1)

    np.save('labels',formating(labels))

if __name__ == '__main__':
    identify()
    