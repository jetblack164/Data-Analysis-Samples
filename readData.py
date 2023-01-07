import serial
import time
import numpy as np
import pandas as pd
#serialPort = serial.Serial(
#    port="COM7", baudrate=9600, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE
#)
#This code is not part of the exercise. It merely shows how the data was collected.
serialPort = serial.Serial('/dev/cu.usbserial-0001',baudrate=115200)
serialString = ""

final_data=[]
dataPoints=3*10**2
n=0
t_0=time.time_ns()
final_data=np.zeros((dataPoints,4))
while n < dataPoints:
    if serialPort.in_waiting > 0:

        serialString = serialPort.readline()
        
        try:

            data=serialString.decode("Ascii")
            data=data.split()
            
            #data.append(time.time_ns())
            #data.append((time.time_ns()-t_0)* 10**(-9))
            #it is generally ill-advised to make construct nparrays this way. However due to convenience I have chosen to do it this way.  
            final_data[n,0]=data[0]
            final_data[n,1]=data[1]
            final_data[n,2]=data[2]
            final_data[n,3]=data[3]
            n=n+1
            
        except:
            pass    


print(np.array(final_data))

pd.DataFrame(np.array(final_data)).to_csv("results.csv",index=None)