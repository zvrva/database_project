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
Любой другой символ - выйти''')
action = input('Выберите цифру: ')

GO = 0
if (action in '12345') and (len(action) == 1):
    GO = 1

while GO:
    if action == '1':
        print('Таблицы базы данных для вывода значений:')
        table = ''
        check = 0
        while check == 0:
            print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
            table = input('Выберите цифру: ')
            if (table in '1234') and (len(table) == 1):
                check = 1
            else:
                print('Введите цифру правильно!')

        if table == '1':
            print('Столбцы базы данных для вывода значений:')
            k = ''
            check = 0
            while check == 0:
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
                else:
                    print('Введите цифру правильно!')

            count = ''
            check = 0
            while check == 0:
                count = input('Введите количество строк для вывода (0 - все строки): ')
                if count.isnumeric():
                    cursor.execute('SELECT students_id FROM Student')
                    data = cursor.fetchall()
                    if (int(count) <= len(data)) and (int(count) >= 0):
                        check = 1
                    else:
                        print('Введите цифру правильно!')
                else:
                    print('Введите цифру правильно!')
            count = int(count)

            if '*' in k:
                cursor.execute('SELECT * FROM Student')
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
                data.insert(0, (
                    'Name', 'Surname', 'Patronymic', 'Age', 'Institute', 'Programme type', 'Gradebook number', 'Mail',
                    'Phone number', 'Id'))

            else:
                k = list(set(k))
                k.sort()
                request = []
                banner = ()
                for i in k:
                    request.append(student[int(i)])
                    banner = banner + (student_for_print[int(i)],)
                z = 'SELECT ' + ', '.join(request) + ' FROM Student'
                cursor.execute(z)
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
                data.insert(0, banner)

            lens = []
            for i in range(len(data[0])):
                s = 0
                for j in range(len(data)):
                    s = max(s, len(str(data[j][i])))
                lens.append(s)

            for i in data:
                s = 0
                for j in i:
                    print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                    s += 1
                print()

        elif table == '2':
            print('Столбцы базы данных для вывода значений:')
            k = ''
            check = 0
            while check == 0:
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
                else:
                    print('Введите цифру правильно!')

            count = ''
            check = 0
            while check == 0:
                count = input('Введите количество строк для вывода (0 - все строки): ')
                if count.isnumeric():
                    cursor.execute('SELECT teachers_id FROM Teacher')
                    data = cursor.fetchall()
                    if (int(count) <= len(data)) and (int(count) >= 0):
                        check = 1
                    else:
                        print('Введите цифру правильно!')
                else:
                    print('Введите цифру правильно!')
            count = int(count)

            if '*' in k:
                cursor.execute('SELECT * FROM Teacher')
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Institute', 'Department', 'Id'))

            else:
                k = list(set(k))
                k.sort()
                request = []
                banner = ()
                for i in k:
                    request.append(teacher[int(i)])
                    banner = banner + (teacher_for_print[int(i)],)
                print()
                z = 'SELECT ' + ', '.join(request) + ' FROM Teacher'
                cursor.execute(z)
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
                data.insert(0, banner)

            lens = []
            for i in range(len(data[0])):
                s = 0
                for j in range(len(data)):
                    s = max(s, len(str(data[j][i])))
                lens.append(s)

            for i in data:
                s = 0
                for j in i:
                    print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                    s += 1
                print()

        elif table == '3':
            print('Столбцы базы данных для вывода значений:')
            k = ''
            check = 0
            while check == 0:
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
                else:
                    print('Введите цифру правильно!')

            count = ''
            check = 0
            while check == 0:
                count = input('Введите количество строк для вывода (0 - все строки): ')
                if count.isnumeric():
                    cursor.execute('SELECT courses_id FROM Course')
                    data = cursor.fetchall()
                    if (int(count) <= len(data)) and (int(count) >= 0):
                        check = 1
                    else:
                        print('Введите цифру правильно!')
                else:
                    print('Введите цифру правильно!')
            count = int(count)

            if '*' in k:
                cursor.execute('SELECT * FROM Course')
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
                data.insert(0, ('Name', 'Description', 'Id'))

            else:
                k = list(set(k))
                k.sort()
                request = []
                banner = ()
                for i in k:
                    request.append(course[int(i)])
                    banner = banner + (course_for_print[int(i)],)
                print()
                z = 'SELECT ' + ', '.join(request) + ' FROM Course'
                cursor.execute(z)
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
                data.insert(0, banner)

            lens = []
            for i in range(len(data[0])):
                s = 0
                for j in range(len(data)):
                    s = max(s, len(str(data[j][i])))
                lens.append(s)

            for i in data:
                s = 0
                for j in i:
                    print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                    s += 1
                print()

        elif table == '4':
            print('Столбцы базы данных для вывода значений:')
            k = ''
            check = 0
            while check == 0:
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
                else:
                    print('Введите цифру правильно!')

            count = ''
            check = 0
            while check == 0:
                count = input('Введите количество строк для вывода (0 - все строки): ')
                if count.isnumeric():
                    cursor.execute('SELECT meetings_id FROM Meeting')
                    data = cursor.fetchall()
                    if (int(count) <= len(data)) and (int(count) >= 0):
                        check = 1
                    else:
                        print('Введите цифру правильно!')
                else:
                    print('Введите цифру правильно!')
            count = int(count)

            if '*' in k:
                cursor.execute('SELECT * FROM Meeting')
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
                data.insert(0, ('Topic', 'House', 'Room', 'Start time', 'End time', 'Id'))

            else:
                k = list(set(k))
                k.sort()
                request = []
                banner = ()
                for i in k:
                    request.append(meeting[int(i)])
                    banner = banner + (meeting_for_print[int(i)],)
                print()
                z = 'SELECT ' + ', '.join(request) + ' FROM Meeting'
                cursor.execute(z)
                if count == 0:
                    data = cursor.fetchall()
                else:
                    data = cursor.fetchmany(count)
                data.insert(0, banner)

            lens = []
            for i in range(len(data[0])):
                s = 0
                for j in range(len(data)):
                    s = max(s, len(str(data[j][i])))
                lens.append(s)

            for i in data:
                s = 0
                for j in i:
                    print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                    s += 1
                print()

    elif action == '2':
        print('Таблицы базы данных для добавления значений:')
        table = ''
        check = 0
        while check == 0:
            print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
            table = input('Выберите цифру: ')
            if (table in '1234') or (len(table) == 1):
                check = 1
            else:
                print('Введите цифру правильно!')

        if table == '1':
            students_name = ''
            check = 0
            while check == 0:
                students_name = input('Введите имя: ')
                s = 0
                for i in students_name:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(students_name):
                    check = 1
                else:
                    print('Введите имя правильно!(русские строчные/заглавные буквы)')
            students_name = students_name.lower()
            students_name = students_name.capitalize()

            students_surname = ''
            check = 0
            while check == 0:
                students_surname = input('Введите фамилию: ')
                s = 0
                for i in students_surname:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(students_surname):
                    check = 1
                else:
                    print('Введите фамилию правильно!(русские строчные/заглавные буквы)')
            students_surname = students_surname.lower()
            students_surname = students_surname.capitalize()

            students_patronymic = ''
            check = 0
            while check == 0:
                students_patronymic = input('Введите отчество: ')
                s = 0
                for i in students_patronymic:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(students_patronymic):
                    check = 1
                else:
                    print('Введите отчество правильно!(русские строчные/заглавные буквы)')
            students_patronymic = students_patronymic.lower()
            students_patronymic = students_patronymic.capitalize()

            students_age = ''
            check = 0
            while check == 0:
                students_age = input('Введите возраст: ')
                s = 0
                for i in students_age:
                    if i in '0123456789':
                        s += 1
                if s == len(students_age):
                    if (int(students_age) >= 17) and (int(students_age) < 100):
                        check = 1
                    else:
                        print('Введите возраст правильно!(число от 17 до 99 включительно)')
                else:
                    print('Введите возраст правильно!(число от 17 до 99 включительно)')

            students_institute = ''
            check = 0
            while check == 0:
                students_institute = input('Введите институт: ')
                s = 0
                for i in students_institute:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                        s += 1
                if s == len(students_institute):
                    check = 1
                else:
                    print('Введите институт правильно!(латинские/русские строчные/заглавные буквы)')
            students_institute = students_institute.lower()
            students_institute = students_institute.capitalize()

            students_programme_type = ''
            check = 0
            while check == 0:
                students_programme_type = input('Введите направление обучения: ')
                s = 0
                for i in students_programme_type:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                        s += 1
                if s == len(students_programme_type):
                    check = 1
                else:
                    print(
                        'Введите направление обучения правильно!(латинские/русские строчные/заглавные буквы)')
            students_programme_type = students_programme_type.lower()
            students_programme_type = students_programme_type.capitalize()

            students_gradebook_number = ''
            check = 0
            while check == 0:
                students_gradebook_number = input('Введите номер зачетной книжки: ')
                s = 0
                for i in students_gradebook_number:
                    if i in '0123456789':
                        s += 1
                if s == len(students_gradebook_number):
                    if (int(students_gradebook_number) >= 100000) and (int(students_gradebook_number) <= 999999):
                        check = 1
                    else:
                        print('Введите номер зачетной книжки правильно!(шестизначное число)')
                else:
                    print('Введите номер зачетной книжки правильно!(шестизначное число)')

            students_mail = ''
            check = 0
            while check == 0:
                students_mail = input('Введите почту (stud0000******@study.utmn.ru - шесть цифр на месте звездочек): ')
                s = 0
                for i in students_mail:
                    if i in '0123456789':
                        s += 1
                if s == len(students_mail):
                    if len(students_mail) == 6:
                        check = 1
                    else:
                        print('Введите почту правильно!(stud0000******@study.utmn.ru - шесть цифр на месте звездочек)')
                else:
                    print('Введите почту правильно!(stud0000******@study.utmn.ru - шесть цифр на месте звездочек)')
            students_mail = 'stud0000' + students_mail + '@study.utmn.ru'

            students_phone_number = ''
            check = 0
            while check == 0:
                students_phone_number = input(
                    'Введите номер телефона (+7********** - десять цифр на месте звездочек): ')
                s = 0
                for i in students_phone_number:
                    if i in '0123456789':
                        s += 1
                if s == len(students_phone_number):
                    if len(students_phone_number) == 10:
                        check = 1
                    else:
                        print('Введите номер телефона правильно!(+7********** - десять цифр на месте звездочек)')
                else:
                    print('Введите номер телефона правильно!(+7********** - десять цифр на месте звездочек)')
            students_phone_number = '+7' + students_phone_number

            info = (students_name, students_surname, students_patronymic, students_age, students_institute,
                    students_programme_type, students_gradebook_number, students_mail, students_phone_number)

            cursor.execute(
                'INSERT INTO Student (students_name, students_surname, students_patronymic, students_age, students_institute, students_programme_type, students_gradebook_number, students_mail, students_phone_number) VALUES (?,?,?,?,?,?,?,?,?)',
                info)
            con.commit()

        elif table == '2':
            teachers_name = ''
            check = 0
            while check == 0:
                teachers_name = input('Введите имя: ')
                s = 0
                for i in teachers_name:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(teachers_name):
                    check = 1
                else:
                    print('Введите имя правильно!(русские строчные/заглавные буквы)')
            teachers_name = teachers_name.lower()
            teachers_name = teachers_name.capitalize()

            teachers_surname = ''
            check = 0
            while check == 0:
                teachers_surname = input('Введите фамилию: ')
                s = 0
                for i in teachers_surname:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(teachers_surname):
                    check = 1
                else:
                    print('Введите фамилию правильно!(русские строчные/заглавные буквы)')
            teachers_surname = teachers_surname.lower()
            teachers_surname = teachers_surname.capitalize()

            teachers_patronymic = ''
            check = 0
            while check == 0:
                teachers_patronymic = input('Введите отчество: ')
                s = 0
                for i in teachers_patronymic:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                        s += 1
                if s == len(teachers_patronymic):
                    check = 1
                else:
                    print('Введите отчество правильно!(русские строчные/заглавные буквы): ')
            teachers_patronymic = teachers_patronymic.lower()
            teachers_patronymic = teachers_patronymic.capitalize()

            teachers_institute = ''
            check = 0
            while check == 0:
                teachers_institute = input('Введите институт: ')
                s = 0
                for i in teachers_institute:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                        s += 1
                if s == len(teachers_institute):
                    check = 1
                else:
                    print('Введите институт (латинские/русские строчные/заглавные буквы)')
            teachers_institute = teachers_institute.lower()
            teachers_institute = teachers_institute.capitalize()

            teachers_department = ''
            check = 0
            while check == 0:
                teachers_department = input('Введите название кафедры: ')
                s = 0
                for i in teachers_department:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                        s += 1
                if s == len(teachers_department):
                    check = 1
                else:
                    print('Введите название кафедры правильно!(латинские/русские строчные/заглавные буквы): ')
            teachers_department = teachers_department.lower()
            teachers_department = teachers_department.capitalize()

            info = (teachers_name, teachers_surname, teachers_patronymic, teachers_institute, teachers_department)

            cursor.execute(
                'INSERT INTO Teacher (teachers_name, teachers_surname, teachers_patronymic, teachers_institute, teachers_department) VALUES (?,?,?,?,?)',
                info)
            con.commit()

        elif table == '3':
            courses_name = ''
            check = 0
            while check == 0:
                courses_name = input('Введите название курса: ')
                s = 0
                for i in courses_name:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIIOOPASDFGHJKLZXCVBNM ':
                        s += 1
                if s == len(courses_name):
                    check = 1
                else:
                    print('Введите название курса правильно!(латинские/русские строчные/заглавные буквы)')
            courses_name = courses_name.lower()
            courses_name = courses_name.capitalize()

            courses_description = ''
            check = 0
            while check == 0:
                courses_description = input('Введите описание курса: ')
                s = 0
                for i in courses_description:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIIOOPASDF\GHJKLZXCVBNM 0123456789.,!"№;%:?*()-_+=/!@#@$%%^^&&*()_+?><:"{}][|/-+~``!@#$%':
                        s += 1
                if s == len(courses_description):
                    check = 1
                else:
                    print(
                        'Введите описание курса правильно!(латинские/русские строчные/заглавные буквы, цифры и знаки препинания)')

            info = (courses_name, courses_description)

            cursor.execute('INSERT INTO Course (courses_name, courses_description) VALUES (?,?)', info)
            con.commit()

        elif table == '4':
            meetings_topic = ''
            check = 0
            while check == 0:
                meetings_topic = input('Введите тему встречи: ')
                s = 0
                for i in meetings_topic:
                    if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ wertyuiopqasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                        s += 1
                if s == len(meetings_topic):
                    check = 1
                else:
                    print('Введите тему встречи правильно!(латинские/русские строчные/заглавные буквы)')
            meetings_topic = meetings_topic.lower()
            meetings_topic = meetings_topic.capitalize()

            meetings_house = ''
            check = 0
            while check == 0:
                meetings_house = input('Введите здание (УЛК-** - две цифры на месте звездочек): ')
                s = 0
                for i in meetings_house:
                    if i in '0123456789':
                        s += 1
                if s == len(meetings_house):
                    if len(meetings_house) == 2:
                        check = 1
                    else:
                        print('Введите здание правильно!(УЛК-** - две цифры на месте звездочек)')
                else:
                    print('Введите здание правильно!(УЛК-** - две цифры на месте звездочек)')
            meetings_house = 'УЛК-' + meetings_house

            meetings_room = ''
            check = 0
            while check == 0:
                meetings_room = input('Введите аудиторию: ')
                s = 0
                for i in meetings_room:
                    if i in '0123456789':
                        s += 1
                if s == len(meetings_room):
                    if int(meetings_room) >= 100 and int(meetings_room) < 1000:
                        check = 1
                    else:
                        print('Введите аудиторию правильно!(трехзначное число)')
                else:
                    print('Введите аудиторию правильно!(трехзначное число)')

            meetings_start_time_hour = ''
            check = 0
            while check == 0:
                meetings_start_time_hour = input('Введите час начала пары: ')
                s = 0
                for i in meetings_start_time_hour:
                    if i in '0123456789':
                        s += 1
                if s == len(meetings_start_time_hour):
                    if (int(meetings_start_time_hour) >= 0) and (int(meetings_start_time_hour) < 23):
                        check = 1
                    else:
                        print('Введите час начала пары правильно!(число от 0 до 22)')
                else:
                    print('Введите час начала пары правильно!(число от 0 до 22)')

            meetings_start_time_minute = ''
            check = 0
            while check == 0:
                meetings_start_time_minute = input('Введите минуты начала пары: ')
                s = 0
                for i in meetings_start_time_minute:
                    if i in '0123456789':
                        s += 1
                if s == len(meetings_start_time_minute):
                    if (int(meetings_start_time_minute) >= 0) and (int(meetings_start_time_minute) < 56):
                        check = 1
                    else:
                        print('Введите минуты начала пары правильно!(число от 0 до 55)')
                else:
                    print('Введите минуты начала пары правильно!(число от 0 до 55)')

            meetings_start_time = meetings_start_time_hour + ':' + meetings_start_time_minute

            if (int(meetings_start_time_minute) >= 0) and (int(meetings_start_time_minute) <= 29):
                meetings_end_time_hour = str(int(meetings_start_time_hour) + 1)
                meetings_end_time_minute = str(int(meetings_start_time_minute) + 30)
            else:
                meetings_end_time_hour = str(int(meetings_start_time_hour) + 2)
                meetings_end_time_minute = str(int(meetings_start_time_minute) - 30)

            meetings_end_time = meetings_end_time_hour + ':' + meetings_end_time_minute

            info = (meetings_topic, meetings_house, meetings_room, meetings_start_time, meetings_end_time)

            cursor.execute(
                'INSERT INTO Meeting (meetings_topic, meetings_house, meetings_room, meetings_start_time, meetings_end_time) VALUES (?,?,?,?,?)',
                info)
            con.commit()

        print('Добавлено!')

    elif action == '3':
        print('Таблицы базы данных для редактирования значений:')
        table = ''
        check = 0
        while check == 0:
            print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
            table = input('Выберите цифру: ')
            if (table in '1234') and (len(table) == 1):
                check = 1
            else:
                print('Введите цифру правильно!')

        if table == '1':
            print('Столбцы базы данных для редактирования значений:')
            st = ''
            check = 0
            while check == 0:
                print('''1 - Name
