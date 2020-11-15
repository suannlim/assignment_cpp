# -*- coding: utf-8 -*-

def float_point_rounding(x):
    """
    This function finds the next representable number, higher and lower 
    than the given input value. It will then return the fractional rounding
    range of that number.
    
    x - Input value to find the fractional rounding range of.
    
    """
    y=0
    counter=0
    while x!=y:
        y=x + (2**counter)
        counter=counter-1

        
    next_high = x+(2**(counter+2))    
    print("The next largest representable number is " + str(next_high))
    
    #the while loops repeatedly prints the given input value by minusing
    #1 in factors of 10 until it can no longer be representable and returns
    #to the original value
    z=0
    counter_1=0
    while x!=z:
        z=x - (2**counter_1)
        counter_1=counter_1 - 1
    
    next_low = x - (2**(counter_1+2))
    print("The next lowest representable number is " + str(next_low))
    
    
    #finding the numerical difference between the next high, next low and
    #the original number
    upper_diff=next_high - x
    lower_diff=x-next_low
    
    #find the total fractional rounding range 
    fracRR=(upper_diff + lower_diff)/x
    
    print("The fractional rounding range of " + str(x) + " is " + str(fracRR))
    
    return(next_high,next_low)
    
    
    

        
    
    