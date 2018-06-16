lst=[10, 10, 10, 2, 10, 3, 10, 45, 10, 10]
new_list=[]
# pierwszy sposób - błędny
for i, value in enumerate(lst):
    lst.remove(10)
print(lst)

#drugi sposób - błędny
for i, value in enumerate(lst):
    if lst[i]==10:
        del lst[i]
print(lst)

#sposób prowadzącego-pierwszy - nieefektywny
target = 10
count = 0

for idx, value in enumerate(lst):
    if value == target:
        count += 1

for i in range(count):
    lst.remove(target)
print(lst)

#sposób prowadzącego - drugi
target = 10
count = 0
to_delete=[]

for idx, value in enumerate(lst):
    if value==target:
        to_delete.append(idx)
for i in reversed(to_delete):
    del lst[i]

print(lst)

