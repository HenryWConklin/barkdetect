barkdetect is a Raspberry Pi based project to put a dog on Twitter. 
See http://henrywconklin.github.io/projects/2015/08/17/oliver-twitter.html for details.

**Requirements**

* [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis)
* [python-twitter](https://github.com/bear/python-twitter) 
* at 

**Installation**

Clone this repository into your home directory

`cd ~`

`git clone https://github.com/HenryWConklin/barkdetect`

If you do not clone into your home directory, or don't use the default user (pi) you will need to change some paths. Do a `grep "/home/pi/barkdetect" *` and change the matches to point to the barkdetect folder.

If you follow the instructions here, you do not need to follow the above instruction.

Move into the new barkdetect directory and Run the install script

`cd barkdetect`

`sudo ./install.sh`

This will download and install all the requirements and set up the cron jobs.

Reboot, and all the appropriate scripts should begin running in the background. Make sure your microphone is plugged in at startup or the recording script will crash. If it does crash, either restart the system, or restart the script with `./startup.py`.


