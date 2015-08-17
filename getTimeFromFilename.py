#!/usr/bin/env python

# Pulls the record time from a sound filename (file format is snd_YYYYMMDD_HHMMSS.wav)

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        exit(1)
    s = sys.argv[1]
    s = s[s.find("snd"):]
	
    # Get hour and minute parts of filename
    hour = int(s[13:15])
    minute = int(s[15:17])

    # Offset to compensate for the filter job scheduling
    minute += 11
    if minute >= 60:
        hour += 1
        hour %= 24
        minute %= 60

    print "{:02d}:{:02d}".format(hour,minute)
    
