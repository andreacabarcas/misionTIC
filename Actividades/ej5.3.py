numero=list(input("ingrese numero de 3 cifras"))
digitos=len(numero)
if digitos != 3:
    print("error")
else:
 pos1 = str(numero[0])
 pos2 = str(numero [1])
 pos3 = str(numero [2])
 max=max(numero)
 min=min(numero)
if(pos1==max) and (pos2==min):
    print(pos1 + pos3 + pos2)
elif (pos1 == max) and (pos3 == min):
    print(pos1 + pos2 + pos3)
elif(pos2==max) and (pos1==min):
    print(pos2 + pos3 + pos1)
elif(pos2==max) and (pos3==min):
    print(pos2 + pos1 + pos3)
elif(pos3==max) and (pos1==min):
    print(pos3 + pos2 + pos1)
else:
    print(pos3 + pos1 + pos2)