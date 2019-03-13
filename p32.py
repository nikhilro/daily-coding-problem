# not sure if it's correct, just trying to look for unbalanced exchange rates 
# solution for maximizing profit: 
# https://stackoverflow.com/questions/2282427/interesting-problem-currency-arbitrage
def arbitrage(forex):
    profitable = set()
    for i in range(len(forex)):
        for j in range(len(forex)):
            if forex[i][j] * forex[j][i] > 1.:
                profitable.add((i, j))
    return not not profitable # bool(profitable)