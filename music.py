
import pretty_midi

# Create a PrettyMIDI object
midi = pretty_midi.PrettyMIDI()

# Instruments (GarageBand-compatible General MIDI numbers)
# Acoustic Grand Piano = 0
# Acoustic Guitar (nylon) = 24
# Electric Bass (finger) = 33
# Pad 2 (warm) = 89

# Create instruments
piano = pretty_midi.Instrument(program=0)       # Soft chords
guitar = pretty_midi.Instrument(program=24)     # Main dreamy rhythm
bass = pretty_midi.Instrument(program=33)       # Soulful bass
pad = pretty_midi.Instrument(program=89)        # Ambient background

# Define tempo
bpm = 75
qn = 60.0 / bpm  # quarter note duration

# Chord progression: C - Am - F - G (standard romantic)
chords = [
    ['C4', 'E4', 'G4'],
    ['A3', 'C4', 'E4'],
    ['F3', 'A3', 'C4'],
    ['G3', 'B3', 'D4']
]

melody = [
    ['E4', 'G4', 'C5', 'E5'],   # In my eyes
    ['C4', 'E4', 'A4', 'C5'],   # she's a beautiful girl
    ['A3', 'C4', 'F4', 'A4'],   # with a heavenly smile
    ['B3', 'D4', 'G4', 'B4'],   # got me falling for her
    ['E4', 'F4', 'G4', 'E4'],   # every day
    ['C4', 'D4', 'E4', 'G4'],   # now my world is complete
    ['A3', 'B3', 'C4', 'E4'],   # just you and me
    ['G3', 'A3', 'B3', 'D4'],   # you will be all that I need
]

# Function to add notes
def add_notes(inst, notes, start, duration, velocity):
    for pitch in notes:
        note_num = pretty_midi.note_name_to_number(pitch)
        note = pretty_midi.Note(velocity=velocity, pitch=note_num,
                                start=start, end=start + duration)
        inst.notes.append(note)
        start += duration
    return start

# Add chords and pad
time = 0.0
for i, chord_notes in enumerate(chords * 2):  # 8 bars total
    for note_name in chord_notes:
        note_num = pretty_midi.note_name_to_number(note_name)
        ch_note = pretty_midi.Note(velocity=50, pitch=note_num,
                                   start=time, end=time + 4 * qn)
        piano.notes.append(ch_note)
        pad.notes.append(ch_note)
    time += 4 * qn

# Add bass line
time = 0.0
bass_roots = ['C2', 'A1', 'F1', 'G1'] * 2
for root in bass_roots:
    note_num = pretty_midi.note_name_to_number(root)
    bass_note = pretty_midi.Note(velocity=70, pitch=note_num,
                                 start=time, end=time + 4 * qn)
    bass.notes.append(bass_note)
    time += 4 * qn

# Add lead melody
time = 0.0
for phrase in melody:
    time = add_notes(guitar, phrase, time, qn, velocity=85)

# Add all instruments to MIDI
midi.instruments.append(piano)
midi.instruments.append(guitar)
midi.instruments.append(bass)
midi.instruments.append(pad)

# Save the MIDI file
midi.write("yungkai_dreamy_rnb_chorus.mid")
print("MIDI file saved as yungkai_dreamy_rnb_chorus.mid")
