barkdetect is a Raspberry Pi based project to put a dog on Twitter. 
See http://henrywconklin.github.io/projects/2015/08/17/oliver-twitter.html for details.

**Requirements**
* [pyAudioAnalysis](https://github.com/tyiannak/pyAudioAnalysis)
* [python-twitter](https://github.com/bear/python-twitter) (`sudo pip install twitter` works)
* at (`sudo apt-get install at`)

**Installation**
Clone pyAudioAnalysis and this repository. Change the paths in the lines in process.sh:

`homedir=/home/pi/barkdetect/`

and

`python /home/pi/libs/python/pyAudioAnalysis/audioAnalysis.py classifyFolder...`

to the absolute paths of this repository and pyAudioAnalsysis/audioAnalysis.py respectively.

Also change the paths in atjob.txt, barkdetect.crontab, and startup.sh. If your username happens to be pi and you clone to your home directory, these paths will already be correct.

Copy the contents of barkdetect.crontab to your crontab file (`crontab -e`).

