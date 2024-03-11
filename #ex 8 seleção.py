#ex 8 seleção
cont=1
while (cont<=6):
    n1 = int (input("Digite o 1° número: "))
    n2 = int (input("Digite o 2° número: "))
    n3 = int (input("Digite o 3° número: "))

    if(n1>n2):
        if(n1>n3):
            print ("O maior número é o ", n1)
        else:
            print ("O maior número é o ", n3)
    else:
        if (n2>n3):
            print ("O maior número é o ", n2)
        else:
            print ("O maior número é o ", n3)
    cont=cont+1


