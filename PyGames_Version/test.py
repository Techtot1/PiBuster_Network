import Networking


#ping = str(pythonping.ping("speedtest.net",count=2,size=1024))
#print(ping)
#ping = ping[ping.index("ms")-5 : ping.index("ms"):1 ].strip()
ping = Networking.speedtest_latency(12)
print(ping)
print(f"{round(sum(ping)/len(ping),2)} ms")
if input("Expand?: ").lower() == 'yes':
    ([print(f"{items} ms") for items in ping]) 


