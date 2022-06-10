numero1 = input("digite numero de 3 digitos")
numero2 = input("digite otro numero de 3 digitos")
digitos1 = len(numero1)
digitos2 = len(numero2)
if (digitos1 !=3) and (digitos2 != 3):
    print("error")
else:
 max1 = str(max(numero1))
 min2 = str(min(numero2))
 resultado= max1 + min2
 print(resultado)