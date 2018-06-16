"""b=0
i=1
a=float(input('Podaj liczbę: '))
done=True

while a>=0:
    a = float(input('Podaj liczbę: '))
    if a>=0:
        b += a
    else:
        done=False
    i += 1
average=b/i

print(i)
print(average)

print(' ')"""
#

total = 0.0
count = 0
number = 0

while number>=0:
    number = float(input('Podaj liczbę: '))
    if number >=0:
        total +=number
        count +=1
if count ==0:
    print('Nie podano ani jednej nie ujemnej liczby')
else:
    print('Podano tyle nieujemnych liczb: ', count)
    print('Ich średnia: ', total//count)
