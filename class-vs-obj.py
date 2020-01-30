class Player:
    def __init__(self, location, name):
        self.location = location
        self.name = name
    
if __name__ == '__main__':
    dog = Player("Miami","Brick")
    cat = Player("Moon", "Schrödinger")
    objects = {cat:"True", dog: "True"}

    for obj in objects:
        print(obj.name)
        print(obj.location)