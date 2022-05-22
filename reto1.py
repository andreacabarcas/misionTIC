print("Deteccion de enfermedades tempranas asociadas con el nivel de hemoglobina")
valorHemoglobina = float(input("Digite el valor de la hemoglobina del paciente en g/dL"))
generoPaciente= int(input("Digite 1 si el paciente es de genero femenino o 2 si es de genero masculino"))
if (generoPaciente != 1) & (generoPaciente !=2):
    print("No es posible generar la alerta")
else:
    if (generoPaciente == 1) & (valorHemoglobina < 13.2):
     print("Baja")
    elif (generoPaciente == 1) & (valorHemoglobina > 16.6):
     print("Alta")
    elif (generoPaciente == 2) & (valorHemoglobina < 11.6):
     print("Baja")
    elif (generoPaciente == 2) & (valorHemoglobina > 15):
     print("Alta")
    else:
     print("Normal")

