n = int (input("Enter any number to reverse: "))
rev = ""
while n > 0:
    dig = n % 10
    rev = rev + str(dig)
    n = n//10
print("After reversing the number: ",rev)