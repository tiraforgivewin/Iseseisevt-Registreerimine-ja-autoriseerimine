import string
import random 
from random import choice

def salasona(k: int):
    sala = ""
    for i in range(k):
        t = choice(string.ascii_letters)  # Aa...Zz
        num = choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        t_num = t + str(num)
        sala += choice(t_num)
    return sala

def login_cheak(login: str):
    login_len = False
    if 8 < len(login) < 25:
        login_len = True
    else:
        print("Login peab olema pikkusega 8-25 tähemärki!")
    return login_len

def password_cheak(password:str):
    simbols_set = "!@#$=%^&><*€%+?"
    pass_len = up = low = dig = simb = False
    if len(password) >= 8 and len(password) <= 16:
        pass_len = True
    else:
        print("Parool peab olema pikkusega 8-16 tähemärki!")
    for char in password:
        if char.isupper():
            up = True
        elif char.islower():
            low = True
        elif char.isdigit():
            dig = True
        elif char in simbols_set:
            simb = True
    return pass_len and up and low and dig and simb

def email_cheak(email: str):
    if "@" in email and "." in email:
        return True
    else:
        print("Viga posti aadressis!")

def registreerimine(email:str,login:str,password:str):
    """
    """
    failnimi = "TextFile1.txt"
    try:
        with open(failnimi, 'a', encoding="utf-8") as f:
            login = input("Sisestage kasutaja login: ")
            if not login_cheak(login):
                return
            val = input("Kui soovite automaatset parooli genereerimist, vajutage 1. Kui soovite sisestada oma, vajutage 2.\n")
            if val == "1":
                password = salasona(random.randint(8, 16))
                print(f"Genereeritud parool on: {password}")
            elif val == "2":
                password = input("Sisestage kasutaja password: ")
                if not password_cheak(password):
                    return
            else:
                print("Vigane valik!")
                return
            email = input("Sisestage kasutaja email: ") 
            if not email_cheak(email):
                return
            f.write(f"{login}, {password}, {email}\n")
            print("Te olete registreerunud\n")
    except Exception as e:
        print(f"Viga! {e}")

def autoriseerimine():
    filename = "TextFile1.txt"
    try:
        login = input("Sisestage kasutajanimi: ")
        password = input("Sisestage parool: ")
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                user_data = line.strip().split(",")  
                if len(user_data) == 3:  
                    username, stored_password = user_data[0], user_data[1]  # Parooli indeks on 1
                    if username == login and stored_password.strip() == password:  # Kasutame strip() parooli puhastamiseks
                        print("Autentimine õnnestus!")
                        return True
            print("Sisselogimine ebaõnnestus. Vale kasutajanimi või parool.")
            return False
    except Exception as e:
        print(f"Viga! {e}")
        return False  
    

def login_update():
    filename = "TextFile1.txt"
    try:
        login = input("Sisestage kasutajanimi: ")
        password = input("Sisestage praegune parool: ")
        with open(filename, 'r', encoding="utf-8") as file:
            lines = file.readlines()
        with open(filename, 'w', encoding="utf-8") as file:
            for line in lines:
                user_data = line.strip().split(",")  
                if len(user_data) == 3:  
                    username, stored_password = user_data[0], user_data[1]
                    if username == login and stored_password.strip() == password:
                        new_password = input("Sisestage uus parool: ")
                        new_username = input("Sisestage uus kasutajanimi: ")
                        file.write(f"{new_username}, {new_password}, {user_data[2]}\n")
                        print("Parooli ja/või kasutajanime muutmine õnnestus!")
                        return
                    else:
                        file.write(line)
            print("Sisselogimine ebaõnnestus. Vale kasutajanimi või parool.")
    except Exception as e:
        print(f"Viga! {e}")
        

def password_recovery():
    filename = "TextFile1.txt"
    try:
        email = input("Sisestage oma e-posti aadress: ")
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                user_data = line.strip().split(",")  
                if len(user_data) == 3:  
                    stored_email, stored_password = user_data[2], user_data[1]
                    if stored_email.strip() == email:
                        print(f"Teie unustatud parool on: {stored_password}")
                        return
            print("Kasutajat selle e-posti aadressiga ei leitud.")
    except Exception as e:
        print(f"Viga! {e}")
        
def valja_logimine():
    print("Olete välja logitud oma kontolt.")
