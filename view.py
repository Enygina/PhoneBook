import controller

#Приветствие
def hello():
    print()
    print(('Телефонный справочник приветсвует Вас! Начнем работу').upper())

#Приветствие
def bye():
    print('До новых встреч!')

# ввод данных
def get_info():
    phone_rec = []
    phone_rec.append((input('Введите фамилию: ').title()).replace(' ', ''))
    phone_rec.append((input('Введите имя: ').title()).replace(' ', ''))
    phone_number = ''
    valid = False
    while not valid:
        try:
            phone_number = (input('Введите номер телефона: ')).replace(' ', '')
            if len(phone_number) != 11:
                print('В номере телефона должно быть 11 цифр.')
            else:
                phone_number = int(phone_number)
                valid = True
        except:
            print('Номер телефона должен состоять только из цифр.')
    phone_rec.append(str(phone_number))
    phone_rec.append(input('Введите описание: ').title())
    print()
    print('Данные внеесены в справочник')
    return phone_rec


# функция меню возвращает int для case в controller
def option():
    print()
    op = (int(input(
        'Для ввода новых данных нажмите 1\nДля поиска нажмите 2\nДля вывода всего телефонного справочника нажмите 3\nДля выхода нажмите 4  ')))
    print()
    if op > 0 and op < 5:
        return int(op)
    else:
        print()
        print('Некорректный ввод')
        controller.button_click()
        print()


# ввод искомых данных
def for_search():
    lastname = input('Введите фамилию: ').title()
    return lastname


# вывод данных
def output_data(list):
    a=['Фамилия', 'Имя', 'Телефон', 'Описание']
    print()
    op = int(input(
        'Выберите способ вывода данных:\nНажмите 1 чтобы вывести все одной строкой\nНажмите 2 чтобы вывести построчно  '))
    match op:
        case 1:
            print()
            print(("{:<15}{:<10}{:<15}{:<10}".format(*a)).upper())
            for x in list:
                print("{:<15}{:<10}{:<15}{:<10}".format(*x))

        case 2:
            for x in list:
                print(f'Фамилия: {x[0]}\nИмя: {x[1]}\nТедефон: {x[2]}\nОписание: {x[3]}')
        case _:
            print('Ошибка ввода')
            output_data()
