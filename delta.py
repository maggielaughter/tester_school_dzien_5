a = float(input ('Podaj zmienna a: '))
b = float(input ('Podaj zmienna b: '))
c = float(input ('Podaj zmienna c: '))

delta = b**2 - 4*a*c
print('delta wynosi: ',delta)

x1=(-b-delta**0.5)/(2*a)
x2=(-b+delta**0.5)/(2*a)
delta_zero=-b / (2*a)

if delta > 0:
    print('Rozwiązania: ',x1, x2)
elif delta == 0:
    print(delta_zero)
else:
    print ('delta jest ujemna')