#ex6sel
s=0
for x in range(1,11):
    if(x%2==0):
        s-=1/x
    else:
        s+=1/x
print(s)
