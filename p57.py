def linify(words, k): # O(n) time, O(n) space for lines
    words = words.split()
    lines, cur, count = [], -1, 0 
    for i, word in enumerate(words):
        if len(word) > k:
            return
        if cur + 1 + len(word) <= k:
            cur, count = cur + 1 + len(word), count + 1
        else:
            lines.append(" ".join(words[i - count:i]))
            cur, count = len(word), 1
    return lines + [" ".join(words[len(words) - count:])] if count > 0 else lines

print(linify("the quick brown fox jumps over the lazy dog", 10))

def linify_recursive(words, k, lines=[]): # v inefficient but O(n) time, 0(n) space for lines
    cur = words.split(' ', 1)
    if len(cur[0]) > k:
        return 
    if not lines:
        lines.append(cur[0])
    else:
        if len(lines[-1]) + 1 + len(cur[0]) <= k:
            lines[-1] += " " + cur[0]
        else:
            lines.append(cur[0])
    if len(cur) == 1:
        return lines 
    else:
        return linify_recursive(cur[1], k, lines)

print(linify_recursive("the quick brown fox jumps over the lazy dog", 10))