2 - Surname
3 - Patronymic
4 - Age
5 - Institute
6 - Programme type
7 - Gradebook number
8 - Mail
9 - Phone number''')
                st = input('Выберите цифру: ')
                if (st in '123456789') and (len(st) == 1):
                    check = 1
                else:
                    print('Введите цифру правильно!')

            if st == '1':
                cursor.execute('SELECT students_name, students_surname, students_patronymic, students_id FROM Student')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                students_id = ''
                check = 0
                while check == 0:
                    students_id = input('Введите Id студента, у которого нужно поменять имя: ')
                    s = 0
                    for i in students_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(students_id):
                                t = 1
                        if t:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                students_name = ''
                check = 0
                while check == 0:
                    students_name = input('Введите новое имя: ')
                    s = 0
                    for i in students_name:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                            s += 1
                    if s == len(students_name):
                        check = 1
                    else:
                        print('Введите имя правильно!(русские строчные/заглавные буквы)')
                students_name = students_name.lower()
                students_name = students_name.capitalize()

                z = 'UPDATE Student SET students_name = "' + students_name + '" WHERE students_id = ' + students_id
                cursor.execute(z)
                con.commit()

            elif st == '2':
                cursor.execute('SELECT students_name, students_surname, students_patronymic, students_id FROM Student')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                students_id = ''
                check = 0
                while check == 0:
                    students_id = input('Введите Id студента, у которого нужно поменять фамилию: ')
                    s = 0
                    for i in students_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(students_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                students_surname = ''
                check = 0
                while check == 0:
                    students_surname = input('Введите новую фамилию: ')
                    s = 0
                    for i in students_surname:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                            s += 1
                    if s == len(students_surname):
                        check = 1
                    else:
                        print('Введите фамилию правильно!(русские строчные/заглавные буквы)')
                students_surname = students_surname.lower()
                students_surname = students_surname.capitalize()

                z = 'UPDATE Student SET students_surname = "' + students_surname + '" WHERE students_id = ' + students_id
                cursor.execute(z)
                con.commit()

            elif st == '3':
                cursor.execute('SELECT students_name, students_surname, students_patronymic, students_id FROM Student')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                students_id = ''
                check = 0
                while check == 0:
                    students_id = input('Введите Id студента, у которого нужно поменять отчество: ')
                    s = 0
                    for i in students_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(students_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                students_patronymic = ''
                check = 0
                while check == 0:
                    students_patronymic = input('Введите новое отчество: ')
                    s = 0
                    for i in students_patronymic:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                            s += 1
                    if s == len(students_patronymic):
                        check = 1
                    else:
                        print('Введите отчество правильно!(русские строчные/заглавные буквы)')
                students_patronymic = students_patronymic.lower()
                students_patronymic = students_patronymic.capitalize()

                z = 'UPDATE Student SET students_patronymic = "' + students_patronymic + '" WHERE students_id = ' + students_id
                cursor.execute(z)
                con.commit()

            elif st == '4':
                cursor.execute(
                    'SELECT students_name, students_surname, students_patronymic, students_age, students_id FROM Student')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Age', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                students_id = ''
                check = 0
                while check == 0:
                    students_id = input('Введите Id студента, у которого нужно поменять возраст: ')
                    s = 0
                    for i in students_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(students_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                students_age = ''
                check = 0
                while check == 0:
                    students_age = input('Введите новый возраст: ')
                    s = 0
                    for i in students_age:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_age):
                        if (int(students_age) >= 17) and (int(students_age) < 100):
                            check = 1
                        else:
                            print('Введите возраст правильно!(число от 17 до 99 включительно)')
                    else:
                        print('Введите возраст правильно!(число от 17 до 99 включительно)')

                z = 'UPDATE Student SET students_age = ' + students_age + ' WHERE students_id = ' + students_id
                cursor.execute(z)
                con.commit()

            elif st == '5':
                cursor.execute(
                    'SELECT students_name, students_surname, students_patronymic, students_institute, students_id FROM Student')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Institute', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                students_id = ''
                check = 0
                while check == 0:
                    students_id = input('Введите Id студента, у которого нужно поменять институт: ')
                    s = 0
                    for i in students_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(students_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                students_institute = ''
                check = 0
                while check == 0:
                    students_institute = input('Введите новый институт: ')
                    s = 0
                    for i in students_institute:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                            s += 1
                    if s == len(students_institute):
                        check = 1
                    else:
                        print('Введите институт правильно!(латинские/русские строчные/заглавные буквы)')
                students_institute = students_institute.lower()
                students_institute = students_institute.capitalize()

                z = 'UPDATE Student SET students_institute = "' + students_institute + '" WHERE students_id = ' + students_id
                cursor.execute(z)
                con.commit()

            elif st == '6':
                cursor.execute(
                    'SELECT students_name, students_surname, students_patronymic, students_programme_type, students_id FROM Student')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Programme type', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                students_id = ''
                check = 0
                while check == 0:
                    students_id = input('Введите Id студента, у которого нужно поменять напраление обучения: ')
                    s = 0
                    for i in students_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(students_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                students_programme_type = ''
                check = 0
                while check == 0:
                    students_programme_type = input('Введите новое направление обучения: ')
                    s = 0
                    for i in students_programme_type:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                            s += 1
                    if s == len(students_programme_type):
                        check = 1
                    else:
                        print('Введите направление обучения правильно!(латинские/русские строчные/заглавные буквы)')
                students_programme_type = students_programme_type.lower()
                students_programme_type = students_programme_type.capitalize()

                z = 'UPDATE Student SET students_programme_type = "' + students_programme_type + '" WHERE students_id = ' + students_id
                cursor.execute(z)
                con.commit()

            elif st == '7':
                cursor.execute(
                    'SELECT students_name, students_surname, students_patronymic, students_gradebook_number, students_id FROM Student')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Gradebook number', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                students_id = ''
                check = 0
                while check == 0:
                    students_id = input('Введите Id студента, у которого нужно поменять номер зачетной книжки: ')
                    s = 0
                    for i in students_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(students_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                students_gradebook_number = ''
                check = 0
                while check == 0:
                    students_gradebook_number = input('Введите новый номер зачетной книжки: ')
                    s = 0
                    for i in students_gradebook_number:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_gradebook_number):
                        if (int(students_gradebook_number) >= 100000) and (int(students_gradebook_number) <= 999999):
                            cursor.execute('SELECT students_gradebook_number FROM Student')
                            data = cursor.fetchall()
                            t = 0
                            for i in data:
                                if i[0] != students_gradebook_number:
                                    t += 1
                            if t == len(data):
                                check = 1
                            else:
                                print('Такая зачетная книжка уже существует')
                        else:
                            print('Введите номер зачетной книжки правильно!(шестизначное число)')
                    else:
                        print('Введите номер зачетной книжки правильно!(шестизначное число)')

                z = 'UPDATE Student SET students_gradebook_number = ' + students_gradebook_number + ' WHERE students_id = ' + students_id
                cursor.execute(z)
                con.commit()

            elif st == '8':
                cursor.execute(
                    'SELECT students_name, students_surname, students_patronymic, students_mail, students_id FROM Student')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Mail', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                students_id = ''
                check = 0
                while check == 0:
                    students_id = input('Введите Id студента, у которого нужно поменять почту: ')
                    s = 0
                    for i in students_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(students_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                students_mail = ''
                check = 0
                while check == 0:
                    students_mail = input(
                        'Введите новую почту (stud0000******@study.utmn.ru - шесть цифр на месте звездочек): ')
                    s = 0
                    for i in students_mail:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_mail):
                        if len(students_mail) == 6:
                            cursor.execute('SELECT students_mail FROM Student')
                            data = cursor.fetchall()
                            t = 0
                            for i in data:
                                if i[0] != 'stud0000' + students_mail + '@study.utmn.ru':
                                    t += 1
                            if t == len(data):
                                check = 1
                            else:
                                print('Такая почта уже существует')
                        else:
                            print(
                                'Введите почту правильно!(stud0000******@study.utmn.ru - шесть цифр на месте звездочек)')
                    else:
                        print('Введите почту правильно!(stud0000******@study.utmn.ru - шесть цифр на месте звездочек)')
                students_mail = 'stud0000' + students_mail + '@study.utmn.ru'

                z = 'UPDATE Student SET students_mail = "' + students_mail + '" WHERE students_id = ' + students_id
                cursor.execute(z)
                con.commit()

            elif st == '9':
                cursor.execute(
                    'SELECT students_name, students_surname, students_patronymic, students_phone_number, students_id FROM Student')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Phone number', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                students_id = ''
                check = 0
                while check == 0:
                    students_id = input('Введите Id студента, у которого нужно поменять номер телефона: ')
                    s = 0
                    for i in students_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(students_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                students_phone_number = ''
                check = 0
                while check == 0:
                    students_phone_number = input(
                        'Введите новый номер телефона (+7********** - десять цифр на месте звездочек): ')
                    s = 0
                    for i in students_phone_number:
                        if i in '0123456789':
                            s += 1
                    if s == len(students_phone_number):
                        if len(students_phone_number) == 10:
                            cursor.execute('SELECT students_phone_number FROM Student')
                            data = cursor.fetchall()
                            t = 0
                            for i in data:
                                if i[0] != '+7' + students_phone_number:
                                    t += 1
                            if t == len(data):
                                check = 1
                            else:
                                print('Такой номер телефона уже существует')
                        else:
                            print('Введите номер телефона правильно!(+7********** - десять цифр на месте звездочек): ')
                    else:
                        print('Введите номер телефона правильно!(+7********** - десять цифр на месте звездочек): ')
                students_phone_number = '+7' + students_phone_number

                z = 'UPDATE Student SET students_phone_number = "' + students_phone_number + '" WHERE students_id = ' + students_id
                cursor.execute(z)
                con.commit()

        elif table == '2':
            print('Столбцы базы данных для редактирования значений:')
            st = ''
            check = 0
            while check == 0:
                print('''1 - Name
