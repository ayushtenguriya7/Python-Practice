r=int(input("Enter no. of rows: "))
c=int(input("Enter no. of columns: "))
matrix=[]
for i in range(1,r+1):
    row=[]
    for j in range (1,c+1):
        el=int(input("Enter elements: "))
        row.append(el)
    matrix.append(row)
print(matrix)