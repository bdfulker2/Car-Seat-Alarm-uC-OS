#import smtplib       #email lib in email_ip_address() 
#from email.MIMEMultipart import MIMEMultipart #for email
#from email.MIMEText import MIMEText           #for email
import sys           #sys
import os            #os
import random
import urllib        #url lib in check_internet_connect()
import time          #time
import socket
#import bluetooth     #bluetooth lib used in main()
import Adafruit_GPIO.SPI as SPI     #display and pi
import Adafruit_SSD1306             #display lib
from PIL import Image      #for display
from PIL import ImageDraw  #for display
from PIL import ImageFont  #for display
#from bluetooth.ble import DiscoveryService

#Raspi Pi Pin Config
RST = 24    # on the PiOLED this pin isn't used
#note the following are only used with SPI
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

# below sets display and display pins from downloaded lib
disp = Adafruit_SSD1306.SSD1306_128_64(
    rst=RST, 
    dc=DC, 
    spi=SPI.SpiDev(
        SPI_PORT, 
        SPI_DEVICE, 
        max_speed_hz=8000000
        )
    )

disp.begin()        #display begin

time.sleep(1)

disp.clear()                #clear display
disp.display()              #display the display
width = disp.width          #set width to display width
height = disp.height        #set height to display height
image = Image.new('1', (width, height)) #create image 
draw = ImageDraw.Draw(image)#draw the image from above

font = ImageFont.load_default()     #set display font

v_status = False 
cs_status = False 
t_status = False

def Client():
    status = False                                             #set local status to false
    #create socket AF_INET refers to ipv4 and SOCK_STREAM means connection is TCP
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #
    try:
        #client.connect(('0,0,0,0', 8080))
        client.connect(('10.0.0.55', 6000))     #connect to server ip on port 6000
    except:
        print_oled("Connection", "to Server", "Failed", False) #print to oled
        print_oled("System", "Shut", "down", False) 
        print "Connection with server failed"            #print console
        print("Shut down")
        raise SystemExit()  
     
    client.send("Server Start\n")           #send start command to server

    from_server = client.recv(4096)         #receive data from server
    if(from_server == "True"):              #if from server is "True"
        status = True                       #assign status to True
    else:                                   #else from_server = "False"
        status = False                      #assign status to False
    client.close()                          #socket close
                                            #print to console
    print "return value from server = " + from_server      
    return status                           #return bool status value


#Timer() uses time library to sleep for 1 second on each iteration counting down
#from 29.
#parameter: int my_timer tells the timer weather its a horn timer or
def Timer(my_timer):
    for sec in range(29,0,-1):             
        time.sleep(1)

        if(my_timer == 1):
            print_oled("Time Left = ", str(sec), " seconds.", True)
            print(str(sec))
        else:
            print_oled("Horn on ", str(sec), " seconds.", True)
            print("Horn Timer = " + str(sec))
    return True
  

#Starts the horn and calls the timer() to countdown 30 seconds and terminates the horn
def Horn():
    print_oled("", "Horn On" , "" , False)
    print("Horn on")
    Timer(2)
    print_oled("", "Horn Off" , "" , False)
    print("Horn off")
    

#method for printing to the oled screen. Sets parameters and creates 3 lines of text
def print_oled(line_one, line_two, line_three, no_sleep):
    draw.rectangle((0, 0, width, height), outline=0, fill = 0)
    draw.text((0, 12), line_one, font=font, fill=255)
    draw.text((0, 24), line_two, font=font, fill=255)
    draw.text((0,36), line_three, font=font, fill=255)
            
    disp.image(image)
    disp.display()
    if no_sleep == False:
        time.sleep(5)
    return

#main method __init__
#parameter: bool vehicle. Passed on/off ignition status of the vehicle
def __init__(vehicle): 
      

    if(vehicle == False):
        print_oled("Vehicle", "Turned", "off", False)         #print oled
        print("Vehicle " + " Turned" +" off")                 #print console
    else:
        print_oled("Vehicle", "Still", "On", False)           #print oled
        print_oled("System", "Shut", "down", False)           #print oled
        print("Vehicle " + " Still" +" On")                   #print console
        print("Shut down")                                    #print console
        raise SystemExit()                           #system shutdown if vehichle is on
    
    if(Client()):        
        t_status = Timer(1)
        print("t_status = " + str(t_status))
    else:
        print_oled("Car Seat", "Was", "Unoccupied", False)    #print oled
        print_oled("System", "Shut", "down", False) 
        print("Car Seat " + " Was" +" Unoccupied")            #print console
        print("Shut down")
        raise SystemExit()                          #system shutdown if vehichle is on
    
    if(t_status):
        cs_status = Client()      #2nd call to Client() to check if car seat is occupied

    if(cs_status):                                         
        t_status = False                                      #reset t_status
        Horn()                                                
    else:
        print_oled("Car Seat", "Is Now", "Unoccupied", False) #print oled
        print_oled("System", "Shut", "down", False)
        print("Car Seat " + " Is Now" +" Unoccupied")         #print console
        print("Shut down")                          #system shutdown if vehichle is on
    
    disp.clear()                                              #clear disply
    disp.display()

__init__(False)
