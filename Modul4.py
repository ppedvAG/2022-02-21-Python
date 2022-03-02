import csv
import pandas as pd
# https://pandas.pydata.org/docs/


# In & Output
# preName = input("Wie ist dein Name?\n")
#
# print(f"Hallo {input('Wie ist dein Name?')}")

# mit Input können wir Eingabe vom User anfragen
# Wird immer als String wiedergegeben


def getNum():
    x = input("Gib mir eine Zahl:")
    while not x.isnumeric():
        print(f"{x} ist keine Zahl.")
        x = input("Gib mir eine Zahl:")
    return int(x)


#
# x = getNum()
# y = getNum()
# z = getNum()

# res = sum((x, y, z))
# print(res)

# Fileinput
# r - read
# a - append
# w - write
# w+ - write and read

# file = open("test.txt", "r+")
# for x in range(1,11):
#      file.write(f"Zeile: {x}\n")
# # file.close()
# # file = open("test.txt", "r+")


# Verhindert das "Vergessen" von Daten, da die Datei nach dem Ende des Blocks immer geschlossen wird
with open("test.txt", "r+") as file:
    for x in range(1, 31):
        file.write(f"Zeile{x}\n")

# CSV Dateien
#
# with open("test.csv", newline="") as csvFile:
#     reader = csv.DictReader(csvFile)
#     for row in reader:
#         print(row)

csvFile = pd.read_csv("test.csv", header=None)
print(csvFile)
# DataFrame - ganze Tabelle
# Series - eine Spalte


myDict = {"name": ["Marius", "Thomas", "Max", "Erika"],
          "nachname": ["Sommer", "Jungwirth", "Mustermann", "Musterfrau"],
          "alter": [27, 28, 22, 39]
          }
df = pd.DataFrame(myDict)
print(df)
newRow = {"name": ["Test"], "nachname": ["Test2"], "alter": [44]}
# df = df.append(newRow, ignore_index=True) Veraltet
newRow = pd.DataFrame(newRow)
print(newRow)
df = pd.concat([df, newRow])
df.to_csv("neueCsv.csv", index=False)
df.reset_index(inplace=True, drop=True)
df.to_excel("test.xlsx")
sumOfAge = df["alter"].sum()
print(sumOfAge)
print(df["nachname"][1])

# for row in df:
#     print(row)
#     for column in row:
#         print(column)

for index, row in df.iterrows():
    print(index , row)

csvFile = pd.read_csv("neueCsv.csv", header=None)
dfDict = csvFile.to_dict("series")
print(dfDict)
dfList = csvFile.values.tolist()
print(dfList)
# dataList = dfDict["data"]
# print(dataList)
#
# for x in range(1, len(dataList)):
#     print(dataList[x])
newFrame = pd.DataFrame()
returnFrame = df.copy()

for index, row in df.iterrows():
    if (row["alter"] > 30):
       returnFrame.drop([index], inplace=True)
else:
    returnFrame.sort_values(inplace=True, by=["alter"], ascending=False)
    returnFrame.reset_index(inplace=True, drop=True)

print(returnFrame)
