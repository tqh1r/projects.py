prvibroj = int(input("Unesite prvi broj: "))
drugibroj = int(input("Unesite drugi broj: "))
print("""Vazece operacije jesu:
1) + jeste sabiranje
2) - jeste oduzimanje
3) * jeste mnozenje
4) / jeste djeljenje """)

operacija = input("Unesite operaciju: ")

if operacija == "+":
    print("Rezultat je:",  prvibroj + drugibroj)
if operacija == "-":
    print("Rezultat je:",  prvibroj - drugibroj)
if operacija == "*":
    print("Rezultat je:",  prvibroj * drugibroj)
if operacija == "/":
    print("Rezultat je:",  prvibroj / drugibroj)


