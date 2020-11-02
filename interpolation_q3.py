# -*- coding: utf-8 -*-


def lagrange_poly(X,Y):
    N=len(X)
    
    sum_poly=0
    for i in range(N):
        for j in range(N):
            multiply=1
            if j!=i:
                multiply=multiply*((x-X[j])/(X[i] - X[j]))*Y[i]
            else:
                continue
        
        sum_poly=sum_poly + multiply
        
    print(sum_poly)
    return sum_poly
        

X=[-0.75,-0.5,-0.35,-0.1,0.05,0.1,0.23,0.29,0.48,0.6,0.92,1.05,1.5]
Y=[0.1,0.3,0.47,0.66,0.60,0.54,0.30,0.15,-0.32,-0.54,-0.6,-0.47,-0.08]



lagrange_poly(X,Y)



            
            
        
            