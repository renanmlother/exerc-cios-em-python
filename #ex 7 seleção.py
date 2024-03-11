#ex 7 seleção
n1 = float (input("Digite a primeira nota: "))
n2 = float (input("Digite a segunda nota: "))
p1 = float (input("Digite a primeira peso: "))
p2 = float (input("Digite a segundo peso: "))

m= ((n1*p1)+(n2*p2))/(p1+p2)

if(m>=7):

    if(m==10):
        print ("Aprovado com distinção")

    else:
        print("Aprovado")
else:
    print ("Reprovado")

