# Lambdas
# anonyme Funktion
lambdaTest = lambda x,y:  x*y
print(lambdaTest(4,5))
(lambda x, y: print(f"{x} + {y} = {x+y}"))(200, 560)

numbers = list(range(401))
evenNumbers = []
for x in numbers:
    if x % 2 == 0:
        evenNumbers.append(x)
print(evenNumbers)


def isEven(number):
    return number % 2 == 0

evenNumbers = list(filter(isEven, numbers))
# filter ist eine höhere Funktion, d.h. sie erwartet eine Funktion als Parameter und ein iterierbares Objekt als zweiten
# Parameter
print(evenNumbers)
evenNumbers = list(
    filter(lambda number: number % 2 == 0,
           numbers)
)
print(evenNumbers)

oddNumbers = list(
    filter(lambda number: number % 2 != 0,
           numbers)
)
print(oddNumbers)
nameList = ["Zeynep", "Antonia", "Marius", "Thomas", "Xaver"]
nameList.sort(reverse=True)
nameList.sort(key=lambda name: name[0], reverse=True)
print(nameList)

oddNumbers = list(
    map(lambda number: number + 1,
        evenNumbers
    )
)
print(oddNumbers)
# map funktioniert ähnlich wie filter, aber wendet die übergeben Funktion auf jedes Element an und verändert
# es dadurch
# map und filter geben immer ein Objekt map/filter zurück, das erst wieder in eine Liste oder ähnliches umgewandelt
# werden muss


def multiplier(multiplier):
    return lambda number: number * multiplier


print(multiplier(2)(4))
doubler = multiplier(2)
print(doubler(12))

# Wir erstellen uns eine Liste mit den ersten 100 Zahlen
# Und die Liste soll gefiltert werden, damit nur noch vielfache von 6 enthalten sind
# Und diese Vielfache sollen dann abschließend durch 3 geteilt werden
# Am Ende soll das Ergebnis als Liste zurückgegeben werden


liste = list(range(100))

newList = list(
    map(
        lambda number: number / 3,
        filter(
            lambda number: number % 6 == 0,
            liste)
            ))
print(newList)

