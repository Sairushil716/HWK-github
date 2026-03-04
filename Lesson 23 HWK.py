userint=int(input("Enter a number"))

list1=[]
for i in range(0,userint):
    list1.append(i)


list2=[x for x in list1 if x%2==1]

print(list2)

fruits=["Apple","Banana","Pear","Orange"]

print(fruits)