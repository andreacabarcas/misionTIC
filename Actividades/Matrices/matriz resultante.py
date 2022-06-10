filas = int(input("Ingresar el numero de filas= "))

columnas = int(input("Ingresar el numero de columnas= "))

matriz =[]

for i in range(filas):

    vector=[]  

    for j in range(columnas):

        numero = input("Digite número: ")

        vector.insert(j,numero)      

        print(vector)

    matriz.insert(i,vector)

print("******************Matriz resultante********************")

print(matriz)

print("*******************************************************")