import unittest
from Lab4 import Notebook, Note

class TestNotebook(unittest.TestCase):
    def setUp(self):
        self.notebook = Notebook()

    def test_create_new_note(self):
        # Assumption: The note is added to the notebook if the length of the notebook's notes list increases by 1
        self.notebook.create_new_note("Test memo", ["tag1", "tag2"])
        self.assertEqual(len(self.notebook.notes), 1)

    def test_search_notes(self):
        # Assumption: The search function works correctly if it returns the note with the matching memo or tags
        self.notebook.create_new_note("Test memo", ["tag1", "tag2"])
        found_notes = self.notebook.search_notes("Test memo")
        self.assertEqual(found_notes[0]["note"].memo, "Test memo")

    def test_modify_note(self):
        # Assumption: The modify function works correctly if the note's memo and tags are updated
        self.notebook.create_new_note("Test memo", ["tag1", "tag2"])
        self.notebook.modify_note(1, "Modified memo", ["tag3", "tag4"])
        modified_note = self.notebook.notes[0]["note"]
        self.assertEqual(modified_note.memo, "Modified memo")
        self.assertEqual(modified_note.tags, ["tag3", "tag4"])

if __name__ == '__main__':
    unittest.main()