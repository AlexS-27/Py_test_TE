import unittest
from notes import ajouter_note, moyenne_notes, note_max, note_min

class TestNotes(unittest.TestCase):

    def test_ajout_note_valide(self):
        notes = []
        notes = ajouter_note(notes, 5)
        self.assertEqual(len(notes), 1)
        self.assertEqual(notes[0], 5)

    def test_ajout_note_invalide_negatif(self):
        notes = []
        notes = ajouter_note(notes, -1)
        self.assertEqual(len(notes), 0)

    def test_ajout_note_invalide_sup6(self):
        notes = []
        notes = ajouter_note(notes, 8)
        self.assertEqual(len(notes), 0)

    def test_moyenne(self):
        notes = [3, 4, 6]
        self.assertEqual(moyenne_notes(notes), 4)

    def test_moyenne_liste_vide(self):
        notes = []
        self.assertEqual(moyenne_notes(notes), 0)

    def test_note_max(self):
        notes = [3, 4, 6]
        self.assertEqual(note_max(notes), 6)

    def test_note_min(self):
        notes = [3, 4, 6]
        self.assertEqual(note_min(notes), 3)

if __name__ == "__main__":
    unittest.main()