"""
this script contains all the answers for the questions in the assignment
by importing the relevant modules and running the functions
"""

#%% Question 1a
import float_point_round_q1 as fpr

result=fpr.float_point_rounding(0.25)


#%% Question 1b
import float_point_round_q1 as fpr

#upper=fpr.float_point_rounding(result[0])
#lower=fpr.float_point_rounding(result[1])

#%% Question 2b

import lu_decomp_q2 as lu

A=[[3,1,0,0,0],[3,9,4,0,0],[0,8,20,10,0],[0,0,-22,31,-25],[0,0,0,-35,61]]
b=[[2],[5],[-4],[8],[9]]

#taking the upper matrix produced by lu_decomp
U=lu.lud(A)[0]
L=lu.lud(A)[1]

#finding the determinant of A
lu.determinant(U)

#%% Question 2d

import lu_decomp_q2 as lu

#solving for x
lu.substitution(U,L,b)

#%% Question 2e
import lu_decomp_q2 as lu
import numpy as np

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
