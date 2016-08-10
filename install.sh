
#Prereqs
sudo apt-get update
sudo apt-get install at
sudo pip install twitter

git clone https://github.com/tyiannak/pyAudioAnalysis

#Crontab setup: append new commands to crontab
(crontab -l ; cat barkdetect.crontab) | crontab -


