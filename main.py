import sqlite3


# Информация
# dept - отдел
# person - ответственный
# inv - учётный номер(только цифры)
# main_status - 0: стоит в кабинете, 1: отдан
# docs_status - 0: нет документов, 1: полный набор документов, 2: ошибки в документах
# defect_status - 0: брак, 1: всё в порядке
# program_status - 0: не закончена установка ОС и настройка СЗИ, 1: ОС поставлена, СЗИ настроены
# seal_status - 0: не опечатан, 1: опечатан

# статусы ошибок в документах
# 0 - прочее
# 1 - неверный учётный номер в документе
# 2 - неверная форма
# 3 - не хватает одного из документов


class PC:
    def __init__(self, d, p, i, m, do, de, pr, s):
        self.dept = d
        self.person = p
        self.inv = i
        self.main_status = m
        self.docs_status = do
        self.defect_status = de
        self.program_status = pr
        self.seal_status = s

    def print_info(self):
        main_status_info = {0: '-', 1: '+'}
        docs_status_info = {0: '-', 1: '+', 2: '+-'}
        defect_status_info = {0: '-', 1: '+'}
        program_status_info = {0: '-', 1: '+'}
        seal_status_info = {0: '-', 1: '+'}
        print(f'Компьютер с учётным номером №{self.inv} (Ответственный {self.person}, отдел {self.dept}) отдан: '
              f'{main_status_info[self.main_status]}.')
        print(f'Документы: {docs_status_info[self.docs_status]}')
        print(f'Работает нормально: {defect_status_info[self.defect_status]}')
        print(f'Всё поставлено: {program_status_info[self.program_status]}')
        print(f'Опечатан: {seal_status_info[self.seal_status]}')

    def print_full_info(self):
        main_status_info_full = {0: 'стоит в кабинете', 1: 'отдан пользователю'}
        docs_status_info_full = {0: 'На данный АРМ нет документов.', 2: 'На данный АРМ выпущены документы с ошибками.',
                                 1: 'На данный АРМ выпущены все необходимые документы.'}
        defect_status_info_full = {0: 'При эксплуатации компьютера наблюдаются проблемы.',
                                   1: 'В процессе эксплуатации компьютера проблемы не выявлены.'}
        program_status_info_full = {0: 'Установка ОС на АРМ не закончена и/или не произведена настройка СЗИ.',
                                    1: 'Установка ОС на данный АРМ выполнена, СЗИ настроены.'}
        seal_status_info_full = {0: 'Компьютер не опечатан.', 1: 'Компьютер опечатан.'}
        print(f'Компьютер с учётным номером №{self.inv} (Ответственный {self.person}, отдел {self.dept}) '
              f'{main_status_info_full[self.main_status]}.')
        print(f'{docs_status_info_full[self.docs_status]}')
        print(f'{defect_status_info_full[self.defect_status]}')
        print(f'{program_status_info_full[self.program_status]}')
        print(f'{seal_status_info_full[self.seal_status]}')


def check_if_values_are_correct(c, inv):
    info = {0: 'Введите значение готовности компьютера (0 - не готов, 1 - отдан):',
            1: 'Готовы ли документы (0 - не готовы, 1 - готовы, 2 - готовы с ошибками):',
            2: 'Присутствуют ли дефекты (0 - да, 1 - нет):',
            3: 'Установлены и настроены ли ОС и СЗИ (0 - нет, 1 - да):',
            4: 'Опечатан ли компьютер(0 - нет, 1 - да):'}
    print('Выполняется проверка введённых значений...')
    if len(c) > 5:
        print('Введено больше 5 значений, будут использоваться только первые 5')
        c = c[0:5]
    elif len(c) < 5:
        print('Введено меньше 5 значений')
        for i in range(len(c) - 1, 5):
            c += [0]
    while c[0] not in ['0', '1']:
        c[0] = str(input(f'{info[0]} '))
    while c[1] not in ['0', '1', '2']:
        c[1] = str(input(f'{info[1]} '))
    if str(c[1]) == '2':
        add_errors(inv)
    while c[2] not in ['0', '1']:
        c[2] = str(input(f'{info[2]} '))
    while c[3] not in ['0', '1']:
        c[3] = str(input(f'{info[3]} '))
    while c[4] not in ['0', '1']:
        c[4] = str(input(f'{info[4]} '))
    print('Проверка завершена')
    return c


