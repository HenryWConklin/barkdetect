#!/usr/bin/env python
import scipy.io.wavfile
import sys
from scipy import signal
import matplotlib.pyplot as plt
import numpy

# Segment size needs to be at least as long as the rising edge of a bark
# and no longer than the gap between two barks. 2500 works reasonably well
SEG_SIZE = 2500


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Takes one filename argument"
        sys.exit(1)

    # (freq, sound data)
    soundFile = scipy.io.wavfile.read(sys.argv[1])
    
    # Group the audio data into segments
    segments = [SEG_SIZE * i for i in range(len(soundFile[1]) // SEG_SIZE)]
    segments = segments + [len(soundFile[1])]
    
    sndSegs = [soundFile[1][segments[i]:segments[i+1]] for i in range(len(segments)-1)]
    
    for i in range(len(sndSegs)):
        sndSegs[i] = [abs(x) for x in sndSegs[i]]
    
    # Define the volume of the segment as the maximum amplitude
    # within that segment
    vol = [max(x) for x in sndSegs]

    # Split the audio file into clips along spikes between two segments'
    # volumes. Barks tend to increase in volume over at least two segments
    # so don't clip again until it stops rising.
    sndStart = 0
    rising = False
    clips = []
    for i in range(len(vol)-1):
        if not rising and vol[i] * 2 < vol[i+1]:
            if sndStart != 0:
                clips = clips + [soundFile[1][segments[sndStart]:segments[i]]]
            sndStart = i
            rising = True
        elif rising:
            if vol[i] > vol[i+1]:
                rising = False
    
    # Add the last clip
    clips = clips + [soundFile[1][segments[sndStart]:]]
    
    # Save each clip
    for i, clip in enumerate(clips):
        scipy.io.wavfile.write("barkClips/{}_{:d}.wav".format(sys.argv[1][sys.argv[1].find("snd"):sys.argv[1].find(".wav")], i), soundFile[0], clip)
        

