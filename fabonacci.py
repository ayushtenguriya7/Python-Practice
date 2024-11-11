#Day9 Fabonacci
def fabonacci(n):
    a=0
    b=1
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n-2):
        c=a+b
        b=c
        a=b
        print(c,end=" ")
    return(c)
n=int(input("Enter a num: "))
fabonacci(n)