title_list = []

title = input('Введите заголовок заметки: ')

while title != '':
    title_list.append(title)
    title = input('Введите следующий заголовок (или оставьте пустым для завершения): ')
    for value in title_list:
        while value == title:
            print('Данный заголовок есть в списке заголовков.')
            title = input('Введите следующий заголовок (или оставьте пустым для завершения): ')

print(title_list)
