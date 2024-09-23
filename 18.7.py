import random
from types import new_class

# список учеников
students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
# отсортируем список учеников
students.sort()
# список предметов
classes = ['Математика', 'Русский язык', 'Информатика']
# пустой словарь с оценками по каждому ученику и предмету
students_marks = {}
# сгенерируем данные по оценкам:
# цикл по ученикам
for student in students:  # 1 итерация: student = 'Александра'
    students_marks[student] = {}  # 1 итерация: students_marks['Александра'] = {}
    # цикл по предметам
    for class_ in classes:  # 1 итерация: class_ = 'Математика'
        marks = [random.randint(1, 5) for i in range(3)]  # генерируем список из 3х случайных оценок
        students_marks[student][class_] = marks  # students_marks['Александра']['Математика'] = [5, 5, 5]
# выводим получившийся словарь с оценками:
for student in students:
    print(f'''{student}
            {students_marks[student]}''')

print('''
        Список команд:
        1. Добавить оценки ученика по предмету
        2. Вывести средний балл по всем предметам по каждому ученику
        3. Вывести все оценки по всем ученикам
        4. Выход из программы
        ''')

while True:
    command = int(input('Введите команду: '))
    if command == 1:
        print('1. Добавить оценку ученику по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # если данные введены верно
        if student in students_marks.keys() and class_ in students_marks[student].keys():
            # добавляем новую оценку для ученика по предмету
            students_marks[student][class_].append(mark)
            print(f'Для {student} по предмету {class_} добавлена оценка {mark}')
        # неверно введены название предмета или имя ученика
        else:
            print('ОШИБКА: неверное имя ученика или название предмета')
    elif command == 2:
        print('2. Вывести средний балл по всем предметам по каждому ученику')
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                # находим сумму оценок по предмету
                marks_sum = sum(students_marks[student][class_])
                # находим количество оценок по предмету
                marks_count = len(students_marks[student][class_])
                # выводим средний балл по предмету
                print(f'{class_} - {marks_sum // marks_count}')
            print()
    elif command == 3:
        print('3. Вывести все оценки по всем ученикам')
        # выводим словарь с оценками:
        # цикл по ученикам
        for student in students:
            print(student)
            # цикл по предметам
            for class_ in classes:
                print(f'\t{class_} - {students_marks[student][class_]}')
            print()
    elif command == 4:
        print('4. Удалить оценку ученика по предмету')
        # считываем имя ученика
        student = input('Введите имя ученика: ')
        # считываем название предмета
        class_ = input('Введите предмет: ')
        # считываем оценку
        mark = int(input('Введите оценку: '))
        # удаляем выбранную оценку
        del students_marks
        print(f'Для {student} по предмету {class_} удалена оценка {mark}')
        # неверно введены название предмета или имя ученика
    elif command == 5:
        print('4. Удалить ученика из списка')
        # считываем имя ученика
        end_student = input('Введите имя ученика: ')
        if end_student in students:
            # выводим список оставшихся учеников
            students.remove(end_student)
            # удаляем ученика
            print(f':{students}')
        print('Этого ученика нет в списке')
    elif command == 6:
        print('6. Добавить нового ученика в список:')
        # выводим список всех учахщихся
        students = ['Аполлон', 'Ярослав', 'Александра', 'Дарья', 'Ангелина']
        # вводим имя нового ученика
        new_student = input('Введите имя нового ученика: ')
        students.append(new_student)
        print('Новый ученик добавлен')
        # выводим весь список учащихся
        print(f':{students}')
    elif command == 7:
        print('7. Добавить новый предмет:')
        # выводим список всех предметов
        classes = ['Математика', 'Русский язык', 'Информатика']
        # вводим наименование нового предмета
        new_class = input('Введите название нового предмета: ')
        classes.append(new_class)
        print('Новый предмет добавлен')
        # выводим список всех предметов
        print(f':{classes}')
    elif command == 8:
        print('8. Вывод информации по всем оценкам для определенного ученика:')
        student = input("Введие имя ученика: ")
            # цикл по предметам
        for class_ in classes:
            # выводим оценки ученика
            print(f'\t{class_} - {students_marks[student][class_]}')
        print()
    elif command == 9:
        print('9. Вывод среднего балла по каждому предмету для определенного ученика.')
        student = input("Введие имя ученика: ")
        # цикл по предметам
        for class_ in classes:
            # находим сумму оценок по предмету
            marks_sum = sum(students_marks[student][class_])
            # находим количество оценок по предмету
            marks_count = len(students_marks[student][class_])
            # выводим средний балл по предмету
            print(f'{class_} - {marks_sum // marks_count}')
        print()
    elif command == 10:
        print('10. Выход из программы')
        break
