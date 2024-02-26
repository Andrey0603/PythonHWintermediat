import json
import os
from datetime import datetime

notes_file = "notes.json"

def save_notes(notes):
    with open(notes_file, "w") as file:
        json.dump(notes, file)

def load_notes():
    if os.path.exists(notes_file):
        with open(notes_file, "r") as file:
            return json.load(file)
    return []

def add_note(title, message):
    notes = load_notes()
    note = {
        "id": len(notes) + 1,
        "title": title,
        "message": message,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    notes.append(note)
    save_notes(notes)
    print("Заметка успешно добавлена.")

def read_notes(date_filter=None):
    notes = load_notes()
    if date_filter:
        filtered_notes = [note for note in notes if date_filter in note["timestamp"]]
        notes = filtered_notes
    for note in notes:
        print(f'ID: {note["id"]}, Заголовок: {note["title"]}, Сообщение: {note["message"]}, Время: {note["timestamp"]}')

def edit_note(note_id, title, message):
    notes = load_notes()
    for note in notes:
        if note["id"] == note_id:
            note["title"] = title
            note["message"] = message
            note["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_notes(notes)
            print("Заметка успешно отредактирована.")
            return
    print("Заметка с указанным ID не найдена.")

def delete_note(note_id):
    notes = load_notes()
    notes = [note for note in notes if note["id"] != note_id]
    save_notes(notes)
    print("Заметка успешно удалена.")