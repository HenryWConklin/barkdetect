#!/bin/bash

# Takes one filename parameter

rm barkClips/*.wav
./barkSplit.py $1

classes=`python -m pyAudioAnalysis.audioAnalysis classifyFolder -i barkClips/ --model knn --classifier knnBarkType --details`

barkString=""
while read -r line; do
    # Only append to barkstring if it is a line with a classification
    # and not the summary at the bottom of the file
    if [[ $line == *".wav"* ]]; then
	barkString="$barkString ${line: -4}"	
    fi
done <<< "$classes"

#Strip the leading space
barkString=${barkString:1}

echo "$barkString"



