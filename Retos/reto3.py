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


entradasIniciales=dividirEntrada(input(""))

cantidadSucursales=entradasIniciales[0]
cantidadPacientes=entradasIniciales[1]
cantidadMedicamentos=[]
cantidadProgramadaMedicamentos=[]
for i in range (cantidadSucursales):
    cantidadMedicamentos.append(validarEntrada("",""))
    cantidadProgramadaMedicamentos.append(0)

for j in range (cantidadPacientes):
    valores=dividirEntrada(input(""))
    numeroSucursal=valores[0]
    presionSistolica=valores[1]
    presionDiastolica=valores[2]
    if numeroSucursal>=1 and numeroSucursal<=cantidadSucursales:
        ctdMedXPaciente=validarPresion(presionSistolica,presionDiastolica)
        cantidadProgramadaMedicamentos[numeroSucursal-1]=cantidadProgramadaMedicamentos[numeroSucursal-1]+ctdMedXPaciente

sucursalMenor=1
cantidadMenor=cantidadMedicamentos[0]-cantidadProgramadaMedicamentos[0]
sucursalMayor=1
cantidadMayor=cantidadMedicamentos[0]-cantidadProgramadaMedicamentos[0]

for k in range(cantidadSucursales):
    cantidadExistencia=cantidadMedicamentos[k]-cantidadProgramadaMedicamentos[k]
    if cantidadExistencia<cantidadMenor:
        cantidadMenor=cantidadExistencia
        sucursalMenor=k+1
    if cantidadExistencia>cantidadMayor:
        cantidadMayor=cantidadExistencia
        sucursalMayor=k+1
print(sucursalMenor,cantidadMenor)
print(sucursalMayor,cantidadMayor)

for l in range(cantidadSucursales):
    print(l+1,format((cantidadProgramadaMedicamentos[l]/cantidadMedicamentos[l])*100, '.2f')+"%")
    



