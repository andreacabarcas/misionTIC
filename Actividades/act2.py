haypeaton = str(input("hay peaton"))
colorLuz= str(input("digite el color de la luz del semaforo"))
if haypeaton == "si":
    print("pare")
elif colorLuz == "verde":
   print("Siga")
elif (colorLuz == "amarillo"):
   print("Precaucion")
elif (colorLuz == "rojo"):
   print("pare")
else: print("no es valido")