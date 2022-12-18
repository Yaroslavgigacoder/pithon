"""Задача 2"""
x = int(input())
y = int(input())
if x > 0 and y > 0:
    print('1')
elif x < 0 and y > 0:
    print('2')
elif x < 0 and y < 0:
    print('3')
elif x > 0 and y < 0:
    print('4')
elif x == 0 and y != 0 :
    print('Точка находится на оси y')
elif y == 0 and x != 0 :
    print('Точка находится на оси x')    
