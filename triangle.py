a = 2
b = -4
c = 5

lengths_nonpositive = a <= 0 and b <= 0 and c <= 0

#inny przykład
#if a > 0 and b > 0 and c >0:
 #   if a +b >c and a + c > b and b + c > a:
  #      print ('da się utworzyć trójkąt')
   # else: print ('nie da się utworzyc trójkąta')
#else:
 #   print ('nie da sie utworzyc trójkąta')

#prostszy
if lengths_nonpositive:
    print('nie da się utworzyc trójkąta - któraś długość jest ujemna')
else:
    if a +b >c and a + c > b and b + c > a:
        print ('da się utworzyć trójkąt')
    else: print ('nie da się utworzyc trójkąta')