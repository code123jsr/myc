a=[];
c=[];
n=int(input("enetr the number of terms"));
for i in range (1,n+1):
    b=int(input("enter the elements in list"));
    a.append(b)
for j in a:
    if(j>0):
        c.append(j)
print(c)
