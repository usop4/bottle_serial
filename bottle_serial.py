# -*- coding: utf-8 -*-

import serial
import sys
from bottle import response,route,run
import os

try:
    files = os.listdir('/dev')
    for file in files:
        if "tty.usbmodem" in file:
            ser = serial.Serial('/dev/'+file,9600)
            print file
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
    try:
        ser.write(command)
        #line = ser.readline()
        #return line
    except:
        print sys.exc_info()[0]
    return "success"

@route('/test')
def arduino():
    response.set_header('Access-Control-Allow-Origin','*')
    return "test"

if "usbmodem" in file:
    run(host="127.0.0.1",port=8946,debug=True)
else:
    print "failed"
