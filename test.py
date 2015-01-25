from subprocess import check_output
from os import system
import logging
logging.basicConfig(level=logging.INFO)

# import gntp.notifier
import sys
import os
# sys.path.insert(0, "C:\Users\Kartikye\Downloads\Leap_Motion_SDK_Windows_2.2.2\LeapDeveloperKit_2.2.2+24469_win\LeapSDK\lib")
sys.path.insert(0, "/LeapSDK/lib")
import LeapPython
import Leap

import speech_recognition as sr


controller = Leap.Controller();
controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
controller.set_policy(Leap.Controller.POLICY_IMAGES)
controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)
controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

# growl = gntp.notifier.GrowlNotifier(
#     applicationName = "GIT",
#     notifications = ["New Updates","New Messages"],
#     defaultNotifications = ["New Messages"],
#     # hostname = "computer.example.com", # Defaults to localhost
#     # password = "abc123" # Defaults to a blank password
# )
# growl.register()

# r = sr.Recognizer()
# with sr.Microphone() as source: # use the default microphone as the audio source
# 	audio = r.listen(source) # listen for the first phrase and extract it into audio data

# audio = r.listen(source)
# # try:
# print("You said " + r.recognize(audio)) # recognize speech using Google Speech Recognition
# except LookupError: # speech is unintelligible
# 	print("Could not understand audio")


while True:
	frame = controller.frame()



	for gesture in frame.gestures():
		swipe = Leap.SwipeGesture(gesture)
		'''print swipe.direction[0]
		print swipe.direction[1]
		print swipe.direction[2] 
		print "\n"'''

		if abs(swipe.direction[0]) > abs(swipe.direction[1]) and abs(swipe.direction[0]) > abs(swipe.direction[2]):
			if swipe.direction[0] < .5:
				print "stash"
				print os.system('git stash')
				# growl.notify(
				# 	noteType = "New Messages",
				# 	title = "Stashed",
				# 	description = "Your Git was stashed",
				# 	icon = "http://example.com/icon.png",
				# 	sticky = False,
				# 	priority = 1,
				# )
		elif abs(swipe.direction[1]) > abs(swipe.direction[0]) and abs(swipe.direction[1]) > abs(swipe.direction[2]):
			if swipe.direction[1] < .5:
				# growl.notify(
				# 	noteType = "New Messages",
				# 	title = "Committing",
				# 	description = "Your Git is being committing",
				# 	icon = "http://example.com/icon.png",
				# 	sticky = False,
				# 	priority = 1,
				# )
				print "commit"
				print os.system('git add -A')
				print os.system('git commit -a -m "from my leap"')
				system('say commit')
				# growl.notify(
				# 	noteType = "New Messages",
				# 	title = "Commited",
				# 	description = "Your Git was commited",
				# 	icon = "http://example.com/icon.png",
				# 	sticky = False,
				# 	priority = 1,
				# )
		
		elif abs(swipe.direction[2]) > abs(swipe.direction[1]) and abs(swipe.direction[2]) > abs(swipe.direction[0]):
			if swipe.direction[2] > .5:
				# growl.notify(
				# 	noteType = "New Messages",
				# 	title = "Pulling",
				# 	description = "Your Git is being pulled",
				# 	icon = "http://example.com/icon.png",
				# 	sticky = False,
				# 	priority = 1,
				# )
				print "pull"
				print os.system('git pull')
				system('say pull')
				# growl.notify(
				# 	noteType = "New Messages",
				# 	title = "Pulled",
				# 	description = "Your Git was pulled",
				# 	icon = "http://example.com/icon.png",
				# 	sticky = False,
				# 	priority = 1,
				# )
			if swipe.direction[2] < .5:
				# growl.notify(
				# 	noteType = "New Messages",
				# 	title = "Pushing",
				# 	description = "Your Git is being pushed",
				# 	icon = "http://example.com/icon.png",
				# 	sticky = False,
				# 	priority = 1,
				# )
				print "push"
				print os.system('git push')
				system('say push, hellyeah!')
				# growl.notify(
				# 	noteType = "New Messages",
				# 	title = "Pushed",
				# 	description = "Your Git was pushed",
				# 	icon = "http://example.com/icon.png",
				# 	sticky = False,
				# 	priority = 1,
				# )
		

		'''if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
			print "0hello"
			print os.system('git commit')
		elif gesture.type == Leap.Gesture.TYPE_KEY_TAP:
			print "bye"
			print check_output("git push")'''

