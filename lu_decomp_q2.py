# -*- coding: utf-8 -*-

#write a function that decomposes a matrix into the upper and lower matrices
#using crout's algorithm

import numpy as np

def lud(A):
    
    rows = len(A)
    columns = len(A[0])
    
    # Create zero matrix with same dimensions as A
    U=[[0 for y in range(columns)] for x in range(rows)]
    L=[[0 for n in range(columns)] for m in range(rows)]
    
    for q in range(columns):
        
        # Set L diagonal values to 1
        L[q][q]=1
     
     # For each U and L column
    for j in range(columns):
         
        # Loop through the column values of U
        for i in range(rows):
            
            # Condition to calculate value
            
            if i<=j:
                
                # Line 37 to 45 will calculate and set accordingly the values of 
                # the matrix U. 
                
                # Initialise a U counter
                
                sum_U = 0
                
                # This loop is for the sum in the U equation
                
                for k in range(i):
                    
                    sum_U = sum_U + (L[i][k] * U[k][j])
                  
                U[i][j] = A[i][j] - sum_U
                
               
            else:
                
                continue
            
        # Loop through the column values of L
        for i in range(rows):

            # Condition to calculate value
            
            if i>=j:
                
                # Line 65 to 73 will calculate and set accordingly the values of 
                # the matrix L. 
                
                # Initialise a L counter
                
                sum_L = 0
                
                # This loop is for the sum in the L equation
                
                for k in range(j):
                    
                    sum_L = sum_L + (L[i][k] * U[k][j])
                
                L[i][j]=(A[i][j] - sum_L)/U[j][j]
                
                
            else:
                
                continue
            
    return(U,L)



def determinant(U):
    #this function uses LU decomposition to find the determinant of a matrix
    #as the det is the multiplicative sum of the diagonal of U
    diagonal=1
    for x in range(len(U)):
        diagonal = diagonal * U[x][x]
    print("This is the determinant " + str(diagonal))
    

def substitution(U,L,b):
    #this function will use forward and backward substitution for the 
    #x vector 
    
    #forward substitution using L
    y=[0 for r in range(len(L))]
    for i in range(len(y)):
        y[i]=(b[i]-np.dot(y,L[i]))/L[i][i]
        
    #now backwards substitution
    x=[0 for p in range(len(U))]
    for i in reversed(range(len(U))):
        x[i]=(y[i]-np.dot(x,U[i]))/U[i][i]
    
    return x

def column(matrix,i):
    return [row[i] for row in matrix]





    
    

