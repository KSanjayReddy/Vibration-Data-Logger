import serial
import csv
import sys
import time

UNO1 = '/dev/ttyUSB0'
UNO2 = '/dev/ttyUSB1'
arduino1 = serial.Serial(UNO1, 115200)
arduino2 = serial.Serial(UNO2, 115200)

myfile = open("test.csv",'wb')
wr = csv.writer(myfile, quoting = csv.QUOTE_ALL)
wr.writerow(["Name1","X1","Name2","X2"])

t_end = int(time.time()) + 16

print "\n \n THE SENSOR NEEDS TIME FOR INITIALISATION \n \n"
print "WAIT 15 SECONDS"
x = 13
while int(time.time()) < t_end:
    if t_end - int(time.time()) == x:
        print x
        x = x -1

    data1 = arduino1.readline()[:-2]
    data2 = arduino2.readline()[:-2]

count = 1
while True:
    try:
        if count:
            print "\n \n DATA LOGGER STARTED. Press Ctrl+C to Stop \n \n"
            count =0
        data1  = arduino1.readline()[:-2]
        data2  = arduino2.readline()[:-2]
        data_list1 = data1.split()
        data_list2 = data2.split()
        ls = data_list1 + data_list2
        wr.writerow(ls)
    except:
        print "YOUR DATA IS SAVED \n"
        print  "RUN graph.py TO VIEW THE RESPONSE GRAPH"
        sys.exit(0)
