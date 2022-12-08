#The authors' names are Julia Bub and Julia Schutz
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return self.name + "("+ str(self.age) + ")"

p1 = Person("John", 36)

print(p1)

#prediction: we think this code will print out both "John" and "36" as strings
#instead, the code printed John(36)
#we think this result is different because the code combined name and age, making age a string
