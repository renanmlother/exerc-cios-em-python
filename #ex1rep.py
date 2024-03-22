#ex1rep
cont25= 0
cont50=0
cont75=0
cont100=0

while True:
    n = int(input("Digite um número (digite um número negativo para encerrar): "))
    if n < 0:
        break
    if n <= 25:
        cont25 += 1
    elif n <= 50:
        cont50 += 1
    elif n <= 75:
        cont75 += 1
    else:
        cont100 += 1

print(f"[0,25]: ", cont25)
print(f"[26,50]: ", cont50)
print(f"[51,75]: ", cont75)
print(f"[76,100]: ", cont100)
print (f"Programa encerrado.")