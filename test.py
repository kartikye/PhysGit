from subprocess import check_output
import sys
import os
sys.path.insert(0, "C:\Users\Kartikye\Downloads\Leap_Motion_SDK_Windows_2.2.2\LeapDeveloperKit_2.2.2+24469_win\LeapSDK\lib")
import LeapPython
import Leap


controller = Leap.Controller();
controller.set_policy(Leap.Controller.POLICY_BACKGROUND_FRAMES)
controller.set_policy(Leap.Controller.POLICY_IMAGES)
controller.set_policy(Leap.Controller.POLICY_OPTIMIZE_HMD)
controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)

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
		elif abs(swipe.direction[1]) > abs(swipe.direction[0]) and abs(swipe.direction[1]) > abs(swipe.direction[2]):
			if swipe.direction[1] < .5:
				print "commit"
				print os.system('git add -A')
				print os.system('git commit')
		
		elif abs(swipe.direction[2]) > abs(swipe.direction[1]) and abs(swipe.direction[2]) > abs(swipe.direction[0]):
			if swipe.direction[2] > .5:
				print "pull"
				print os.system('git pull')
			if swipe.direction[2] < .5:
				print "push"
				print os.system('git push')	
		

		'''if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
			print "0hello"
			print os.system('git commit')
		elif gesture.type == Leap.Gesture.TYPE_KEY_TAP:
			print "bye"
			print check_output("git push")'''

