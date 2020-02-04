'''
Sign your name: Tristan
 
 1. Write code that defines a class named Animal:
     * Add a constructor for the Animal class that prints 'An animal has been born.'
     * Add an attribute for the animal name.
     * Add an eat() method for Animal that prints 'Munch munch.'
     * Add a make_noise() method for Animal that prints 'Grrr says [animal name].'

     
 2. Write code that defines a class named Cat:
     * Make Animal the parent.
     * Add a constructor for Cat that prints 'A cat has been born.'
     * Modify the constructor so it calls the parent constructor as well.
     * Add a make_noise() method for Cat that prints 'Meow says [animal name].'

     
 3. Write code that defines a class named Dog:
     
     * Make Animal the parent.
     * Add a constructor for Dog that prints 'A dog has been born.'
     * Modify the constructor so it calls the parent constructor as well.
     * Add a make_noise() method for Dog that prints 'Bark says [animal name].'

     
 4. Write a main program with:
     
     * Code that creates a cat, two dogs, and an animal with names.
     * Code that calls eat() and make_noise() for each animal.
     
 OUTPUT:
An animal has been born.
A cat has been born.
Munch munch
Meow says (cat name) .
An animal has been born.
A dog has been born.
Munch munch
Bark says (dog name).
An animal has been born.
A dog has been born.
Munch munch
Bark says (another dog name) .
An animal has been born.
Munch munch
Grrr says (animal name) .
'''

class Animal():
    def __init__(self):
        print("An animal has been born.")
        self.name = ""

    def eat(self):
        print("Munch munch.")

    def make_noise(self):
        print("Grrr says "+self.name)

class Cat(Animal):
    def __init__(self):
        super().__init__()
        print("A cat has been born.")

    def make_noise(self):
        print("Meow says "+self.name)

class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("A dog has been born.")
    def make_noise(self):
        print("Bark says "+self.name)

cat = Cat()
cat.name = "Whiskers"
cat.eat()
cat.make_noise()
dog_1 = Dog()
dog_1.name = "Sans"
dog_1.eat()
dog_1.make_noise()
dog_2 = Dog()
dog_2.name = "Iggy"
dog_2.eat()
dog_2.make_noise()
animal = Animal()
animal.name = "Mr. Hermon"
animal.eat()
animal.make_noise()
