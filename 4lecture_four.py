# Dictionries in python - DICTONARIES ARE USED TO STORE DATA VALUES AS KEY:VALUE PAIRS
info={
"name" : "ayush",
"age" : 18,
"subjects" : ["python","html","css","java script"],
}
print(info["name"])
print(info["age"])
print(info["subjects"])
print(info)

print(info.keys())   #return all the keys in dictionary.

print(info.values())   #return all the values.

print(info.items())   #return all the keys and values pairs

print(info.get("name"))    #return the value for the key if present in dictionary

new={"income" : "1cr" ,"adress" : "mp"}
info.update(new)
print(info)






#Sets is the collection of unordered items.each element inside the set must be unique and immutable
setA={1,2,4,7,9}

setA.add(3)   #adds an element
setA.remove(9)  #removes an elements
setA.clear()    #empty the set


set1={1,2,3}
set2={3,4,5}
print(set1.union(set2))  #combines the elements of set and returns unique value (1,2,3,4,5)
print(set1.intersection(set2) )  #combines the similar value and return




#practice
dict={
   "table" : ["a piece of furniture","list of facts and figures"],
     "cat" : "a small animal"
      }
print(dict)



set={
    "python","java","c++","python","javascript","java","python","java","c++","c"
}
print(len(set))




dic={}
a=int(input("enter a python num"))
dic.update({"python":a})
b=int(input("enter a html no."))
dic.update({"html":b})
c=int(input("enter a javascript no."))
dic.update({"javascript":c})
print(dic)


    