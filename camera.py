#!/usr/bin/python
import os, sys
import ctypes
KIPR=ctypes.CDLL("/usr/lib/libkipr.so")
    
MODE = 0
# 0 = search 
# 1 = drivin to the color
# 2 = grip the color 

hasColor = 0

found = 0
    
greifSuccess = 0
    
COLOR = 10
    
def modeChange():
	global MODE, greifSuccess, found, hasColor
	if hasColor == 1:
		MODE = 1
		hasColor = 0
	if found == 1:
		print("GEHT")
		KPIR.msleep(10000)
		MODE = 2
		found = 0
	if greifSuccess == 1:
		MODE = 0
		greifSuccess = 0
    
def greif():
	global MODE,greifSuccess
	if MODE!=2:
		return
	greifSuccess = 1

def findColor():
	global MODE, hasColor, COLOR
	if MODE !=0:
		return

	see_red = 0
	see_green = 1
	see_blue = 2
           
            
	if KIPR.get_object_count(see_red) > 0:
		COLOR = 0
		hasColor = 1
        
	if KIPR.get_object_count(see_green) > 0:
		COLOR = 1
		hasColor = 1
        
	if KIPR.get_object_count(see_blue) > 0:
		COLOR = 2
		hasColor = 1

	else:
		KIPR.create_drive_direct(50, -50)
	
   
def searchObject(color):
	global MODE, found
	KIPR.camera_update()
	if MODE!=1:
		return
            
	elif KIPR.get_object_count(color) > 0:  							 
		x = KIPR.get_object_center_x(color, 0)
		y = KIPR.get_object_center_y(color, 0)
		if x < 65:
			KIPR.create_drive_direct(-25, 25)
		elif y > 100:
			KIPR.create_drive_direct(0,0)
			found = 1
			return found
		elif x > 80:
			KIPR.create_drive_direct(25, -25)
		else:
			KIPR.create_drive_direct(150, 150)
		print(x,y)
                  
                    
def main():
	global COLOR

	KIPR.camera_open()
	KIPR.create_connect()
	KIPR.create_full()
        
	while KIPR.a_button() == 0:
		findColor()
		modeChange()
		searchObject(COLOR)
		greif()


	KIPR.camera_close()
                
if __name__== "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(),"w",0)
    main();

