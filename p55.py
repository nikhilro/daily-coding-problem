import random, string

class URLShortener:
    def __init__(self):
        self.long_short = {}
        self.short_long = {}

    @staticmethod
    def rand_string(n):
        return "".join(random.choice(string.ascii_letters + string.digits) for _ in range(n))
    
    def gen_rand_string(self, n):
        s = self.rand_string(n)
        while s in self.short_long:
            s = self.rand_string(n)
        return s 
        
    def shorten(self, long):
        if long in self.long_short:
            return self.long_short[long]
        short = self.gen_rand_string(6)
        self.long_short[long] = short
        self.short_long[short] = long 
        return short
    
    def restore(self, short):
        return self.short_long.get(short, None)
    
    