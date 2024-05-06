from module1 import *

email = []
login = []
password = []
while True:
    t = int(input("Valige suvanad:\n 1.Registreerimine\n 2.Autoriseerimine\n 3.Nime või parooli muutmine\n 4.Unustanud parooli taastamine\n 5.Lõpetamine\n"))
    if t == 1:
        registreerimine(login,password,email)
    elif t==2:
        autoriseerimine()
    elif t==3:
        login_update()
    elif t==4:
        password_recovery()
    elif t==5:
        pass