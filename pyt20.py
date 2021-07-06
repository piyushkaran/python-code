a = int(input("Enter a: "))
b = int(input("Enter b: "))
print("before swapping a = ",a)
print("before swapping b = ",b)

a = a + b
b = a - b
a = a - b

print("After swapping a = ",a)
print("After swapping b = ",b)
