def original_sentence_naive(string, words):  # O(2^N) time, O(n) space
    for i in range(1, len(string) + 1):
        if string[:i] in words:
            if string[i:] == "":
                return [string[:i]]
            next_words = original_sentence_naive(string[i:], words)
            if next_words is not None:
                return [string[:i], *next_words]
    return None


print(original_sentence_naive("thequickbrownfox", set(
    ["quick", "brown", "the", "fox"])))
print(original_sentence_naive("bedbathandbeyond", set(
    ["bed", "bath", "bedbath", "and", "beyond"])))


def original_sentence(string, words):  # O(n^2) time, O(n) space
    sentence = [("", len(string) + 1)]
    for _ in range(1, len(string) + 1):
        for j in range(0, sentence[-1][1]):
            if string[j: sentence[-1][1]] in words:
                sentence.append((string[j:sentence[-1][1]], j))
                break
        if sentence[-1][1] == 0:
            break
    return [word for word, loc in reversed(sentence) if word != ""] \
        if sentence[-1][1] == 0 else None


print(original_sentence("thequickbrownfox",
                        set(["quick", "brown", "the", "fox"])))
print(original_sentence("bedbathandbeyond", set(
    ["bed", "bath", "bedbath", "and", "beyond"])))

# other backtracking problems 
# (https://www.dailycodingproblem.com/blog/an-introduction-to-backtracking/)

# The N queens puzzle
# You have an N by N board. Write a function that returns the number 
# of possible arrangements of the board where N queens can be placed on the 
# board without threatening each other, i.e. no two queens share the same 
# row, column, or diagonal.

def count_queens(n):
    count = 0
    rows = set()
    diagonals = set()
    orth_diagonals = set()

    def helper(x):
        nonlocal count, rows, diagonals
        if x >= n:
            count += 1
            return
        for y in range(n):
            if y not in rows and x - y not in diagonals and x + y not in orth_diagonals:
                rows.add(y)
                orth_diagonals.add(x + y)
                diagonals.add(x - y)
                helper(x + 1)
                try: 
                    rows.remove(y)
                    orth_diagonals.remove(x + y)
                    diagonals.remove(x - y)
                except KeyError:
                    pass
        return
            
    helper(0)
    return count
import time
start = time.time()
print(count_queens(8))
print("Execution time: ", time.time() - start)

# Flight itinerary problem
# The flight itinerary problem is as follows:

# Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person’s itinerary. If no such itinerary exists, return null. All flights must be used in the itinerary.

# For example, given the following list of flights:

# HNL ➔ AKL
# YUL ➔ ORD
# ORD ➔ SFO
# SFO ➔ HNL
# and starting airport YUL, you should return YUL ➔ ORD ➔ SFO ➔ HNL ➔ AKL.

        


