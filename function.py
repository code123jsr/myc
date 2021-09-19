s=input("Please enter a string ");
e=[];
for i in s:
    d = [i,s.count(i)];
    e.append(d)    
f=[];
for x in e:
    if x not in f:
        f.append(x)
def Sort(f):
    return(sorted(f, key = lambda x: x[1]))    
print(Sort(f))
h=Sort(f);
h.reverse()
print(h)
