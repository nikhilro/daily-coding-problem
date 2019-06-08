# def readN(n):
#     string = ""
#     while n:
#         string += read7() if n >= 7 else read7()[:n]
#         n -= 7 if n >= 7 else n 
#     return string

# above is wrong because you lose some of the text i.e. you need context 
# to carry from one function call to next

class Reader:
    def __init__(self):
        self.remainder = ''

    def readN(self, n):
        result = self.remainder
        text = None 

        while len(result) < n: 
            # the check if we have exhausted the text is 
            # hopefully in read7 so the error should propagate through
            text = read7()
            result += text 
        
        self.remainder = result[n:]

        return result[:n]




    