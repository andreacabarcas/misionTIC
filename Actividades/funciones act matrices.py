def llenarMatriz():
   cantidad = int(input("Digite el tamaño de la matriz: "))
   matriz= [] # lista de listas
   for i in range(cantidad):
        vector = [] #lista
        for j in range(cantidad):
            elemento = int(input(f"Digite el número en la fila {i} columna {j}: "))
            while elemento < 1:
                print("Los números ingresados deben de estar por encima de 1. ")
                elemento = int(input(f"Digite el número en la fila {i} columna {j}: "))
            vector.insert(j,elemento)
            print(vector)
        matriz.insert(i,vector)
   return matriz

def imprimir(matrix):
   for x in range(len(matrix)):
     print()
     print(matrix[x], end=' ') 

def buscar(matrix,elemento):
    bandera = False
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == elemento:
                print(f"Encontrado el elemento {elemento} en la fila {i} columna{j}")
                bandera = True
                break
    if bandera == False:
        print(f"El elemento {elemento} no se encuentra en la matriz. ")   
                 
def actualizarElemento(matrix,f,c,elemento):    
    oldElemento = matrix[f][c] #Se guarda el elemento anterior en una variable oldElemento
    matrix[f][c]= elemento #Se reemplaza el elemento anterior por el nuevo
    print(f"El elemento {oldElemento} estaba en la posición fila {f} columna {c}, se ha reemplazado por {elemento}.")

def eliminarElemento(matrix,f,c):    
    oldElemento = matrix[f][c] #Se guarda el elemento anterior en una variable oldElemento
    matrix[f][c]= 0 #Se reemplaza el elemento anterior por el nuevo
    print(f"El elemento {oldElemento} estaba en la posición fila {f} columna {c}, se ha reemplazado por 0.")
    
def menu():
    print()
    op= 0
    while op < 1 or op > 14:
       print("1. Crear o llenar  una matriz \n"
       "2. Imprimir una matriz \n3. Buscar un elemento en la Matriz \n4. Actualizar un elemento en la Matriz \n5. Eliminar un elemento en la Matriz \n6. Ordenar de menor a mayor una fila seleccionada de la matriz \n7. Diagonal principal \n8. Diagonal Secundaria \n9. Hallar el número mayor en la matriz \n10. Hallar el número menor en la matriz \n11. Contar la cantidad de números pares \n12. Contar la cantidad de números impares \n13. Hallar el promedio de la matriz \n14. Salir")
       op = int(input())
    return op