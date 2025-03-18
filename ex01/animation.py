#!/usr/bin/python3

import time
from time import sleep

def typing(string):
   for c in string:
      time.sleep(10000/1000000)
      print(c, end="", flush=True)
   print("")

def lining(string_arr):
   for line in string_arr:
      time.sleep(100000/1000000)
      print(line)