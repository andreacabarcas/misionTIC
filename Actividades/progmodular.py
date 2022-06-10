print("seleccione una de las siguientes opciones")
menu=int(input("1 para sumar, 2 para restar, 3 para multiplicar, 4 para dividir, 5 para finalizar el programa"))
while (menu != 5):
 menu=int(input("1 para sumar, 2 para restar, 3 para multiplicar, 4 para dividir, 5 para finalizar el programa"))
 while (menu>5) or (menu<1):
   menu=int(input(" la opción no es valida, por favor digite 1 para sumar, 2 para restar, 3 para multiplicar, 4 para dividir, 5 para finalizar el programa"))
   n1=int(input("Digite un numero"))
   n2=int(input("Digite otro numero"))
   while n2==0:
    n2=int(input("Digite otro numero"))
   if(menu==1):
    suma=n1+n2
    print(f"la suma de los numeros es {suma}")
   elif (menu==2):
    resta=n1-n2
    print(f"la resta de los numeros es {resta}")
   elif (menu==3):
    multiplicacion=n1*n2
    print(f"la multiplicacion de los numeros es {multiplicacion}")
   elif(menu==4):
    division=n1/n2
    print(f"la division de los numeros es {division}")
   else:
    print("se finalizará el programa")
    exit

