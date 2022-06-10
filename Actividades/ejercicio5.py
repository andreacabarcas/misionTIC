numero = list(input("digite numero de 4 digitos"))
#list coloca en una posicion cada linea
cantidad = len(numero) #que hace len
if cantidad != 4:
    print("numero equivocado")
else:
    mayor = int(max(numero))
    print(mayor)
if mayor % 2 == 0:
    print("el numero es par")
else: print("el numero es impar")