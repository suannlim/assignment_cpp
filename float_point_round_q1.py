# -*- coding: utf-8 -*-



def float_point_rounding(x):
    
    """
    #the while loops keeps printing the given input value with more decimal
    #places ending in 1 until it can no longer be extended and is equal 
    #to the original value
    
    """
    y=0
    counter=0
    while x!=y:
        y=x + (10**counter)
        counter=counter-1

        
    next_high = x+(10**(counter+2))    
    print("The next largest representable number is " + str(next_high))
    
    #the while loops repeatedly prints the given input value by minusing
    #1 in factors of 10 until it can no longer be representable and returns
    #to the original value
    z=0
    counter_1=0
    while x!=z:
        z=x - (10**counter_1)
        counter_1=counter_1 - 1
    
    next_low = x - (10**(counter_1+2))
    print("The next lowest representable number is " + str(next_low))
    
    
    #finding the numerical difference between the next high, next low and
    #the original number
    upper_diff=next_high - x
    lower_diff=x-next_low
    
    #finding the fractional representation of the difference and original 
    #number
    upper_diff_frac= upper_diff/x
    lower_diff_frac=lower_diff/x
    
    print("The upper difference as a fraction is " + str(upper_diff_frac))
    print("The lower difference as a fraction is " + str(lower_diff_frac))
    
    return(next_high,next_low)
    
    
    

        
    
    