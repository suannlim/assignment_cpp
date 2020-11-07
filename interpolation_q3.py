# -*- coding: utf-8 -*-

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange
import lu_decomp_q2 as lu




def lagrange_poly(X,Y):
    
    #the lagrange function will take a set of data to find the polynomial 
    #that fits the points and outputs a set of Y values of a lin.space x
    #range of values that are appropriate to the given X
    
    N=len(X)
    
    #create a linearly spaced new set of X values
    new_X=np.arange(X[0],X[N-1],0.05)
    
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
        
    
    print(new_X)
    print(new_Y)
    return(new_X,new_Y)
    
    
def cubic_spline(X,Y):
    #the cubic spline algorithm should return an array of polynomials, one 
    #for each interval, N points and N-1 polynomials
    
    #number of data points
    N=len(X) 
    
    #create a linearly spaced new set of X values
    new_X=np.arange(X[0],X[N-1],0.1)
    
    #create an empty array to store interpolated Y values
    new_Y=[]
    
    #create an empty array that contain the second derivatives as well as
    #the boundary conditions for the natural spline
    secDeriv=[0 for y in range(N)]
    
    #generate the matrix for the simultaneous equations of second derivatives
    derivCoeff=[[0 for x in range(N)] for y in range(N)]
    for i in range(N):
        firstCoeff=(X[i]-X[i-1])/6
        if (i + 1) == N:
            secCoeff = 0
        else:
            secCoeff=(X[i+1]-X[i-1])/3
        if (i + 1) == N:
            thirdCoeff = 0
        else:
            thirdCoeff=(X[i+1]-X[i])/6
        for j in range(3):
           if j==0:
               derivCoeff[i][i+j]=firstCoeff
           if j==1:
               if i!=(N-1):
                   derivCoeff[i][i+j]=secCoeff
           if j==2:
               if i!=(N-1) and i!=(N-2):
                   derivCoeff[i][i+j]=thirdCoeff
                   
    print(derivCoeff)
    
    #generate array that contains solution to each equation
    matrixSoln=[[0]for x in range(N)]
    for i in range(N-1):
        firstTerm=(Y[i+1]-Y[i])/(X[i+1]-X[i])
        secTerm=(Y[i]-Y[i-1])/(X[i]-X[i-1])
        matrixSoln[i][0]= firstTerm - secTerm
        
    print("matrixSoln:")
    print(matrixSoln)    
    
    #import matrix LU decomposition and solver from q2 to solve for second
    #derivatives
    U=lu.lud(derivCoeff)[0]
    L=lu.lud(derivCoeff)[1]
    
    secDeriv=lu.substitution(U,L,matrixSoln)
    
    print("length of new X: " + str(len(new_X)))

    # Create a new running index for which polynomial we are using
    index = 0
        
    # For every new X value, we want to check which polynomial to use
    for x in new_X:
        
        # While the current range is incorrect, we go up one index
        while x >= X[index] and x >= X[index + 1]:
            index += 1
            
        if (index + 1) == len(secDeriv):
            break
            
        # If the current range is correct, we continue to the calculating of
        # coefficients
        if x >= X[index] and x <= X[index + 1]:
            
            # Calculate the coefficients
            A_coeff=(X[index+1]-x)/(X[index+1]-X[index])
            B_coeff=1-A_coeff
            C_coeff=(1/6)*(((A_coeff)**3)-A_coeff)*((X[index+1]-X[index])**2)
            D_coeff=(1/6)*(((B_coeff)**3)-B_coeff)*((X[index+1]-X[index])**2)
                
            new_Y.append((A_coeff*Y[index]) + (B_coeff*Y[index+1]) + \
            (C_coeff*secDeriv[index]) + (D_coeff*secDeriv[index+1]))
            
        else:  
            print("Oh no! Something went wrong.")
            return(new_Y)
    
    print(len(new_Y))
    print(new_Y)
    return(new_Y)


        
        
X=[-0.75,-0.5,-0.35,-0.1,0.05,0.1,0.23,0.29,0.48,0.6,0.92,1.05,1.5]
Y=[0.1,0.3,0.47,0.66,0.60,0.54,0.30,0.15,-0.32,-0.54,-0.6,-0.47,-0.08]


cubic_spline(X,Y)

#new_X=lagrange_poly(X,Y)[0]
#new_Y=lagrange_poly(X,Y)[1]


#poly=lagrange(X,Y)


#plt.scatter(X,Y)
#plt.scatter(new_X,new_Y)
#plt.show





            
            
        
            