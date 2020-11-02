# -*- coding: utf-8 -*-
import sympy as sym


def lagrange_poly(X,Y):
    
    # Find the number of distinct points, we create a polynomial of degree n-1
    n = len(X)
    
    # Initialise the list of coefficients
    coeff = []
    
    # Used to allow sympy to expand the expression
    x = sym.Symbol('x')
    
    # Initialise base string which stores the expression
    expBuilder = ""
    
    
    for i in range(n):
        multiply_sum=""
        for j in range(n):
            
            if (j + 1) == n and (i + 1) != n:
                multiply_sum += ("((x-" + str(X[j]) + ")/(" + \
                                             str(X[i]) + "-" + str(X[j]) + "))")
            elif (j + 2) == n and (i + 1) == n:
                multiply_sum += ("((x-" + str(X[j]) + ")/(" + \
                                             str(X[i]) + "-" + str(X[j]) + "))")
            elif j!=i:
                multiply_sum += ("((x-" + str(X[j]) + ")/(" + \
                                             str(X[i]) + "-" + str(X[j]) + ")) * ")
            else:
                continue
        
        if (i + 1) == n:
            expBuilder += multiply_sum
        else:     
            expBuilder += (multiply_sum + " + ")
        
        
    print(expBuilder)
        
    # Store the expanded polynomial in a new variable which we can use to 
    # extract the coefficients from
    polynomial = sym.expand(expBuilder)
    print(polynomial)
    return 0
        


sX = [0, 1, 2, 3]
sY = [-25, 0, 5, 10]

X=[-0.75,-0.5,-0.35,-0.1,0.05,0.1,0.23,0.29,0.48,0.6,0.92,1.05,1.5]
Y=[0.1,0.3,0.47,0.66,0.60,0.54,0.30,0.15,-0.32,-0.54,-0.6,-0.47,-0.08]



lagrange_poly(X,Y)



            
            
        
            