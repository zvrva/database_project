import sqlite3 as sq3

student = {1: 'students_name',
           2: 'students_surname',
           3: 'students_patronymic',
           4: 'students_age',
           5: 'students_institute',
           6: 'students_programme_type',
           7: 'students_gradebook_number',
           8: 'students_mail',
           9: 'students_phone_number'}

student_for_print = {1: 'Name',
                     2: 'Surname',
                     3: 'Patronymic',
                     4: 'Age',
                     5: 'Institute',
                     6: 'Programme type',
                     7: 'Gradebook number',
                     8: 'Mail',
                     9: 'Phone number'}

teacher = {1: 'teachers_name',
           2: 'teachers_surname',
           3: 'teachers_patronymic',
           4: 'teachers_institute',
           5: 'teachers_department'}

teacher_for_print = {1: 'Name',
                     2: 'Surname',
                     3: 'Patronymic',
                     4: 'Institute',
                     5: 'Department'}

course = {1: 'courses_name',
          2: 'courses_description'}

course_for_print = {1: 'Name',
                    2: 'Description'}

meeting = {1: 'meetings_topic',
           2: 'meetings_house',
           3: 'meetings_room',
           4: 'meetings_start_time',
           5: 'meetings_end_time'}

meeting_for_print = {1: 'Topic',
                     2: 'House',
                     3: 'Room',
                     4: 'Start time',
                     5: 'End time'}

database = 'C:/Users/zvrva/OneDrive/Рабочий стол/UTMN/БД/Лабораторная 6/Students_DB'

con = sq3.connect(database, timeout=5.0, detect_types=0,
                  isolation_level='DEFERRED', check_same_thread=True,
                  factory=sq3.Connection, cached_statements=128, uri=False)

cursor = con.cursor()

print('БАЗА ДАННЫХ УНИВЕРСИТЕТА')
print('Действия с базой данных:')
print('''1 - вывести данные
2 - добавить данные
3 - редактировать данные
4 - вывести статистику
5 - сортировать данные
6 - exit''')
action = input('Выберите цифру: ')

GO = 0
if (action == '1') or (action == '2') or (action == '3') or (action == '4') or (action == '5') or (action == '6'):
    GO = 1

while GO == 0:
    print('Введите цифру правильно!')
    print('''1 - вывести данные
2 - добавить данные
3 - редактировать данные
4 - вывести статистику
5 - сортировать данные
6 - exit''')

    action = input('Выберите цифру: ')

    if (action == '1') or (action == '2') or (action == '3') or (action == '4') or (action == '5') or (action == '6'):
        GO = 1

