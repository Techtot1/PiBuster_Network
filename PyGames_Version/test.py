import pythonping


ping = str(pythonping.ping("speedtest.net",count=2,size=1024))
print(ping)
ping = ping[ping.index("ms")-5 : ping.index("ms"):1 ].strip()

