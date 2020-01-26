def division(a, b):
    power, quotient = 0, 0
    
    while a >= (b << 1):
        b = b << 1
        power += 1
    # can skip above and initialize power to 32 or 64 assuming max num bits
    
    while power >= 0:
        if (a >= b):
            quotient += 1 << power 
            a = a - b 
        b = b >> 1 
        power -= 1
    
    return quotient

print(division(12, 3))