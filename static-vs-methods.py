# this file shows the difference between a static method and regular method 
# in a defined class.

# Static methods have a very clear use-case. When we need some functionality 
# not w.r.t an Object but w.r.t the complete class, we make a method static.

# Note: a static method doesn't need the "self" as the 1st arg to be defined
#       although if the method needs "self", we can pass it as an arg 

class Player:
    def __init__(self, location, name):
        self.location = location
        self.name = name
    @staticmethod
    def print_greeting(self):
        print("Hello World, this is "+self.name)

if __name__ == '__main__':
    dog = Player("Miami","Brick")
    Player.print_greeting(dog) # can also be called with object "dog"
                               # note "dog" needed to be passed an arg to the 
                               # method just like a normal arg to a function