a=0;
b=1;
c=0;
n=int(input("enter the number of terms"));
if (n==0):
    print("invalid")
elif(n==1):
    print(a)
else:
    print("The fibonacci series with ",n,"terms is")
    while c<n:
        print(a)
        d=a+b;
        a=b;
        b=d;
        c+=1;
