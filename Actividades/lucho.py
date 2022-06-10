numerosALeer=int(input("cuantos numeros"))
contadorMultiplos=0
variableGuardadora =100000000
variableGuardadora2=-1000000
suma=0
producto=1
for lucho in range(numerosALeer):
    numero=int(input(f"ingrese numero {lucho+1}"))
    suma=suma+numero
    producto=producto*numero
    if(numero>variableGuardadora2):
        variableGuardadora2=numero
    if(numero<variableGuardadora):
        variableGuardadora=numero
    if  (numero%7 == 0):
        contadorMultiplos+=1
print(f"hay {contadorMultiplos} numeros multiplos de 7")
print(f"el numero menor es {variableGuardadora}")
print(f"la suma es {suma}")
print(f"el producto es {producto}")
factorial=1
for lucho2 in range(1,variableGuardadora2+1,1):
    factorial*=lucho2
print(f"el factorial es {factorial}")
    