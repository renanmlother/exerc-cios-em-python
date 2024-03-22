#ex4 rep
n = int (input("Digite a quantidade de números que deseja inserir: "))

somapar= 0
somaimp= 0

while (n>0):
    num= int(input("Digite um número: "))
    if(num%2==0):
        somapar += num
    else:
        somaimp += num
    n=n-1
print(f"Soma dos pares: ", somapar) 
print(f"Soma dos ímpares: ", somaimp)     
