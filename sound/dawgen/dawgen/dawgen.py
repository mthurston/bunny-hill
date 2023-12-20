from music21 import note, stream, midi

def play_mary_had_a_little_lamb():
    # Define the notes of the song
    notes = ['E4', 'D4', 'C4', 'D4', 'E4', 'E4', 'E4', 'D4', 'D4', 'D4', 'E4', 'G4', 'G4', 
             'E4', 'D4', 'C4', 'D4', 'E4', 'E4', 'E4', 'E4', 'D4', 'D4', 'E4', 'D4', 'C4']

    # Create a stream and add the notes to it
    melody = stream.Stream()
    for pitch in notes:
        melody.append(note.Note(pitch))

    # Play the stream
    sp = midi.realtime.StreamPlayer(melody)
    sp.play()

if __name__ == "__main__":
    play_mary_had_a_little_lamb()