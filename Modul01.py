print("Hello World!")
# Ich bin ein Kommentar
# TODO: Python Kurs halten
name = "Marius Sommer"
print("Hallo " + name)
# Formatted Strings:
print(f"Hallo {name}!")

zahl = 50
floatZahl = 55.5
print(zahl + floatZahl)
zahl = "ich bin jetzt ein string"
print(zahl + str(floatZahl))

# str - String
# int - Integer
# float - Float
# complex - Komplex
complexNum = 5j + 3
# bool - Boolean True/False

# dict
# Key:Value Paar
meinAuto = {
    "Marke": "BMW",
    "Modell": "X3",
    "Baujahr": 2019
}

meinAuto["Gewicht"] = 150
print(meinAuto["Marke"])
meinAuto["Modell"] = "I3"
print(meinAuto["Modell"])
meinAuto.update({"Baujahr": 2021})
print(meinAuto["Baujahr"])

# keys()
print(meinAuto.keys())

# items()
print(meinAuto.items())

# values()
print(meinAuto.values())

# copy()
meinZweitAuto = meinAuto.copy()  # Kopiert meinAuto => Ändert sich nicht wenn mein Auto geändert wird
# meinZweitAuto = meinAuto # Referenziert auf meinAuto => Ändert sich wenn meinAuto geändert wird
meinAuto["Marke"] = "Audi"
print(meinZweitAuto)

# pop(Key) Entfernt das K:V Paar mit dem entsprechenden Key
meinZweitAuto.pop("Modell")
print(meinZweitAuto)

# popitem() Entfernt das letzte Key:Value Paar
meinZweitAuto.popitem()
print(meinZweitAuto)

# update({"Key": "Value"})
meinZweitAuto.update({"Marke": "Volvo"})  # Setzt Marke auf Volvo
meinZweitAuto.update({"Key": "Wert"})  # Fügt neues K:V Paar hinzu, falls Key nicht exisitiert
print(meinZweitAuto)

# setdefault("Key", "Value")
marke1 = meinZweitAuto.setdefault("Marke", "Fiat")
modell1 = meinZweitAuto.setdefault("Modell", "Panda")
print(f"Marke1: {marke1}, Modell1: {modell1}")
print(meinZweitAuto)

if ("Marke" in meinZweitAuto):  # in prüft ob ein Key in einem dict vorkommt
    print(f"Marke: {meinZweitAuto['Marke']}")

# clear()
meinZweitAuto.clear()
print(meinZweitAuto)

# list

meineListe = ["Test", 123, 65, True]
meineZweiteListe = [[1, 2, 3, 9], [4, 5, 6]]

print(meineListe[0])
print(meineZweiteListe[0])

# append()
meineListe.append(555)  # Fügt Element an das Ende der Liste an
print(meineListe)

# Wert ändern:
meineListe[4] = 444
print(meineListe)

# Von hinten beginnen:
print(meineListe[-1])

# Mehrere Elemente wiedergeben lassen:

print(meineListe[2:4])  # Gibt Elemente von Index 2 bis Index 4(nicht inklusiv) zurück => 65, True

# copy()
# clear()
# Wie beim dict

# count(Item) Gibt zurück wie oft das Item Vorkommt
print(meineListe.count(123))

# extend(iterierbares Objekt)
meineListe.extend(meineZweiteListe)
print(meineListe)

# index(Element)
print(meineListe.index(True))  # => 3
meineListe.append(True)
print(meineListe.index(True))  # => 3

# insert(index, element) # Fügt Element am Index ein, ersetzt das vorherige Element nicht
meineListe.insert(2, "Test2")
print(meineListe)

# pop(index) Entfernt das Element am angegebenen Index

meineListe.pop(2)
print(meineListe)

# remove(Element)
meineListe.remove(True)  # Entfernt nur das erste True
print(meineListe)

try:
    name.remove(False)
except ValueError as e:
    print(e)
    print("Element wurde nicht gefunden")
except Exception as e:
    print(e)
    print("Anderer Fehler")

if True in meineListe:
    meineListe.remove(True)
    print(meineListe)

# reverse()
meineListe.reverse()  # inplace
print(meineListe)

# sort()
meineDritteListe = [8, 4, 6, 12, 9, 1, 0, -5]
meineDritteListe.sort(reverse=True)
print(meineDritteListe)
meineZweiteListe.sort(key=len, reverse=True)
print(meineZweiteListe)
# reverse=True kehrt Reihenfolge um
# key nutzt eine übergeben Funktion als Vergleich

# Tuple
# Sind nicht änderbar
meinTupel = (1, 2, 3, 4)
print(meinTupel[2])
meinTupel = list(meinTupel)
meinTupel[2] = 4
meinTupel = tuple(meinTupel)
print(meinTupel[2])

# count(element)
# index(element)
# Funktioniert wie bei den Listen

# range()
# range(ende) Ende ist nicht inklusiv
# range(start, ende) start ist inklusiv
# range(start, ende, schrittweite)

# sets
meinSet = {"test", "test2"}
print(meinSet)
meinSet = {"test", "test", "test2"}
print(meinSet)

meinSet = {1, 2, 3, 4, 5}
meinZweitesSet = {4, 5, 6, 7}
meinDrittesSet = {6, 7, 8, 9}

# add(Element)

meinDrittesSet.add(10)
print(meinDrittesSet)

# copy()
# clear()
# Wie List,Dict

# discard(elemet)
meinDrittesSet.discard(10)
print(meinDrittesSet)

# pop()
# Entfernt das erste Element aus dem Set
print(meinDrittesSet.pop())

# remove(Element)
# meinDrittesSet.remove(12)
# Entfernt das angegebene Element aus dem Set und wirft fehler, falls nicht vorhanden
if 9 in meinDrittesSet:
    print("jup")

# difference(set)
# Gibt ein neues Set zurück, dass nur aus Elementen des aufrufenden Sets besteht,
# die nicht im Parameter-Set enthalten sind

meinViertesSet = meinZweitesSet.difference(meinSet)
print(meinViertesSet)

# difference_update(set)
meinViertesSet.difference_update(meinDrittesSet)
print(meinViertesSet)

# intersection(set)
# GIbt ein neues Set zurück, das nur aus den Gemeinsamkeiten besteht
meinViertesSet = meinSet.intersection(meinZweitesSet)
print(meinViertesSet)

# intersection_update(set)
# Löscht die Elemente, die nicht in beiden Sets vorkommen
meinViertesSet.intersection_update(meinDrittesSet)
print(meinViertesSet)

# issubset(set)
# Prüft ob das Set in dem aufrufenden enthalten ist
print("Ist enthalten") if meinSet.issubset(meinZweitesSet) else print("Ist kein Subset")

# issuperset(set)
# Pürft ob das aufrufende Set in dem Parameter-Set enthalten ist
print("Ist enthalten") if meinSet.issuperset(meinZweitesSet) else print("Ist kein Superset")


for element in meineListe:
    print(element)