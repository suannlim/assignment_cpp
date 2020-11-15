# -*- coding: utf-8 -*-

def float_point_rounding(x):
    """
    This function finds the next representable number, higher and lower 
    than the given input value. It will then return the fractional rounding
    range of that number.
    
    INPUT:
    x - Input value to find the fractional rounding range of.
    
    OUTPUT:
    next_high - Next highest representable real number
    next_low - Next lowest representable real number
    fracRR - Fractional rounding range of input value

    """
    #adding 2^n where n is decreasing in increments of 1 until the 
    #computer can no longer represent the number and it returns to the
    #original input
    y=0
    counter=0
    while x!=y:
        y=x + (2**counter)
        counter=counter-1

        
    next_high = x+(2**(counter+2))    
    print("The next largest representable number is " + str(next_high))
    
    #similar to what is done above but instead we are taking away 2^n
    z=0
    counter_1=0
    while x!=z:
        z=x - (2**counter_1)
        counter_1=counter_1 - 1
    
    next_low = x - (2**(counter_1+2))
    print("The next lowest representable number is " + str(next_low))
    
    
    #finding the numerical difference between the next high, next low and
    #the original number and halving it to find the rounding range
    upper_diffHalf=(next_high - x)/2
    lower_diffHalf=(x-next_low)/2
    
    #find the total fractional rounding range 
    fracRR=(upper_diffHalf + lower_diffHalf)/x
    
    print("The fractional rounding range of " + str(x) + " is " + str(fracRR))
    
    return(next_high,next_low,fracRR)
    
    
    

        
    
    