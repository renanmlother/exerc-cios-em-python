#ex6 rep
n= int (input("Digite um número para descobrir seu fatorial: "))
cont=1
fatorial=1
if (n==0):
    print("1")
else:
    while (cont<=n):
        fatorial *= cont
        cont= cont+1
print (fatorial)