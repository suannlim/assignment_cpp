

def firstOrder(t,Vout,R,C,Vin):
    """
    This function defines the first order differential equation we are solving.
    
    t - The time at which the ODE is being evaluated at
    Vout - Voltage out at the specified time
    R - Resistance of component in the circuit
    C - Capacitance of component in the circuit
    Vin - Voltage in at the specified time
    """
    return (Vin-(Vout*(1+R)))/(R*C)

def square_wave(V0,T,t0,tend,h):
    """
    This function defines the square wave we use as Vin for Q5e. A dictionary
    is used to find corresponding values of Vin at a specified time.
    
    V0 - Peak voltage of the square wave
    T- Time period of the wave
    t0 - Start time of the square wave
    tend - Time when square wave terminates
    h - Step size in time axis
    """

    #initialise arrays to store t and Vin values
    TimeVal=[]
    V=[]
    
    #Finding the number of iterations depending on the input step size
    n=int((tend-t0)/h)
    t=t0
    
    for i in range(n):
        t1 = (t - t0)
        TimeVal.append(t)
        #While bigger than time period, reduce it until it comes into range
        while t1 >= T:
            t1 = t1 - T
        # If within 0 and T/2, square wave function results to V0
        if t1 < T/2 and t1 >= 0:
            V.append(0)
        # Otherwise, it is within T/2 and T, sqf results to 0
        else:
            V.append(V0)
            
        #update t value
        t+=h
            
    res = {TimeVal[i]: V[i] for i in range(len(TimeVal))}        
    return res
   

def runge_kutta(t0,Vout,tend,h,Vin,T,IsSquare):
    """
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
    
    """
        
    #initialise array to store t,Q values
    t=[]
    t.append(t0)
    V=[]
    V.append(Vout)
    
    #find the number of steps/iterations
    n=int((tend-t0)/h)
    R=1
    C=1
    
    
    #checking for square wave input Vin
    if IsSquare:
        sqrmap=square_wave(Vin,T,t0,tend,h)
        
    #then we loop through the 4 equations n times to find the value of Q
    #at our given t
    for i in range(n):
        if IsSquare:
            Vin = sqrmap[t0]
        else:
            Vin = Vin
        f_a=firstOrder(t0,Vout,R,C,Vin)
        f_b=firstOrder(t0+(h*0.5),Vout + (f_a*0.5*h),R,C,Vin)
        f_c=firstOrder(t0+(h*0.5),Vout + (f_b*0.5*h),R,C,Vin)
        f_d=firstOrder(t0+h,Vout+(h*f_c),R,C,Vin)
        
        #update new Q0 value
        Vout=Vout + (h/6)*(f_a+(2*f_b)+(2*f_c)+f_d)
        V.append(Vout)
        #update new t value
        t0=t0+h
        t.append(t0)
        
    return(t,V,V[n])


#same concept as runge kutta, just different formula
def adam_bash(t0,Vout,tend,h,init_Vin,Vin):
    
    """
    This function defines the 4th Order Adam Bashforth method to solve for
    an ODE at a specified time with given initial conditions
    
    t0 - Initial time of ODE
    Vout - Output voltage of circuit at t0
    tend - Time at which function calculates Vout of the ODE
    h - Step size on time axis
    init_Vin - Value of input voltage at t<0
    
    """
    #find step size
    n=int((tend-t0)/h)
    R=1
    C=1
    Vin=0
    
    #euler steps to find V1
    k=10 #number of euler steps
    V0=Vout
    t_start=t0
    for l in range(k):
        V0=V0+((h/k)*firstOrder(t_start,V0,R,C,init_Vin))
        t_start=t_start+(h/k)
    V1=V0
    
    #now we can implement leap frog method
    Vneg1=V1-2*firstOrder(t0,Vout,R,C,init_Vin)*h
    Vneg2=Vout-2*firstOrder(t0-h,Vneg1,R,C,init_Vin)*h
    Vneg3=Vneg1-2*firstOrder(t0-(h*2),Vneg2,R,C,init_Vin)*h
    
    #store values V values in array
    V=[]
    V.append(Vneg3)
    V.append(Vneg2)
    V.append(Vneg1)
    V.append(Vout)
    
    #store t values in array
    t=[]
    for i in reversed(range(4)):
        t.append(t0-(h*i))
        
    #now we have all info we need and can implement adam bashforth method
    for i in range(n):
        f_a=firstOrder(t[i+3],V[i+3],R,C,Vin)
        f_b=firstOrder(t[i+2],V[i+2],R,C,Vin)
        f_c=firstOrder(t[i+1],V[i+2],R,C,Vin)
        f_d=firstOrder(t[i],V[i],R,C,Vin)
        
        V.append(V[i+3]+((h/24)*(55*f_a - 59*f_b + 37*f_c -9*f_d)))
        t.append(t[i+3]+h)
    
    return(t,V,V[n])
    
def OdeSolver(IsRK4, t0, Vout, tend, h, init_Vin,Vin,T,IsSquare):
    """
    This function is a switch that either solves the ODE using the RK4 method
    or the AB4 method. The default is RK4.
    
    IsRK4 - Boolean. If true, RK4 method is called. If false, AB4 method
            is called
    t0 - Initial time of ODE
    Vout - Output voltage of circuit at t0
    tend - Time at which function calculates Vout of the ODE
    h - Step size on time axis
    init_Vin - Value of input voltage at t<0 (only relevant to AB4)
    Vin - FOR RK4:If IsSquare=False, Vin is the input Voltage for t>0. If 
                    IsSquare=True, Vin is the peak voltage of the square wave.
                    
          FOR AB4: Value of input voltage at t>0
    T - Time period of square wave
    IsSquare - Boolean to check if Vin is a square wave
    
    """
    if IsRK4:
        t_RK=runge_kutta(t0,Vout,tend,h,Vin,T,IsSquare)[0]
        V_RK=runge_kutta(0,Vout,tend,h,Vin,T,IsSquare)[1]
        answer=runge_kutta(0,Vout,tend,h,Vin,T,IsSquare)[2]
        return(t_RK,V_RK,answer)
        
    else:
        t_AB=adam_bash(t0,Vout,tend,h,init_Vin,Vin)[0]
        V_AB=adam_bash(t0,Vout,tend,h,init_Vin,Vin)[1]
        answer=adam_bash(t0,Vout,tend,h,init_Vin,Vin)[2]
        return(t_AB,V_AB,answer)
        



    

            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
    