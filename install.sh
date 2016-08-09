if [ "`whoami`" !=  "root" ]; then
    echo "Error: Must be run as root"
    exit 1
fi

#Prereqs
apt-get install at
pip install twitter

git clone https://github.com/tyiannak/pyAudioAnalysis

#Crontab setup: append new commands to crontab
(crontab -l ; cat barkdetect.crontab) | crontab -