2 - Surname
3 - Patronymic
4 - Institute
5 - Department''')
                st = input('Выберите цифру: ')
                if (st in '12345') and (len(st) == 1):
                    check = 1
                else:
                    print('Введите цифру правильно!')

            if st == '1':
                cursor.execute('SELECT teachers_name, teachers_surname, teachers_patronymic, teachers_id FROM Teacher')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                teachers_id = ''
                check = 0
                while check == 0:
                    teachers_id = input('Введите Id учителя, у которого нужно поменять имя: ')
                    s = 0
                    for i in teachers_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(teachers_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(teachers_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                teachers_name = ''
                check = 0
                while check == 0:
                    teachers_name = input('Введите новое имя: ')
                    s = 0
                    for i in teachers_name:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                            s += 1
                    if s == len(teachers_name):
                        check = 1
                    else:
                        print('Введите имя правильно!(русские строчные/заглавные буквы)')
                teachers_name = teachers_name.lower()
                teachers_name = teachers_name.capitalize()

                z = 'UPDATE Teacher SET teachers_name = "' + teachers_name + '" WHERE teachers_id = ' + teachers_id
                cursor.execute(z)
                con.commit()

            elif st == '2':
                cursor.execute('SELECT teachers_name, teachers_surname, teachers_patronymic, teachers_id FROM Teacher')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                teachers_id = ''
                check = 0
                while check == 0:
                    teachers_id = input('Введите Id учителя, у которого нужно поменять фамилию: ')
                    s = 0
                    for i in teachers_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(teachers_id):
                        cursor.execute('SELECT students_id FROM Student')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(teachers_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                teachers_surname = ''
                check = 0
                while check == 0:
                    teachers_surname = input('Введите новую фамилию: ')
                    s = 0
                    for i in teachers_surname:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                            s += 1
                    if s == len(teachers_surname):
                        check = 1
                    else:
                        print('Введите фамилию правильно!(русские строчные/заглавные буквы)')
                teachers_surname = teachers_surname.lower()
                teachers_surname = teachers_surname.capitalize()

                z = 'UPDATE Teacher SET teachers_surname = "' + teachers_surname + '" WHERE teachers_id = ' + teachers_id
                cursor.execute(z)
                con.commit()

            elif st == '3':
                cursor.execute('SELECT teachers_name, teachers_surname, teachers_patronymic, teachers_id FROM Teacher')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                teachers_id = ''
                check = 0
                while check == 0:
                    teachers_id = input('Введите Id учителя, у которого нужно поменять отчество: ')
                    s = 0
                    for i in teachers_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(teachers_id):
                        cursor.execute('SELECT teachers_id FROM Teacher')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(teachers_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                teachers_patronymic = ''
                check = 0
                while check == 0:
                    teachers_patronymic = input('Введите новое отчество: ')
                    s = 0
                    for i in teachers_patronymic:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ':
                            s += 1
                    if s == len(teachers_patronymic):
                        check = 1
                    else:
                        print('Введите отчество правильно!(русские строчные/заглавные буквы)')
                teachers_patronymic = teachers_patronymic.lower()
                teachers_patronymic = teachers_patronymic.capitalize()

                z = 'UPDATE Teacher SET teachers_patronymic = "' + teachers_patronymic + '" WHERE teachers_id = ' + teachers_id
                cursor.execute(z)
                con.commit()

            elif st == '4':
                cursor.execute(
                    'SELECT teachers_name, teachers_surname, teachers_patronymic, teachers_institute, teachers_id FROM Teacher')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Institute', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                teachers_id = ''
                check = 0
                while check == 0:
                    teachers_id = input('Введите Id учителя, у которого нужно поменять институт: ')
                    s = 0
                    for i in teachers_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(teachers_id):
                        cursor.execute('SELECT teachers_id FROM Teacher')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(teachers_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                teachers_institute = ''
                check = 0
                while check == 0:
                    teachers_institute = input('Введите новый институт: ')
                    s = 0
                    for i in teachers_institute:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                            s += 1
                    if s == len(teachers_institute):
                        check = 1
                    else:
                        print('Введите институт правильно!(латинские/русские строчные/заглавные буквы): ')
                teachers_institute = teachers_institute.lower()
                teachers_institute = teachers_institute.capitalize()

                z = 'UPDATE Teacher SET teachers_institute = "' + teachers_institute + '" WHERE teachers_id = ' + teachers_id
                cursor.execute(z)
                con.commit()

            elif st == '5':
                cursor.execute(
                    'SELECT teachers_name, teachers_surname, teachers_patronymic, teachers_department, teachers_id FROM Teacher')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Surname', 'Patronymic', 'Department', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                teachers_id = ''
                check = 0
                while check == 0:
                    teachers_id = input('Введите Id учителя, у которого нужно поменять кафедру: ')
                    s = 0
                    for i in teachers_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(teachers_id):
                        cursor.execute('SELECT teachers_id FROM Teacher')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(teachers_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                teachers_department = ''
                check = 0
                while check == 0:
                    teachers_department = input('Введите новую кафедру: ')
                    s = 0
                    for i in teachers_department:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM ':
                            s += 1
                    if s == len(teachers_department):
                        check = 1
                    else:
                        print('Введите кафедру правильно!(латинские/русские строчные/заглавные буквы)')
                teachers_department = teachers_department.lower()
                teachers_department = teachers_department.capitalize()

                z = 'UPDATE Teacher SET teachers_department = "' + teachers_department + '" WHERE teachers_id = ' + teachers_id
                cursor.execute(z)
                con.commit()

        elif table == '3':
            print('Столбцы базы данных для редактирования значений:')
            st = ''
            check = 0
            while check == 0:
                print('''1 - Name
