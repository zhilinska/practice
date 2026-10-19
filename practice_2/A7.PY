x = 0
while x == 0: #цикл будет просить ввести данные, пока польз. не введет подходящие
    try:
        x1, y1 = map(int, input('введите координаты первой клетки (x1:y1): ').split(':'))
        x2, y2 = map(int, input('введите координаты второй клетки (x2:y2): ').split(':'))
        x = 1
        if x1 not in range(1, 9) or\
        x2 not in range(1, 9) or\
        y1 not in range(1, 9) or\
        y2 not in range(1, 9):
            print('клеточек не так много')
            x = 0
    except: #если пользователь введет неподходящий тип данных
        print('попробуйте ввести числа от 1 до 8 по образцу')
if (x1 + y1) % 2 == 0 and (x2 + y2) % 2 == 0:
    cell = 'white'
    print('YES')
    print(cell)
elif (x1 + y1) % 2 != 0 and (x2 + y2) % 2 != 0: 
    cell = 'black' 
    print('YES')
    print(cell)
else:
    print('NO')