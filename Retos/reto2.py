cantidadPacientes=int(input(" "))
mujeresAlta=0
mujeresBaja=0
mujeresNormal=0
hombresAlta=0
hombresBaja=0
hombresNormal=0
for x in range(cantidadPacientes):
  valorHemoglobina = float(input(" "))
  generoPaciente= int(input(" "))
  while (generoPaciente != 1) and (generoPaciente != 2):
   generoPaciente= int(input(" "))
  if (generoPaciente == 1) & (valorHemoglobina <= 13.2):
     mujeresBaja=mujeresBaja+1
  elif (generoPaciente == 1) & (valorHemoglobina >= 16.6):
     mujeresAlta=mujeresAlta +1
  elif (generoPaciente ==1):
     mujeresNormal=mujeresNormal+1
  elif (generoPaciente == 2) & (valorHemoglobina <= 11.6):
     hombresBaja=hombresBaja+1
  elif (generoPaciente == 2) & (valorHemoglobina >= 15):
     hombresAlta=hombresAlta+1
  else:
     hombresNormal=hombresNormal+1  
print(hombresBaja,hombresAlta,hombresNormal,mujeresBaja,mujeresAlta,mujeresNormal)