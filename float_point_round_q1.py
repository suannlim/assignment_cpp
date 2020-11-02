# -*- coding: utf-8 -*-


#find nearest representable real numbers higher and lower than a given floating
#point value
#find upper and lower difference within which real numbers are rounded
#then find the fractional value of this

def float_point_rounding(x):
    #while loop to find the next highest
    y=0
    counter=0
    while x!=y:
        y=x + (10**counter)
        counter=counter-1
        #print(y,counter)
        
    next_high = x+(10**(counter+2))    
    print("The next largest representable number is " + str(next_high))
    
    #while loop to find the next lowest
    z=0
    counter_1=0
    while x!=z:
        z=x - (10**counter_1)
        counter_1=counter_1 - 1
        #print(z,counter_1)
    
    next_low = x - (10**(counter_1+2))
    print("The next lowest representable number is " + str(next_low))
    
    upper_diff=next_high - x
    lower_diff=x-next_low
    
    upper_diff_frac= upper_diff/x
    lower_diff_frac=lower_diff/x
    
    print("The upper difference as a fraction is " + str(upper_diff_frac))
    print("The lower difference as a fraction is " + str(lower_diff_frac))
    
    return(next_high,next_low)
    
    
    

        
    
    