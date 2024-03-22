#ex7 rep
n = int(input(f"Digite a quantidade de números que deseja digitar (maior ou igual a 10): "))

while (n<10):
    print (f"Digite um número inválido")
    n= int(input(f"Digite a quantidade de números que deseja digitar (maior ou igual a 10): "))


maior = menor = int(input("Digite o 1º número inteiro: "))
for i in range(n - 1):
    x = int(input(f"Digite o {i + 2}º número inteiro: "))
    if x > maior:
        maior = x
        
    if x < menor:
         menor = x
    
   
print(f"O maior número digitado é: {maior}")
print(f"O menor número digitado é: {menor}")
