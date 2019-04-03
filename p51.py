def shuffle(deck): # O(n) time, O(1) space
    n = len(deck) - 1
    for i in range(n):
        j = randint(i, n)
        deck[i], deck[j] = deck[j], deck[i]
    