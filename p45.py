def rand7():
    num = (rand5() - 1) + 5 * (rand5() - 1) # O <= num <= 24
    if num > 20:
        return rand7()
    return num // 3 + 1
