#ex2 rep
n= int (input("Digite um número a ser elevado: "))
e= int (input("Digite o expoente: "))

cont=1
soma=1

if (e<=1):
    if (e==0):
        print ("1")
    else:
        print (n)

else:
    while (cont<=e):
        soma *= n
        cont= cont+1
print (soma)