def add_pc():
    dept = str(input("Введите номер отдела: "))
    person = str(input("Введите фамилию ответственного: "))
    inv = ''
    main_status = ''
    docs_status = ''
    defect_status = ''
    program_status = ''
    seal_status = ''
    while not inv.isdigit():
        inv = str(input("Введите учётный номер: "))
    while not main_status.isdigit():
        while main_status not in ['0', '1']:
            main_status = str(input("0: стоит в кабинете, 1: отдан: "))
    main_status = int(main_status)
    if main_status == 0:
        while not docs_status.isdigit():
            while docs_status not in ['0', '1', '2']:
                docs_status = str(input("0: нет документов, 1: полный набор документов, 2: ошибки в документах: "))
        docs_status = int(docs_status)
        if docs_status == 2:
            add_errors(inv)
        while not defect_status.isdigit():
            while defect_status not in ['0', '1']:
                defect_status = str(input("0: брак, 1: всё в порядке: "))
        defect_status = int(defect_status)
        while not program_status.isdigit():
            while program_status not in ['0', '1']:
                program_status = str(
                    input("0: не закончена установка ОС и настройка СЗИ, 1: ОС поставлена, СЗИ настроены: "))
        program_status = int(program_status)
        while not seal_status.isdigit():
            while seal_status not in ['0', '1']:
                seal_status = str(input("0: не опечатан, 1: опечатан: "))
        seal_status = int(seal_status)
    else:
        docs_status = defect_status = program_status = seal_status = 1
    comp = PC(dept, person, inv, main_status, docs_status, defect_status, program_status, seal_status)
    return comp


def add_errors(inv):
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    errors = ''
    while not errors.isdigit():
        while errors not in ['0', '1', '2', '3']:
            errors = str(input(
                "0: прочее, 1: неверный учётный номер в документе, 2: неверная форма, "
                "3 - не хватает одного из документов: "))
    errors = int(errors)
    c.execute('SELECT inv FROM docs_errors WHERE inv = ?', [inv])
    if len(c.fetchall()) > 0:
        c.execute('UPDATE docs_errors SET status = ? WHERE inv = ?', (errors, inv))
    else:
        c.execute('INSERT INTO docs_errors (inv, status) VALUES (?, ?)', (inv, errors))
    connection.commit()
    connection.close()
    print(f'Данные об ошибках в документах для АРМ №{inv} записаны в базу.')


def view_base():
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    c.execute('SELECT * FROM pc')
    base = c.fetchall()
    print("{:<3} {:<6} {:<15} {:<10} {:<6} {:<6} {:<6} {:<6} {:<6}".format('№', 'Отдел', 'Ответственный', 'Уч. №',
                                                                           'Отдан', 'Док.', 'Брак', 'ПО', 'Печать'))
    for i in base:
        print("{:<3} {:<6} {:<15} {:<10} {:<6} {:<6} {:<6} {:<6} {:<6}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6],
                                                                               i[7], i[8]))
    connection.close()
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')


def write_to_base(comp):
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    c.execute(
        'INSERT INTO pc (dept, person, inv, main_status, docs_status, defect_status, program_status, seal_status) '
        'VALUES (?, ?, ?, ?, ?, ?, ?, ?)', (comp.dept, comp.person, comp.inv, comp.main_status, comp.docs_status,
                                            comp.defect_status, comp.program_status, comp.seal_status))
    connection.commit()
    connection.close()
    print(f'Данные об АРМ №{comp.inv} записаны в базу.')
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
    view_base()


def view_pc_info(num=''):
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    c.execute('SELECT * FROM pc')
    base = c.fetchall()
    print("{:<3} {:<6} {:<15} {:<10} {:<6} {:<6} {:<6} {:<6} {:<6}".format('№', 'Отдел', 'Ответственный', 'Уч. №',
                                                                           'Отдан', 'Док.', 'Брак', 'ПО', 'Печать'))
    for i in base:
        print("{:<3} {:<6} {:<15} {:<10} {:<6} {:<6} {:<6} {:<6} {:<6}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6],
                                                                               i[7], i[8]))
    connection.close()
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    c.execute('SELECT num FROM pc')
    indexes = []
    for i in c.fetchall():
        indexes += [i[0]]
    number = ''
    if num != '':
        number = num
        while not number.isdigit() or int(number) not in indexes:
            number = str(input('Введите номер компьютера, информацию о котором вы хотите узнать: '))
    else:
        if int(num) not in indexes:
            print('Ошибочно передан индекс компьютера.')
            while not number.isdigit() or int(number) not in indexes:
                number = str(input('Введите номер компьютера, информацию о котором вы хотите узнать: '))
    c.execute('SELECT * FROM pc WHERE num = ?', number)
    comp_info = c.fetchall()[0]
    comp = PC(comp_info[1], comp_info[2], comp_info[3], comp_info[4], comp_info[5], comp_info[6], comp_info[7],
              comp_info[8])
    comp.print_full_info()
    connection.close()


