#!/bin/python3
import speedtest
import time 
from colorama import Fore, init
init()
for i in range(1,15):
    time.sleep(1)
    print(i)

s = speedtest.Speedtest()


s.get_servers()
s.get_best_server()
s.download()


res = s.results.dict()
Results = int(res["download"])/1000000
if Results > 100:
    print("{0}The cable good for Gbps with results of {1} down".format(Fore.GREEN,Results))
else: 
    print("{0}The cable is less than Gbps with results of {1} down".format(Fore.RED,Results))

