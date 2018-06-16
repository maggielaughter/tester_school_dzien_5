#for i in range(101):
#    if (i**0.5)==i*i:
#        print(i)
#    else:
#        ('nie ma kwadratu innej liczby')

x = 100
square = False

for i in range(x+1):
    if i**2 == x:
        print('x to kwadrat liczby', i)
#        square = True
        break
else:
    print('x nie jest kwadratem')
#        break
#    elif i ** 2 > x:
#        break
#    print(i)

#if not square:
#    print('x nie jest kwadratem')
print(' ')
#teraz pętla while

while wyrażenie:
    #ciało pętli

z = 0

while z < 10:
    print(z)
    z+=1