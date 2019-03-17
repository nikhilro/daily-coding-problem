def make_palindrome(s): # O(n) time, O(n) space
    chars, i, j = [], 0, len(s) - 1
    while i < j:
        chars.append(s[j])
        if s[i] == s[j]:
            i, j = i + 1, j - 1
        else:
            j = j - 1
    return "".join(chars) + s[i:] 

print(make_palindrome('google'), make_palindrome('race'))
