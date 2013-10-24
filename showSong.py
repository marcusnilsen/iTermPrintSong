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

# Binding iTunes and VLC
iTunes = SBApplication.applicationWithBundleIdentifier_("com.apple.iTunes")
VLC = SBApplication.applicationWithBundleIdentifier_("org.videolan.vlc")

# iTunes code:
# INT representing state
if (iTunes.playerState() == 1800426320):
	if iTunes.currentStreamTitle():
		# Print streaming name
		print "/me is listning to '" + iTunes.currentStreamTitle() + " [Stream: " + iTunes.currentTrack().name() + "]" + "' (iTunes/iTerm2)"
	else:
		# Local file:
		print "/me is listning to '" + iTunes.currentTrack().artist() + " - " + iTunes.currentTrack().name() + "' (iTunes/iTerm2)"

# VLC code:
elif VLC.playing(): 
	print "/me is listning to '" + VLC.nameOfCurrentItem() + "' (VLC/iTerm2)"
else: 
	print "/echo Not playing enything (VLC/iTunes)"
