#!/usr/bin/python3
import pythonping
import speedtest
import iperf3
import threading
from subprocess import call
from adapter import Adapters

def speedtestinit():
    print()
    global s 
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server() 


def iperfInit():
    print()

#
def speedtest_download():
    print()
#
def speedtest_upload():
    print()
#
def speedtest_latency():
    print()
#
def speedtest_cabletest():
    print()

#
def iperf_download():
    print()
#
def iperf_upload():
    print()
#
def iperf_latency():
    print()
#
def iperf_cabletest():
    print()

#
def google_ping():
    print()
#
def ewen_ping():
    print()



def wifi_toggle():
    print()

def ethernet_toggle():
    print()
    # for reference when using call rc = call("./sleep.sh")

def display_ip():
    print()