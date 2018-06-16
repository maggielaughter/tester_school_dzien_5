print(1, end='')
print(2)

x='*'
print(x*2)

print(' ')

n=5

for i in range(1, n+1):
    print('*' * i)

print(' ')

for i in range(n):
    for j in range(i+1):
        print('*', end='')
    print()