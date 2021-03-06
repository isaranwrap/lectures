# -*- coding: utf-8 -*-
"""00_Functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Eejuy69wODEwy3F0CUWlBpXfKMQUwLRc
"""

# Imports
import numpy as np
import matplotlib.pyplot as plt

"""Logistic function"""

# Parameters
L = 10
x_0 = 9
k = 0.3

xLEFT = -20 
xRIGHT = 30

x = np.linspace(xLEFT, xRIGHT, (xRIGHT - xLEFT + 1))
y = L / (np.exp(-k * (x - x_0)) + 1)

plt.plot(x, y)

ol

