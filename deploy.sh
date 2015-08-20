#!/bin/bash

cd /home/pi/barkdetect/

# Pull the code from the git repository
git pull

# Update cron jobs, taken from:
# http://stackoverflow.com/questions/2367824/storing-crontab-file-inside-my-project
test -f barkdetect.crontab && { { crontab -u pi -l | awk '/^#BEGIN BARKDETECT/{hide=1;next}/^#END BARKDETECT/{hide=0;next}!hide{print}' ; echo '#BEGIN BARKDETECT' ; cat barkdetect.crontab ; echo '#END BARKDETECT' ; } | crontab -u pi -; }


cd /
