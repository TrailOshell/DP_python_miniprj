#!/usr/bin/python3

import time

def usleep(val):
   time.sleep(val/1000000)

def typing(string, val=5000, end="\n"):
   for c in string:
      usleep(val)
      print(c, end="", flush=True)
   print("", end=end)

def lining(string_arr, val=100000):
   for line in string_arr:
      usleep(val)
      print(line)