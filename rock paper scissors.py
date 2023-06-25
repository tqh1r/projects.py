import random
print("Ajde da igramo papir, kamen, makaze!")
opcije = ("Papir", "Kamen", "Makaze")

player = input("Izaberite: ")
bot = random.choice(opcije)
print("Papir, kamen, makaze! Ja sam izabrao " + bot)

if player == "Papir":
    if bot == "Papir":
        print("Nereseno!")
    elif bot == "Kamen":
        print("Pobedili ste!")
    elif bot == "Makaze":
        print("Izgubili ste!")
elif player == "Kamen":
    if bot == "Papir":
        print("Izgubili ste!")
    elif bot == "Kamen":
        print("Nereseno!")
    elif bot == "Makaze":
        print("Pobedili ste!")
elif player == "Makaze":
    if bot == "Papir":
        print("Pobedili ste!")
    elif bot == "Kamen":
        print("Izgubili ste!")
    elif bot == "Makaze":
        print("Nereseno!")
else:
    print("Nevazeca opcija")
