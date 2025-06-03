from midiutil import MIDIFile

midi = MIDIFile(1)
track = 0
time = 0
tempo = 135
midi.addTempo(track, time, tempo)

melody = [
    (69, 1, 0), (72, 0.5, 1), (76, 0.5, 1.5), (79, 2, 2),
    (77, 0.5, 4), (76, 0.5, 4.5), (72, 1, 5), (74, 0.5, 6), (69, 0.5, 6.5),
    (69, 1, 8), (71, 1, 9), (72, 0.5, 10), (76, 1.5, 10.5),
    (79, 0.5, 12), (76, 1, 12.5), (72, 1, 13.5), (69, 1, 14.5)
]

channel = 0
volume = 100

for pitch, duration, start_time in melody:
    midi.addNote(track, channel, pitch, start_time, duration, volume)

with open("yung_kai_blue_inspired_melody.mid", "wb") as output_file:
    midi.writeFile(output_file)
