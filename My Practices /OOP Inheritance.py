class Animal:
    alive = True 
    def __init__(self, color ):
        self.color = color
    def eat(self):
        print ("The animal is eating its food")
    def sleep(self):
        print ("The animal is sleeping")
    
class Rabbit(Animal):
    pass
class Fish(Animal):
    pass
class Hourse(Animal):
    pass

rabbit = Rabbit("pink")
fish = Fish("red")
hourse = Hourse("gray")

print (rabbit.color)
print (fish.alive)
rabbit.eat()
fish.sleep()
