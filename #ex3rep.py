#ex3rep
cont=0
maior1 = maior2 = int(input("Digite o 1º número inteiro: "))
for i in range(9):
    x = int(input(f"Digite o {i + 2}º número inteiro: "))
    if x > maior1:
        maior2 = maior1
        maior1 = x
    elif x > maior2:
        maior2 = x
    
   
print(f"O maior número digitado é: {maior1}")
print(f"O segundo maior número digitado é: {maior2}")
