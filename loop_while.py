z = 0

while z < 10:
    print(z)
    z+=1
print(' ')

n=64
i = 0
square=False
done = False
current_sqaure=i**2

while not done:
    if i**2 == n:
        square=True
        done=True
    elif current_sqaure > n:
        done = True
    i +=1
    current_sqaure=i**2
if square:
    print('n jest kwadratem')
else:
    print('n nie jest kwadratem')

####

while current_sqaure <= n:
    if current_sqaure ==n:
        square=True
    i +=1
if square:
    print('n jest kwadratem')
else:
    print('n nie jest kwadratem')