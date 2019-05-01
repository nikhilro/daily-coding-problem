def toss_unbiased():
    '''1 = heads, 0 = tails'''
    while True:
        one, two = toss_biased(), toss_biased() 
        if one == 1 and two == 0:
            return 1 
        elif one == 0 and two == 1:
            return 0
        