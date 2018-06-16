numbers=[-5, -12, -23, -6]
min_num=numbers[0]

for i in range(len(numbers)):
    if numbers[i] < min_num:
        min_num = numbers[i]

print('Największa licza w liście to: ',min_num)