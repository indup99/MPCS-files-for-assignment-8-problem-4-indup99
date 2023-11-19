#Indumathi Prakash

def greatest_common_divisor(a,b):
    """The gcd function takes two whole numbers and returns the gcd"""
    #checks for the two whole numbers
    if isinstance(a, int) == True and isinstance(b, int) == True:
        # if we recursively use the gcd rule and get here then the gcd is a
        if b == 0:
            return a
            # return the greatest common divisor
        # if we dont get to that 0 format then the greatest common divisor function is called again
        else:
            r = a % b
            return greatest_common_divisor(b, r)
    else:
        print("Choose whole numbers please")
 
#my test
#print(greatest_common_divisor(-20,10))