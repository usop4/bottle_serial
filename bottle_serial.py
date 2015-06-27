# -*- coding: utf-8 -*-

import serial
import sys
from bottle import response,route,run

try:
    ser = serial.Serial('/dev/tty.usbmodem1451',9600)
except OSError as (errno,strerror):
    if errno == 2 : # No such file or directory
        print "USB device is not connected"
    else:
        print errno, strerror
    ser = False
except:
    print sys.exc_info()[0]
    raise

@route('/arduino/<command>')
def arduino(command):
    response.set_header('Access-Control-Allow-Origin','*')
    if ser:
        ser.write(command)
        line = ser.readline()
        return line
    else:
        return "arduino is not connected"

run(host="localhost",port=8946,debug=True)
