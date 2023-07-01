import random

european_countries = [
    "Albanija", "Andora", "Armenija", "Austrija", "Azerbejdžan", "Belgija",
    "Bjelorusija", "Bosna i Hercegovina", "Bugarska", "Crna Gora", "Češka",
    "Danska", "Estonija", "Finska", "Francuska", "Grčka", "Holandija",
    "Hrvatska", "Island", "Irska", "Italija", "Kazahstan", "Kosovo",
    "Latvija", "Litvanija", "Luksemburg", "Mađarska", "Makedonija", "Malta",
    "Moldavija", "Monako", "Njemačka", "Norveška", "Poljska", "Portugal",
    "Rumunija", "Rusija", "San Marino", "Slovačka", "Slovenija", "Srbija",
    "Sjeverna Makedonija", "Španija", "Švedska", "Švicarska", "Turska",
    "Ujedinjeno Kraljevstvo", "Ukrajina", "Vatikan"
]

european_country = random.choice(european_countries)
print("Okej, ja mislim na jedno evropsku drzavu, pogodi njeno ime!")
print("Prvo slovo je...", european_country[0] )
guess1 = input("Ta drzava je? ")
if guess1 != european_country:
    print("Netacno! ")
else:
    print("Uspesno si pogodio, bravo!")
print("Prvo slovo je, ", european_country[0], "trece slovo je", european_country[2])
guess2 = input("Ajde pogodi opet, imas jos 1 pokusaj posle ovog: ")
if guess2 != european_country:
    print("netacno, ajde dat cu ti jos 1 slovo.")
if guess2 == european_country:
    print("Bravo, pogodio si!")
guess3 = input("Treca sreca, Zadnje slovo je..", european_country[-1])
if guess3 != european_country:
    print("Netacno, tacan odgovor je", european_country)
if guess3 == european_country:
    print("Napokon! Tacan odgovor, bravo!")
