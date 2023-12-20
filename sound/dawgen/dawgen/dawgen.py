# dawgen.py

# project imports
from Models import MidiNote
import piano_constants

# typings
from typing import List

# 3rd party imports
import mido

def midi_sound(notes: List[MidiNote]) -> mido.MidiFile:
    if not all(isinstance(note, MidiNote) for note in notes):
        raise TypeError('All notes must be instances of MidiNote')

    # Create a new MIDI file
    mid = mido.MidiFile()
    track = mido.MidiTrack()
    mid.tracks.append(track)

    # Set the tempo
    track.append(mido.MetaMessage('set_tempo', tempo=600000))  # Adjust the tempo value as needed

    # Set the time signature
    track.append(mido.MetaMessage('time_signature', numerator=6, denominator=8, clocks_per_click=24, notated_32nd_notes_per_beat=8))  # Adjust the time signature values as needed

    # Set the key signature
    track.append(mido.MetaMessage('key_signature', key='C'))  # Adjust the key signature value as needed

    # Add notes to track
    for note in notes:
        track.append(note.to_mido_message())

    track.append(mido.MetaMessage('end_of_track'))

    # return mid
    return mid

def play_mid(mid: mido.MidiFile) -> None:
    # Play the MIDI file
    with mido.open_output() as port:
        for message in mid.play():
            port.send(message)

if __name__ == "__main__":
    #Test the module plays sounds.  Functionaly play "Mary Had a Little Lamb"
    notes = [piano_constants.E4, piano_constants.D4, piano_constants.C4, piano_constants.D4, piano_constants.E4, piano_constants.E4, piano_constants.E4, piano_constants.D4, piano_constants.D4, piano_constants.D4, piano_constants.E4, piano_constants.E4, piano_constants.E4, piano_constants.E4, piano_constants.D4, piano_constants.C4]
    midi_notes = []
    
    for note in notes:        
        midi_notes.append(MidiNote("note_on", note[0], note[2], 60))
    
        midi_notes.append(MidiNote("note_off", note[0], note[2], 100))

    play_mid(midi_sound(midi_notes))