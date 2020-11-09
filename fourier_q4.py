# -*- coding: utf-8 -*-

import numpy as np
import math
import matplotlib.pyplot as plt


"""
use numpy.fft to convolve the given signal function with a given
response function

using the convolution theorem, have to find fourier transform
of one and multiply with the fourier transform of the other

"""
#define the two given functions
def h(t):    
    if t<=7 and t>=5:
        function=4
    if t<5 or t>7:
        function=0
    return function


def g(t):
    exponent=(-1*(t**2))/4
    function=(1/math.sqrt(2*math.pi))*math.exp(exponent)
    return function

#Number of sample points
N=100

#Sample spacing
T=1.0/80
X=np.arange(-10,100,N)
print(X)

#sample h function
h_time=h(X)
print(h_time)

#sample g function
g_time=g(X)

#perform fourier transform
h_fft=np.fft(h_time)
g_fft=np.fft(g_time)

#find the new x values(Frequency)
xf=np.linspace(-10.0,1.0/(2.0*T),N/2)

plt.plot(xf,h_fft)








