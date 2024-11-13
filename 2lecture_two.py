#concatenation
str1="ayush"
str2="tenguriya"
print(str1+str2) #ayushtenguriya

#length of string
print(len(str1)) #5 

#Indexing 'indexing is a function from which we can print even single character of string .it count first letter as a zero.
print(str1[2])    #u

#Slicing
print(str1[2:4])    #us
print(str1[ :4])    #ayus


#string functions
str="i am ayush"
print(str.endswith("sh"))    #true
print(str.endswith("uh"))     #false


print(str.capitalize())   #this function is used to make first small lette to capital


print(str.replace("ayush","tenguriya"))

print(str.find("ayush"))

print(str.count("a"))


#WAP to input user first name and print its length

firstname= input("enter your first name" )
print(len(firstname))

#WAP to find the occurence of '@'
password="@ar@you@@"
print(password.count("@"))

#Conditional statements
age=18
if(age>=18):
    print("you are eligible to apply for license and to vote")


colour="green"
if(colour=="red"):
    print("stop please")

elif(colour=="green"):
    print("go fast")

elif(colour=="yellow"):
    print("be ready to move")


marks=int(input("please enter your marks - "))

if marks>=90:
    grade="a"
elif marks>=80 and marks<90:
    grade="b"
elif marks>=70 and marks<80:
    grade="c"
else:
    grade="d"
print("grade of the student - ",grade)

#WAP to detect the number input by a user is even or odd
numb=int(input("enter A NUM - "))
rem= numb%2
if (rem==0):
    print("even")
else:
    print("odd")

    #wap to find the greatest of 3 numbers entered by the user
ans1=5
ans2=7
ans3=9
if(ans1>ans2 and ans1>ans3):
    print(ans1)
elif(ans2>ans1 and ans2>ans3):
    print(ans2)
else:
    print(ans3)


    #wap to check if a num is a multiple of 7 or not
x=9
if(x%7==0):
    print("x is multiple of 7")
else:
    print("x is not a multiple of 7")


    #wap to find the greATEST OF 4 NUM

    x1=1
    x2=3
    x3=5
    x4=7
    if(x1>x2>x3>x4):
        print("x1")
    elif(x2>x3>x4>x1):
        print("x2")
    elif(x3>x2>x1>x4):
        print("x3")
    else:
        print("X4")