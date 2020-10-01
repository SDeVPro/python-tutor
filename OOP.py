"""
Obyektga yo'naltirilgan dasturlash
"""
#Classlar bilan ishlash
# class Nomi:
#     age = 15
#     name = 'Fozilbek'
#     surname = 'Jahongirov'
#     address = 'Minor metro yaqini'
#     email = 'fozilbek@mail.ru'
#     dictionary = {'age':15, 'name':'Fozilbek', 'surname':'Jahongirov'}
#
# nomi = Nomi()
# print(nomi.age, nomi.name, nomi.address)
# print(nomi.dictionary)

#Vorislik
# class Pet(object):
#     def __init__(self,name, species):
#         self.name = name
#         self.species = species
#
#     def getName(self):
#         return self.name
#     def getSpecies(self):
#         return self.species
#     def __str__(self):
#         return "%s is a %s"%(self.name, self.species)
#
# class Dog(Pet):
#     def __init__(self, name, chases_cats):
#         Pet.__init__(self, name, "Dog")
#         self.chases_cats = chases_cats
#
#     def chasesCats(self):
#         return self.chases_cats
#
# class Cat(Pet):
#     def __init__(self, name, hates_dog):
#         Pet.__init__(self, name, "Cat")
#         self.hates_dog=hates_dog
#     def hatesDog(self):
#         return self.hates_dog
#
#
# petomets = Cat(name='Mosh', hates_dog='tishliydi')
# print(petomets.name, petomets.hatesDog())

# class Car:
#     carCount = 0
#     def __init__(self, name, year):
#         self.name = name
#         self.year = year
#         Car.carCount +=1
#
#     def displayCount(self):
#         print("Total Car :", Car.carCount)
#
#     def displayCar(self):
#         print("Name: ", self.name, "Year:", self.year)
# car1 = Car("Honda",2000)
# car2 = Car("BMW X6", 2017)
# car1.displayCar()
# car2.displayCar()
# Car.displayCount(Car.carCount)




