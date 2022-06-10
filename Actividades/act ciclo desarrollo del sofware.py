#actividad ciclo desarrollo del sofware

"""def conteoGenero(lista,cantidad):
    contadorF=0
    contadorM=0
        for i in range (cantidad):
            if lista[i]=="f":
                contadorF=contadorF+1
            else:
                contadorM=contadorM+1   
    print(f"la cantidad de mujeres es {contadorF} ")
    print(f"la cantidad de hombres es {contadorM}")"""

cantidadEstudiantes=int(input("Digite el numero de estudiantes: "))
vectorNombre=[]
vectorApellido=[]
vectorEdad=[]
vectorGenero=[]
for i in range (cantidadEstudiantes):
    nombre=str(input("Digite el nombre: "))
    vectorNombre.append(nombre)
    apellido=str(input("Digite el apellido: "))
    vectorApellido.append(apellido)
    edad=int(input("Digite la edad: "))
    vectorEdad.append(edad)
    genero=str(input("Digite el genero: "))
    vectorGenero.append(genero)
print(vectorNombre , vectorApellido , vectorEdad , vectorGenero)

acumulador=0
for j in range (cantidadEstudiantes):
    acumulador=vectorEdad[j]+acumulador
promedio=acumulador/cantidadEstudiantes
print(f"el promedio de edad es {promedio}") 




contadorF=0
contadorM=0
for j in range (len(vectorGenero)):
    if vectorGenero[j]=="f":
        contadorF=contadorF+1
    else:
        contadorM=contadorM+1
print(f"la cantidad de mujeres es {contadorF} ")
print(f"la cantidad de hombres es {contadorM}")


"""contadorPar=0
contadorImpar=0
for j in range (cantidadEstudiantes):
    if vectorEdad[j]%2 """