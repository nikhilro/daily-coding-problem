def power(x, y): # O(log y) time
    neg, y, rem = y < 0, abs(y), 1
    while y > 1:
        if y % 2:
            rem *= x 
        x, y = x * x, y // 2
    return x * rem if not neg else 1 / (x * rem)


print(pow(3, 10), power(3, 10), pow(3, 11), power(3, 11), pow(3, -11), power(3, -11))