def change_pc_info():
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    c.execute('SELECT * FROM pc')
    base = c.fetchall()
    print("{:<3} {:<6} {:<15} {:<10} {:<6} {:<6} {:<6} {:<6} {:<6}".format('№', 'Отдел', 'Ответственный', 'Уч. №',
                                                                           'Отдан', 'Док.', 'Брак', 'ПО', 'Печать'))
    for i in base:
        print("{:<3} {:<6} {:<15} {:<10} {:<6} {:<6} {:<6} {:<6} {:<6}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6],
                                                                               i[7], i[8]))
    connection.close()
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    c.execute('SELECT num FROM pc')
    indexes = []
    for i in c.fetchall():
        indexes += [i[0]]
    number = ''
    while not number.isdigit() or int(number) not in indexes:
        number = str(input('Введите номер компьютера, информацию о котором вы хотите изменить: '))
    c.execute('SELECT * FROM pc WHERE num = ?', number)
    comp_info = c.fetchall()[0]
    docs_errors_start = comp_info[6]
    comp = PC(comp_info[1], comp_info[2], comp_info[3], comp_info[4], comp_info[5], comp_info[6], comp_info[7],
              comp_info[8])
    print(f'Компьютер {comp.inv}: Отдан: {comp.main_status}, Док-ты: {comp.docs_status}, Дефекты: {comp.defect_status},'
          f' ОС и СЗИ: {comp.program_status}, Печать: {comp.seal_status}')
    changes = str(input("Введите пять значений через пробел: "))
    changes = changes.split()
    changes = check_if_values_are_correct(changes, comp.inv)
    c.execute(
        'UPDATE pc SET main_status = ?, docs_status = ?, defect_status = ?, program_status = ?, seal_status = ? '
        'WHERE num = ?',
        (changes[0], changes[1], changes[2], changes[3], changes[4], number))
    docs_errors_finish = changes[1]

    if docs_errors_start == 2 and docs_errors_finish != 2:
        delete_from_errors(comp_info[3])
    connection.commit()
    connection.close()
    view_pc_info(number)
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')


def view_ready_for_sealing():
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    c.execute('SELECT * FROM pc WHERE main_status=0 AND docs_status=1 AND defect_status=1 AND '
              'program_status=1 AND seal_status = 0')
    print("{:<3} {:<6} {:<15} {:<10} {:<6} {:<6} {:<6} {:<6} {:<6}".format('№', 'Отдел', 'Ответственный', 'Уч. №',
                                                                           'Отдан', 'Док.', 'Брак', 'ПО', 'Печать'))
    for i in c.fetchall():
        print("{:<3} {:<6} {:<15} {:<10} {:<6} {:<6} {:<6} {:<6} {:<6}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6],
                                                                               i[7], i[8]))
    connection.close()
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')


def view_given_away():
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    c.execute('SELECT * FROM pc WHERE main_status=1')
    print("{:<3} {:<6} {:<15} {:<10} {:<6} {:<6} {:<6} {:<6} {:<6}".format('№', 'Отдел', 'Ответственный', 'Уч. №',
                                                                           'Отдан', 'Док.', 'Брак', 'ПО', 'Печать'))
    for i in c.fetchall():
        print("{:<3} {:<6} {:<15} {:<10} {:<6} {:<6} {:<6} {:<6} {:<6}".format(i[0], i[1], i[2], i[3], i[4], i[5], i[6],
                                                                               i[7], i[8]))
    connection.close()
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')


def view_docs_errors():
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    c.execute('SELECT * FROM pc WHERE docs_status=2')
    info = c.fetchall()
    errors_info = {0: 'прочее',
                   1: 'неверный учётный номер в документе',
                   2: 'неверная форма',
                   3: 'не хватает одного из документов'}
    print("{:<3} {:<6} {:<15} {:<10} {:<40}".format('№', 'Отдел', 'Ответственный', 'Уч. №', 'Статус документов'))
    for i in info:
        inv = i[3]
        c.execute('SELECT status FROM docs_errors WHERE inv=?', [inv])
        status = c.fetchall()[0][0]
        print("{:<3} {:<6} {:<15} {:<10} {:<40}".format(i[0], i[1], i[2], i[3], errors_info[status]))
    connection.close()
    print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')


def delete_from_errors(inv):
    connection = sqlite3.connect('pcbase.db')
    c = connection.cursor()
    c.execute('DELETE * FROM docs_errors WHERE inv=?', inv)
    connection.commit()
    connection.close()


def menu():
    main_menu = {'0': 'Просмотреть список компьютеров',
                 '1': 'Добавить компьютер в базу',
                 '2': 'Изменить статус компьютера',
                 '3': 'Компьютеры, готовые к опечатыванию',
                 '4': 'Отданные компьютеры',
                 '5': 'Компьютеры с ошибками в документах',
                 'q': 'Выход'}
    for k, v in main_menu.items():
        print(f'{k}: {v}')
    flag = ''
    while flag not in main_menu.keys():
        flag = str(input('Выберите пункт меню: '))
    if flag == 'q':
        exit()
    elif int(flag) == 0:
        print('Список компьютеров')
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        view_base()
        menu()
    elif int(flag) == 1:
        print('Добавление в базу')
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        pc = add_pc()
        write_to_base(pc)
        menu()
    elif int(flag) == 2:
        print('Изменение статуса компьютера')
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        change_pc_info()
        menu()
    elif int(flag) == 3:
        print('Можно опечатать и отдать')
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        view_ready_for_sealing()
        menu()
    elif int(flag) == 4:
        print('Отданные компьютеры')
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        view_given_away()
        menu()
    elif int(flag) == 5:
        print('Ошибки в документах')
        print('_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ')
        view_docs_errors()
        menu()


if __name__ == '__main__':
    menu()
