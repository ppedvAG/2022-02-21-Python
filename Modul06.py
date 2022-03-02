# import sys # In Python integriertes Modul
# from sys import argv
# import sys as s
from sys import *
from helper import add, subtract

# # sys.argv erlaubt es uns auf die übergebenen Parameter/argumente zuzugreifen
# output = ""
#
# for x in argv:
#     output += f"{x} \n"
# print(output)
# # Erstes Element in argv ist immer der Modul/Skript-Name
#
# var1 = argv[1]
# var2 = argv[2]
# print(var1, var2)

functions = {
    "add": add,
    "subtract": subtract
}

if len(argv) < 3:
    print("Es müssen 3 Parameter übergeben werden")
    print("Modul06.py zahl1 zahl2 operation")
else:
    x = int(argv[1])
    y = int(argv[2])
    choice = argv[3]
    if choice in functions:
        print(functions[choice](x, y))
    else:
        print("Gültige operations:\nadd\nsubtract")
