
import controller

# функция принимает на вход список списков, осуществляет поиск значения, возвращаент новый список найденных совпадений
def fnd_lastname(data):
    fnd_res = []
    search = str((input('Введите фамилию для поиска: ').title()).replace(' ', ''))
    for i in range(len(data)):
        if search == data[i][0]:
            fnd_res.append(data[i])
    return fnd_res


# функция проверяет список на пустоту
def empty_fnd(data):
        if not data:
            print('В телефонной книге контакта нет')
            exit(controller.button_click())
        else:
            return data
