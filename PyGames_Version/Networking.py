#!/usr/bin/python3
import pythonping
import speedtest
import iperf3

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
    speedtestinit()
    s.download()
    res = s.results.dict()
    return int(res["download"])/1000000 

#
def speedtest_upload():
    speedtestinit()
    s.upload()
    res = s.results.dict()
    return int(res["upload"])/1000000 
#
def speedtest_latency(times):
    ping = []
    for i in range(0,times):
        ping_cur = str(pythonping.ping("speedtest.net",count=2,size=1024))
        ping.append(ping_cur[ping_cur.index("ms")-5 : ping_cur.index("ms"):1].strip())
    #print(ping)

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