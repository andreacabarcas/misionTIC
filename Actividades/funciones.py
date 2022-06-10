
def producto (numero):     
 print(f"esta es la tabla del numero {numero}")
 for i in range(1,11):
     multiplicacion=numero*i
     print(f"el resultado de multiplicar {numero} * {i} es {numero*i}")

def factorial(numero):
 factorial=1 
 for i in range(1,numero+1,1):
    factorial*=i
    print(f"el factorial de {numero} es {factorial}")

num=int(input("digite un numero a multiplicar"))
producto(num)
factorial(num)