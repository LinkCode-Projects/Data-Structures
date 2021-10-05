n = int(input("Enter Number"))
for x in range(n):
    print(" "*(n-x), end="")
    print(" ".join(map(str,str(11**x))))