class Dog:
    legs = 4
    eyes = 2
    tail = 1
    can_fly = False
    teeth = 42
#self means that your reffering to your own class's object
    def bark(self):
        print("Woof Woof")
huskey = Dog()
lebrador = Dog()
chuwawa = Dog()

print(huskey.tail)
print(lebrador.eyes)
print(chuwawa.bark())


