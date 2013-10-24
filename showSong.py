#!/usr/bin/python

# How to use:
#	1. Save this file somewhere on your disk
#	2. Set up iTerm2 to run a coprocess:
#		Preferences -> Keys -> Under 'Global Shortcut Key', bind a key:
#		Add (+), Shortcut: 		F5
#			 Action: 		Run Coprocess
#			 Add script path: 	python /path/to/the/script.py
#
#	Pressing F5 in a Irssi window show print the songs playing in the channel
#
#
#	by @marcusnilsen, 24.10.2013
#
# Importing Apple Script binding
from Foundation import *
from ScriptingBridge import *

# Process binding
Processes = SBApplication.applicationWithBundleIdentifier_("com.apple.systemevents")

# Set default song playing to none
playing = 0

for item in Processes.processes():
	# Listing processes to see if VLC/iTunes are running
	# to prevent them from starting if they are not currently running
	if item.bundleIdentifier() == 'org.videolan.vlc':
		VLC = SBApplication.applicationWithBundleIdentifier_("org.videolan.vlc")
		# VLC Code
		if VLC.playing():
			print "/me is listning to '" + VLC.nameOfCurrentItem() + "' (VLC/iTerm2)"
			playing = 1
	elif item.bundleIdentifier() == 'com.apple.iTunes':
		# iTunes Code
		iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
		# INT representing state
		if (iTunes.playerState() == 1800426320):
			playing = 1
			if iTunes.currentStreamTitle():
				# Print streaming name
				print "/me is listning to '" + iTunes.currentStreamTitle() + " [Stream: " + iTunes.currentTrack().name() + "]" + "' (iTunes/iTerm2)"
			else:
				# Local file:
				print "/me is listning to '" + iTunes.currentTrack().artist() + " - " + iTunes.currentTrack().name() + "' (iTunes/iTerm2)"

if not playing:
	print "/echo Not playing anything (VLC/iTunes)"

