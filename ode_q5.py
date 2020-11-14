import matplotlib.pyplot as plt

def firstOrder(t,Vout,R,C,Vin):
    return (Vin-(Vout*(1+R)))/(R*C)

def square_wave(V0,T,t0,tend,h):
    """
    #V0 is max value of square wave
    #T is period of square wave
    #t0 is the start time
    #tend is the time step
    #h is the step size
    """
    #defining our square wave function to be used in part e

    #initialise arrays to store t and Vin values
    TimeVal=[]
    V=[]
    
    print("Tend: " + str(tend), "T0: " + str(t0))
    n=int((tend-t0)/h)
    t=t0
    
    for i in range(n):
        t1 = (t - t0)
        print(str(t1))
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
    print(res)     
    return res
   

def runge_kutta(t0,Vout,tend,h,Vin,T,IsSquare):
    """
    the runge kutta takes 4 pieces of information to calculate the next y
    value corresponding to the step in direction x
    
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
        
    return(t,V)


#same concept as runge kutta, just different formula
def adam_bash(t0,Vout,tend,h,init_Vin):
    
    """
    the adam bashforth method takes the values of the 3 previous steps in order
    to calculate the next value of y at the corresponding x

    in order to implement the adam bashforth method, we need V-1,V-2,V-3. this
    can be achieved using the leap frog method with some initial euler steps 
    to find V1
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
    
    print(t)
    print(V)
    return(t,V)


#
#define V at t<0
V=2    
    
t_RK=runge_kutta(0,1,1,0.001,0,0,False)[0]
V_RK=runge_kutta(0,1,1,0.001,0,0,False)[1]

t_AB=adam_bash(0,1,1,0.001,V)[0]
V_AB=adam_bash(0,1,1,0.001,V)[1]

#partc, comparing the runge kutta and adam bashforth 4th order
plt.figure(1)
plt.title("Adam Bashforth vs Runge Kutta 4th Order")
plt.grid()
plt.plot(t_RK,V_RK,label="Runge Kutta")
plt.plot(t_AB,V_AB, label="Adam Bashforth")
plt.legend()


#partd,varying step size on runge kutta method
#new runge kutta with double the step size of the original
t2_RK=runge_kutta(0,1,1,0.002,0,0,False)[0]
V2_RK=runge_kutta(0,1,1,0.002,0,0,False)[1]
plt.figure(2)
plt.title("Comparing varying step size of RK4")
plt.plot(t_RK,V_RK,label="RK4 step size 0.001")
plt.plot(t2_RK,V2_RK,label="RK4 step size 0.002")
plt.legend()
plt.grid()

#parte,now we use a square wave with a runge kutta
t3_RK=runge_kutta(0,1,1,0.001,2,0.2,True)[0]
V3_RK=runge_kutta(0,1,1,0.001,2,0.2,True)[1]
plt.figure(3)
plt.title("Runge Kutta with Square Wave")
plt.plot(t3,V3)






plt.show()



    

            
            
        
        
        
        
        
        
        
        
        
        
        
        
        
    