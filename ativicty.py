class Tiger:
    def move(self):
        return "The tiger is running"
    
class Shark:
    def move(self):
        return "The shark is swmimming"
    
class Bird:
    def move(self):
        return "The bird is flying"
    
for animals in [Tiger(), Shark(), Bird()]:
    print(animals.move())