2 - Description''')
                st = input('Выберите цифру: ')
                if (st == '1') or (st == '2'):
                    check = 1
                else:
                    print('Введите цифру правильно!')

            if st == '1':
                cursor.execute('SELECT courses_name, courses_description, courses_id FROM Course')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Description', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                courses_id = ''
                check = 0
                while check == 0:
                    courses_id = input('Введите Id курса, у которого нужно поменять имя: ')
                    s = 0
                    for i in courses_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(courses_id):
                        cursor.execute('SELECT courses_id FROM Course')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(courses_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                courses_name = ''
                check = 0
                while check == 0:
                    courses_name = input('Введите новое название курса: ')
                    s = 0
                    for i in courses_name:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ wertyuiopqasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                            s += 1
                    if s == len(courses_name):
                        check = 1
                    else:
                        print('Введите название курса правильно!(латинские/русские строчные/заглавные буквы)')
                courses_name = courses_name.lower()
                courses_name = courses_name.capitalize()

                z = 'UPDATE Course SET courses_name = "' + courses_name + '" WHERE courses_id = ' + courses_id
                cursor.execute(z)
                con.commit()

            elif st == '2':
                cursor.execute('SELECT courses_name, courses_description, courses_id FROM Course')
                data = cursor.fetchall()
                data.insert(0, ('Name', 'Description', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                courses_id = ''
                check = 0
                while check == 0:
                    courses_id = input('Введите Id курса, у которого нужно поменять описание: ')
                    s = 0
                    for i in courses_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(courses_id):
                        cursor.execute('SELECT courses_id FROM Course')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(courses_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                courses_description = ''
                check = 0
                while check == 0:
                    courses_description = input('Введите новое описание курса: ')
                    s = 0
                    for i in courses_description:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮqwertyuiopasdfghjklzxcvbnmQWERTYUIIOOPASDFGHJKLZXCVBNM 0123456789.,!"№;%:?*()-_+=/':
                            s += 1
                    if s == len(courses_description):
                        check = 1
                    else:
                        print(
                            'Введите описание курса правильно!(латинские/русские строчные/заглавные буквы, цифры и знаки препинания)')

                z = 'UPDATE Course SET courses_description = "' + courses_description + '" WHERE courses_id = ' + courses_id
                cursor.execute(z)
                con.commit()

        elif table == '4':
            print('Столбцы базы данных для редактирования значений:')
            st = ''
            check = 0
            while check == 0:
                print('''1 - Topic
