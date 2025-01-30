def valid_input_status(status, options):
    '''
    Забирает текущий статус выполнения заметки status и сравнивает с корректными
    вариантами заметок options. Возвращает True если заметка есть в списке,
    False если заметки нет в списке.
    '''
    if status in options:
        return True
    else:
        return False
status_options = ['выполнено', 'в процессе', 'отложено']
# Есть словарь с данными о заметке пользователя
note = {'username': 'Радмир',
        'content': 'ДЗ по второму модулю',
        'status': 'в процессе',
        'created_date': '29-01-2025',
        'issue_date': '31-01-2025',
        'title_list': ['Grade1', 'Этап2', 'Задание2']}

#Сохраняем текущий статус пользователя в переменную
status = note['status']

print(f"Текущий статус заметки:{status}.")

status = input('Введите новый статус: ')

if status in status_options:
    print('Статус заметки успешно обновлен!')
    print(f'Текущий статус: {status}.')
else:
    print('Вы ввели неверный статус')