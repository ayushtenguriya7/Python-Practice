print("hello world")

# type FUNCTION
a=5
name="ayush"
print(type(a))    #int
print(type(name)) #str

# id FUNCTION
int=4
print(id(int))

# ARITHMETIC OPERATORS 
a=5
b=3
sum=a+b
print(sum)   #8

# LOGICAL OPERATORS
#and
nam1="ayush"
nam2="ayush"
print(nam1 and nam2)
#or
val1=21
val2=3
print(val1 or val2)
#not
d=50
e=21
print(not(d==e)) #TRUE


# RELATIONAL OPERATORS
a=5
b=5
c=2
print(a==b) #TRUE
print(b==c) #FALSE

# ASSINGMENT OPERATORS
num=10
num+=10
print(num)  #20

num1=10
num1**=10
print(num1)   #10000000000


# input function 
name= input("enter your name")
print("my name is:",name)

age= (input("enter your age:  "))
print("age",age)

#input two numbers and add their sum
first=float(input("enter a num1"))
second=float(input("enter second num"))
print(first+second)

#write a program to find the area of square
side = float(input("enter the length of the side"))
print("area of the square is:",side*side,"cm")