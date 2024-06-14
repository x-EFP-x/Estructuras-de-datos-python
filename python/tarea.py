a=input()
b=[]
c=len(a)
for i in range (c):
    if (a[i]!="["):
        if(a[i]!="]"):
            if(a[i]!=","):
                b.append(a[i])
print(b)
