class calculator:
    def add(self, a=0, b=0, c=0):        
        return a + b + c        
    
c = calculator()
print("Addition of 2 numbers:", c.add(5, 10))   
print("Addition of 3 numbers:", c.add(5, 10, 15))
