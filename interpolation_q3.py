# -*- coding: utf-8 -*-

import numpy as np
import lu_decomp_q2 as lu




def lagrange_poly(X,Y):
    """
    This function will take a set of data points to find the polynomial
    that fits the points and outputs a set of Y values for a linearly spaced
    array of X values determined by the input
    
    X - Data points for x axis
    Y - Data points for y axis
    
    """
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
    This function uses the cubic spline algorithm to find a suitable 
    polynomial between each set of X points. Then using a linearly spaced
    array of new X values determiend by the range of the input values, it 
    outputs an array of Y values to be plotted.
    
    X - Data points for x axis
    Y - Data points for y axis
    
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
                
                interpolatedVal=(A_coeff*Y[i])+(B_coeff*Y[i+1])+\
                (C_coeff*secDeriv[i][0])+(D_coeff*secDeriv[i+1][0])
                new_Y.append(interpolatedVal)
    
    
    return(new_X,new_Y)           
        







            
            
        
            