import math #подключение библиотеки математических функций

z = math.pow(3.2*math.pow(10, -5), 3/2)

x = float(input('x = '))#ввод значения x
y = float(input('y = '))
z = float(input('z = '))

a = float(2*math.cos(x-math.pi/6)/(0.5+math.pow(math.sin(y),2)))
print ('a = %.3f'%a)
b = float(1+math.pow(z,2)/(3.2*math.pow(10,-5)+math.pow(z,2/3)))
print ('b = %.3f'%b)

if math.cos(a*x)>=0:
    c = float(math.tan(2.5*x))+b*math.pow(math.cos(a*x),1/3)
    print ('c = %.3f'%c)
else:
    print ("Корень из отрицательного числа не вычисляется")
