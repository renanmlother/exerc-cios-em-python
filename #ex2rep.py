#ex2rep
n=int(input("Digite um número para saber quais números menores que ele são divisíveis por 4: "))
for i in range (1,n+1):
    if(i%4==0):
        print(i)