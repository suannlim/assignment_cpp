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


"""
In order to determine our sampling frequency, we have to ensure that it will
lead to a Nyquist frequency that is larger than the max frequency of our
function. As our input functions are not explicitly periodic, we assume that
outside the time period, it repeats periodically, so we take T as the duration
that our function is defined for

As for the Gaussian, we have our range of values centered on 0 so N/2 values
should be x<0 and N/2 values should be x>0 - so as to not shift our gaussian.
As there is no specific frequency of the Gaussian function, we sample using an
N that will give a frequency larger than that of h(t) but not too large so that
it is too computationally taxing on the computer

np.fft will automatically pad your sample value 

how to find wmax????

"""



#Frequency of h(t)
w_maxH=1/(7-5)


#Number of sample points
N=100

#Sample spacing
X=np.arange(-10,10,1/N)
#print(X)

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

#fourier h(t)
plt.figure(1)
plt.title("Fourier h(t)")
plt.xlabel("Frequency space")
#plt.xlim(-10,10)
plt.plot(xf,h_fft)

#fourier g(t)
plt.figure(2)
plt.title("Fourier g(t)")
plt.xlabel("Frequency space")
#plt.xlim(-0.5,0.5)
plt.plot(xf,g_fft)

#Find the fft convolution and the convolution
fftConvo=h_fft*g_fft
convo=np.fft.ifft(fftConvo)

plt.figure(3)
plt.title("Convolution of g(t) and h(t)")
plt.xlabel("Time space")
#plt.xlim(-300,0)
plt.plot(X,convo)


plt.figure(4)
plt.plot(X,g_time,label="g(t)")
plt.plot(X,h_time,label="h(t)")
plt.plot(X,convo,label="convolution")
plt.legend()












