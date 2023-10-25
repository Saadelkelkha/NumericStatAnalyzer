t=[]
s=0
p=1
for i in range (0,10) :
    print("type the number N",i+1,":")
    n=float(input())
    t.append(n)
    s=s+n
    p=p*n
m=s/10
print("The sum is",s)
print("The multiplication",p)
print("The average",m)