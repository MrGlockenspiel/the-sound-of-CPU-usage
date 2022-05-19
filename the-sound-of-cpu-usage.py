#!/usr/bin/env python3

import psutil
from yaml import parse
from midiutil import MIDIFile
from midi2audio import FluidSynth
import argparse
import os

# Default Values

# Set the number of notes in the output MIDI file
midiLength = 120

# Set the output MIDI file's volume
volume = 100

# Set the output MIDI filename
outputFileName = "the-sound-of-cpu-usage.mid"

# Set the MIDI tempo
tempo = 120
	
# Set the number of MIDI tracks
midiTrackCount = psutil.cpu_count()

# Argument parsing
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--length", help = "MIDI length in notes", type=int)
parser.add_argument("-t", "--tracks", help = "Number of MIDI tracks", type=int)
parser.add_argument("-T", "--tempo", help = "MIDI tempo", type=int)
parser.add_argument("-v", "--volume", help = "MIDI volume", type=int)
parser.add_argument("-o", "--output", help = "Output file name", type=str)
parser.add_argument("-c", "--convert-to-mp3", help = "Convert MIDI to MP3", type=bool)
args = parser.parse_args()

# Check arguments and set values
if args.length:
    midiLength = args.length
if args.tracks:
    midiTrackCount = args.tracks
if args.tempo:
    tempo = args.tempo
if args.volume:
    volume = args.volume
if args.output:
    outputFileName = args.output
convert = args.convert_to_mp3

# Define the MIDI info
MyMIDI = MIDIFile(midiTrackCount)
MyMIDI.addTempo(0, 0, tempo)

for i in range(0, midiTrackCount):
	print("Core #"+str(i+1))
	MyMIDI.addTrackName(i, 0, "Core #"+str(i+1))

# Define clamp function
def clamp(n, smallest, largest):
	return max(smallest, min(n, largest))

def genNote(pitch_core, duration_core, track):
	# pitch_core    = CPU core to use for note pitch
	# duration_core = CPU core to use for note duration
	# channel       = MIDI channel for note
	# track         = MIDI track for note
	
	# Set pitch based on CPU core usage
	pitch = int(psutil.cpu_percent(interval=0.1, percpu=True)[pitch_core])+15

	# Set duration based on CPU core usage
	duration = clamp(round(int(psutil.cpu_percent(interval=0.1, percpu=True)[duration_core])%3, 2), 0.2, 2.5)

	# Push note to channel of the MIDI
	MyMIDI.addNote(track, 0, pitch, i, duration, volume)

# Loop for MIDI generation
for i in range(1, midiLength + 1):
	
	# Generate notes
	for a in range(0, midiTrackCount):
		if (a < midiTrackCount-1):
			genNote(a, a+1, a)
		else:
			genNote(0, midiTrackCount-1, midiTrackCount-1)

	# Log completion percent
	print("Generating MIDI - " + str(round((i/midiLength)*100)) + "% complete")

# Save output MIDI file
with open(outputFileName, "wb") as output_file:
    MyMIDI.writeFile(output_file)

# Display output filename when done
print("MIDI generated as \'" + outputFileName + "\'")

# If MP3 conversion is enabled, convert MIDI to MP3
if convert:
	print("Converting MIDI to MP3...")
	FluidSynth().midi_to_audio(outputFileName, outputFileName.replace(".mid", ".mp3"))
	os.remove(outputFileName)
	print("MP3 generated as \'" + outputFileName.replace(".mid", ".mp3") + "\'")