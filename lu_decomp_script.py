# -*- coding: utf-8 -*-

import lu_decomp_q2 as lu
import numpy as np


A=[[3,1,0,0,0],[3,9,4,0,0],[0,8,20,10,0],[0,0,-22,31,-25],[0,0,0,-35,61]]
b=[[2],[5],[-4],[8],[9]]

#taking the upper matrix produced by lu_decomp
U=lu.lud(A)[0]
L=lu.lud(A)[1]

#finding the determinant of A
lu.determinant(U)

#solving for x
lu.substitution(U,L,b)

"""
in order to solve for A inverse, we need to solve for Ax=I, thus we use our
substitution function and replace b with the identity matrix. as our function
only takes 1d arrays for b, we call the function multiple times and compile
the solutions into one
"""

N=len(A)
identityMat=np.identity(N)
inverse=[]
for i in range(N):
    b=lu.column(identityMat,i)
    soln=lu.substitution(U,L,b)
    inverse.append(soln)
inverse=np.column_stack((inverse))
          
print(inverse)
        
    


