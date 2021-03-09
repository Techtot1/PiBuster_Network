#!/usr/bin/python3
import subprocess
import os
import json
from random import getrandbits

def Onstart():
    os.remove(os.getcwd()+"/Interfaces.json")
    os.remove(f"{os.getcwd()}/Interfaces_orgin.json")
def Adapters():
    
    if os.name == "nt":
        adapters = ("wlan0","eth0","eth1","eth2","ed","esh1","oog") 
        
    else:    
        adapters_NoParse = subprocess.Popen(['./adapter_check.sh'],shell=True, stdout=subprocess.PIPE, universal_newlines=True)
        adapters_NoParse = adapters_NoParse.communicate()[0]
        adapters = adapters_NoParse.strip("\n")
        adapters = adapters.split(" ")

    #adapters_parse = adapters.split(" ")
    
    return adapters

def connection():
    return("connected")
def Json_update(Var,File):
    json_pre = json.dumps(Var, indent=4)

    with open(File, "w+") as Json_OUT_file:
        Json_OUT_file.write(json_pre)
        Json_OUT_file.close()
def get_status():
    adatps = Adapters()
    json_out = {}

    Onstart()
    if os.name == "nt":
        for i in adatps:
            if "wlan" in i:
                json_out[i] = True
            else:
                json_out[i] = bool(getrandbits(1))
        
    else:
        for i in adatps:
            if "wlan" in i:
                json_out[i] = True
                subprocess.run(f"ifconfig {i} up")
            else:
                if "yes" in subprocess.run([f'ethtool {i} |& grep "Link detected: "'],shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]:
                    json_out[i] = True
                elif "no" in subprocess.run([f'ethtool {i} |& grep "Link detected: "'],shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]: 
                    print()
    Json_update(json_out,f"{os.getcwd()}/Interfaces.json")
    Json_update(json_out,f"{os.getcwd()}/Interfaces_orgin.json")    


def toggle(Adapter):
    
    with open(os.getcwd()+"/Interfaces.json","r+") as Adapters_status_get:
        Adapters_status = json.load(Adapters_status_get)

    if os.name == "nt":
        if Adapters_status[Adapter] == True:
            print(f"{Adapter} Toggled to False")
            Adapters_status[Adapter] = False
            Json_update(Adapters_status,f"{os.getcwd()}/Interfaces.json")
            return False
        elif Adapters_status[Adapter] == False:
            print(f"{Adapter} Toggled to True")
            Adapters_status[Adapter] = True
            Json_update(Adapters_status,f"{os.getcwd()}/Interfaces.json")
            return True

    else:
        if Adapters_status[Adapter] == True:
            print(f"{Adapter} Toggled to False")
            Adapters_status[Adapter] = False
            Json_update(Adapters_status,f"{os.getcwd()}/Interfaces.json")
            
            subprocess.run([f'sudo ifconfig {Adapter} down"'],shell=True)
            return False
        elif Adapters_status[Adapter] == False:
            print(f"{Adapter} Toggled to True")
            Adapters_status[Adapter] = True
            Json_update(Adapters_status,f"{os.getcwd()}/Interfaces.json")
            
            subprocess.run([f'sudo ifconfig {Adapter} up"'],shell=True)
            return True
def adapter_stop(Adapter):
    with open(os.getcwd()+"/Interfaces.json","r+") as Adapters_status_get:
        Adapters_status = json.load(Adapters_status_get)
    if os.name == "nt":
        print(f"{Adapter} Turned off")
        Adapters_status[Adapter] = False
        Json_update(Adapters_status,f"{os.getcwd()}/Interfaces.json")
    else:
        print(f"{Adapter} Turned Off")
        subprocess.run([f'sudo ifconfig {Adapter} down"'],shell=True)
        return

def adapter_reset():
    with open(f"{os.getcwd()}/Interfaces_orgin.json") as In_org:
        interfaces = json.load(In_org)
    Json_update(interfaces,f"{os.getcwd()}/Interfaces.json")
    if os.name == "nt":
        for i in interfaces:
            if interfaces[i] == False:
                print(f"{i} Is down")
            else:
                print(f"{i} is up")
    else:
        for i in interfaces:
            if interfaces[i] == False:
                subprocess.run([f'sudo ifconfig {i} down"'],shell=True)
            else:
                subprocess.run([f'sudo ifconfig {i} down"'],shell=True)

def get_cur_status(Adapter):
    with open(os.getcwd()+"/Interfaces.json","r+") as Adapters_status_get:
        Adapters_status = json.load(Adapters_status_get)
        if Adapters_status[Adapter] == True: return True
        else:return False
        
    

        
