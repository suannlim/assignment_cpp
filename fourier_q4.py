# -*- coding: utf-8 -*-

import numpy as np
import math

#define the two given functions
def h(t):
    """
    Defining the top hat function.
    
    INPUT:
    t - array of time values
    
    OUTPUT:
    function - array of h values
    """
    
    function=np.array([])
    for x in t:
        if x<=7 and x>=5:
            function=np.append(function,4)
        if x<5 or x>7:
            function=np.append(function,0)
    return function


def g(t):
    """
    Defining the Gaussian function.
    
    INPUT:
    t - array of time values
    
    OUTPUT:
    function - array of g values
    """
    function=np.array([])
    for x in t:
        exponent=(-1*(x**2))/4
        function=np.append(function,\
                           (1/math.sqrt(2*math.pi))*math.exp(exponent))
    return function

def convolve(N,start,stop):
    """
    This function will convolve g(t) and h(t).
    
    INPUT:
    N - Number of sampling points
    start - Start point of range of samples
    stop - End point of range of samples
    
    OUTPUT:
    X - array of time values
    convoNew*deltaT - normalised convolved functions values
    
    """
    #first we need to ensure that our number of samples is in the form 2^m
    newN=pow(2, math.ceil(math.log(N)/math.log(2)))
    
    #now we set our X array for our time space values
    X=np.linspace(start,stop,newN)

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
    
    return(X,convoNew*deltaT)
    
    
    














