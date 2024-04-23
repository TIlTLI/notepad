
import datetime
import unittest

class Note:
    def __init__(self, memo, tags):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.datetime.now()

class Notebook:
    def __init__(self):
        self.notes = []
        self.note_id = 1

    def create_new_note(self, memo, tags):
        note = Note(memo, tags)
        self.notes.append({"id": self.note_id, "note": note})
        self.note_id += 1

    def search_notes(self, search_string):
        found_notes = []
        for note_entry in self.notes:
            note = note_entry["note"]
            if (
                search_string in note.memo
                or search_string in note.tags
                or search_string == str(note_entry["id"])
            ):
                found_notes.append({"id": note_entry["id"], "note": note})
        return found_notes

    def modify_note(self, note_id, memo, tags):
        for note_entry in self.notes:
            if note_id == note_entry["id"]:
                note_entry["note"].memo = memo
                note_entry["note"].tags = tags
                break

    def delete_note(self, note_id):
        for note_entry in self.notes:
            if note_id == note_entry["id"]:
                self.notes.remove(note_entry)
                break

    def sort_notes(self, criteria):
        self.notes.sort(key=lambda note_entry: note_entry["note"].creation_date)

class Menu:
    def __init__(self, notebook):
        self.notebook = notebook
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.delete_note,
            "6": self.sort_notes,
            "7": self.quit,
        }

    def display_menu(self):
        print(
            """
        Notebook Menu

        1. Show Notes
        2. Search Notes
        3. Add Notes
        4. Modify Notes
        5. Delete Note
        6. Sort Notes
        7. Quit
        """
        )

    def get_user_choice(self):
        choice = input("Enter an option: ")
        return choice

    def show_notes(self):
        for note_entry in self.notebook.notes:
            note = note_entry["note"]
            print(
                f'ID: {note_entry["id"]}, Memo: {note.memo}, Tags: {note.tags}, Created on: {note.creation_date}'
            )

    def search_notes(self):
        search_string = input("Enter the search string: ")
        found_notes = self.notebook.search_notes(search_string)
        for note_entry in found_notes:
            note = note_entry["note"]
            print(
                f'ID: {note_entry["id"]}, Memo: {note.memo}, Tags: {note.tags}, Created on: {note.creation_date}'
            )

    def add_note(self):
        memo = input("Enter the memo: ")
        tags = input("Enter the tags (comma separated): ").split(',')
        self.notebook.create_new_note(memo, tags)

    def modify_note(self):
        note_id = int(input("Enter the note ID: "))
        memo = input("Enter the new memo: ")
        tags = input("Enter the new tags (comma separated): ").split(',')
        self.notebook.modify_note(note_id, memo, tags)

    def delete_note(self):
        try:
            note_id = int(input("Enter the note ID to delete: "))
            self.notebook.delete_note(note_id)
        except ValueError:
            print("Invalid input. Please enter a valid note ID.")

    def sort_notes(self):
        self.notebook.sort_notes("date")
        print("Notes sorted by creation date.")

    def quit(self):
        print("Thank you for using the notebook!")
        exit(0)

if __name__ == "__main__":
    notebook = Notebook()
    menu = Menu(notebook)

    while True:
        menu.display_menu()
        choice = menu.get_user_choice()

        action = menu.choices.get(choice)
        if action:
            action()
        else:
            print("Invalid choice. Please try again.")

