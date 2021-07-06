def check(yr):
        if yr < 40:
            return 2
        if yr < 20:
            return 3
yr = int(input("enter: "))
print(check(yr))