print("Konvertor Valute")

valuta = input("""
Iz koje valute u koju valutu biste željeli da pretvorite novac, važeće opcije su:
1) Euro u Američki Dolar
2) Američki Dolar u Euro
Izaberite: """)

if valuta == "1":
    ea = float(input("Koliko Eura biste željeli da pretvorite? "))
    eap = ea * 1.093326
    print(str(ea) + " Eura je " + str(eap) + " Američkih dolara")

elif valuta == "2":
    ae = float(input("Koliko Američkih dolara biste željeli da pretvorite? "))
    aep = ae / 1.093326
    print(str(ae) + " Američkih dolara je " + str(aep) + " Eura")

else:
    print("Niste uneli validnu opciju!")
