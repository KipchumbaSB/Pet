class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 5  # Default hunger level
        self.energy = 5  # Default energy level
        self.happiness = 5  # Default happiness level
        self.tricks = []  # List to store learned tricks

    def eat(self):
        self.hunger = max(0, self.hunger - 3)  # Hunger decreases but not below 0
        self.happiness = min(10, self.happiness + 1)  # Happiness increases but not above 10

    def sleep(self):
        self.energy = min(10, self.energy + 5)  # Energy increases but not above 10

    def play(self):
        self.energy = max(0, self.energy - 2)  # Energy decreases but not below 0
        self.happiness = min(10, self.happiness + 2)  # Happiness increases but not above 10
        self.hunger = min(10, self.hunger + 1)  # Hunger increases but not above 10

    def get_status(self):
        print(f"Pet Name: {self.name}")
        print(f"Hunger Level: {self.hunger}")
        print(f"Energy Level: {self.energy}")
        print(f"Happiness Level: {self.happiness}")

    def train(self, trick):
        self.tricks.append(trick)  # Add new trick to the list
        self.happiness = min(10, self.happiness + 1)  # Happiness increases for learning a trick

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} knows the following tricks:")
            for trick in self.tricks:
                print(f"- {trick}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")

# Example usage:
my_pet = Pet("Buddy")
my_pet.get_status()
my_pet.eat()
my_pet.play()
my_pet.train("roll over")
my_pet.train("play dead")
my_pet.show_tricks()
my_pet.get_status()