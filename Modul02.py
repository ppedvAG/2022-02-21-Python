# Kontrollstrukturen

# if

numOne = 10
numTwo = 10

if numOne < numTwo:
    print("Nummer eins ist kleiner")
elif numOne > numTwo:
    print("Nummer eins ist größer")

else:
    print("Beide Zahlen sind gleich groß")

if numOne == numTwo: print("Die Zahlen sind gleich")

# ternary
# effektiv das gleiche wie Zeilen 8-13, aber unübersichtlicher
print("numTwo ist größer als numOne") if numOne < numTwo else print("numOne ist größer") if numOne > numTwo else print(
    "numOne und numTwo sind gleich groß")

# Erweitere den if-Block auf Zeile 8 bis 13 so, dass auch noch geprüft wird, ob die jeweils größere Zahl gerade oder
# ungerade ist, das Ergebnis soll in der Konsole angezeigt werden
print(numOne % 2 == 0)

# Match-Case

x = 40

match x:
    case 1:
        print("x ist 1")
    case 60 | 50:  # Mit Pipe (oder) können wir zwei Fälle abfangen
        print("x ist 60")
    case 40 if x % 2 == 0:
        print("x ist 40 und gerade")
    case _ if x > 60:
        print("Größer als erwartet")
    case _ if x < 1:
        print("Kleiner als erwartet")
    case _:
        print("Keine der Fälle trat ein")
    # die Verknüpfung mit if nennen wir guard

liste = [3]

match liste:
    case _ if 1 in liste:
        print("DIe Liste enthält 1")
    case _ if len(liste) < 2:
        print("Liste ist zu kurz")
    case _:
        print("Liste enthält das Element nicht")

# while

i = 55

while i < 11:

    i += 1
    if i == 3:
        print("3 wurde erreicht")
        continue  # Gehe wieder an den Anfang der Schleife
    print(i)
    # if i == 3:
    #     print("Schleife wird beendet")
    #     break

while True:
    i += 1
    print(i)
    if i > 20:
        break
# Gebasteltete Fußgesteuerte Schleife
# Wird immer mindestens einmal ausgeführt

# for Schleife
liste = [1, 2, 3, 4, 5, 6, 7, 8]
for element in liste:
    print(element)

name = "Marius Sommer"
name = "Max"

for character in name:
    print(character)
# C#: (int i = 0; i < name.length; i++)
for i in range(len(name)):
    if name[i] == " ":
        break
    print(i)
    print(name[i])
else:
    print("Die Schleife ist vorbei")
    # Wird nach dem natürlichen Ende der Schleife ausgeführt, also nicht wenn break erreicht wurde

liste = [[1, 2, 3, 4], [5, 6, 7, 8]]

for innerList in liste:
    for element in innerList:
        print(element, innerList.index(element))

# FizzBuzz
# wir wollen dass über eine Liste von 1 bis 100 (inklusive) iteriert wird
# Jede Zahl soll auf ihre Teilbarkeit ohne Rest durch 3 und 5 geprüft werden
# Falls die Zahl durch 3 teilbar ist, soll in der Konsole "Fizz" ausgegeben werden
# Falls die Zahl durch 3 teilbar ist, soll in der Konsole "Buzz" ausgegeben werden
# Falls die Zahl durch 3 und 5teilbar ist, soll in der Konsole "FizzBuzz" ausgegeben werden
# Falls es durch keine der beiden Zahlen teilbar ist soll die Zahl selbst ausgegeben werden

for i in range(1, 101, 1):
    answer = ""
    if i % 3 == 0:
        answer += "Fizz"
    if i % 5 == 0:
        answer += "Buzz"
    if answer == "":
        print(i)
    else:
        print(answer)

for x in range(1,101):
    match x:
        case _ if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        case _ if x % 3 == 0:
            print("Fizz")
        case _ if x % 5 == 0:
            print("Buzz")
        case _:
            print(x)

# Das kleine einmaleins
# Wir brauchen eine Schleife von 1 bis 10 (inklusive)
# FÜr jede der Zahlen soll das kleine einmal eins berechnet werden
# 1 x 1 = 1
# ...
# 10 x 10 = 100

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")


