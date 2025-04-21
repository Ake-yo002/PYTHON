# PART 1
class Dress:
    def __init__(self, style, size, color, price):
        #  We are making a dress object here.
        self.style = style 
        self.size = size   
        self.color = color 
        self.price = price 

    def describe(self):
        #  This tells you about the dress.
        return f"{self.color} {self.style} dress, size {self.size}, for ${self.price:.2f}"  #  Returns a formatted description

class RedDress(Dress):
    def __init__(self, style, size, price, shade="Crimson"):
        #  Making a *red* dress now.
        super().__init__(style, size, "Red", price)  #  Use the Dress init, but force color to "Red"
        self.shade = shade  # Store the specific shade of red

    def describe(self):
        #  Describes the red dress, including the shade.
        return f"{self.shade} {super().describe()}"  #  Adds shade to the description from the Dress class

dress1 = Dress("Summer", "M", "Blue", 25.99)
print(dress1.describe())  #  Let's see what dress1 looks like

red_dress1 = RedDress("Evening", "S", 75.00, "Ruby")
print(red_dress1.describe())  #  And now, let's check out red_dress1

# PART 2: POLYMORPHISM

class Horse:
    def move(self):
        #  How a horse moves.
        return "Trots"  #  Returns "Trots"

class Antelope:
    def move(self):
        #  How an antelope moves.
        return "Gallops"  # Returns "Gallops"

# Polymorphism in action
animals = [Horse(), Antelope()]  #  List of animal objects
for animal in animals:
    print(animal.move())  #  Calls the move() method of each animal

