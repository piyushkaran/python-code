s=0
n=int(input("Enter no. to check prime:"))
for i in range(1,n+1):
    if n%i==0:
        s=s+1
if s==2:
    print("prime")    
else:
    print(" not prime")    