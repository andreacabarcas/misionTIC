def validarEntrada (msg,msgError):       
    numero=0
    while True:
        try:
            numero = int(input(msg))
            if  numero>0:
                break
            else:
                print(msgError)
        except ValueError:
            print("no es un numero")
    return numero

def validarPresion (presionSistolica,presionDiastolica):
    '''
    Esta funcion asigna numero de dosis a entregar de acuerdo a los valores de presión del paciente
    '''
    numeroDosis=0
    if(presionSistolica<80) and (presionDiastolica<60):
        numeroDosis=5
    #elif(presionSistolica>=80) & (presionSistolica<120) & (presionDiastolica>=60) & (presionDiastolica<80):
    #elif(presionSistolica>=120) & (presionSistolica<130) &(presionDiastolica>=80) &(presionDiastolica<85):
    elif(presionSistolica>=130) & (presionSistolica<140) & (presionDiastolica>=85) &(presionDiastolica<90):
        numeroDosis=2
    elif(presionSistolica>=140) & (presionSistolica<160) &(presionDiastolica>=90) & (presionDiastolica<100):
        numeroDosis=5
    elif(presionSistolica>=160) & (presionSistolica<180) & (presionDiastolica>=100) &(presionDiastolica<110):
        numeroDosis=10
    elif(presionSistolica>=180) & (presionDiastolica>=110):
        numeroDosis=30
    elif(presionSistolica>=140) & (presionDiastolica<90):
        numeroDosis=20
    return numeroDosis

def dividirEntrada (entrada):
    numeros=entrada.split()
    numerosEnteros=[]
    for hola in numeros:
        numerosEnteros.append(int(hola))
    return numerosEnteros


entradasIniciales=dividirEntrada(input("Ingrese cantidad de sucursales, numero de tipos de medicamenrtos y cantidad total de pacientes"))
print (entradasIniciales)

cantidadSucursales=entradasIniciales[0]
cantidadTipoMedicamentos=entradasIniciales[1]
cantidadPacientes=entradasIniciales[2]
cantidadMedicamentosXSucursal=[]
cantidadProgramadaMedicamentos=[]
matrizMed=[]
matrizPacientes=[]


#se puede hacer una funcion para llenar matrices

for i in range (cantidadSucursales):
    vectorCtdXMed=[]
    vectorCtdXMed=dividirEntrada(input(f"Digite cantidad de medicamentos de cada tipo en la sucursal {i+1}"))
    matrizMed.insert(i,vectorCtdXMed)
print(matrizMed)
       
for i in range (cantidadPacientes):
    vectorPacientes=[]
    vectorPacientes=dividirEntrada(input(f"Digite numero de sucursal, tipo medicamento, existencias solicitadas, presion sistolica y presion diastolica del paciente {i+1}"))
    matrizPacientes.insert(i,vectorPacientes)
    x=matrizPacientes[i][0] #sucursal
    y=matrizPacientes[i][1] #tipo medicamento
    z=matrizPacientes[i][3] #existencias
    #como llenar otra matriz del tamaño sucursal X tipomed con contenido existencias a entregar
    for j in range (cantidadSucursales):
        vectorCtdProgMed=[]
        vectorCtdXMed.append(z)
print(matrizPacientes)





"""

for i in range (cantidadPacientes):
    temporal1=matrizPacientes[i][0] 
    temporal2=matrizPacientes[i][1] 
    print(temporal1 , temporal2)
    print(matrizPacientes[temporal1][temporal2])

for i in range (cantidadSucursales):
    vectorCtdProgMed=[]




for i in range (cantidadPacientes):
    for j in range (cantidadSucursales):
        presionSistolica=matrizPacientes[i][4]
        presionDiastolica=matrizPacientes[i][5]
        ctdMedXPaciente=validarPresion(presionSistolica,presionDiastolica)
        cantidadProgramadaMedicamentos=matrizPacientes[i][3]

#dejar las cantidades a entregar
for i in range (cantidadSucursales):
    for j in range:
         matrizMed[i][j]    
         """
