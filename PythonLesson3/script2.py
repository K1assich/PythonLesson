cord = [0, 0]
print("Управление персонажем осуществляется командами: вверх, вниз, влево, вправо")
print("Для остановки используйте слово стоп")
move = ''
while True:
    print('Введите команду: ')
    move = input()
    if move == 'вверх':
        cord[1] += 1
        print(f'Текущее положение: {cord}')
    elif move == 'вниз':
        cord[1] += -1
        print(f'Текущее положение: {cord}')
    elif move == 'вправо':
        cord[0] += 1
        print(f'Текущее положение: {cord}')
    elif move == 'влево':
        cord[0] += -1
        print(f'Текущее положение: {cord}')
    elif move == 'стоп':
        break
    else:
        print('Вы ввели неподдерживаемую команду')