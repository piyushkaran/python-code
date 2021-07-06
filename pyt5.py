a=[]
n=int(input("Enter no. of elements"))
for i in range(1,n+1):
    b= int(input("Enter element:"))
    a.append(b)
a.sort()
print("largest element is:", a[n-1],a[n-2],a[n-3])