while GO:
    if action == '1':
        print('Таблицы базы данных для вывода значений:')
        print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
        table = input('Выберите цифру: ')
        check = 0
        if (table == '1') or (table == '2') or (table == '3') or (table == '4'):
            check = 1
        while check == 0:
            print('Введите цифру правильно!')
            print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
            table = input('Выберите цифру: ')
            if (table == '1') or (table == '2') or (table == '3') or (table == '4'):
                check = 1

        if table == '1':
            print('Столбцы базы данных для вывода значений:')
            print('''1 - Name
2 - Surname
3 - Patronymic
4 - Age
5 - Institute
6 - Programme type
7 - Gradebook number
8 - Mail
9 - Phone number
* - All''')
            k = input('Введите знак звездочки или цифру(ы) через пробел: ')
            k = k.split()
            s = 0
            for i in k:
                if len(i) == 1 and i in '123456789*':
                    s += 1
            check = 0
            if s == len(k):
                check = 1
            while check == 0:
                print('Введите цифру правильно!')
                print('''1 - Name
2 - Surname
3 - Patronymic
4 - Age
5 - Institute
6 - Programme type
7 - Gradebook number
8 - Mail
9 - Phone number
* - All''')
                k = input('Введите знак звездочки или цифру(ы) через пробел: ')
                k = k.split()
                s = 0
                for i in k:
                    if len(i) == 1 and i in '123456789*':
                        s += 1
                if s == len(k):
                    check = 1

            count = int(input('Введите количество строк для вывода (0 - все строки): '))

            if '*' in k:
                cursor.execute('SELECT * FROM Student')
                print(
                    'Name    Surname    Patronymic    Age    Institute    Programme type     Gradebook number     Mail     Phone number')
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)

            else:
                k = list(set(k))
                k.sort()
                request = []
                for i in k:
                    request.append(student[int(i)])
                    print(student_for_print[int(i)], end='\t')
                print()
                z = 'SELECT ' + ', '.join(request) + ' FROM Student'
                cursor.execute(z)
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
            for i in data:
                for j in i:
                    print(j, end='\t')
                print()

        elif table == '2':
            print('Столбцы базы данных для вывода значений:')
            print('''1 - Name
2 - Surname
3 - Patronymic
4 - Institute
5 - Department
* - All''')
            k = input('Введите знак звездочки или цифру(ы) через пробел: ')
            k = k.split()
            s = 0
            for i in k:
                if len(i) == 1 and i in '12345*':
                    s += 1
            check = 0
            if s == len(k):
                check = 1
            while check == 0:
                print('Введите цифру правильно!')
                print('''1 - Name
2 - Surname
3 - Patronymic
4 - Institute
5 - Department
* - All''')
                k = input('Введите знак звездочки или цифру(ы) через пробел: ')
                k = k.split()
                s = 0
                for i in k:
                    if len(i) == 1 and i in '12345*':
                        s += 1
                if s == len(k):
                    check = 1

            count = int(input('Введите количество строк для вывода (0 - все строки): '))

            if '*' in k:
                cursor.execute('SELECT * FROM Teacher')
                print(
                    'Name    Surname    Patronymic    Institute    Department')
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)

            else:
                k = list(set(k))
                k.sort()
                request = []
                for i in k:
                    request.append(teacher[int(i)])
                    print(teacher_for_print[int(i)], end='\t')
                print()
                z = 'SELECT ' + ', '.join(request) + ' FROM Teacher'
                cursor.execute(z)
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
            for i in data:
                for j in i:
                    print(j, end='\t')
                print()

        elif table == '3':
            print('Столбцы базы данных для вывода значений:')
            print('''1 - Name
2 - Description
* - All''')
            k = input('Введите знак звездочки или цифру(ы) через пробел: ')
            k = k.split()
            s = 0
            for i in k:
                if len(i) == 1 and i in '12*':
                    s += 1
            check = 0
            if s == len(k):
                check = 1
            while check == 0:
                print('Введите цифру правильно!')
                print('''1 - Name
2 - Description
* - All''')
                k = input('Введите знак звездочки или цифру(ы) через пробел: ')
                k = k.split()
                s = 0
                for i in k:
                    if len(i) == 1 and i in '12*':
                        s += 1
                if s == len(k):
                    check = 1

            count = int(input('Введите количество строк для вывода (0 - все строки): '))

            if '*' in k:
                cursor.execute('SELECT * FROM Course')
                print(
                    'Name    Description')
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)

            else:
                k = list(set(k))
                k.sort()
                request = []
                for i in k:
                    request.append(course[int(i)])
                    print(course_for_print[int(i)], end='\t')
                print()
                z = 'SELECT ' + ', '.join(request) + ' FROM Course'
                cursor.execute(z)
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
            for i in data:
                for j in i:
                    print(j, end='\t')
                print()

        elif table == '4':
            print('Столбцы базы данных для вывода значений:')
            print('''1 - Topic
2 - House
3 - Room
4 - Start time
5 - End time
* - All''')
            k = input('Введите знак звездочки или цифру(ы) через пробел: ')
            k = k.split()
            s = 0
            for i in k:
                if len(i) == 1 and i in '12345*':
                    s += 1
            check = 0
            if s == len(k):
                check = 1
            while check == 0:
                print('Введите цифру правильно!')
                print('''1 - Topic
2 - House
3 - Room
4 - Start time
5 - End time
* - All''')
                k = input('Введите знак звездочки или цифру(ы) через пробел: ')
                k = k.split()
                s = 0
                for i in k:
                    if len(i) == 1 and i in '12345*':
                        s += 1
                if s == len(k):
                    check = 1

            count = int(input('Введите количество строк для вывода (0 - все строки): '))

            if '*' in k:
                cursor.execute('SELECT * FROM Meeting')
                print('Topic    House    Room    Start time    End time')
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)

            else:
                k = list(set(k))
                k.sort()
                request = []
                for i in k:
                    request.append(meeting[int(i)])
                    print(meeting_for_print[int(i)], end='\t')
                print()
                z = 'SELECT ' + ', '.join(request) + ' FROM Meeting'
                cursor.execute(z)
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
            for i in data:
                for j in i:
                    print(j, end='\t')
                print()

    elif action == '2':
        print('Таблицы базы данных для добавления значений:')
        print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
        table = input('Выберите цифру: ')
        check = 0
        if (table == '1') or (table == '2') or (table == '3') or (table == '4') or (table == '5'):
            check = 1
        while check == 0:
            print('Введите цифру правильно!')
            print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
            table = input('Выберите цифру: ')
            if (table == '1') or (table == '2') or (table == '3') or (table == '4'):
                check = 1

        if table == '1':
            students_name = input('Введите имя (русские строчные/заглавные буквы): ')
            check = 0
            s = 0
            for i in students_name:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                    s += 1
            if s == len(students_name):
                check = 1
            while check == 0:
                students_name = input('Введите имя правильно!(русские строчные/заглавные буквы): ')
                s = 0
                for i in students_name:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(students_name):
                    check = 1
            students_name = students_name.lower()
            students_name = students_name.capitalize()

            students_surname = input('Введите фамилию (русские строчные/заглавные буквы): ')
            check = 0
            s = 0
            for i in students_surname:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                    s += 1
            if s == len(students_surname):
                check = 1
            while check == 0:
                students_surname = input('Введите фамилию правильно!(русские строчные/заглавные буквы): ')
                s = 0
                for i in students_surname:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(students_surname):
                    check = 1
            students_surname = students_surname.lower()
            students_surname = students_surname.capitalize()

            students_patronymic = input('Введите отчество (русские строчные/заглавные буквы): ')
            check = 0
            s = 0
            for i in students_patronymic:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                    s += 1
            if s == len(students_patronymic):
                check = 1
            while check == 0:
                students_patronymic = input('Введите отчество правильно!(русские строчные/заглавные буквы): ')
                s = 0
                for i in students_patronymic:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(students_patronymic):
                    check = 1
            students_patronymic = students_patronymic.lower()
            students_patronymic = students_patronymic.capitalize()

            students_age = input('Введите возраст (число от 17 до 99 включительно): ')
            check = 0
            s = 0
            for i in students_age:
                if i in '0123456789':
                    s += 1
            if s == len(students_age):
                if (int(students_age) >= 17) and (int(students_age) < 100):
                    check = 1
            while check == 0:
                students_age = input('Введите возраст правильно!(число от 17 до 99 включительно): ')
                s = 0
                for i in students_age:
                    if i in '0123456789':
                        s += 1
                if s == len(students_age):
                    if (int(students_age) >= 17) and (int(students_age) < 100):
                        check = 1

            students_institute = input('Введите институт (допускаются латинские/русские строчные/заглавные буквы): ')
            check = 0
            s = 0
            for i in students_institute:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                    s += 1
            if s == len(students_institute):
                check = 1
            while check == 0:
                students_institute = input(
                    'Введите институт правильно!(допускаются латинские/русские строчные/заглавные буквы): ')
                s = 0
                for i in students_institute:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                        s += 1
                if s == len(students_institute):
                    check = 1
            students_institute = students_institute.lower()
            students_institute = students_institute.capitalize()

            students_programme_type = input(
                'Введите направление обучения (допускаются латинские/русские строчные/заглавные буквы и цифры): ')
            check = 0
            s = 0
            for i in students_programme_type:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM 0123456789':
                    s += 1
            if s == len(students_programme_type):
                check = 1
            while check == 0:
                students_programme_type = input(
                    'Введите направление обучения правильно!(допускаются латинские/русские строчные/заглавные буквы и цифры): ')
                s = 0
                for i in students_programme_type:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM 01232456789':
                        s += 1
                if s == len(students_programme_type):
                    check = 1
            students_programme_type = students_programme_type.lower()
            students_programme_type = students_programme_type.capitalize()

            students_gradebook_number = input('Введите номер зачетной книжки (шестизначное число): ')
            check = 0
            s = 0
            for i in students_gradebook_number:
                if i in '0123456789':
                    s += 1
            if s == len(students_gradebook_number):
                if (int(students_gradebook_number) >= 100000) and (int(students_gradebook_number) <= 999999):
                    check = 1
            while check == 0:
                students_gradebook_number = input('Введите номер зачетной книжки правильно!(шестизначное число): ')
                s = 0
                for i in students_gradebook_number:
                    if i in '0123456789':
                        s += 1
                if s == len(students_gradebook_number):
                    if (int(students_gradebook_number) >= 100000) and (int(students_gradebook_number) <= 999999):
                        check = 1

            students_mail = input('Введите почту (stud0000******@study.utmn.ru - шесть цифр на месте звездочек): ')
            check = 0
            s = 0
            for i in students_mail:
                if i in '0123456789':
                    s += 1
            if s == len(students_mail):
                if len(students_mail) == 6:
                    check = 1
            while check == 0:
                students_mail = input(
                    'Введите почту правильно!(stud0000******@study.utmn.ru - шесть цифр на месте звездочек): ')
                s = 0
                for i in students_mail:
                    if i in '0123456789':
                        s += 1
                if s == len(students_mail):
                    if len(students_mail) == 6:
                        check = 1
            students_mail = 'stud0000' + students_mail + '@study.utmn.ru'

            students_phone_number = input('Введите номер телефона (+7********** - десять цифр на месте звездочек): ')
            check = 0
            s = 0
            for i in students_phone_number:
                if i in '0123456789':
                    s += 1
            if s == len(students_phone_number):
                if len(students_phone_number) == 10:
                    check = 1
            while check == 0:
                students_phone_number = input(
                    'Введите номер телефона правильно!(+7********** - десять цифр на месте звездочек): ')
                s = 0
                for i in students_phone_number:
                    if i in '0123456789':
                        s += 1
                if s == len(students_phone_number):
                    if len(students_phone_number) == 10:
                        check = 1
            students_phone_number = '+7' + students_phone_number

            info = (students_name, students_surname, students_patronymic, students_age, students_institute,
                    students_programme_type, students_gradebook_number, students_mail, students_phone_number)

            cursor.execute(
                'INSERT INTO Student (students_name, students_surname, students_patronymic, students_age, students_institute, students_programme_type, students_gradebook_number, students_mail, students_phone_number) VALUES (?,?,?,?,?,?,?,?,?)',
                info)
            con.commit()

        elif table == '2':
            teachers_name = input('Введите имя (русские строчные/заглавные буквы): ')
            check = 0
            s = 0
            for i in teachers_name:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                    s += 1
            if s == len(teachers_name):
                check = 1
            while check == 0:
                teachers_name = input('Введите имя правильно!(русские строчные/заглавные буквы): ')
                s = 0
                for i in teachers_name:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(teachers_name):
                    check = 1
            teachers_name = teachers_name.lower()
            teachers_name = teachers_name.capitalize()

            teachers_surname = input('Введите фамилию (русские строчные/заглавные буквы): ')
            check = 0
            s = 0
            for i in teachers_surname:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                    s += 1
            if s == len(teachers_surname):
                check = 1
            while check == 0:
                teachers_surname = input('Введите фамилию правильно!(русские строчные/заглавные буквы): ')
                s = 0
                for i in teachers_surname:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(teachers_surname):
                    check = 1
            teachers_surname = teachers_surname.lower()
            teachers_surname = teachers_surname.capitalize()

            teachers_patronymic = input('Введите отчество (русские строчные/заглавные буквы): ')
            check = 0
            s = 0
            for i in teachers_patronymic:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                    s += 1
            if s == len(teachers_patronymic):
                check = 1
            while check == 0:
                teachers_patronymic = input('Введите отчество правильно!(русские строчные/заглавные буквы): ')
                s = 0
                for i in teachers_patronymic:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(teachers_patronymic):
                    check = 1
            teachers_patronymic = teachers_patronymic.lower()
            teachers_patronymic = teachers_patronymic.capitalize()

            teachers_institute = input('Введите институт (допускаются латинские/русские строчные/заглавные буквы): ')
            check = 0
            s = 0
            for i in teachers_institute:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                    s += 1
            if s == len(teachers_institute):
                check = 1
            while check == 0:
                teachers_institute = input(
                    'Введите институт правильно!(допускаются латинские/русские строчные/заглавные буквы): ')
                s = 0
                for i in teachers_institute:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                        s += 1
                if s == len(teachers_institute):
                    check = 1
            teachers_institute = teachers_institute.lower()
            teachers_institute = teachers_institute.capitalize()

            teachers_department = input(
                'Введите название кафедры (допускаются латинские/русские строчные/заглавные буквы): ')
            check = 0
            s = 0
            for i in teachers_department:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                    s += 1
            if s == len(teachers_department):
                check = 1
            while check == 0:
                teachers_department = input(
                    'Введите название кафедры правильно!(допускаются латинские/русские строчные/заглавные буквы): ')
                s = 0
                for i in teachers_department:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                        s += 1
                if s == len(teachers_department):
                    check = 1
            teachers_department = teachers_department.lower()
            teachers_department = teachers_department.capitalize()

            info = (teachers_name, teachers_surname, teachers_patronymic, teachers_institute, teachers_department)

            cursor.execute(
                'INSERT INTO Teacher (teachers_name, teachers_surname, teachers_patronymic, teachers_institute, teachers_department) VALUES (?,?,?,?,?)',
                info)
            con.commit()

        elif table == '3':
            courses_name = input('Введите название курса (латинские/русские строчные/заглавные буквы и цифры): ')
            check = 0
            s = 0
            for i in courses_name:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIIOOPASDFGHJKLZXCVBNM 0123456789':
                    s += 1
            if s == len(courses_name):
                check = 1
            while check == 0:
                courses_name = input(
                    'Введите название курса правильно!(латинские/русские строчные/заглавные буквы и цифры): ')
                s = 0
                for i in courses_name:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIIOOPASDFGHJKLZXCVBNM 0123456789':
                        s += 1
                if s == len(courses_name):
                    check = 1
            courses_name = courses_name.lower()
            courses_name = courses_name.capitalize()

            courses_description = input(
                'Введите описание курса (латинские/русские строчные/заглавные буквы, цифры и знаки препинания): ')
            check = 0
            s = 0
            for i in courses_description:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIIOOPASDFGHJKLZXCVBNM 0123456789.,!"№;%:?*()-_+=/':
                    s += 1
            if s == len(courses_description):
                check = 1
            while check == 0:
                courses_description = input(
                    'Введите описание курса правильно!(латинские/русские строчные/заглавные буквы, цифры и знаки препинания): ')
                s = 0
                for i in courses_description:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIIOOPASDFGHJKLZXCVBNM 0123456789.,!"№;%:?*()-_+=/':
                        s += 1
                if s == len(courses_description):
                    check = 1
            courses_description = courses_description.lower()
            courses_description = courses_description.capitalize()

            info = (courses_name, courses_description)

            cursor.execute('INSERT INTO Course (courses_name, courses_description) VALUES (?,?)', info)
            con.commit()

        elif table == '4':
            meetings_topic = input('Введите тему встречи (латинские/русские строчные/заглавные буквы): ')
            check = 0
            s = 0
            for i in meetings_topic:
                if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ wertyuiopqasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                    s += 1
            if s == len(meetings_topic):
                check = 1
            while check == 0:
                meetings_topic = input('Введите тему встречи правильно!(латинские/русские строчные/заглавные буквы): ')
                s = 0
                for i in meetings_topic:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ wertyuiopqasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                        s += 1
                if s == len(meetings_topic):
                    check = 1
            meetings_topic = meetings_topic.lower()
            meetings_topic = meetings_topic.capitalize()

            meetings_house = input('Введите здание (УЛК-** - две цифры на месте звездочек): ')
            check = 0
            s = 0
            for i in meetings_house:
                if i in '0123456789':
                    s += 1
            if s == len(meetings_house):
                if len(meetings_house) == 2:
                    check = 1
            while check == 0:
                meetings_house = input('Введите здание правильно!(УЛК-** - две цифры на месте звездочек): ')
                s = 0
                for i in meetings_house:
                    if i in '0123456789':
                        s += 1
                if s == len(meetings_house):
                    if len(meetings_house) == 2:
                        check = 1
            meetings_house = 'УЛК-' + meetings_house

            meetings_room = input('Введите аудиторию (трехзначное число): ')
            check = 0
            s = 0
            for i in meetings_room:
                if i in '0123456789':
                    s += 1
            if s == len(meetings_room):
                if int(meetings_room) >= 100 and int(meetings_room) < 1000:
                    check = 1
            while check == 0:
                meetings_room = input('Введите аудиторию правильно!(трехзначное число): ')
                s = 0
                for i in meetings_room:
                    if i in '0123456789':
                        s += 1
                if s == len(meetings_room):
                    if int(meetings_room) >= 100 and int(meetings_room) < 1000:
                        check = 1

            meetings_start_time_hour = input('Введите час начала пары (число от 0 до 23): ')
            check = 0
            s = 0
            for i in meetings_start_time_hour:
                if i in '0123456789':
                    s += 1
            if s == len(meetings_start_time_hour):
                if (int(meetings_start_time_hour) >= 0) and (int(meetings_start_time_hour) < 24):
                    check = 1
            while check == 0:
                meetings_start_time_hour = input('Введите час начала пары правильно!(число от 0 до 23): ')
                s = 0
                for i in meetings_start_time_hour:
                    if i in '0123456789':
                        s += 1
                if s == len(meetings_start_time_hour):
                    if (int(meetings_start_time_hour) >= 0) and (int(meetings_start_time_hour) < 24):
                        check = 1

            meetings_start_time_minute = input('Введите минуты начала пары (число от 0 до 55): ')
            check = 0
            s = 0
            for i in meetings_start_time_minute:
                if i in '0123456789':
                    s += 1
            if s == len(meetings_start_time_minute):
                if (int(meetings_start_time_minute) >= 0) and (int(meetings_start_time_minute) < 56):
                    check = 1
            while check == 0:
                meetings_start_time_minute = input('Введите минуты начала пары правильно!(число от 0 до 55): ')
                s = 0
                for i in meetings_start_time_minute:
                    if i in '0123456789':
                        s += 1
                if s == len(meetings_start_time_minute):
                    if (int(meetings_start_time_minute) >= 0) and (int(meetings_start_time_minute) < 56):
                        check = 1

            meetings_start_time = meetings_start_time_hour + ':' + meetings_start_time_minute

            meetings_end_time_hour = input('Введите час конца пары (число от 0 до 23): ')
            check = 0
            s = 0
            for i in meetings_end_time_hour:
                if i in '0123456789':
                    s += 1
            if s == len(meetings_end_time_hour):
                if (int(meetings_end_time_hour) >= 0) and (int(meetings_end_time_hour) < 24):
                    check = 1
            while check == 0:
                meetings_end_time_hour = input('Введите час конца пары правильно!(число от 0 до 23): ')
                s = 0
                for i in meetings_end_time_hour:
                    if i in '0123456789':
                        s += 1
                if s == len(meetings_end_time_hour):
                    if (int(meetings_end_time_hour) >= 0) and (int(meetings_end_time_hour) < 24):
                        check = 1

            meetings_end_time_minute = input('Введите минуты конца пары (число от 0 до 55): ')
            check = 0
            s = 0
            for i in meetings_end_time_minute:
                if i in '0123456789':
                    s += 1
            if s == len(meetings_end_time_minute):
                if (int(meetings_end_time_minute) >= 0) and (int(meetings_end_time_minute) < 56):
                    check = 1
            while check == 0:
                meetings_end_time_minute = input('Введите минуты конца пары правильно!(число от 0 до 55): ')
                s = 0
                for i in meetings_end_time_minute:
                    if i in '0123456789':
                        s += 1
                if s == len(meetings_end_time_minute):
                    if (int(meetings_end_time_minute) >= 0) and (int(meetings_end_time_minute) < 56):
                        check = 1

            meetings_end_time = meetings_end_time_hour + ':' + meetings_end_time_minute

            info = (meetings_topic, meetings_house, meetings_room, meetings_start_time, meetings_end_time)

            cursor.execute(
                'INSERT INTO Meeting (meetings_topic, meetings_house, meetings_room, meetings_start_time, meetings_end_time) VALUES (?,?,?,?,?)',
                info)
            con.commit()

    elif action == '3':
        print('Таблицы базы данных для редактирования значений:')
        print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
        table = input('Выберите цифру: ')
        check = 0
        if (table == '1') or (table == '2') or (table == '3') or (table == '4'):
            check = 1
        while check == 0:
            print('Введите цифру правильно!')
            print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
            table = input('Выберите цифру: ')
            if (table == '1') or (table == '2') or (table == '3') or (table == '4'):
                check = 1

        if table == '1':
            print(1)
        elif table == '2':
            print(2)
        elif table == '3':
            print(3)
        elif table == '4':
            print(4)

    elif action == '4':
        print('Таблицы базы данных для вывода статистики:')
        print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
        m = input('Выберите цифру: ')
        check = 0
        if (m == '1') or (m == '2') or (m == '3') or (m == '4') or (m == '5'):
            check = 1
        while check == 0:
            print('Введите цифру правильно!')
            print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
            m = input('Выберите цифру: ')
            if (m == '1') or (m == '2') or (m == '3') or (m == '4') or (m == '5'):
                check = 1

    elif action == '5':
        print('Таблицы базы данных для сортировки данных:')
        print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
        m = input('Выберите цифру: ')
        check = 0
        if (m == '1') or (m == '2') or (m == '3') or (m == '4') or (m == '5'):
            check = 1
        while check == 0:
            print('Введите цифру правильно!')
            print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
            m = input('Выберите цифру: ')
            if (m == '1') or (m == '2') or (m == '3') or (m == '4') or (m == '5'):
                check = 1

    else:
        print('Завершение работы')
        break

    print('Действия с базой данных:')
    print('''1 - вывести данные
2 - добавить данные
3 - редактировать данные
4 - вывести статистику
5 - сортировать данные
6 - exit''')
    action = input('Выберите цифру: ')
