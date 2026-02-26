class Box():
    def __init__(self,weight):
        self.weight = weight
    def __add__(self,other):
        return self.weight + other.weight
b1 = Box(1500)
b2 = Box(2750)

print("Total weight of box is:",b1+b2)