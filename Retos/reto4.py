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
    programacionEntrega=False
    if(presionSistolica<80) and (presionDiastolica<60):
        programacionEntrega=True
    #elif(presionSistolica>=80) & (presionSistolica<120) & (presionDiastolica>=60) & (presionDiastolica<80):
    #elif(presionSistolica>=120) & (presionSistolica<130) &(presionDiastolica>=80) &(presionDiastolica<85):
    elif(presionSistolica>=130) & (presionSistolica<140) & (presionDiastolica>=85) &(presionDiastolica<90):
        programacionEntrega=True
    elif(presionSistolica>=140) & (presionSistolica<160) &(presionDiastolica>=90) & (presionDiastolica<100):
        programacionEntrega=True
    elif(presionSistolica>=160) & (presionSistolica<180) & (presionDiastolica>=100) &(presionDiastolica<110):
        programacionEntrega=True
    elif(presionSistolica>=180) & (presionDiastolica>=110):
        programacionEntrega=True
    elif(presionSistolica>=140) & (presionDiastolica<90):
        programacionEntrega=True
    return programacionEntrega

def dividirEntrada (entrada):
    numeros=entrada.split()
    numerosEnteros=[]
    for hola in numeros:
        numerosEnteros.append(int(hola))
    return numerosEnteros

def estadisticasSucursal (numSucursal,cantidadMedTotales,existenciasMed,cantidadProgramada,matrizPacientes):
    print(numSucursal+1)
    medMenor=0
    ctdMenor=existenciasMed[numSucursal][0]
    medMayor=0
    ctdMayor=existenciasMed[numSucursal][0]
    for i in range(cantidadMedTotales):
        if existenciasMed[numSucursal][i] < ctdMenor: 
            medMenor=i
            ctdMenor=existenciasMed[numSucursal][i]
        if existenciasMed[numSucursal][i] > ctdMayor:
            medMayor=i
            ctdMayor=existenciasMed[numSucursal][i]
    print(medMenor+1, ctdMenor)
    print(medMayor+1, ctdMayor)
    print(format(min(cantidadProgramada[numSucursal]),'.2f'),format(sum(cantidadProgramada[numSucursal])/len(cantidadProgramada[numSucursal]),'.2f'), format(max(cantidadProgramada[numSucursal]),'.2f'))
    acumulador=0
    contador=0
    for i in range (len(matrizPacientes)):
        if matrizPacientes[i][0] == numSucursal+1:
            acumulador=acumulador+matrizPacientes[i][2]
            contador+=1
    try:       
        print(format(acumulador/contador,'.2f'))
    except:
        print('0.00')

def estadisticasMedicamentos (cantidadProgramada,tipoMed):
    sucMenor=0
    ctdSucMenor=cantidadProgramada[0][tipoMed-1]
    sucMayor=0
    ctdSucMayor=cantidadProgramada[0][tipoMed-1]
    for i in range (len(cantidadProgramada)):
        if cantidadProgramada[i][tipoMed-1] < ctdSucMenor: 
            sucMenor=i
            ctdSucMenor=cantidadProgramada[i][tipoMed-1]
        if cantidadProgramada[i][tipoMed-1] > ctdSucMayor:
            sucMayor=i
            ctdSucMayor=cantidadProgramada[i][tipoMed-1]
    print (sucMenor+1,ctdSucMenor)
    print (sucMayor+1, ctdSucMayor)


entradasIniciales=dividirEntrada(input(""))
#print (entradasIniciales)

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
    vectorCtdXMed=dividirEntrada(input(""))
    matrizMed.insert(i,vectorCtdXMed)
    vectorCtdMedXProg=[]
    for i in range (cantidadTipoMedicamentos):
        vectorCtdMedXProg.append(0)
    cantidadProgramadaMedicamentos.insert(i,vectorCtdMedXProg) #inserta en la iesima posicion el vector
#print(matrizMed)
#print(cantidadProgramadaMedicamentos)
       
for i in range (cantidadPacientes):
    vectorPacientes=[]
    vectorPacientes=dividirEntrada(input(""))
    x=vectorPacientes[0] #sucursal
    y=vectorPacientes[1] #tipo medicamento
    z=vectorPacientes[2] #existencias
    presionSistolica=vectorPacientes[3]
    presionDiastolica=vectorPacientes[4]
    if validarPresion(presionSistolica,presionDiastolica):
        matrizPacientes.append(vectorPacientes) #para que las posiciones no queden vacias
        matrizMed[x-1][y-1]-=z
        cantidadProgramadaMedicamentos[x-1][y-1]+=z
    #como llenar otra matriz del tamaño sucursal X tipomed con contenido existencias a entregar
#print(matrizPacientes)

for i in range(cantidadSucursales):
    estadisticasSucursal(i,cantidadTipoMedicamentos,matrizMed,cantidadProgramadaMedicamentos,matrizPacientes)
estadisticasMedicamentos(cantidadProgramadaMedicamentos,1)


