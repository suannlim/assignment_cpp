# -*- coding: utf-8 -*-

"""
a) Vout(t))=Vin(t) - (R)*(dQ/dT)

    

runge kutta 4th order will find y value for a given x with a given step
size h using intial conditions (y0 and x0)

"""

def firstOrder(t,Q,R,C,Vin):
    return (Vin/R)-(Q/(R*C))
    

def runge_kutta(t0,Q0,t,h):
    #find the number of steps/iterations
    n=int((t-t0)/h)
    R=10
    C=1.6*(10**-19)
    Vin=2
    #then we loop through the 4 equations n times to find the value of Q
    #at our given t
    for i in range(n):
        f_a=firstOrder(t0,Q0,R,C,Vin)
        f_b=firstOrder(t0+(h*0.5),Q0 + (f_a*0.5*h),R,C,Vin)
        f_c=firstOrder(t0+(h*0.5),Q0 + (f_b*0.5*h),R,C,Vin)
        f_d=firstOrder(t0+h,Q0+(h*f_c),R,C,Vin)
        
        #update new Q0 value
        Q0=Q0 + (h/6)*(f_a+(2*f_b)+(2*f_c)+f_d)
        
        #update new t value
        t0=t0+h
        
    print(Q0)
    return Q0

runge_kutta(0,3.2*(10**-16),2,1)
    