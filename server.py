from cmath import log
import datetime
from xmlrpc.server import SimpleXMLRPCServer
import xmlrpc.client
import os
import time
import asyncio




def bubbleSort(arr1):
    array = arr1
    n = len(array)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def additionoftwonumbers(first,last):
    time.sleep(3)
    return first+last

def asyadd(first,last):
    return first+last



server = SimpleXMLRPCServer(("localhost", 8000))
print("-----Listening on port 8000-----")
server.register_function(bubbleSort, "bubbleSort")
server.register_function(additionoftwonumbers, "additionoftwonumbers")
server.register_function(asyadd, "asyadd")
server.serve_forever()