2 - House
3 - Room
4 - Start time''')
                st = input('Выберите цифру: ')
                if (st in '1234') and (len(st) == 1):
                    check = 1
                else:
                    print('Введите цифру правильно!')

            if st == '1':
                cursor.execute('SELECT meetings_topic, meetings_id FROM Meeting')
                data = cursor.fetchall()
                data.insert(0, ('Topic', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                meetings_id = ''
                check = 0
                while check == 0:
                    meetings_id = input('Введите Id пары, у которого нужно поменять тему: ')
                    s = 0
                    for i in meetings_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(meetings_id):
                        cursor.execute('SELECT meetings_id FROM Meeting')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(meetings_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                meetings_topic = ''
                check = 0
                while check == 0:
                    meetings_topic = input('Введите новую тему пары: ')
                    s = 0
                    for i in meetings_topic:
                        if i in 'ёйцукенгшщзхъфывапролджэячсмитьбюЁЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮ wertyuiopqasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM':
                            s += 1
                    if s == len(meetings_topic):
                        check = 1
                    else:
                        print('Введите тему пары правильно!(латинские/русские строчные/заглавные буквы)')
                meetings_topic = meetings_topic.lower()
                meetings_topic = meetings_topic.capitalize()

                z = 'UPDATE Meeing SET meetings_topic = "' + meetings_topic + '" WHERE meetings_id = ' + meetings_id
                cursor.execute(z)
                con.commit()

            elif st == '2':
                cursor.execute('SELECT meetings_topic, meetings_house, meetings_id FROM Meeting')
                data = cursor.fetchall()
                data.insert(0, ('Topic', 'House', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                meetings_id = ''
                check = 0
                while check == 0:
                    meetings_id = input('Введите Id пары, у которого нужно поменять здание: ')
                    s = 0
                    for i in meetings_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(meetings_id):
                        cursor.execute('SELECT meetings_id FROM Meeting')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(meetings_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                meetings_house = ''
                check = 0
                while check == 0:
                    meetings_house = input('Введите новое здание (УЛК-** - две цифры на месте звездочек): ')
                    s = 0
                    for i in meetings_house:
                        if i in '0123456789':
                            s += 1
                    if s == len(meetings_house):
                        if len(meetings_house) == 2:
                            check = 1
                        else:
                            print('Введите здание правильно!(УЛК-** - две цифры на месте звездочек)')
                    else:
                        print('Введите здание правильно!(УЛК-** - две цифры на месте звездочек)')
                meetings_house = 'УЛК-' + meetings_house

                z = 'UPDATE Meeting SET meetings_house = "' + meetings_house + '" WHERE meetings_id = ' + meetings_id
                cursor.execute(z)
                con.commit()

            elif st == '3':
                cursor.execute('SELECT meetings_topic, meetings_room, meetings_id FROM Meeting')
                data = cursor.fetchall()
                data.insert(0, ('Topic', 'Room', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                meetings_id = ''
                check = 0
                while check == 0:
                    meetings_id = input('Введите Id пары, у которого нужно поменять аудиторию: ')
                    s = 0
                    for i in meetings_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(meetings_id):
                        cursor.execute('SELECT meetings_id FROM Meeting')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(meetings_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                meetings_room = ''
                check = 0
                while check == 0:
                    meetings_room = input('Введите новую аудиторию: ')
                    s = 0
                    for i in meetings_room:
                        if i in '0123456789':
                            s += 1
                    if s == len(meetings_room):
                        if int(meetings_room) >= 100 and int(meetings_room) < 1000:
                            check = 1
                        else:
                            print('Введите аудиторию правильно!(трехзначное число)')
                    else:
                        print('Введите аудиторию правильно!(трехзначное число)')

                z = 'UPDATE Meeting SET meetings_room = "' + meetings_room + '" WHERE meetings_id = ' + meetings_id
                cursor.execute(z)
                con.commit()

            elif st == '4':
                cursor.execute('SELECT meetings_topic, meetings_start_time, meetings_id FROM Meeting')
                data = cursor.fetchall()
                data.insert(0, ('Topic', 'Start time', 'Id'))
                lens = []
                for i in range(len(data[0])):
                    s = 0
                    for j in range(len(data)):
                        s = max(s, len(str(data[j][i])))
                    lens.append(s)

                for i in data:
                    s = 0
                    for j in i:
                        print(str(j) + ' ' * (lens[s] - len(str(j))), end=' ')
                        s += 1
                    print()

                meetings_id = ''
                check = 0
                while check == 0:
                    meetings_id = input('Введите Id пары, у которого нужно поменять время начала: ')
                    s = 0
                    for i in meetings_id:
                        if i in '0123456789':
                            s += 1
                    if s == len(meetings_id):
                        cursor.execute('SELECT meetings_id FROM Meeting')
                        t = 0
                        data = cursor.fetchall()
                        for i in data:
                            if i[0] == int(meetings_id):
                                t = 1
                        if t == 1:
                            check = 1
                        else:
                            print('Введите Id правильно!(целое число)')
                    else:
                        print('Введите Id правильно!(целое число)')

                meetings_start_time_hour = ''
                check = 0
                while check == 0:
                    meetings_start_time_hour = input('Введите новый час начала пары: ')
                    s = 0
                    for i in meetings_start_time_hour:
                        if i in '0123456789':
                            s += 1
                    if s == len(meetings_start_time_hour):
                        if (int(meetings_start_time_hour) >= 0) and (int(meetings_start_time_hour) <= 21):
                            check = 1
                        else:
                            print('Введите час начала пары правильно!(число от 0 до 21)')
                    else:
                        print('Введите час начала пары правильно!(число от 0 до 21)')

                meetings_start_time_minute = ''
                check = 0
                while check == 0:
                    meetings_start_time_minute = input('Введите новые минуты начала пары: ')
                    s = 0
                    for i in meetings_start_time_minute:
                        if i in '0123456789':
                            s += 1
                    if s == len(meetings_start_time_minute):
                        if (int(meetings_start_time_minute) >= 0) and (int(meetings_start_time_minute) <= 55):
                            check = 1
                        else:
                            print('Введите минуты начала пары правильно!(число от 0 до 55)')
                    else:
                        print('Введите минуты начала пары правильно!(число от 0 до 55)')

                meetings_start_time = meetings_start_time_hour + ':' + meetings_start_time_minute

                z = 'UPDATE Meeting SET meetings_start_time = "' + meetings_start_time + '" WHERE meetings_id = ' + meetings_id
                cursor.execute(z)
                con.commit()

                if (int(meetings_start_time_minute) >= 0) and (int(meetings_start_time_minute) <= 29):
                    meetings_end_time_hour = str(int(meetings_start_time_hour) + 1)
                    meetings_end_time_minute = str(int(meetings_start_time_minute) + 30)
                else:
                    meetings_end_time_hour = str(int(meetings_start_time_hour) + 2)
                    meetings_end_time_minute = str(int(meetings_start_time_minute) - 30)

                meetings_end_time = meetings_end_time_hour + ':' + meetings_end_time_minute

                z = 'UPDATE Meeting SET meetings_end_time = "' + meetings_end_time + '" WHERE meetings_id = ' + meetings_id
                cursor.execute(z)
                con.commit()

        print('Обновлено!')

    elif action == '4':
        print('Таблицы базы данных для вывода статистики:')
        table = ''
        check = 0
        while check == 0:
            print('''1 - Student
