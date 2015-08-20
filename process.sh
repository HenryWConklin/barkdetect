#!/bin/bash

# Filters sounds and schedules posts

# Project home directory
homedir=/home/pi/barkdetect/

# Classify sounds, writes class to ${homedir}classification.txt
python /home/pi/libs/python/pyAudioAnalysis/audioAnalysis.py classifyFolder -i ${homedir}samples --model knn --classifier ${homedir}knnBarkDetect --details > ${homedir}classification.txt

# Iterate over unfiltered samples
for filename in ${homedir}samples/snd*.wav
do
    # Find the classification of the current file
    res=`grep $filename < ${homedir}classification.txt`

    # Filter into appropriate file
    if [[ $res == *"barks"* ]]; then
	mv $filename ${homedir}samples/barks
    elif [[ $res == *"junk"* ]]; then
	mv $filename ${homedir}samples/junk
    fi
done

# Schedule a twitter post for each filtered bark, 
# delayed 10 minutes from original recording
for file in ${homedir}samples/barks/snd*.wav; do
    at -f ${homedir}atjob.txt `${homedir}getTimeFromFilename.py $file`
    mv $file ${homedir}samples/barks/processed
done
