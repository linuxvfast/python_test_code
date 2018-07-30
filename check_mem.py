#!/bin/env python3
import psutil
import math
def bytes2human(n):
    symbols = ('K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols,start=1):
        #prefix[s] = 1 << (i + 1) * 10
        #print(prefix[s])
        prefix[s] =  math.pow(1024,i)  #将单位换算成bytes
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value, s)
    return "%sB" % n

print(bytes2human(psutil.virtual_memory().total))
