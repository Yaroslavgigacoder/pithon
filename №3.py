number = int(input())
if number == 1:
    print('x > 0 y > 0')
elif number == 2:
    print('x < 0 y > 0')
elif  number == 3:
    print('x < 0 y < 0')
elif number == 4:
    print('x > 0 y < 0')  
elif number > 4 or number < 1:
    print('такой четверти нет')