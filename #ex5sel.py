#ex5sel
'''nom=1
den=1
s=0

while (nom<=99):
    s += nom/den
    nom+=2
    den+=1
print (s)'''
s=0
for x in range(1,51):
    s+=((2*x-1)/x)
print(s)