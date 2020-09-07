#Engels
#14/08/2020
#calcula los cm que puede reocrrer un caracole en los minutos dados
n=0
m=0
a = input()
while a[n]!= " ":
    n = n+1
n=n+1
o=n
while a[m]!=a[n]:
    if n==(len(a)-1):
        n=o
        m=m+1
    else:
        n=n+1
x=0
y=o
t=len(a)
o=o-1
l=""
while y!=t:
    if y!=n:
        while x!=o:
            if x!=m:
                l=l+"."
            else:
                l=l+a[y]
            x=x+1
        print(l)
        l=""
        x=0
    else:
        print(a[:(o+1)])
    y=y+1    
