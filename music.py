from midiutil import MIDIFile

midi = MIDIFile(4)
tempo = 97
track_names = ["Acoustic Guitar", "Strings Pad", "Electric Bass", "Percussion"]
channels = [0, 1, 2, 9]
programs = [24, 48, 33, None]
volumes = [100, 70, 80, 90]

for i, name in enumerate(track_names):
    midi.addTrackName(i, 0, name)
    midi.addTempo(i, 0, tempo)
    if programs[i] is not None:
        midi.addProgramChange(i, channels[i], 0, programs[i])

chords = [
    [64, 68, 71], [61, 64, 68], [57, 61, 64], [59, 62, 66]
]

for bar in range(4):
    start_time = bar * 2
    for i, note in enumerate(chords[bar]):
        midi.addNote(0, channels[0], note, start_time + i * 0.4, 1.5, volumes[0])

melody_notes = [64, 66, 68, 71, 68, 66, 64, 62]
for i, note in enumerate(melody_notes):
    midi.addNote(0, channels[0], note, 8 + i * 0.5, 1, 110)

for bar, chord in enumerate(chords * 2):
    for note in chord:
        midi.addNote(1, channels[1], note, bar * 2, 2, volumes[1])

bassline = [40, 37, 33, 35] * 2
for bar, note in enumerate(bassline):
    midi.addNote(2, channels[2], note, bar * 2, 2, volumes[2])

for i in range(16):
    time = i * 0.5
    if i % 4 == 0:
        midi.addNote(3, channels[3], 36, time, 0.25, volumes[3])
    elif i % 4 == 2:
        midi.addNote(3, channels[3], 38, time, 0.25, volumes[3])

with open("romantic_acoustic_full_arrangement.mid", "wb") as f:
    midi.writeFile(f)
