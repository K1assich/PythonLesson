def checkPassword(passwd):
    if len(passwd) < 6:
        return False
    i = 0
    for char in passwd:
        if char.isdigit():
            i += 1
    if i == 0:
        return False
    if i == len(passwd):
        return False
    if passwd.lower() == 'password':
        return False
    return True

passwd = input('Введите пароль: ')

if checkPassword(passwd):
    print('Пароль подходит')
else:
    print('Пароль не подходит')