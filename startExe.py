import os
import sys, subprocess

# os.system(r"C:/Windows/System32/notepad.exe")

# https://docs.python.org/3/library/subprocess.html
# https://stackoverflow.com/questions/21944895/running-powershell-script-within-python-script-how-to-make-python-print-the-pow
p = subprocess.Popen(["powershell.exe", r"C:\Users\ms5\Documents\Kurse\2021-02-21-Python\test.ps1", "Testfall"],
                     stdout=sys.stdout)
p.communicate()