2 - Teacher
4 - Meeting''')
            table = input('Выберите цифру: ')
            if (table == '1') or (table == '2') or (table == '4'):
                check = 1
            else:
                print('Введите цифру правильно!')

        if table == '1':
            print('Столбцы базы данных для вывода статистики:')
            st = ''
            check = 0
            print('''1 - Name
2 - Surname
3 - Patronymic
4 - Age
5 - Institute
6 - Programme type''')
            while check == 0:
                st = input('Введите цифру: ')
                s = 0
                for i in st:
                    if len(i) == 1 and i in '123456':
                        s += 1
                if s == len(st):
                    check = 1
                else:
                    print('Введите цифру правильно!')

            if (st == '1') or (st == '2') or (st == '3') or (st == '5') or (st == '6'):
                cursor.execute('SELECT ' + student[int(st)] + ' FROM Student')
                data = cursor.fetchall()
                names = []
                for i in data:
                    names.append(i[0])
                uniq = list(set(names))
                uniq.sort()
                counts = []
                for i in uniq:
                    counts.append(names.count(i))
                m = max(counts)
                mode = []
                if list(set(counts)).sort() != counts.sort():
                    for i in range(len(counts)):
                        if counts[i] == m:
                            mode.append(uniq[i])
                else:
                    mode.append('-')

                if st == '1':
                    print('Самое распространенное имя:', ', '.join(mode))
                elif st == '2':
                    print('Самая распространенная фамилия:', ', '.join(mode))
                elif st == '3':
                    print('Самое распространенное отчество:', ', '.join(mode))
                elif st == '5':
                    print('Самый распространенный институт:', ', '.join(mode))
                elif st == '6':
                    print('Самое распространенное направление:', ', '.join(mode))
            elif st == '4':
                cursor.execute('SELECT students_age FROM Student')
                data = cursor.fetchall()
                ages = []
                for i in data:
                    ages.append(int(i[0]))
                print('Минимальный возраст студентов: ', min(ages))
                print('Максимальный возраст студентов: ', max(ages))
                print('Средний возраст студентов: ', round(sum(ages) / len(ages), 2))

        elif table == '2':
            print('Столбцы базы данных для вывода статистики:')
            st = ''
            check = 0
            print('''1 - Name
