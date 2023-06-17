import random

while True:
    print("Dobrodosli, kreirajte svoj nalog.")
    user = input("Unesite svoje ime: ")
    password = input("Unesite svoju sifru: ")
    if "123" in password:
        print("Nesigurna sifra, probajte ponovo!")
        break        
    PIN = random.randint(100, 999)
    print("Vas PIN je:", PIN)
    confirmation = input("Da li ste sigurni? (Da/Ne): ")
    if confirmation.lower() == "da":
        print("Kreiranje naloga je uspelo.")
        break
    if confirmation.lower() == "ne":
        print("Kreiranje naloga nije uspjelo.")
        break
    else:
        print("Nevazeci unos, probajte ponovo!")

while True:
    print("Dobrodosli, prijavite se na vas postojeci nalog.")
    userlogin = input("Unesite vase ime: ")
    if userlogin != user:
        print("Netacno ime, probajte ponovo!")
        break
    passwordlogin = input("Unesite vasu sifru: ")
    if passwordlogin != password:
        print("Netacna sifra, probajte ponovo!")
        break
    pinlogin = input("Unesite vas PIN kod: ")
    if pinlogin != PIN:
        print("Netacan PIN kod, probajte ponovo.")
        break
