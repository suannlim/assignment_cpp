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
        function=np.append(function,\
                           (1/math.sqrt(2*math.pi))*math.exp(exponent))
    return function



#first we need to ensure that our number of samples is in the form 2^m
N=1000
newN=pow(2, math.ceil(math.log(N)/math.log(2)))

#now we set our X array for our time space values
X=np.linspace(-10,10,newN)


#sample h function
h_time=h(X)
#pad the values of h
h_pad=np.concatenate((h_time,np.zeros(newN)))

#sample g function
g_time=g(X)
#pad the values of g
g_pad=np.concatenate((g_time,np.zeros(newN)))

h_fft=np.fft.fft(h_pad)
g_fft=np.fft.fft(g_pad)

#Find the fft convolution and the convolution
fftConvo=h_fft*g_fft
convo=np.fft.ifft(fftConvo)
#now we splice our convolution array to get the middle half
start=round(len(convo)/4)
end=round((len(convo)*3)/4)
convoNew=convo[start:end]

#normalise our convolution by our step size
deltaT=X[1]-X[0]

#plotting the convolution of g and h
plt.figure(1)
plt.title("Convolution of g(t) and h(t)")
plt.xlabel("Time space")
plt.grid()
plt.plot(X,convoNew*deltaT)

#comparing the convolution against the original functions
plt.figure(2)
plt.title("Comparison of convolution and original functions")
plt.grid()
plt.plot(X,g_time,label="g(t)")
plt.plot(X,h_time,label="h(t)")
plt.plot(X,convoNew*deltaT,label="convolution")
plt.legend()












