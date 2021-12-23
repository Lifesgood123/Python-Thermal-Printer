#!/usr/bin/python

# Current time and temperature display for Raspberry Pi w/Adafruit Mini
# Thermal Printer.  Retrieves data from DarkSky.net's API, prints current
# conditions and time using large, friendly graphics.
# See forecast.py for a different weather example that's all text-based.
# Written by Adafruit Industries.  MIT license.
#
# Required software includes Adafruit_Thermal, Python Imaging and PySerial
# libraries. Other libraries used are part of stock Python install.
#
# Resources:
# http://www.adafruit.com/products/597 Mini Thermal Receipt Printer
# http://www.adafruit.com/products/600 Printer starter pack

from __future__ import print_function
from Adafruit_Thermal import *
import time, requests, json
current conditions = requests.get("wttr.in?T&0")
t = time.localtime()
forcast = requests.get("wttr.in?T1").text
current_and_morning = "\n".join([ i [0:32] for i in f.split('\n')][2:-3])
noon = "\n".join([ i [31:63] for i in f.split('\n')][8:-3])
evening = "\n".join([ i [62:94] for i in f.split('\n')][8:-3])
night = "\n".join([ i [93:125] for i in f.split('\n')][8:-3])



# Open connection to printer and print image
printer = Adafruit_Thermal("/dev/serial0", 19200, timeout=5)
printer.println(current_and_morning)
printer.println(noon)
printer.println(evening)
printer.println(night)
printer.feed(3)
