x = 9
y = 100
z = 10

if x <= y <= z or z <= y <= x:
    print('mediana to y: ', y)
elif y <= x <= z or z <=x <=y:
    print('mediana to x: ', x)
else:
    print ('mediana to z: ', z)