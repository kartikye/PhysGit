from subprocess import check_output
from os import system
import logging
logging.basicConfig(level=logging.INFO)

try:
	import gntp.notifier
except:
	pass	
import sys
import os
import LeapPython
import Leap
import time

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
				merge()
			else:
				swipe = Leap.SwipeGesture(gesture)

				if abs(swipe.direction[0]) > abs(swipe.direction[1]) and abs(swipe.direction[0]) > abs(swipe.direction[2]):
					
					if swipe.direction[0] < .5:
						stash()

				elif abs(swipe.direction[1]) > abs(swipe.direction[0]) and abs(swipe.direction[1]) > abs(swipe.direction[2]):
					
					if swipe.direction[1] < .5:
						commit()
				
				elif abs(swipe.direction[2]) > abs(swipe.direction[1]) and abs(swipe.direction[2]) > abs(swipe.direction[0]):
	
					if swipe.direction[2] > .5:
						pull()
	
					if swipe.direction[2] < .5:
						push()

def growlNotify(message):
	try:
		growl.notify(
			noteType = "New Messages",
			title = message,
			description = "",
			icon = "http://example.com/icon.png",
			sticky = False,
			priority = 1,
		)
	except:
		pass	

def say(message):
	try:
		system('say '+message)		
	except:
		pass

def merge():
	growlNotify("Merging")
	print "merge"
	print os.system('git merge')
	growlNotify("Merged")
	say('merged')

def stash():
	print "stash"
	print os.system('git stash')
	growlNotify("Stashed")
	say(stashed)

def commit():
	growlNotify("Committing")
	print "commit"
	print os.system('git add -A')
	print os.system('git commit -a -m "from my leap"')
	growlNotify("Commited")
	say('commited')

def push():
	growlNotify("Pushing")
	print "push"
	print os.system('git push')
	growlNotify("Pushed")
	say('pushed')

def pull():
	growlNotify("Pulling")
	print "pull"
	print os.system('git pull')
	growlNotify("Pulled")
	say('pulled')


def main():

	try:
		growl = gntp.notifier.GrowlNotifier(
			applicationName = "GIT",
			notifications = ["New Updates","New Messages"],
			defaultNotifications = ["New Messages"],
			hostname = "", # Defaults to localhost
			password = "" # Defaults to a blank password
		)
		growl.register()
	except:
		pass
		
	listener = LeapListener()
	controller = Leap.Controller()
	controller.add_listener(listener)
	while True:
		time.sleep(1)
	controller.remove_listener(listener)

if __name__ == '__main__':
	main()