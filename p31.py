def diff_naive(s1, s2): # O(2^n) time, O(1) space
    s1, s2 = (s1, s2) if len(s1) >= len(s2) else (s2, s1)

    if s2 == "":
        return len(s1)
    
    if s1[0] == s2[0]:
        return diff_naive(s1[1:], s2[1:])
    else:
        sub = 1 + diff_naive(s1[1:], s2[1:])
        ins = 1 + diff_naive(s1[1:], s2)
        return min(sub, ins)
    

print(diff_naive("kitten", "sitting"))

def diff(s1, s2): # O(n*m) time, O(1) space, alternatively modify above to dp
    s1, s2 = (s1, s2) if len(s1) >= len(s2) else (s2, s1)

    if s2 == "":
        return len(s1)
    
    if s1[0] == s2[0]:
        return diff(s1[1:], s2[1:])
    else:
        if s2[0] in s1:
            return 1 + diff(s1[1:], s2) # ins
        else: 
            return 1 + diff(s1[1:], s2[1:]) # sub
        

print(diff("kitten", "sitting"))