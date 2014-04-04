# Laundry Machine Monitor with Arduino, Python, Heroku and Firebase

Author: [Desmond Duggan](http://www.desmondrduggan.com)

The days of walking down four flights of stairs with a full load of laundry only to be let down once again by the busy rumbling of occupied laundry machines are over. **For Free.**In this project, we used the following technologies to build an online-accessible monitor for the washing machine in our home. 

In short, the Arduino board outputs a signal to its usb serial port, which is observed by a scheduled python script. This python script uses a python-firebase wrapper to make a REST call to update an entry in the Firebase. Simultaneously, the Heroku hosted static Rack application listens to any updates made to the Firebase and updates the page asynchronously. 

## Technologies

**Washing Machine**

- [Arduino Uno](http://www.arduino.cc/)
- [Python - Firebase](https://github.com/ozgur/python-firebase) - thanks Ozgur
- PySerial
- APScheduler
- Ubuntu OS

**Web**

- [Ruby Rack](http://rack.github.io/)
- [Firebase](https://www.firebase.com/)
- [Heroku](https://www.heroku.com/)
- Bundle
- Bootstrap :)

**Pre-reqs**

1. Create a Heroku Account
2. Create a Firebase account

## Overview

![Overview](https://raw2.github.com/drduggan/Arduino_Laundry_Machine/master/image.png)

Attach the Arduino to the washing machine and hook it up to the Ubuntu machine. Once the Arduino script is uploaded to the unit, run the readArduino.py script to update the firebase url. Then, upload the index.html file and supporting structure to a free Heroku dyno. 

## Arduino

Assemble the [Arduino Uno](http://arduino.cc/en/Main/ArduinoBoardUno) and an accelerometer like the [ADXL345](https://www.sparkfun.com/products/9836). Attach to the washing machine and link to machine running Ubuntu. Install the Arduino IDE and upload the script. 

## Python Script
	
	$ pip install apscheduler
	$ pip install pyserial
	$ pip install python-firebase
	
Adjust the name of the serial port to the value of the port being used for the Arduino board - will be a USB port. Insert the address of your Firebase.  Run it. 

## Heroku and Web
We used a magical tool developed by Marshall Huss located [here](http://herokustaticmagico.herokuapp.com/) to auto generate a static site framework in Rack with instructions on how to upload to Heroku. Rack is a lightweight static site framework written in Ruby. 

	$ pip install bundle
	$ pip install heroku
	$ gem install rack
	
Steps:

3. Make a Firebase
1. Download the package from the link above
2. Unpack and bundle install
3. Heroku Create
4. git add .
5. git commit -m "Initial Commit"
6. git push heroku master
7. git shit done





This is a collaborative project between [Andrew Ng](https://github.com/andrewng1023), Ben Huang and [Desmond Duggan](https://github.com/drduggan). 
