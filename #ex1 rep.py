#ex1 rep
p = int (input("Digite o plano atual: "))
s = float (input("Digite o salário atual: "))

if (p!=3):
    if(p==1):
        print(f"O novo salário é ", s+(0.1*s))
    else:
        print(f"O novo salário é ", s+(0.15*s))
else:
    print(f"O novo salário é ", s+(0.20*s))
    

