class Device:
    def __init__(self, name, color, model, battery, memory_RAM):
        self.name = name
        self.color = color
        self.model = model
        self.battery = battery
        self.memory_RAM= memory_RAM
    
    def turning(self):
        print("The smartphone is turning on.")
    
    def unlocking(self):
        print("The smartphone is unlocking.")
        
class Smartphone(Device):
    pass

class samsung():
    def Sound(self):
        return "smooth sailing"
    
class iphone():
    def Sound(self):
        return "calm"

phone = Smartphone("samsung","red", "345", "5000mAh", "8GB")
print(phone.name)
print(phone.color)
print(phone.model)
print(phone.battery)
print(phone.memory_RAM)
for smartphon in [samsung(), iphone()]:
    print(smartphon.Sound())