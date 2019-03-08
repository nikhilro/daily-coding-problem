def justify_text(words, k): # O(n) time, O(n) space
    lines = [[[], 0]]
    for word in words:
        if not (len(lines[-1][0]) - 1 + lines[-1][1] + len(word) <= k):
            lines.append([[], 0])
        lines[-1][0].append(word)
        lines[-1][1] += len(word)

    for i, line in enumerate(lines):
        string = ""
        padding = (k - line[1]) // (len(line[0]) - 1)
        extra = (k - line[1]) % (len(line[0]) - 1)
        for j, word in enumerate(line[0][:-1]):
            string += word
            string += " " * (padding + 1) if j < extra else " " * padding
        string += line[0][-1]
        lines[i] = string
    return lines


print(justify_text(["the", "quick", "brown", "fox",
                    "jumps", "over", "the", "lazy", "dog"], 16))
