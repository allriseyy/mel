from mido import Message, MidiFile, MidiTrack, bpm2tempo

mid = MidiFile()
track = MidiTrack()
mid.tracks.append(track)

tempo = bpm2tempo(80)
track.append(Message('program_change', program=0, time=0))

# Define chord progression (Am, F, C, G)
chords = [
    [57, 60, 64],  # A minor
    [53, 57, 60],  # F major
    [48, 52, 55],  # C major
    [55, 59, 62]   # G major
]

# Add chords
for _ in range(2):  # repeat progression twice
    for chord_notes in chords:
        for note in chord_notes:
            track.append(Message('note_on', note=note, velocity=70, time=0))
        for note in chord_notes:
            track.append(Message('note_off', note=note, velocity=70, time=480))

# Add lead melody (C5–D5–E5…)
melody = [72, 74, 76, 74, 72, 71, 69, 71, 72, 74, 76, 77, 76, 74, 72, 71]
for note in melody:
    track.append(Message('note_on', note=note, velocity=90, time=120))
    track.append(Message('note_off', note=note, velocity=90, time=120))

mid.save("dreamy_indie_rnb_python.mid")
