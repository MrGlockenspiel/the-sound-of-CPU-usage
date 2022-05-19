# The Sound of CPU Usage
What does CPU usage sound like? Like this, apparently. <br>
To be honest, it doesn't sound that bad.

Also 69 SLOC ( ͡° ͜ʖ ͡°)

## What is this

This is a Python script that uses your current CPU usage to generate beautiful sounds for your listening pleasure.

## How to use

You will need `midiutil` and `psutil`, which can be installed using 
`pip install MIDIUtil` and `pip install psutil` respectively.

Then just run the script with `./the-sound-of-cpu-usage.py`.

After you run the script, you will find a file named `the-sound-of-cpu-usage.mid` in the current directory. <br>
The default name for this file can be changed by changing the `outputFileName` variable on line 16 of the script. <br>
(Command line options and possibly MP3 output coming soon!) <br>

## ~~Bugs~~ Features:

 - If your CPU is too good, you may just get a lot of low notes in a row. The lesson? Get a worse computer, nerd.

## FAQ

#### Why did you do this
Yes.

