    # while True:
    #     try:
    #         n = int(input('введите количество строк: '))
    #         m = int(input('введите количество столбцов: '))
    #         if n <= 0 or m <= 2:
    #             print('отказано')
    #         else:
    #             break
    #     except:
    #         print('введите лучше число')
    # sign = input('введите знак: ')
def draw_rectangle(rows, columns, ch):
    for i in range(rows):
        for j in range(columns):
            print(ch, end='')
        print('')
#    draw_rectangle(n, m, sign)
def draw_triangle(rows, ch):
    x = 1
    for i in range(rows):
        columns = ch * x
        print(columns)
        x += 1
#    print('')
#    draw_triangle(n, sign)
def draw_frame(rows, columns, ch):
    line = ch * columns
    print(line)
    pass_columns = columns - 2
    pass_rows = rows - 2
    pass_columns_line = " " * pass_columns
    for i in range(pass_rows):
        print(ch, pass_columns_line, ch, sep="")
    print(line)
#    print('')
#    draw_frame(n, m, sign)
while True:
    while True:
        figure = input('введите фигуру (прямоугольник, треугольник, рамка): ')
        if figure == "прямоугольник":
            break
        elif figure == "треугольник":
            break
        elif figure == "рамка":
            break
        else:
            print('выберите одну из трех фигур')
    while True:
        try:
            n = int(input('введите количество строк: '))
            if n <= 0:
                print('отказано')
            else:
                break
        except:
            print('введите лучше число')
    while True:
        if figure != 'треугольник':
            try:
                m = int(input('введите количество столбцов: '))
                if m <= 2:
                    print('отказано')
                else:
                    break
            except:
                print('введите лучше число')
        else:
            break
    sign = input('введите знак: ')
    if figure == "прямоугольник":
        draw_rectangle(n, m, sign)
    elif figure == 'треугольник':
        draw_triangle(n, sign)
    elif figure == 'рамка':
        draw_frame(n, m, sign)
    while True:
        end = input('хотите еще? (да, нет): ')
        if end == 'да' or end == 'нет':
            break
        else:
            print('введите по образцу')
    if end == 'нет':
        break
