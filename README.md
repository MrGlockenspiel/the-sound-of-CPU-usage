# The Sound of CPU Usage
What does CPU usage sound like? Like this, apparently. <br>
To be honest, it doesn't sound that bad.

## What is this

This is a Python script that uses your current CPU usage to generate beautiful sounds for your listening pleasure.

## How to use

You will need `midiutil` and `psutil`, which can be installed using 
`pip install MIDIUtil` and `pip install psutil` respectively.

Then just run the script with `python3 the-sound-of-cpu-usage.py`.

After you run the script, you will find a file named `the-sound-of-cpu-usage.mid` in the current directory. <br>
The default name for this file can be changed by changing the `outputFileName` variable on line 16 of the script. <br>
(Command line options and possibly MP3 output coming soon!) <br>

## ~~Bugs~~ Features:

 - If your CPU is too good, you may just get a lot of low notes in a row. The lesson? Get a worse computer, nerd.
 - The script does not write to different MIDI tracks, even though it's supposed to, it just places them end to end on the same track.

## FAQ

#### Why are there so many comments and newlines? Your style is terrible!
I usually don't write like that, I swear! <br>
I usually have no comments! (cry about it) <br>
But uhhhhhhhh... <br>

Check the line count ( ͡° ͜ʖ ͡°) <br>

#### Why did you do this
Yes.

