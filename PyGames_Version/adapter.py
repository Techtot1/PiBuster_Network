#!/usr/bin/python3
import subprocess

adapters = subprocess.Popen(['./adapter_check.sh'], stdout=subprocess.PIPE)
adapters_parse = adapters.communicate()[0]
#adapters_parse = adapters.split(" ")
print(adapters_parse) 