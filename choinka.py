n=5
for i in range(1,n+1):
    for j in range(i*2-1):
        print('*', end='')
    print()

print(' ')

for i in range(1,n+1):
    print((n-i)*' ' + (2*i-1)*'*')