matriz=[[1,2,3],[4,5,6],[7,6,9]]
resultado1=[]
resultado2=[]
for i in range(len(matriz)):
    resultado1.append(matriz[i][i])
print("Diagonal Principal:")
print(resultado1)
#Diagonal Secundaria
for i in range(len(matriz)):
    resultado2.append(matriz[i][len(matriz)-i-1])
print("Diagonal Secundaria:")
print(resultado2)

"""Matriz =[

    [1,2,3] ,

    [4,5,6],

    [3,6,9]

]

diagonal=[]



for i in range(len(Matriz)):

 for j in range(len(Matriz[i])):

   if i == j:

        diagonal.append(Matriz[i][j])



print(diagonal)"""