def rand5():
    num = rand7()
    return num if num <= 5 else rand5()