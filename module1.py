def registreerimine(email:list,login:list,password:list):
    """
    """
    failname = "TextFile1.txt"
    try:
        f = open(failname,'a',encoding="utf-8")
        login = input("Sisestage kasutaja login: ") 
        password = input("Sisestage kasutaja password: ") 
        email = input("Sisestage kasutaja email: ") 
        f.write(f"{login}, {email}, {password}"+"\n")
        print("Te olete registreerunud""\n")
    except: print("Viga! Proovi uuesti")

    
