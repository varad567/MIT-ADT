class vehicle():
    def move(self):
        print("Vehicle is moving")

class car(vehicle):
    def move(self):
        print("driving on the road")

class cycle(vehicle):
    def move(self):
        print("Cycle is padding on road ")    

c = car()
c.move()
c1 = cycle()
c1.move()
