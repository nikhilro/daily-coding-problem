def count_missing(parentheses):
    total, running = 0, 0

    for p in parentheses:
        if p == "(":
            running += 1 
        if p == ")":
            running -= 1 
        if running < 0:
            total, running = total + 1, 0
    
    return total + running

print(count_missing("()())()"))
print(count_missing(")("))
