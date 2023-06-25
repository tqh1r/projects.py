print("Konvertor Temperature")

jedinice = input("""
Iz koje jedinice u koju jedinicu biste željeli da pretvorite temperaturu, vazece opcije jesu
1) Celzijus (Celsius) u Fahrenhajt (Fahrenheit)
2) Fahrenhajt (Fahrenheit) u Celzijus (Celsius)
Izaberite: """)

if jedinice == "1":
    cf = float(input("Koliko Celzijus (Celsius) biste željeli da pretvorite? "))
    cfp = cf * 1.8 + 32
    print(str(cf) + " Celzijusa (Celsius) je " + str(cfp) + " Fahrenhajta (Fahrenheit)")

if jedinice == "2":
    fc = float(input("Koliko Fahrenhajta (Fahrenheit) biste željeli da pretvorite? "))
    fcp = (fc - 32) / 1.8
    print(str(fc) + " Fahrenhajta (Fahrenheit) je " + str(fcp) + " Celzijusa (Celsius)")
