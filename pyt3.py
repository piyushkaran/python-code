def factorial(n):
    if(n==1):
        return n
    else:
        return n*factorial(n-1)
n=int(input("enter no. to find its factorial:"))
if n<0:
    print("Not found for less than 0")
if n==0:
    print("fact of 0 is: 1",)
else:
    print("fact of",n,"is:",factorial(n))