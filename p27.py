def is_well_formed(brackets): # O(n) time, O(n) space
    lst = []
    for bracket in brackets:
        if bracket == ']' and lst[-1] == '[':
            lst.pop()
        elif bracket == '}' and lst[-1] == '{':
            lst.pop()
        elif bracket == ')' and lst[-1] == '(':
            lst.pop()
        elif bracket == '(' or bracket == '{' or bracket == '[':
            lst.append(bracket)
        else:
            return False

    return not lst 
    
print(is_well_formed("([])[]({})"))
print(is_well_formed("([)]"))
print(is_well_formed("((()"))

class Value:
    def __init__(self, v):
        self.v = v
    def __repr__(self):
        return "Value({})".format(self.v)

def is_well_formed_experimental(brackets): # O(n) time, O(1) space but doesn't work
    v1, v2, v3 = Value(0), Value(0), Value(0)
    count = { '[': v1, '(': v2, '{': v3, ']': v1, ')': v2, '}': v3}
    
    for bracket in brackets:
        if bracket == ')' or bracket == '}' or bracket == ']':
            count[bracket].v -= 1
        elif bracket == '(' or bracket == '{' or bracket == '[':
            count[bracket].v += 1
        else:
            return False
        if count[bracket].v < 0:
            return False

    return v1.v == v2.v == v3.v == 0

print(is_well_formed_experimental("([])[]({})"))
print(is_well_formed_experimental("([)]"))
print(is_well_formed_experimental("((()"))
