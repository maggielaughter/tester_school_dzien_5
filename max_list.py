numbers=[-5, -12, -23, -6]
max_num=numbers[0]

for i in range(len(numbers)):
    if numbers[i] > max_num:
        max_num = numbers[i]

print('Największa licza w liście to: ',max_num)

a = max_num

for i in range(len(numbers)):
    if numbers[i]< a:
        a = numbers[i]
print('Najmniejsza liczba w liście to: ',a)