import time
import os
import smbus
import RPi.GPIO as GPIO


bus = smbus.SMBus(1)

GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN,pull_up_down=GPIO.PUD_UP)


# function to shut down Pi
def Int_shutdown(channel):  
	# wait ten seconds
	time.sleep(5)      
	# shutdown Raspberry Pi if power is still down
	if (GPIO.input(4) == False):
		os.system("sudo shutdown -h now")
	
	return
	
	
#start I2C communication to disable hardware reset from I/O Module
out_values = [0x00]
bus.write_i2c_block_data(0x1C ,0,out_values)

#add interrupt 
GPIO.add_event_detect(4, GPIO.FALLING, callback = Int_shutdown, bouncetime = 2000)   
	
# do nothing while waiting for power failure
while 1:
	time.sleep(1)
