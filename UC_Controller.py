import smtplib       #email lib in email_ip_address()
from email.MIMEMultipart import MIMEMultipart #for email
from email.MIMEText import MIMEText           #for email
import sys           #sys
import os            #os
import random
import urllib        #url lib in check_internet_connect()
import time          #time
import bluetooth     #bluetooth lib used in main()
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

time.sleep(3)

disp.clear()                #clear display
disp.display()              #display the display
width = disp.width          #set width to display width
height = disp.height        #set height to display height
image = Image.new('1', (width, height)) #create image 
draw = ImageDraw.Draw(image)#draw the image from above

font = ImageFont.load_default()     #set display font
ellipsis = ".   "           
count = 0                   #initialize count to 0

v_status = False 
cs_status = False 
t_status = False

def bool Client():
    return True


def Timer(my_timer):
    for sec in range(29,0,-1):
        time.sleep(1)
        
        if(my_timer == 1):
            #print_oled("Time Left = ", str(sec), " seconds.", True)
            print(str(sec))
        else:
            #print_oled("Horn on ", str(sec), " seconds.", True)
            print("Horn Timer = " + str(sec))
    return True
  


def Horn():
    #print_oled("", "Horn On" , "" , False)
    print("Horn on")
    Timer(2)
    #print_oled("", "Horn Off" , "" , False)
    print("Horn off")
    


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

#The check_internet_connect method try's to check if there is Wi-Fi connection 
#to a specified URL to verify that it is connect to the internet 
def check_internet_connect(macAddress):   #method to check internet connection
    try:
        url = "https://www.google.com/"     #using google.com as url to test
        urllib.urlopen(url)                 #uses urllib to open a url
        status = "Connected"                #assign status = connected
    except urllib2.URLError, e:             #exception URLError
        status = "Not connected"            #if url error status = not connected
    
    print status                            #print status to console
    if  (status == "Connected"):            #if status is still connected
        mail_mac_address(macAddress)        #call to mail_mac_address
                                            #with parameter of macAddress
    return


def __init__(vehicle): 
      

    if(vehicle == False):
        #print_oled("Vehicle", "Turned", "off", False)
        print("Vehicle " + " Turned" +" off")
    else:
        #print_oled("Vehicle", "Still", "On", False)
        #print_oled("System", "Shut", "down", False)
        print("Vehicle " + " Still" +" On")
        print("Shut down")
        raise SystemExit()
    
    if(Client()):
        t_status = Timer(1)
        print(str(t_status))
    else:
        #print_oled("Car", "Still", "On", False)
        #print_oled("System", "Shut", "down", False)
        print("Vehicle " + " Still" +" On")
        print("Shut down")
        raise SystemExit()
    
    if(t_status):
        cs_status = Client()

    if(cs_status):
        t_status = False
        Horn()

__init__(False)