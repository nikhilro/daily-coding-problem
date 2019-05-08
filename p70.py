def find_perfect_naive(nth):
    cur, num = 0, 10
    while True:
        if 10 == sum(int(dig) for dig in str(num)):
            cur += 1
            if cur == nth:
                return num 
        num += 1 

print(find_perfect_naive(1), find_perfect_naive(2))

# there's no straightforward direct combinatorial way that could give the nth 
# number. Stars and bars approach with some exclusion gives 
# (10 + n - 1) C (n - 1) - n as the formula for calculating the number of 
# `n` digit naturals whose digits add to 10. This could be used theoretically
# as a starting point building gradations and not having to run a large loop
