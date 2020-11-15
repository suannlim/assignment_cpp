"""
This script contains all the answers for the questions in the assignment
by importing the relevant modules and running the functions.

*IMPORTANT* 
PLEASE RUN THE BLOCKS IN ORDER AS SOME QUESTIONS DEPEND ON PRE DEFINED 
VARIABLES FOUND IN PREVIOUS BLOCKS.
"""

#%% Question 1a
import float_point_round_q1 as fpr

result=fpr.float_point_rounding(0.25)

#%% Question 1b

print("For the next highest representable number after 0.25" )
upper=fpr.float_point_rounding(result[0])

print("For the next lowest representable number after 0.25" )
lower=fpr.float_point_rounding(result[1])

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
#solving for x
lu.substitution(U,L,b)

#%% Question 2e
#finding the inverse of the original matrix A

lu.findInverse(A,U,L)

#%% question 3c

import interpolation_q3 as inter
from scipy.interpolate import lagrange
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np

#input given values for X and Y        
X=[-0.75,-0.5,-0.35,-0.1,0.05,0.1,0.23,0.29,0.48,0.6,0.92,1.05,1.5]
Y=[0.1,0.3,0.47,0.66,0.60,0.54,0.30,0.15,-0.32,-0.54,-0.6,-0.47,-0.08]
N=len(X)

#interpolate values using lagrange polynomial method
x_lagrange=inter.lagrange_poly(X,Y)[0]
y_lagrange=inter.lagrange_poly(X,Y)[1]


#interpolate values using cubic spline method
x_spline=inter.cubic_spline(X,Y)[0]
y_spline=inter.cubic_spline(X,Y)[1]


#compare against scipy lagrange
poly=lagrange(X,Y)
new_X=np.arange(X[0],X[N-1],0.01)
Y_scipy=poly(new_X)


#compare against scipy spline
f=CubicSpline(X,Y)

#comparing the cubic spline method and lagrange method
plt.figure(1)
plt.title("Compare cubic spline method and lagrange method")
plt.plot(x_spline,y_spline,label="Spline Interpolation")
plt.plot(x_lagrange,y_lagrange,label="Lagrange approximation")
plt.grid()
plt.legend()

#validating lagrange interpolation method
plt.figure(2)
plt.title("Lagrange interpolation vs Scipy")
plt.plot(x_lagrange,y_lagrange,label="Lagrange")
plt.plot(new_X,Y_scipy,label="Scipy Lagrange")
plt.legend()
plt.grid()

#validating cubic spline method
plt.figure(3)
plt.title("Cubic spline vs Scipy")
plt.plot(x_spline,y_spline, label="Spline")
plt.plot(new_X,f(new_X),label="Scipy spline")
plt.legend()
plt.grid()

plt.show

print("Please see graph produced")

#%% question 4b

import matplotlib.pyplot as plt
import fourier_q4 as fourier

X=fourier.convolve(1000,-10,10)[0]
convolution=fourier.convolve(1000,-10,10)[1]
g_time=fourier.g(X)
h_time=fourier.h(X)

#plotting the convolution of g and h
plt.figure(1)
plt.title("Convolution of g(t) and h(t)")
plt.xlabel("Time space")
plt.grid()
plt.plot(X,convolution)

#comparing the convolution against the original functions
plt.figure(2)
plt.title("Comparison of convolution and original functions")
plt.grid()
plt.plot(X,g_time,label="g(t)")
plt.plot(X,h_time,label="h(t)")
plt.plot(X,convolution,label="convolution")
plt.legend()

print("Please see graph produced")

#%%question 5c
import ode_q5 as ode
import matplotlib.pyplot as plt

#Solve using the RK4 method
#If AB4 is required, change first True -> False
t=ode.OdeSolver(True,0,1,3,0.001,2,0,0,False)[0]
V=ode.OdeSolver(True,0,1,3,0.001,2,0,0,False)[1]
answer=ode.OdeSolver(True,0,1,3,0.001,2,0,0,False)[2]
print("The solution of Vout is " + str(answer) + "V")

plt.figure(1)
plt.title("ODE Solver")
plt.grid()
plt.plot(t,V,label="Runge Kutta")
plt.legend()



#%%question 5d
#Solve using RK4 for h=0.001
h1=0.001
t1=ode.OdeSolver(True,0,1,3,h1,2,0,0,False)[0]
V1=ode.OdeSolver(True,0,1,3,h1,2,0,0,False)[1]
answer1=ode.OdeSolver(True,0,1,3,h1,2,0,0,False)[2]
print("The solution of Vout is " + str(answer1) + "V" + " for h=" + str(h1))

#Solve using RK4 for h=0.002
h2=0.002
t2=ode.OdeSolver(True,0,1,3,h2,2,0,0,False)[0]
V2=ode.OdeSolver(True,0,1,3,h2,2,0,0,False)[1]
answer2=ode.OdeSolver(True,0,1,3,h2,2,0,0,False)[2]
print("The solution of Vout is " + str(answer2) + "V" + " for h=" + str(h2))


plt.title("Comparing varying step size of RK4")
plt.plot(t1,V1,label="RK4 step size 0.001")
plt.plot(t2,V2,label="RK4 step size 0.002")
plt.legend()
plt.grid()


#%%question 5e

#Time period of square wave is RC/2
t3=ode.OdeSolver(True,0,1,3,0.001,0,2,0.5,True)[0]
V3=ode.OdeSolver(True,0,1,3,0.001,0,2,0.5,True)[1]
answer3=ode.OdeSolver(True,0,1,3,0.001,0,2,0.5,True)[2]
print("The solution of Vout is " + str(answer3) + "V" + " for T=RC/2")

#Time period of square wave is 2RC
t4=ode.OdeSolver(True,0,1,3,0.001,0,2,2,True)[0]
V4=ode.OdeSolver(True,0,1,3,0.001,0,2,2,True)[1]
answer3=ode.OdeSolver(True,0,1,3,0.001,0,2,2,True)[2]
print("The solution of Vout is " + str(answer3) + "V" + " for T=2RC")

plt.title("Runge Kutta with Square Wave")
plt.plot(t3,V3,label="RC/2 period")
plt.plot(t4,V4,label="2RC period")
plt.legend()
plt.grid()


















