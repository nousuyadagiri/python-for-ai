# Inheritance
# Parent class - general animal
class Person:
    def __init__(self, name, age, work, food):
        self.name = name
        self.age = age
        self.work = work
        self.food = food

    def eat(self):
        return f"{self.name} is eating {self.food}"

    def do_work(self):
        return f"{self.name} is working as a {self.work}"

    def get_age(self):
        return f"I am {self.name}, and my current age is {self.age}"


# Child class - specific animal
class Student(Person):
    def sleep(self):
        return f"{self.name} is sleeping"


data1 = Student("Nousu", 31, "AI engineer", "Noodles")
data2 = Student("Sowmya", 25, "MRO", "Junk Food")

print(data1.eat())
print(data1.do_work())
print(data1.get_age())
print(data1.sleep())

print("-----------------")

print(data2.eat())
print(data2.do_work())
print(data2.get_age())
print(data2.sleep())
