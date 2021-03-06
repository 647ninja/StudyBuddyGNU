# Program: Study Buddy For Linux
# Author: R.
# Original creation date: 2020-12-19
# Version: 2
# Updated: 2020-12-24

#!/usr/bin/env python3
import random
import time
import sys
import subprocess as s

def countdown(mins, secs=0):
    t = (mins*60) + secs
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        t -= 1

a = []
with open("topics.txt", "r") as f:
  a = f.readlines()
print("Let's study, how about?:",random.choice(a)),
input("Press Enter to Start timer")
countdown(30),
s.call(['notify-send','Well done!, Have a Great Day!']),print('\a')
