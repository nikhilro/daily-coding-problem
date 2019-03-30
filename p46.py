def longest_palindrome_naive(s): # O(n^2) time, O(1) space
    p = ""
    for i in range(len(s)):
        forward, backward, end  = i, len(s) - 1, len(s)
        while forward <= backward:
            if s[backward] == s[forward]:
                forward = forward + 1
            else: 
                forward, end = i, backward
            backward -= 1
        if end - i >= len(p):
            p = s[i:end]
    return p

print(longest_palindrome_naive("aabcdcb"), longest_palindrome_naive("bananas"))

# don't know a straightforward way to do better than this