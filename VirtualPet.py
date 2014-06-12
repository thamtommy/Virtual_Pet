class VirtualPet:
    """a representation of a pet"""
    def __init__(self,name):
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.hygiene = 5

        print("I have been born - my name is {0}.".format(self.name))

    #methods
    def talk(self):
        print("Hi, I'm your virtual pet!")

    def feed(self,food):
        self.hunger = self.hunger - 1
        self.energy = self.energy + 1

    def clean(self,wash):
        if self.hygiene < 5:
            self.hygiene = self.hygiene = 1
        else:
            print("{0} is already clean!".format(self.name))

def ShowMenu():
    print()
    print("MENU")
    print()
    print("What would you like do to with your pet today?")
    print()
    print("1. Feed your pet?")
    print("2. Clean your pet?")
    print("3. Talk to your pet?")
    print()

def GetOption():
    valid = False   
    while not valid:
        MenuChoice = input("Select your option: ")
        if MenuChoice in ['1','2','3']:
            valid = True
            return MenuChoice
        else:
            print("Please enter a valid choice.")

def main():
    name = input("Please enter the name of your pet: ")
    #create an instance of the class
    pet_one = VirtualPet(name)
    #call the talk method
    pet_one.talk()
    
    ShowMenu()
    MenuChoice = GetOption()

    if MenuChoice == '1':
        print("{0}'s energy was {1}".format(pet_one.name,pet_one.energy))
        pet_one.feed("Scooby Snacks")
        print("{0}'s energy is now {1}".format(pet_one.name,pet_one.energy))
    elif MenuChoice == '2':
        pet_one.clean("Wash")

if __name__ == "__main__":
    main()
