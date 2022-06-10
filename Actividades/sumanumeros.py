i = 1
suma = 0
while (i <= 10):
    numero = int(input(f"Digite un número {i}:  "))
    print("cuando i vale:",i, ",   la suma va en:", suma, "   y el valor ingresado es:", numero)
    suma = suma + numero
    i += 1
print ("La suma de los números ingresados es:  ", suma)
