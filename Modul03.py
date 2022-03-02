import time


# Funktionen

def greeter(name):
    print(f"Hallo {name}")
    returnString = f"Hallo {name}"
    return returnString


greeter("Max")
greeter("Martina")
greeter("Marius")
name = "Thomas"
greeter(name)
greetstring = greeter("Max")
print(greetstring)


def nestedFunc(func, param):
    def innerFunc():
        print("Hallo aus der inneren Funktion")

    innerFunc()
    return func(param)


x = nestedFunc(greeter, "Jürgen")
print(x)


# Arbitrary Arguments


def summieren(*numbers):
    # numbers wird als Tupel übergeben => wir können darüber iterieren
    # *args in dne Python Docs
    sum = 0
    for i in numbers:
        sum += i
    return sum


result1 = summieren(1, 2, 3)
result2 = summieren(1)
result3 = summieren(1, 2, 3, 5, 6, 7, 3, 24, 234, 23456345, 435235234)
result4 = summieren(1, 2, 3, 124, 765)


# Arbitrary Keyword Arguments


def readAloud(**words):
    # Hier werden alle übergebenen keywordarguments als Dictionary zusammengefasst
    for key, value in words.items():
        print(f"{key}: {value}", end=" ")
        print(key, value, sep="+")


readAloud(firstName="Max", lastName="Mustermann", age=27, employed=True)

nestedFunc(param="Martina", func=greeter)  # Wir können die Variablen auch direkt benennen


def multiplier(intOne, /, intTwo):
    # intOne kann jetzt nur als Positional übergeben werden
    return intOne * intTwo


print(multiplier(12, intTwo=44))


def multiplierKw(*, intOne, intTwo):
    # intOne und intTwo können nur noch als Keyword übergeben werden
    return intOne * intTwo


print(multiplierKw(intOne=12, intTwo=44))


def divide(intOne=1, intTwo=1):
    return intOne / intTwo


print(divide(10))
print(divide(10, 5))
print(divide())


# Decorator:


def doTwice(func):
    def wrapper(intOne, intTwo):
        print("Ich werde vor der dekorierten Funktion ausgeführt")
        func(intOne, intTwo)
        func(intOne, intTwo)
        print("Ich werde nach der dekorierten Funktion ausgeführt")

    return wrapper


# test = doTwice(print)
# test()
# test()


def calc(intOne, intTwo):
    print(intOne + intTwo)


doubleCalc = doTwice(calc)
doubleCalc(12, 22)


# calc(12,12)


def discardList(listToCheck: list, elem) -> list:
    """
    Checks if an element is part of the list and delete it if so
    :param listToCheck: list
    :param elem:
    :return: list
    """
    if elem in listToCheck:
        count = listToCheck.count(elem)
        for i in range(count):
            listToCheck.remove(elem)
        return listToCheck


testList = [1, 2, 3, 4, 4, 4, 5, 6]

# testList = discardList(testList, 4)
print(testList)


class customList(list):
    def discardList(this, elem):
        """
        Checks if an element is part of the list and delete it if so
        :param listToCheck: list
        :param elem:
        :return: list
        """
        if elem in this:
            count = this.count(elem)
            for i in range(count):
                this.remove(elem)
            return this


testList = customList(testList)
testList.discardList(4)
#
# def discardList(this, elem):
#     if elem in this:
#         count = this.count(elem)
#         for i in range(count):
#             this.remove(elem)
#         return this
#
#
# list.discardList = discardList
# testList.discardList(4)
print(testList)

# Unpacking Operators

print(summieren(*testList))
# Der unpacking Operator löst die Liste/Tupel in seine Bestandteile auf und übergibt diese einzeln

myDict = {"test1": 1, "test2": 2, "test3": 3}
readAloud(**myDict)


# readAloud(test1=1, test2=2, test3=3) entspricht Zeile 173
# Bei den Dictionaries teilt der Unpacking Operator die Key:value Paare ind keyword=wert Paare auf


def allParams(test, abc, test2, default=1, *args, **kwargs):
    pass


# Reihenfolge: Erst positionals/Keywords, dann default und dann arbitrary (Keyword) Arguments


def factorial(number):
    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)


current_time = time.time()
factorial(998)
print(time.time() - current_time)


def factorialFor(number):
    sum = 1
    if number <= 1:
        return sum
    for i in range(number, 0, -1):
        sum *= i
    return sum


current_time = time.time()
factorialFor(998)
print(time.time() - current_time)


# Schreibe eine Funktion, die beliebig viele Zahlen als Parameter akzeptiert
# Die Funktion soll die größte dieser Zahlen zurückgeben
# Es soll nun auch ein keyword akzeptiert werden, das entscheidedt ob man die größte oder die kleinste
# Zahl zurück bekommen will
# Standardmäßig soll die größte zurückgegeben werden

def returnMax(*args, mode="max"):
    max = args[0]
    if mode == "max":
        for x in args:
            if max < x:
                max = x
    else:
        for x in args:
            if x < max:
                max = x
    return max


print(returnMax(1, 2, 3, 4, 5, 6, 7, 8, 9, mode="max"))


def returnMinMax(*args, returnBiggestNumber=True):
    args = list(args)
    args.sort(reverse=returnBiggestNumber)
    return args[0]

# Erstelle eine Funktion, die einen String als Parameter akzeptiert
# und ausgibt wie viele klein und wie viele großbuchstaben im String enthalten sind
# .isUpper(), .isLower()