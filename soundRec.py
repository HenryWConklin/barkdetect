#!/usr/bin/env python

# Modified from:
# http://stackoverflow.com/questions/892199/detect-record-audio-in-python

# Records distinct sounds and discards intermittent silences

from sys import byteorder
from array import array
from struct import pack

import pyaudio
import wave
import os.path
import time

THRESHOLD = 1800
CHUNK_SIZE = 2048
FORMAT = pyaudio.paInt16
RATE = 48000
END_TIME = 50*1024

def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
    def _trim(snd_data):
        snd_started = False
        r = array('h')

        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)

            elif snd_started:
                r.append(i)
        return r

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in xrange(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in xrange(int(seconds*RATE))])
    return r

def record():
    """
    Record a word or words from the microphone and 
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the 
    start and end, and pads with 0.5 seconds of 
    blank sound to make sure VLC et al can play 
    it without getting chopped off.
    """

    print "Opening Stream"
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
                    frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False

    r = array('h')
    print "Waiting for sound"
    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        
        silent = is_silent(snd_data)

        if not silent and not snd_started:
            snd_started = True
            print "Sound started"
        
        if snd_started:
            r.extend(snd_data)
        
        if snd_started and silent:
            num_silent += 1
        elif snd_started:
            num_silent = 0

        if CHUNK_SIZE * num_silent > END_TIME:
            print "Sound ended"
            break
            
 

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    #r = trim(r)
    r = normalize(r)
    r = add_silence(r, .5)
    return sample_width, r

def record_to_file():
    "Records from the microphone and outputs the resulting data to 'path'"
    sample_width, data = record()
    data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open("snd_{}.wav".format(time.strftime("%Y%m%d_%H%M%S")), 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()



if __name__ == '__main__':
    
    while 1:
        record_to_file()
