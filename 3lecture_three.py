#Lists- It is an built in data type that stores sets of values
list=[1,5,7,9,0]
print(list[0])  #1  
print(list[0:5])  #slicing in list

#list functions

#append function- it is a function from which we can add anything else in the last of our list
list.append(55)
print(list)

#sorting function-- i is a function from which we can arrange the elements in ascending and decending order
list1=[99,95,105,455,100,0,1,12,25]
list1.sort() #command for ascending
print(list1)

list1.sort(reverse=True)  #it is a sorting command to arrange lists datan in descending
print(list1)

#reverse function- this function helps us to reverse all the values present in list from back to front
hello=["ram","shiv","krishna"]
hello.reverse()
print(hello)

#wap to input three movies and append it in a list
movies=[]
mov1=input("enter a first movie")
mov2=input("enter a second movie")
mov3=input("enter a third movie")
movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)

#insert function- this function can insert any value at any index in the list
int=[1,3,4,5,1]
int.insert(1,2)
print(int)

#remove fun- It removes the first occurence of elements
int.remove(1)
print(int)

#tuples in python
tup=(12,15,17,18)
print(tup.index(15))     #this function returns the index of element
print(tup.count(12))     #this function returns the occurence of elements


#WAP to check the list is palindrome using copy function
A=[1,2,3,3,2,1]
B=A.copy()
B.reverse()
if(A==B):
    print("palindrome")
else:
    print("not palindrome")



    #WAp to check the no. of students scored grade "A" in tuple
GRADE = ("A", "B", "A", "C", "A")
print(GRADE.count("A"))

   