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
    

cantidadSucursales=int(input("Digite numero de sucursales"))
cantidadPacientes=int(input("Digite el numero de pacientes"))
while cantidadSucursales<0:
    cantidadSucursales=int(input("Digite numero de sucursales"))
    cantidadPacientes=int(input("Digite el numero de pacientes"))
for i in range (1,cantidadSucursales+1,1):
    cantidadMedicamentos=int(input("Digite cantidad de medicamentos"))
    while cantidadMedicamentos < 0:
       cantidadMedicamentos=int(input("Digite cantidad de medicamentos")) 
for j in range (1,cantidadPacientes+1,1):
    numeroSucursal=int(input("DIgite el numero de la sucursal del paciente")) #toca guardarlo en un vector?
    presionSistolica=float(input("Digite el valor de la presion sistolica del paciente"))
    presionDiastolica=float(input("Digite el valor de la presion diastolica del paciente"))
    if(presionSistolica<80) and (presionDiastolica<60):
        categoria="Hipotension"
        tipoMedicamento=1
        numeroDosis=5
    elif(presionSistolica>=80) & (presionSistolica<120) & (presionDiastolica>=60) & (presionDiastolica<80):
        categoria="optima"
    elif(presionSistolica>=120) & (presionSistolica<130) &(presionDiastolica>=80) &(presionDiastolica<85):
        categoria="normal"
    elif(presionSistolica>=130) & (presionSistolica<140) & (presionDiastolica>=85) &(presionDiastolica<90):
        categoria="normal - alta"
        tipoMedicamento=1
        numeroDosis=2
    elif(presionSistolica>=140) & (presionSistolica<160) &(presionDiastolica>=90) & (presionDiastolica<100):
        categoria="Hipertension grado 1"
        tipoMedicamento=1
        numeroDosis=5
    elif(presionSistolica>=160) & (presionSistolica<180) & (presionDiastolica>=100) &(presionDiastolica<110):
        categoria="Hipertension grado2"
        tipoMedicamento=1
        numeroDosis=10
    elif(presionSistolica>=180) & (presionDiastolica>=110):
        categoria="Hipertension grado 3"
        tipoMedicamento=1
        numeroDosis=30
    elif(presionSistolica>=140) & (presionDiastolica<90):
        categoria="Hipertension sistolica aislada"
        tipoMedicamento=1
        numeroDosis=20
    else:
        categoria="muerto"

    

