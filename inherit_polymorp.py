# 2. Super class
class Dog:
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness

    def likes_wlaks(self):
        return True

    def bark(self):
        return 'Woof!'

# 1. Duplicated
class Samoyed(Dog):
    # def __init__(self, name):
    #     self.name = name

    # def likes_walks(self):
    #     return True
    
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def bark(self):
        return 'Arf arf!'
    
class Poodle(Dog):
    # def __init__(self, name):
    #     self.name = name
    
    # def likes_walks(self):
    #     return True
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

class GoldenRetriever(Dog):
    # def __init__(self, name):
    #     self.name = name
    
    # def likes_walks(self):
    #     return True
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

    def bark(self):
        return 'AROOO!'

sammy = Samoyed('Sammy', 2, 10)
print(sammy.name, sammy.age, sammy.friendliness)
print(sammy.likes_wlaks())

# 3. Polymorphism
goldie = GoldenRetriever('Goldie', 1, 10)
generic_dog = Dog('Gene', 10, 10)
poodie = Poodle('Poodie', 1, 10)

print(generic_dog.bark())
print(poodie.bark())
print(sammy.bark())
print(goldie.bark())