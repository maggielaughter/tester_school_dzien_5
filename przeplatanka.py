list1=[1,2,3]
list2=['a','b','c']
list_finale=[]

if len(list1) == len(list2):
    for i in range (len(list1)):
        list_finale.append(list1[i])
        list_finale.append(list2[i])
    print(list_finale)

result2=[]

for i,value in enumerate(list1):
    result2.append(value)
    result2.append(list2[i])
print(result2)

result3 =[]
for first, second in zip(list1, list2):
    result3.append(first)
    result3.append(second)
print(result3)