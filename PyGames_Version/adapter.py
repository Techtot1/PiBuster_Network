#!/usr/bin/python3
import subprocess
import os
def Adapters():
    
    if os.name == "nt":
        adapters = ("wlan0","eth0","eth1","eth2","ed","esh1","esh2") 
        
    else:    
        adapters_NoParse = subprocess.Popen(['./adapter_check.sh'],shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
        adapters = adapters_NoParse.strip("\n")
        adapters = adapters.split(" ")

    #adapters_parse = adapters.split(" ")
    
    return adapters

def connection():
    return("connected")

 
#sudo ifconfig wlan0 up
