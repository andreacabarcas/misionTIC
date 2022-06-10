numero = int(input("digite un numero entre 0 y 20"))
contador=1
while (numero>20 or numero<0):
    numero = int(input("digite un numero entre 0 y 20"))
    contador=contador+1
    if (contador==5):
        print("se han realizado 5 lecturas")
        break   
else:
    print("el numero es", numero)