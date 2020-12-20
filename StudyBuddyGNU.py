# Study Buddy For Linux
# R.
# 2020-12-19
# Requirements
# https://gitea.com/chopin42/countdown > pip install countdown-timer

import random
from countdown import countdown

a = []
with open("topics.txt", "r") as f:
  a = f.readlines()
print("Let's study, how about?:",random.choice(a)),
input("Press Enter to Start timer")
countdown(30),
import subprocess as s
s.call(['notify-send','Finished!, Well done, have a Good Day!'])