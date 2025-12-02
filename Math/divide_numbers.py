'''
Divide two numbers without using multiplication, division, and modulus operator

'''

def divide(dividend, divisor):
    quotient = 0
    lol = abs(dividend)
    while lol - abs(divisor) >= 0:
        lol -= abs(divisor)
        quotient +=1 
    if divisor < 0 and dividend < 0:
        return quotient 
    if divisor < 0 or dividend <0:
        return -quotient
    return quotient

print(divide(0, 1))