2 - Surname
3 - Patronymic
4 - Institute
5 - Department''')
            while check == 0:
                st = input('Введите цифру: ')
                s = 0
                for i in st:
                    if len(i) == 1 and i in '12345':
                        s += 1
                if s == len(st):
                    check = 1
                else:
                    print('Введите цифру правильно!')

            cursor.execute('SELECT ' + teacher[int(st)] + ' FROM Teacher')
            data = cursor.fetchall()
            names = []
            for i in data:
                names.append(i[0])
            uniq = list(set(names))
            uniq.sort()
            counts = []
            for i in uniq:
                counts.append(names.count(i))
            m = max(counts)
            mode = []
            if list(set(counts)).sort() != counts.sort():
                for i in range(len(counts)):
                    if counts[i] == m:
                        mode.append(uniq[i])
            else:
                mode.append('-')
            if st == '1':
                print('Самое распространенное имя:', ', '.join(mode))
            elif st == '2':
                print('Самая распространенная фамилия:', ', '.join(mode))
            elif st == '3':
                print('Самое распространенное отчество:', ', '.join(mode))
            elif st == '4':
                print('Самый распространенный институт:', ', '.join(mode))
            elif st == '5':
                print('Самая распространенная кафедра:', ', '.join(mode))

        elif table == '4':
            print('Столбцы базы данных для вывода статистики:')
            st = ''
            check = 0
            print('''1 - Topic
