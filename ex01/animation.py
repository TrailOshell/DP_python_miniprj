#!/usr/bin/python3

import time
import color

def usleep(val):
   time.sleep(val/1000000)

def typing(string, val=5000, clr="", end="\n"):
   if clr:
      print(f"{clr}", end="")
   for c in string:
      usleep(val)
      print(c, end="", flush=True)
   if clr != "":
      print(f"{color.style.reset}", end="")
   print(end=end)

def lining(string_arr, val=100000):
   for line in string_arr:
      usleep(val)
      print(line)