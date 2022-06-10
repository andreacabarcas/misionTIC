i = 1

suma = 0

contador = 0

limite = int(input("Digite el limite del ciclo: "))

while(i <= limite):

    numero = int(input(f"Digite un número {i}:  "))

    suma = suma + numero

    contador = contador + 1

    i +=1

print("La suma de los números es: ", suma)

print("La cantidad de números ingresados son: ", contador)

promedio = suma / contador

print("El promedio de los números es: ", promedio)