# class Person:
#     def __init__(self, firstName, lastName, age):
#         self.firstname = firstName
#         self.lastName = lastName
#         self.age = age
#
from Modul05 import Tisch


class Schreibtisch(Tisch):
    def __init__(self, anzBeine: int, ablageflaeche: float, material: str, schubladen):
        super().__init__(anzBeine, ablageflaeche, material)
        self.schubladen = schubladen


class MyClass:
    def __init__(self, x, y, z):
        self.z = z
        self.y = y
        self.x = x

    def returnOne(self):
        return 1


class secondClass:
    def __init__(self, x, y, z, w):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
