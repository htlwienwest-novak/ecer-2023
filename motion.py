#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")

def servoUnten():
	KIPR.set_servo_position(1, 1900)
	KIPR.set_servo_position(0, 150)
	print("UNTEN")
def servoMitte():
	KIPR.set_servo_position(1, 1024)
	KIPR.set_servo_position(0, 1024)
	print("MITTE")
def servoOben():
	KIPR.set_servo_position(1, 150)
	KIPR.set_servo_position(0, 1900)
	print("OBEN")
def main():
	KIPR.enable_servos()
	
	while 1:
		servoMitte()
		KIPR.msleep(4000)
		servoUnten()
		KIPR.msleep(4000)
		servoOben()
		KIPR.msleep(4000)
            
	KIPR.disable_servos()

if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();
