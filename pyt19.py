sub1 = int(input("Enter sub 1 marks: "))
sub2 = int(input("Enter sub 2 marks: "))
sub3 = int(input("Enter sub 3 marks: "))
sub4 = int(input("Enter sub 4 marks: "))
sub5 = int(input("Enter sub 5 marks: "))
sub6 = int(input("Enter sub 6 marks: "))
avg = (sub1 + sub2 + sub3 + sub4 + sub5 + sub6) / 6
print(avg)
if avg >90:
    print("Grade A")
elif avg > 60:
    print("Grade B")
elif avg > 40:
    print("Grade c")
else: 
    print("Fail")
