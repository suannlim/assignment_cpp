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
    function=np.array([])
    for x in t:
        if x<=7 and x>=5:
            function=np.append(function,4)
        if x<5 or x>7:
            function=np.append(function,0)
    return function


def g(t):
    function=np.array([])
    for x in t:
        exponent=(-1*(x**2))/4
        function=np.append(function,(1/math.sqrt(2*math.pi))*math.exp(exponent))
    return function


#Number of sample points
N=100

#Sample spacing
X=np.arange(-10,100,1/N)
print(X)

#sample h function
h_time=h(X)
print(h_time)

#sample g function
g_time=g(X)

#perform fourier transform

h_fft=np.fft.fft(h_time)
g_fft=np.fft.fft(g_time)

#find the new x values(Frequency)
xf=(2*np.pi)/X

plt.figure(1)
plt.plot(xf,h_fft)
plt.figure(2)
plt.plot(xf,g_fft)

#Find the fft convolution and the convolution
fftConvo=h_fft*g_fft
convo=np.fft.ifft(fftConvo)

plt.figure(3)
plt.plot(X,convo)









