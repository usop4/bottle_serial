import serial
from bottle import response,route,run

ser = serial.Serial('/dev/tty.usbmodem1411',9600)

@route('/arduino')
def arduino():
    ser.write("1")
    response.set_header('Access-Control-Allow-Origin','*')
    return "Arduino!"

run(host="localhost",port=8946,debug=True)
