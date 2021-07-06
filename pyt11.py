# letter replace

letter='''Dear namea,
You are Selected!

Date: <|Date|>
'''
name=input("Enter name:\n")
date=input("Enter date:\n")
letter = letter.replace("namea",name)
letter = letter.replace("<|Date|>",date)
print(letter)