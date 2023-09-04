__name__ = '__main__'
from ResNet import identity_block,convolutional_block,ResNet34
import numpy as np
from formatting import formating
import tkinter as tk
from tkinter.filedialog import askopenfilename
tk.Tk().withdraw() # part of the import if you are not using other tkinter functions
from tensorflow.keras import models

input_shape = (36, 18, 1)
model = ResNet34(input_shape=input_shape)
model.load_weights('cat11/.cp_model_4_pages/model')

def identify():
    digits = np.load(askopenfilename())
    
    labels = model.predict(digits)
    labels = np.argmax(labels,axis = 1)

    np.save('labels',formating(labels))

if __name__ == '__main__':
    identify()
