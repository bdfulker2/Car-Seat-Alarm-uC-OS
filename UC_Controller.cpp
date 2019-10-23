/*
 * This project is for a car seat alarm system. This software will communicate
 * over WiFi 802.11g with a simulated car seat device (Rasberry Pi Zero W) the 
 * car seat device (server) will return the car seats occupied status. If the 
 * car seat is occupied a count down timer will begin. Upon its expiration
 * this software will again connect to the car seat device to see if the car
 * seat is still occupied. Upon receiving that it is still occupied a simulated 
 * horn will be printed to the Micro-controller display to simulate output to a
 * cars horn.  
 */

/* 
 * File:   main.cpp
 * Author: Ben Surface Book
 *
 * Created on October 23, 2019, 8:53 AM
 */


////////////// Area for uC MicroController hardware initialization ////////////



////////////////////////////////////////////////////////////////////////////////

#include <cstdlib>
#include <iostream>

#include <stdlib.h>
#include <string>
#include <sstream>
#include <ctime>
#include <chrono>
#include <windows.h>
#include <thread>
bool v_Status = false, cs_Status = false, t_Status = false;


using namespace std;

bool Client() {
    return true;  //for testing change when
}

bool Timer() {
    
    for(int sec = 29; sec>=0; sec--) {
        //Sleep(1000);
        cout << "\t" << sec;
    }
    
    return true;
}

void Horn() {
    cout << "Horn On";
    if(Timer() == true) {
        cout << "Horn Off";
    }
    
}
/*
 * 
 */
int main(int argc, char** argv) {
    argc = 2;
    if(argc < 2) {
        printf("Not enough arguments");
        exit(1);
    }
    //for testing purposes
    argv[1] = "false";
    
    if(argv[1] == "false") {
        v_Status = false;
    } else {
        v_Status = true;
    }
    
    printf("%s\n", argv[1]);
    cout << v_Status;
    cout << "\n";
    
    
    if (v_Status) {
        printf("The car is still running system exit");
        exit(0);
    }
    
    //////////////// change after client is created////////////////////////////
    
    
    if(Client()) {
        t_Status = Timer();
        cout << t_Status;
    } else {
        cout << "Car Seat is not occupied system exit";
        exit(0);
    }
    
    if(t_Status) {
        cs_Status = Client();
    } 
    
    if(cs_Status) {
        t_Status = false;
        Horn();
    }
    
    exit(0);
}





