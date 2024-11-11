#Right-Angled Triangle Number Pattern
n=5
for i in range (1,5):
    print("*")
    for j in range (1,i):
        if j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end="")
    print()