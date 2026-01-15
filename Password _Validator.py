pwd = input("Enter Your Password: ")
p = len(pwd)
a = False
b = False
c = False

for ch in pwd:
    if ch.isupper():
        a = True
    if ch.islower():
        b = True
    if ch.isdigit():
        c = True

if 8 < p < 15 and a and b and c:
    print("Congrates Password is valid")
else:

    print("Password is invalid,You Need to Make More Strong Password!")
