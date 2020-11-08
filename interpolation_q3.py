# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
from scipy.interpolate import CubicSpline
import lu_decomp_q2 as lu




def lagrange_poly(X,Y):
    
    #the lagrange function will take a set of data to find the polynomial 
    #that fits the points and outputs a set of Y values of a lin.space x
    #range of values that are appropriate to the given X
    
    N=len(X)
    
    #create a linearly spaced new set of X values
    new_X=np.arange(X[0],X[N-1],0.01)
    
    #empty array to store corresponding Y values
    new_Y=[]
    
    #this loop will iterate through the new values of X to input into the
    #polynomial found using the formula
    for k in range(len(new_X)):
        #function sum stores the sum to n part of the formula for each
        #new X value
        function_sum=0
        
        #the i loop iterates through the sum
        for i in range(N):
            #initiate multiply_sum counter to store the multiplicative sum
            #in the formula
            multiply_sum=1
            
            for j in range(N):
                #if statement to prevent dividing by zero
                if i!=j:
                    factor = ((new_X[k]-X[j])/(X[i]-X[j]))
                    multiply_sum=factor*multiply_sum
                else:
                    continue

            function_sum = function_sum + (multiply_sum*Y[i])
        new_Y.append(function_sum)
        
    
    return(new_X,new_Y)
    
    
def cubic_spline(X,Y):
    
    """
    the cubic spline algorithm takes an array of X and Y values and finds a 
    suitable polynomial between each set of X points. we can then input a
    new array of X values into each of these polynomials to find a new
    array of Y values that fit the points
    """
    
    #number of data points
    N=len(X)
    
    
    #create a linearly spaced new set of X values
    new_X=np.arange(X[0],X[N-1],0.01)
    
    #create an empty array to store interpolated Y values
    new_Y=[]
    
    
    #generate the matrix for the simultaneous equations of second derivatives
    derivCoeff=[[0 for x in range(N)] for y in range(N)]
    
    for i in range(N):
        
        if i>=1 and i<=(N-2):
            firstCoeff=(X[i]-X[i-1])/6
            secCoeff=(X[i+1]-X[i-1])/3
            thirdCoeff=(X[i+1]-X[i])/6
            
            derivCoeff[i][i-1]=firstCoeff
            derivCoeff[i][i]=secCoeff
            derivCoeff[i][i+1]=thirdCoeff
            
    derivCoeff[0][0]=1
    derivCoeff[N-1][N-1]=1
            
     
        
    #generate array that contains solution to each equation
    matrixSoln=[[0]for x in range(N)]
    for i in range(N):
        
        if i>=1 and i<=(N-2):
            firstTerm=(Y[i+1]-Y[i])/(X[i+1]-X[i])
            secTerm=(Y[i]-Y[i-1])/(X[i]-X[i-1])
            matrixSoln[i][0]= firstTerm - secTerm
        
    
    #import matrix LU decomposition and solver from q2 to solve for second
    #derivatives
    U=lu.lud(derivCoeff)[0]
    L=lu.lud(derivCoeff)[1]
    
    secDeriv=lu.substitution(U,L,matrixSoln)

    
    
    # For every new X value, we want to check which polynomial to use
    for x in range(len(new_X)):
        
        for i in range(N-1):
            
            if X[i]<=new_X[x] and new_X[x]<=X[i+1]:
                
                A_coeff=(X[i+1]-new_X[x])/(X[i+1]-X[i])
                B_coeff=1-A_coeff
                C_coeff=(1/6)*(((A_coeff)**3)-A_coeff)*((X[i+1]-X[i])**2)
                D_coeff=(1/6)*(((B_coeff)**3)-B_coeff)*((X[i+1]-X[i])**2) 
                
                interpolatedVal=(A_coeff*Y[i])+(B_coeff*Y[i+1])+(C_coeff*secDeriv[i][0])+(D_coeff*secDeriv[i+1][0])
                new_Y.append(interpolatedVal)
    
    
    return(new_X,new_Y)           
        



#input given values for X and Y        
X=[-0.75,-0.5,-0.35,-0.1,0.05,0.1,0.23,0.29,0.48,0.6,0.92,1.05,1.5]
Y=[0.1,0.3,0.47,0.66,0.60,0.54,0.30,0.15,-0.32,-0.54,-0.6,-0.47,-0.08]


#interpolate values using lagrange polynomial method
x_lagrange=lagrange_poly(X,Y)[0]
y_lagrange=lagrange_poly(X,Y)[1]


#interpolate values using cubic spline method
x_spline=cubic_spline(X,Y)[0]
y_spline=cubic_spline(X,Y)[1]


#compare against scipy lagrange
poly=lagrange(X,Y)
N=len(X)
new_X=np.arange(X[0],X[N-1],0.01)
print(poly)
Y_scipy=poly(new_X)


#compare against scipy spline
f=CubicSpline(X,Y)
plt.plot(new_X,f(new_X))

plt.plot(x_spline,y_spline)






plt.show








            
            
        
            