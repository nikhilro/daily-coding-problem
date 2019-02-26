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
