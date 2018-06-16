numbers=[1,'foo',62,15,34]

"""for i in range(len(numbers)):
    print(numbers[i])

print(' ')

for value in numbers:
    print(value)

print(' ')
"""

for i in range(len(numbers)-1,-1,-1):
    print(numbers[i])

print(' ')

for value in reversed(numbers):
    print(value)

print(' ')

for idx, value in enumerate(reversed(numbers)):
    print(idx, value)

