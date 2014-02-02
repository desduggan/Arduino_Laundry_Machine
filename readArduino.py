import serial
import time

from firebase import firebase


port = serial.Serial('/dev/tty.usbmodemfa131', 9600)

base = firebase.FirebaseApplication("https://washubetalaundry.firebaseio.com", None)

while True:
    print port.read()
    status = port.read()

    if (status == "A"):
        base.patch("", {"machine_status":"in use"})
    elif (status == "F"):
        base.patch("", {"machine_status":"not in use"})
    else:
        print "ShIT"

    time.sleep(2)




# print port.name


port.close()