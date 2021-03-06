"""
This script contains all the answers for the questions in the assignment
by importing the relevant modules and running the functions.

*IMPORTANT* 
PLEASE RUN THE BLOCKS IN ORDER AS SOME QUESTIONS DEPEND ON PRE DEFINED 
VARIABLES FOUND IN PREVIOUS BLOCKS.

Please use the "run current cell" function whilst hovering over the desired
cell, rather than running the entire script at once. These provides outputs
for the answers one by one rather than all at once.
"""
#%%
"""
*PLEASE RUN THIS BLOCK FIRST TO IMPORT ALL RELEVANT MODULES*
"""
import float_point_round_q1 as fpr
import lu_decomp_q2 as lu
import interpolation_q3 as inter
from scipy.interpolate import lagrange
from scipy.interpolate import CubicSpline
import matplotlib.pyplot as plt
import numpy as np
import fourier_q4 as fourier
import ode_q5 as ode

#%% Question 1a

result=fpr.float_point_rounding(0.25)

#Validate result using np.nextafter()
real_high=np.nextafter(0.25,1)
real_low=np.nextafter(0.25,0)
print("The true next high and next low values are " + str(real_high) + " and "\
      + str(real_low))

#%% Question 1b

#Finding the rounding range of the next highest number after 0.25
print("For the next highest representable number after 0.25" )
fpr.float_point_rounding(result[0])

#Validating these values
real_high1=np.nextafter(result[0],1)
real_low1=np.nextafter(result[0],0)
print("The true next high and next low values are " + str(real_high1)+" and " \
      + str(real_low1))


#Finding the rounding range of the next lowest number after 0.25
print("For the next lowest representable number after 0.25" )
fpr.float_point_rounding(result[1])

#Again performing validation
real_high2=np.nextafter(result[1],1)
real_low2=np.nextafter(result[1],0)
print("The true next high and next low values are " + str(real_high2)+" and " \
      + str(real_low2))

#%% Question 2b

A=[[3,1,0,0,0],[3,9,4,0,0],[0,8,20,10,0],[0,0,-22,31,-25],[0,0,0,-35,61]]
b=[[2],[5],[-4],[8],[9]]

#taking the upper matrix produced by lu_decomp
U=lu.lud(A)[0]
L=lu.lud(A)[1]

print("The upper matrix is")
print(U)
print("The lower matrix is")
print(L)

#validation to check that the multiplication of upper and lower matrix returns 
#A
original = np.dot(L,U)
print("This matrix is L*U and should result in the original input matrix")
print(original)

#finding the determinant of A
lu.determinant(U)

#Validating our determinant using numpy
det = np.linalg.det(A)
print("The true determinant is " + str(det))

#%% Question 2d
#solving for x
mySolution=lu.substitution(U,L,b)
print("The solution given by my algorithm is")
print(mySolution)

#Validating our solution using numpy
solution=np.linalg.solve(A,b)
print("The true solution given by NumPy is")
print(solution)

#%% Question 2e
#finding the inverse of the original matrix A
myInverse=lu.findInverse(A,U,L)
print("The inverse of the original matrix (given by my function) is")
print(myInverse)

#Validating using numpy
trueInverse=np.linalg.inv(A)
print("The true inverse given by numpy is")
print(trueInverse)

#%% question 3c

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
new_X=np.arange(X[0],X[N-1],0.001)
Y_scipy=poly(new_X)


#compare against scipy spline
f=CubicSpline(X,Y,bc_type='natural')

#comparing the cubic spline method and lagrange method
plt.figure(1)
plt.title("Compare cubic spline method and lagrange method")
plt.plot(x_spline,y_spline,label="Spline Interpolation")
plt.plot(X,Y,"x",label="Data points")
plt.plot(x_lagrange,y_lagrange,label="Lagrange approximation")
plt.grid()
plt.legend()

#validating lagrange interpolation method
plt.figure(2)
plt.title("Validation of Lagrange method")
plt.plot(x_lagrange,y_lagrange,label="Lagrange")
plt.plot(X,Y,"x",label="Data points")
plt.plot(new_X,Y_scipy,label="Scipy Lagrange")
plt.legend()
plt.grid()

#validating cubic spline method
plt.figure(3)
plt.title("Validation of Cubic Spline method")
plt.plot(x_spline,y_spline, label="Spline")
plt.plot(X,Y,"x",label="Data points")
plt.plot(new_X,f(new_X),label="Scipy spline")
plt.legend()
plt.grid()

plt.show

print("Please see graph produced")

#%% question 4b

X=fourier.convolve(1000,-10,10)[0]
convolution=fourier.convolve(1000,-10,10)[1]
g_time=fourier.g(X)
h_time=fourier.h(X)

