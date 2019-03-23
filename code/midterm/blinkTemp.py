#import libraries
import RPi.GPIO as GPIO
import Adafruit_DHT
import time
import os
import sqlite3

#Assign GPIO pins
motion1Pin = 13
motion2Pin = 25
#---------------------------------------------------------------------

#initialize GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(motion1Pin, GPIO.IN)
GPIO.setup(motion2Pin, GPIO.IN)
#SQLite stuff
motionDb = sqlite3.connect('../../log/motions.db')
motionCursor = motionDb.cursor() #Get cursor

motionDb.commit() #commite the stuffs
#motionCursor.execute('''CREATE TABLE recorded(time TEXT, people INT)''')

#Assign variables
people = 0
#call oneBlink function
try:
	while True:

		time.sleep(10)
		if (GPIO.input(motion1Pin)) :
			print("true")
#			time.sleep(10)
#			if (GPIO.input(motion2Pin)) :
#				people = people + 1
#		if (GPIO.input(motion2Pin)) :
#			if (GPIO.input(motion1Pin)) :
#				people = people - 1

		currentTime = time.strftime("%Y-%m-%d %H:%M:%S") 
#		motionCursor.execute('''INSERT INTO recorded(time, people) VALUES(?,?)''', (currentTime, people))
#		motionDb.commit()
#		rows = motionCursor.execute('''SELECT * FROM recorded''')
		os.system('clear')
#		for row in rows:
#			print('{0} : {1}'.format(str(row[0]), row[1],))
#clear shell, print goodbyes, and clean up GPIO
except KeyboardInterrupt:
	os.system('clear')
	print('Thanks for Blinking and Thinking!')
	GPIO.cleanup()
	motionDb.close()
