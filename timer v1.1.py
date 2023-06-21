#This is a timer made with reference to this blog post: https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html
#This uses some of the code from the section titled "A simple countdown timer"
#This code has been modifed by myself to include a title uing pyfiglet (when it works lol), an end sound using winsound, and the ability
#to repeat the console app without having to launch it again.
#Posted for my convenience but feel free to use it - most of this isn't mine anyway lmao - Steven

import time
import datetime
import winsound
#import pyfiglet

def countdown(h, m, s):
	total_s = h * 3600 + m * 60 + s

	
	while total_s > 0:

		timer = datetime.timedelta(seconds = total_s)

		print(timer, end="\r")

		time.sleep(1)

		total_s -= 1

		while total_s == 0:
			print("Time is up!")
			winsound.PlaySound('ringtone.wav', winsound.SND_FILENAME)
			total_s = -1

while True:
	#pyfiglet.print_figlet("Timer", colors='GREEN')
	print("Timer")
	print("Slapped together by Steven")
	h = input("Enter the time in hours: ")
	m = input("Enter the time in minutes: ")
	s = input("Enter the time in seconds: ")
	countdown(int(h), int(m), int(s))
	total_s = 0

	if total_s == 0:
		repeat = input("Start again? y/n ")

		if repeat.lower() != "y":
    			break