#Validate using numpy convolve function
del_t=X[1]-X[0]
trueConvolve=np.convolve(g_time,h_time,mode='same')*del_t

#plotting the convolution of g and h
plt.figure(1)
plt.title("Validation of convolution using numpy")
plt.xlabel("Time space")
plt.grid()
plt.plot(X,convolution,label="My script convolution")
plt.plot(X,trueConvolve,label="Numpy convolution")
plt.legend()
plt.xlabel("Time")

#comparing the convolution against the original functions
plt.figure(2)
plt.title("Comparison of convolution and original functions")
plt.grid()
plt.plot(X,g_time,label="g(t)")
plt.plot(X,h_time,label="h(t)")
plt.plot(X,convolution,label="convolution")
plt.legend()
plt.xlabel("Time")

print("Please see graph produced")

#%%question 5a
"""
Start with Vin-Vout=R*(dQ/dt)
Substitute in Q=C*Vout

Vin-Vout=R*C*(dVout/dt)
sub t_new=t/RC 
then change t_new back to t

the change of variable gives us 
dVout/dt = Vin- Vout

"""
#%%question 5c

#Solve using the RK4 method
#If AB4 is required, change first True -> False
t=ode.OdeSolver(True,0,1,3,0.01,2,0,0,False)[0]
V=ode.OdeSolver(True,0,1,3,0.01,2,0,0,False)[1]
answer=ode.OdeSolver(True,0,1,3,0.001,2,0,0,False)[2]
print("The solution of Vout is " + str(answer) + "V")

#We can validate the graph by plotting the analytical solution of the ODE
V_analytical=ode.analyticalSoln(t)
trueAnswer=V_analytical[-1]
print("The analytical answer is " + str(trueAnswer) + "V")

#Plot the graph
plt.figure(1)
plt.title("ODE Solver")
plt.grid()
plt.plot(t,V,label="Runge Kutta or Adam Bashforth")
plt.plot(t,V_analytical,label="Analytical Solution")
plt.legend()
plt.xlabel("Time")
print("Please see graph produced")


#%%question 5d
#Solve using RK4 for h=0.001
h1=0.01
t1=ode.OdeSolver(True,0,1,3,h1,2,0,0,False)[0]
V1=ode.OdeSolver(True,0,1,3,h1,2,0,0,False)[1]
answer1=ode.OdeSolver(True,0,1,3,h1,2,0,0,False)[2]
print("The solution of Vout is " + str(answer1) + "V" + " for h=" + str(h1))

#Solve using RK4 for h=0.002
h2=0.02
t2=ode.OdeSolver(True,0,1,3,h2,2,0,0,False)[0]
V2=ode.OdeSolver(True,0,1,3,h2,2,0,0,False)[1]
answer2=ode.OdeSolver(True,0,1,3,h2,2,0,0,False)[2]
print("The solution of Vout is " + str(answer2) + "V" + " for h=" + str(h2))

#Comparing percentage error to analytical result 
trueVal=V_analytical[-1]
error1=((answer1-trueVal)/trueVal)
error2=((answer2-trueVal)/trueVal)
print("The error for h=0.01 and h=0.02 is")
print(error1,error2)


#plot the graph
plt.title("Comparing varying step size of RK4")
plt.plot(t1,V1,label="RK4 step size 0.001")
plt.plot(t2,V2,label="RK4 step size 0.002")
plt.legend()
plt.grid()
plt.xlabel("Time")
print("Please see graph produced")


#%%question 5e

#Time period of square wave is RC/2
t3=ode.OdeSolver(True,0,1,3,0.01,0,1,0.5,True)[0]
V3=ode.OdeSolver(True,0,1,3,0.01,0,1,0.5,True)[1]
answer3=ode.OdeSolver(True,0,1,3,0.01,0,1,0.5,True)[2]
print("The solution of Vout is " + str(answer3) + "V" + " for T=RC/2")

#Time period of square wave is 2RC
t4=ode.OdeSolver(True,0,1,3,0.001,0,1,1,True)[0]
V4=ode.OdeSolver(True,0,1,3,0.001,0,1,1,True)[1]
answer3=ode.OdeSolver(True,0,1,3,0.001,0,1,1,True)[2]
print("The solution of Vout is " + str(answer3) + "V" + " for T=2RC")

#Plot the graph
plt.title("Runge Kutta with Square Wave")
plt.plot(t3,V3,label="RC/2 period")
plt.plot(t4,V4,label="2RC period")
plt.legend()
plt.xlabel("Time")
plt.grid()
print("Please see graph produced")
