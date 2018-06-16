lst = [-12, -3, -4, -123, -1]

for idx, value in enumerate(lst):
    if idx ==0:
        current_min = value
        current_max = value
    elif current_max < value:
        current_max=value
    elif current_min >value:
        current_min = value

print('Maksimum :', current_max)
print('Minimum :', current_min)