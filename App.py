from Main import add_note, read_notes, edit_note, delete_note

def print_menu():
    print("Выберите действие:")
    print("1. Добавить заметку")
    print("2. Просмотреть заметки")
    print("3. Редактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

while True:
    print_menu()
    user_choice = input("Введите номер действия: ")

    if user_choice == "1":
        title = input("Введите заголовок заметки: ")
        message = input("Введите тело заметки: ")
        add_note(title, message)
    elif user_choice == "2":
        date_filter = input("Введите дату (гггг-мм-дд) для фильтрации (если нет нажмите Enter): ")
        read_notes(date_filter)
    elif user_choice == "3":
        note_id = int(input("Введите ID заметки для редактирования: "))
        title = input("Введите новый заголовок заметки: ")
        message = input("Введите новое тело заметки: ")
        edit_note(note_id, title, message)
    elif user_choice == "4":
        note_id = int(input("Введите ID заметки для удаления: "))
        delete_note(note_id)
    elif user_choice == "5":
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите номер действия из списка.")