#The authors' names are Julia Bub and Julia Schutz

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)

print(p1.name)
print(p1.age)

#predition: we think the code will assign the values "John" and 36 to the attributes name and age, then print them
#The code printing what we predicted

p2 = Person("Taylor", 32)

print(p2.name)
print(p2.age)
