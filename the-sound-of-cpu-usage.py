#!/usr/bin/env python

from midiutil import MIDIFile
import psutil


# CONFIGURATION

# Set the number of notes in the output MIDI file
midiLength = 120

# Set the output MIDI file's volume
volume = 100

# Set the output MIDI filename
outputFileName = "the-sound-of-cpu-usage.mid"

# Set the MIDI tempo
tempo = 120

# END OF CONFIGURATION


# Define the MIDI
MyMIDI = MIDIFile(1)
MyMIDI.addTempo(0, 0, tempo)

# Define clamp function
def clamp(n, smallest, largest): return max(smallest, min(n, largest))

# Loop for MIDI generation
for i in range(1, midiLength + 1):
	
	# MIDI Channel 1
	# Core 1 pitch
	# Core 3 note duration

	# Set pitch based on CPU Core 1 usage
	pitch = int(psutil.cpu_percent(interval=0.1, percpu=True)[0])+15

	# Set duration based on CPU Core 3 usage
	duration = clamp(round(int(psutil.cpu_percent(interval=0.1, percpu=True)[2])%3, 2), 0.2, 2.5)

	# Push note to channel 1 of the MIDI
	MyMIDI.addNote(0, 0, pitch, i, duration, volume)


	# MIDI Channel 2
	# Core 2 pitch
	# Core 4 note duration

	# Set pitch based on CPU Core 2 usage
	pitch = int(psutil.cpu_percent(interval=0.1, percpu=True)[1])+15

	# Set duration based on CPU Core 4 usage
	duration = clamp(round(int(psutil.cpu_percent(interval=0.1, percpu=True)[3])%3, 2), 0.2, 2.5)

	# Push note to channel 2 of the MIDI
	MyMIDI.addNote(0, 1, pitch, i, duration, volume)

	# Log completion percent
	print("Generating MIDI - " + str(round((i/midiLength)*100)) + "% complete")

# Save output MIDI file
with open(outputFileName, "wb") as output_file:
    MyMIDI.writeFile(output_file)

# Display output filename when done
print("MIDI generated as \'" + outputFileName + "\'")
