#!/usr/bin/python3
import subprocess

def Adapters():
    adapters_NoParse = subprocess.Popen(['./adapter_check.sh'],shell=True, stdout=subprocess.PIPE, universal_newlines=True).communicate()[0]
    adapters = adapters_NoParse.strip("\n")
    adapters = adapters.split(" ")

    #adapters_parse = adapters.split(" ")
    return adapters
