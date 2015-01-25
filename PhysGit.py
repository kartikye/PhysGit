from subprocess import check_output
from os import system
import logging
logging.basicConfig(level=logging.INFO)

import gntp.notifier
import sys
import os
sys.path.insert(0, "C:\Users\Kartikye\Downloads\Leap_Motion_SDK_Windows_2.2.2\LeapDeveloperKit_2.2.2+24469_win\LeapSDK\lib")
#sys.path.insert(0, "/LeapSDK/lib")
import LeapPython
import Leap
import time

growl = gntp.notifier.GrowlNotifier(
	applicationName = "GIT",
	notifications = ["New Updates","New Messages"],
	defaultNotifications = ["New Messages"],
	hostname = "localhost", # Defaults to localhost
	password = "" # Defaults to a blank password
)
growl.register()

def growlNotify(message):
	growl.notify(
		noteType = "New Messages",
		title = message,
		description = "",
		icon = "http://example.com/icon.png",
		sticky = False,
		priority = 1,
	)

class LeapListener(Leap.Listener):
	def on_init(self, controller):
		controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
		controller.set_policy(Leap.Controller.POLICY_IMAGES)
		controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)
		print "Initialized"
		

	def on_connect(self, controller):
		print "Connected"
		controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
		controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)	

	def on_disconnect(self, controller):
		print "Disconnected"

	def on_exit(self, controller):
		print "Exited"

	def on_frame(self, controller):
		frame = controller.frame()

		for gesture in frame.gestures():

			if gesture.type == Leap.Gesture.TYPE_CIRCLE:
				growlNotify("Merging")
				print "merge"
				print os.system('git merge')
				growlNotify("Merged")
			else:
				swipe = Leap.SwipeGesture(gesture)

				if abs(swipe.direction[0]) > abs(swipe.direction[1]) and abs(swipe.direction[0]) > abs(swipe.direction[2]):
					if swipe.direction[0] < .5:
						print "stash"
						print os.system('git stash')
						growlNotify("Stashed")
				elif abs(swipe.direction[1]) > abs(swipe.direction[0]) and abs(swipe.direction[1]) > abs(swipe.direction[2]):
					if swipe.direction[1] < .5:
						growlNotify("Committing")
						print "commit"
						print os.system('git add -A')
						print os.system('git commit -a -m "from my leap"')
						system('say commit')
						growlNotify("Commited")
				elif abs(swipe.direction[2]) > abs(swipe.direction[1]) and abs(swipe.direction[2]) > abs(swipe.direction[0]):
					if swipe.direction[2] > .5:
						growlNotify("Pulling")
						print "pull"
						print os.system('git pull')
						system('say pull')
						growlNotify("Pulled")
					if swipe.direction[2] < .5:
						growlNotify("Pushing")
						print "push"
						print os.system('git push')
						system('say push, hellyeah!')
						growlNotify("Pushed")

def main():
	listener = LeapListener()
	controller = Leap.Controller()
	controller.add_listener(listener)
	while True:
		time.sleep(1)
	controller.remove_listener(listener)

if __name__ == '__main__':
	main()