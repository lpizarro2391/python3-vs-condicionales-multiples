moneda1=input('ingrese el nombre de la moneda')
cant1=float(input('ingrese la cantidad de '+moneda1+":"))
moneda2=input('ingrese el nombre de la moneda')
cant2=float(input('ingrese la cantidad de '+moneda2+":"))
moneda3=input('ingrese el nombre de la moneda')
cant3=float(input('ingrese la cantidad de '+moneda3+":"))
if cant1>cant2 and cant1>cant3:
    print(moneda1,cant1)
    if cant2>cant3:
        print(moneda2,cant2)
        print(moneda3,cant3)
    else:
        print(moneda3,cant3)
        print(moneda2,cant2)
elif cant2>cant1 and cant2> cant3:
    print(moneda2,cant2)
    if cant1>cant3:
        print(moneda1,cant1)
        print(moneda3,cant3)
    else:
        print(moneda3,cant3)
        print(moneda1,cant1)
else:
    print(moneda3,cant3)
    if(cant1>cant2):
        print(moneda1,cant1)
        print(moneda2,cant2)
    else:
        print(moneda2,cant2)
        print(moneda1,cant1)