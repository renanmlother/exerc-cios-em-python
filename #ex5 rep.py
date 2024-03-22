#ex5 rep
a = float(input(f"Digite o valor de a: "))
b = float(input(f"Digite o valor de b: "))
c = float(input(f"Digite o valor de c: "))
d = float(input(f"Digite o valor de d: "))
e = float(input(f"Digite o valor de e: "))
f = float(input(f"Digite o valor de f: "))

while (a != 0 or b != 0 or c != 0 or d != 0):
    if (a * e - b * d == 0):
        print(f"Sistema sem solução.")
    else:
        x = (c * e - b * f) / (a * e - b * d)
        y = (a * f - c * d) / (a * d - b * c)
        print("x =", x)
        print("y =", y)
    a = float(input(f"Digite o valor de a: "))
    b = float(input(f"Digite o valor de b: "))
    c = float(input(f"Digite o valor de c: "))
    d = float(input(f"Digite o valor de d: "))
    e = float(input(f"Digite o valor de e: "))
    f = float(input(f"Digite o valor de f: "))
print (f"Programa finalizado.")