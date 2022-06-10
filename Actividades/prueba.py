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
            print("Muy listo smart-ass, Ingresaste algo que no es un numero")
    return numero
    



miVariable=validarEntrada("Ingrese un numero mayor que cero: ","Se ingreso un numero menor que cero, por favor ingresar otro ") 
print(miVariable)

miVariable2=validarEntrada("Digite numero de medicamentos: ","Se ingreso un numero menor que cero, por favor ingresar otro ") 
print(miVariable2)