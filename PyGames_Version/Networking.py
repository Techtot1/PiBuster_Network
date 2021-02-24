import pythonping
import speedtest
import iperf3
import threading



def speedtestinit():
    print()
    global s 
    s = speedtest.Speedtest()
    s.get_servers()
    s.get_best_server() 


def iperfInit():
    print()

def connection():
    print(pythonping.ping("google.ca",count=1,))


def speedtest_download():
    print()

def speedtest_upload():
    print()

def speedtest_latency():
    print()

def speedtest_cabletest():
    print()


def iperf_download():
    print()

def iperf_upload():
    print()

def iperf_latency():
    print()

def iperf_cabletest():
    print()

def google_ping():
    print()

def ewen_ping():
    print()


