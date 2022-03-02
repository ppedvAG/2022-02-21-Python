from enum import Enum


# Definiert ein Enum Color mit den angegebene Werten
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3


c = Color.GREEN
print(c)
print(c.name)
print(c.value)

for name, member in Color.__members__.items():
    print(name, member, member.value)

