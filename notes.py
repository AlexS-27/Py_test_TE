def ajouter_note(liste_notes, note):
    if note < 0:
        return liste_notes
    liste_notes.append(note)
    return liste_notes

def moyenne_notes(liste_notes):
    total = sum(liste_notes)
    return int(total / len(liste_notes))

def note_max(liste_notes):
    return max(liste_notes)

def note_min(liste_notes):
    return min(liste_notes)