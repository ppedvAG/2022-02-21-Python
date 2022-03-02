f = open("error.txt", mode="w+")
try:
    for i in range(21):
        if i == 10:
            raise Exception("10 wurde erreicht")
        f.write(f"Zeile{i}\n")
except Exception as e:
    print(e)
finally:
    f.close()