2 - House
3 - Room
4 - Start time''')
            while check == 0:
                st = input('Введите цифру: ')
                s = 0
                for i in st:
                    if len(i) == 1 and i in '1234':
                        s += 1
                if s == len(st):
                    check = 1
                else:
                    print('Введите цифру правильно!')

            cursor.execute('SELECT ' + meeting[int(st)] + ' FROM Meeting')
            data = cursor.fetchall()
            names = []
            for i in data:
                names.append(i[0])
            uniq = list(set(names))
            uniq.sort()
            counts = []
            for i in uniq:
                counts.append(names.count(i))
            m = max(counts)
            mode = []
            if list(set(counts)).sort() != counts.sort():
                for i in range(len(counts)):
                    if counts[i] == m:
                        mode.append(uniq[i])
            else:
                mode.append('-')
            if st == '1':
                print('Самая распространенная тема пары:', ', '.join(mode))
            elif st == '2':
                print('Самый распространенный корпус:', ', '.join(mode))
            elif st == '3':
                print('Самая распространенная аудитория:', ', '.join(mode))
            elif st == '4':
                print('Самое распространенное время начала пары:', ', '.join(mode))

    elif action == '5':
        print('Таблицы базы данных для сортировки данных:')
        table = ''
        check = 0
        while check == 0:
            print('''1 - Student
2 - Teacher
3 - Course
4 - Meeting''')
            table = input('Выберите цифру: ')
            if (table in '1234') and (len(table) == 1):
                check = 1
            else:
                print('Введите цифру правильно!')

        if table == '1':
            print('Столбцы базы данных для сортировки:')
            st = ''
            check = 0
            while check == 0:
                print('''1 - Name
2 - Surname
3 - Patronymic
4 - Age
5 - Institute
6 - Programme type''')
                st = input('Выберите цифру: ')
                if (st in '123456') and (len(st) == 1):
                    check = 1
                else:
                    print('Введите цифру правильно!')
            if (st == '1') or (st == '2') or (st == '3') or (st == '5') or (st == '6'):
                cursor.execute('SELECT ' + student[int(st)] + ' FROM Student')
                data = cursor.fetchall()
                data2 = []
                for i in data:
                    data2.append(i[0])
                data2.sort()
                print('\n'.join(data2))
            elif st == '4':
                cursor.execute('SELECT students_age FROM Student')
                data = cursor.fetchall()
                data2 = []
                for i in data:
                    data2.append(int(i[0]))
                data2.sort()
                for i in data2:
                    print(str(i))

        elif table == '2':
            print('Столбцы базы данных для сортировки:')
            st = ''
            check = 0
            while check == 0:
                print('''1 - Name
2 - Surname
3 - Patronymic
4 - Institute
5 - Department''')
                st = input('Выберите цифру: ')
                if (st in '12345') and (len(st) == 1):
                    check = 1
                else:
                    print('Введите цифру правильно!')
            cursor.execute('SELECT ' + teacher[int(st)] + ' FROM Teacher')
            data = cursor.fetchall()
            data2 = []
            for i in data:
                data2.append(i[0])
            data2.sort()
            print('\n'.join(data2))

        elif table == '3':
            cursor.execute('SELECT courses_name FROM Course')
            data = cursor.fetchall()
            data2 = []
            for i in data:
                data2.append(i[0])
            data2.sort()
            print('\n'.join(data2))

        elif table == '4':
            print('Столбцы базы данных для сортировки:')
            st = ''
            check = 0
            while check == 0:
                print('''1 - Topic
2 - House
3 - Room''')
                st = input('Выберите цифру: ')
                if (st in '123') and (len(st) == 1):
                    check = 1
                else:
                    print('Введите цифру правильно!')
            if (st == '1') or (st == '2'):
                cursor.execute('SELECT ' + meeting[int(st)] + ' FROM Meeting')
                data = cursor.fetchall()
                data2 = []
                for i in data:
                    data2.append(i[0])
                data2.sort()
                print('\n'.join(data2))
            elif st == '3':
                cursor.execute('SELECT meetings_room FROM Meeting')
                data = cursor.fetchall()
                data2 = []
                for i in data:
                    data2.append(int(i[0]))
                data2.sort()
                for i in data2:
                    print(str(i))


    else:
        GO = 0

    print('Действия с базой данных:')
    print('''1 - вывести данные
2 - добавить данные
3 - редактировать данные
4 - вывести статистику
5 - сортировать данные
Любой другой символ - выйти''')
    action = input('Выберите цифру: ')
    if (action not in '12345') or (len(action) != 1):
        GO = 0

print('Завершение работы')
