UPDATE: I have made some minor changes to the setup and code, can now verify it does indeed run fine headless on a raspberry pi 1 and above.
-------------------------------


STEP 1: If you haven’t already, go to https://www.raspberrypi.com/software/operating-systems/ and download “Raspberry Pi OS”. Flash this to your SD card and setup as necessary. It isn't necessary to have the desktop version as we aren't logging into your Tesla account.

STEP 2: Once you are up and running, install the necessary packages by entering the following commands:

      sudo apt-get update
      sudo apt-get upgrade -y
      sudo apt-get install chromium-chromedriver python3-pip xserver-xephyr -y
      sudo pip3 install selenium


INSTRUCTIONS FOR USE

1.) GO TO TESLA INVENTORY AND CUSTOMISE YOUR SEARCH PARAMETERS EXACTLY. IT MUST DISPLAY NO RESULTS (VERY IMPORTANT OR THIS WON'T WORK)

2.) ONCE DONE, COPY THE LINK AND PASTE IN LINK FIELD IN THE CODE. IT IS PRE LOADED FOR MODEL Y GOLD COAST QLD

3.) IF DESIRED, SIGN UP TO PUSHBULLET ($5 fee) TO HAVE NOTIFICATIONS SENT TO YOUR DEVICE

4.) WHEN YOU HAVE THEM, INSERT TOKEN AND USER DATA INTO RELEVANT FIELDS

5.) REMOVE "#" FROM CODE TO ENABLE PUSH NOTIFICATIONS

6.) FROM A TERMINAL RUN python3 /dir_where_your_file_lives/filename.py OR FROM SSH "DISPLAY=:0 python3 /dir_where_your_file_lives/filename.py"


NOTES:

*THIS IS A VERY DUMB SCRIPT THAT SIMPLY CHECKS IF ANY RESULTS ARE RETURNED AND THEN SENDS YOU A NOTIFICATION, THEREFORE IT IS IMPORTANT TO CONFIGURE YOUR SEARCH PARAMETERS TO EXACTLY WHAT YOU ARE LOOKING FOR.

*I RECOMMEND YOU USE PUSHBULLET SO YOU CAN SET AND FORGET. IT COSTS $5 PER DEVICE.

*PLEASE DON'T FLOOD THE TESLA SITE WITH TOO MANY REQUESTS. I PRE-CONFIGURED FOR ONCE EVERY 10 MINUTES.

*USE AT YOUR OWN RISK
