# Computational Physics - Assignment

This assignment has 5 questions that tests my understanding on the following topics: floating point variables, matrix methods, interpolation methods, 
fourier transforms and ordinary differential equations. My submission is comprimised of 5 function scripts and one answer script (answerScript.py). 
The answer script is split into blocks of code that are labelled with the respective question that they provide answers to. Please run the first block
of code first to import all the necessary modules. Subsequently, all blocks of code must be run in the order they are presented as some blocks may
refer to pre defined variables.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing 
purposes.

### Prerequisites

```
Matplotlib
Numpy
Scipy
```
Matplotlib is required to plot the output data on graphs. Numpy and scipy are used for validation using in-built methods as well as using the fast fourier 
numpy method for question 4.

### Obtaining solutions

As stated earlier, the blocks of code must be run in the order presented. The solutions will either be presented as graphs or numerical values and matrices 
in the console. In the cases where the answers are printed into the console, there will be a string above that details what the answer refers to. In the 
alternate case where the data is presented as a graph, the data points are colour coded in a legend. In the graphs titled "Validation", if there only
appears to be a singular curve, this is because my function output and the in-built functions are exactly equal - thus providing validation.

##Question 1 - Floating Point Variables

This section will detail the functions found in float_point_round_q1.py.

```
float_point_rounding(x):

This function finds the next representable number, higher and lower 
than the given input value. It will then return the fractional rounding
range of that number by adding the upper and lower difference and dividing 
by the original input value.
    
x - Input value to find the fractional rounding range of.
 
 ```
 
##Question2 - Matrix Methods

This section will detail the functions found in lu_decomp_q2.py.

```
lud(A):

This function decomposes a given NxN matrix into the upper and lower matrices. 
This is done using Crout's algorithm with the Doolittle choice (setting the
diagonal of the lower matrix to 1). 
    
A - Input matrix to decompose
```

```
determinant(U):

This function finds the determinant of a matrix using the multiplicative
sum of the diagonal of its upper matrix.
    
U - Upper matrix
```

```
substitution(U,L,b):

This function uses forward and backwards substitution as well as the 
decomposed upper and lower matrix to solve the matrix equation.
    
U - Upper matrix
L - Lower matrix
b - Solution matrix
```

```
column(matrix,i):

This function decomposes a given matrix into the ith collumn

matrix - Matrix to decompose
i - Column number desired
```

```
findInverse(A,U,L):
This function finds the inverse of a matrix using the solution of the 
matrix equation
    
A - Coefficient matrix
U - Upper matrix
L - Lower matrix
```

##Question 3 - Interpolation

This section will detail the functions found in interpolation_q3.py.

```
lagrange_poly(X,Y):

This function will take a set of data points to find the polynomial
that fits the points and outputs a set of Y values for a linearly spaced
array of X values determined by the input
    
X - Data points for x axis
Y - Data points for y axis
```

```
cubic_spline(X,Y):

This function uses the cubic spline algorithm to find a suitable 
polynomial between each set of X points. Then using a linearly spaced
array of new X values determiend by the range of the input values, it 
outputs an array of Y values to be plotted.
    
X - Data points for x axis
Y - Data points for y axis
```

##Question 4 - Fourier Transforms

This section will detail the functions found in fourier_q4.py

```
h(t):

Defining the top hat function.
   
t - array of time values
```

```
g(t):

Defining the gaussian function.

t- array of time values
```

```
convolve(N,start,stop):

This function will convolve g(t) and h(t) using the in-built np.fft
method as well as the convolution theorem.
    
N - Number of sampling points
start - Start point of range of samples
stop - End point of range of samples
```

##Question 5 - Ordinary Differential Equations

```
firstOrder(t,Vout,R,C,Vin):

This function defines the first order differential equation we are solving.
    
t - The time at which the ODE is being evaluated at
Vout - Voltage out at the specified time
R - Resistance of component in the circuit
C - Capacitance of component in the circuit
Vin - Voltage in at the specified time
```
```
square_wave(V0,T,t0,tend,h):

This function defines the square wave we use as Vin for Q5e. A dictionary
is used to find corresponding values of Vin at a specified time.
    
V0 - Peak voltage of the square wave
T- Time period of the wave
t0 - Start time of the square wave
tend - Time when square wave terminates
h - Step size in time axis
```
```
runge_kutta(t0,Vout,tend,h,Vin,T,IsSquare):

This function defines the Runge Kutta 4th order equation to solve for 
our ODE at a specified time.
    
t0 - Initial time of the ODE
Vout - Time at which functions calculates Vout of ODE
tend - Time at which we want to find Vout
h - Step size in time axis
Vin - If IsSquare=False, Vin is the input Voltage for t>0. If 
IsSquare=True, Vin is the peak voltage of the square wave.
T - Time period of square wave
IsSquare - Boolean to check if Vin is a square wave

```

```
adam_bash(t0,Vout,tend,h,init_Vin,Vin):
    
This function defines the 4th Order Adam Bashforth method to solve for
an ODE at a specified time with given initial conditions
    
t0 - Initial time of ODE
Vout - Output voltage of circuit at t0
tend - Time at which function calculates Vout of the ODE
h - Step size on time axis
init_Vin - Value of input voltage at t<0

```

```
OdeSolver(IsRK4, t0, Vout, tend, h, init_Vin,Vin,T,IsSquare):

This function is a switch that either solves the ODE using the RK4 method
or the AB4 method. The default is RK4.
    
IsRK4 - Boolean. If true, RK4 method is called. If false, AB4 method
        is called
t0 - Initial time of ODE
Vout - Output voltage of circuit at t0
tend - Time at which function calculates Vout of the ODE
h - Step size on time axis
init_Vin - Value of input voltage at t<0 (only relevant to AB4)
Vin - FOR RK4:If IsSquare=False, Vin is the input Voltage for t>0. 
              If IsSquare=True, Vin is the peak voltage of the square wave.
                    
      FOR AB4: Value of input voltage at t>0
T - Time period of square wave
IsSquare - Boolean to check if Vin is a square wave

```

##Ending
Thanks for reading! If you have any issues running the code, please contact me at su.lim18@imperial.ac.uk










