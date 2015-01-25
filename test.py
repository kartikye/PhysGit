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

while True:
	frame = controller.frame()

	for gesture in frame.gestures():
		if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
			print "0hello"
			print os.system('git commit')
		elif gesture.type == Leap.Gesture.TYPE_KEY_TAP:
			print "bye"
			print check_output("git push")

