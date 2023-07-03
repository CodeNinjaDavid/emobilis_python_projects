class People:
    def __init__(self, name,gender,age):
        self.my_name= name
        self.my_gender = gender
        self.my_age = age
    def show(self):
        print(self.my_name, self.my_gender, self.my_age)
#create an object
mydetails = People("Rick Sanchez", "Male", 34)
mydetails.show()

class laptop:
    def __init__(self, name, processor, RAM, monitor_inches):
        self.laptop_name = name
        self.laptop_processor = processor
        self.laptop_RAM = RAM
        self.laptop_monitor_inches = monitor_inches
    def show(self):
        print(self.laptop_name, self.laptop_processor, self.laptop_RAM, self.laptop_monitor_inches)
#create an object
mylaptop = laptop("Lenovo","3.10GHz","8GB","17inches")
mylaptop.show()
