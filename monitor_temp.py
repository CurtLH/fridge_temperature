#!/usr/bin/env python

import RPi.GPIO as GPIO
from time import sleep
import ds18b20
import psycopg2
from datetime import datetime


# connect to the databse
conn = psycopg2.connect(database="postgres",
                        user="postgres",
                        password="apassword",
                        host="192.168.0.104")

conn.autocommit = True
cur = conn.cursor()

# create table
cur.execute("""CREATE TABLE IF NOT EXISTS apartment_fridge
               (id SERIAL PRIMARY KEY NOT NULL,
                datetime timestamp NOT NULL,
                sensor1 numeric,
                sensor2 numeric,
                sensor3 numeric)""")

# setup GPIO 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

# get temp sensors
sensors = ds18b20.get_sensors()

# read sensors on loop
while True:

    # read the sensors
    temps = ds18b20.read_multiple_sensors(sensors)

    # print temps to screen
    print(temps)

    # insert temps into database
    cur.execute("""INSERT INTO apartment_fridge
               (datetime, sensor1, sensor2, sensor3)
               VALUES (%s, %s, %s, %s)""", [datetime.now(), temps['sensor1'], temps['sensor2'], temps['sensor3']])

    # blink LED
    for i in range(0,10):
        GPIO.output(18, True)
        sleep(0.1)
        GPIO.output(18, False)
        sleep(0.1)

    # wait 30 seconds then do it again
    sleep(30)
