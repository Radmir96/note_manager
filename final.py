note = []

username = input('Введите имя пользователя: ')
title1 = input('Введите первый заголовок заметки: ')
title2 = input('Введите второй заголовок заметки: ')
title3 = input('Введите третий заголовок заметки: ')
content = input('Введите описание заметки: ')
status = input('Введите статус заметки: ')
created_date = input('Введите дату создания заметки в формате "дд-мм-гггг": ')
issue_date = input('Введите дату истечения заметки в формате "дд-мм-гггг": ')

title_list = []
title_list.append(title1)
title_list.append(title2)
title_list.append(title3)

note = [username, content, status,created_date, issue_date, title_list]

print(f"Имя пользователя: {note[0]}.")
print(f"Заголовоки заметок: {note[5]}.")
print(f"Описание заметки: {note[1]}.")
print(f"Статус заметки: {note[2]}.")
print(f"Дата создания заметки: {note[3][:5]}.")
print(f"Дата истечения заметки: {note[4][:5]}.")