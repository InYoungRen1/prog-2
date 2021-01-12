# animals.py
# a look at object-oriented programming

class Animals():
    # CONSTRUCTOR
    def __init__(self):
        self.legs = 2
        self.hairy = True

    def talk(self):
        return "damn you."
    def eat(self, food):
        if food == "meat":
            return"yummm"
        elif food in["veggies", "vegetable"]:
            return"yummm"


dog = Animals()
dog.legs = 2
dog.hairy = True

if dog.hairy:
    print("the dog is hairy brush its hair")