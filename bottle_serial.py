import serial
import sys
from bottle import response,route,run

try:
    ser = serial.Serial('/dev/tty.usbmodem1411',9600)
except OSError:
    ser = False
except:
    print sys.exc_info()[0]

@route('/arduino')
def arduino():
    if ser:
        ser.write("1")
    response.set_header('Access-Control-Allow-Origin','*')
    return "Arduino!"

run(host="localhost",port=8946,debug=True)
