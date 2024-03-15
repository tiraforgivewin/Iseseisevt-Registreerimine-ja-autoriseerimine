from module1 import *

email = []
login = []
password = []
while True:
    t = int(input("Valige suvanad:\n 1.Registreerimine\n "))
    if t == 1:
        registreerimine(email,login,password)
