BITCOIN=7630.80
DASHUSD=315.56
LTCUSD=120.84
moneda=input("ingrese la moneda a utilizar (BTC, DASH o LTC):")
if moneda=="BTC" or moneda=="DASH" or moneda=="LTC":
    cantidad=float(input("ingrese la cantidad a utilizar:"))
    if moneda=="BTC":
        monto=cantidad * BITCOIN
    elif moneda=="DASH":
            monto=cantidad * DASHUSD
    else:
            monto=cantidad * LTCUSD
    print("la cantidad de USD recargado fue de: "+str(monto))
else:
    print("Error solo se permite utilizar BTC, DASH o LTC")
