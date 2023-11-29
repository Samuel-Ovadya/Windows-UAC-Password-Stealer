# Windows_UAC_Password_Stealer

This program is actually somthing i have done a month ago (before i began this formation)  for educational purposes .

####DISCLAIMER: I am not responsible for anything you do with it ; don't use it on anyone without his explicit authorisation


## What will happend?
when you launch main.py you will first see a tkinter based typing game and nothing else
BUT when you close it after a delay (for not the user to link the admin prompt to the game close 5 sec ago )
the keylogger will be activated which will after launch the fake Windows's Admin prompt
while you enter your cred the keylogger take them and send them to destination.

### keylogger:
the keylogger begin to save every X sec the string typed in a file and try to send the file either via smtp or http
if for example the http POST didn't went through ( being a TCP we know this )
i just keep the file for the next send_time and the program will try to send all the files of the directory
but if it went through i just  delete the files and wait the next session of 'backup'

### log.php
mainly sanitize filename , filter format and store them in the storage dir(/log/)

### fake microsoft admin prompt:
the goal was to being able to steal someone windows admin password


### typing_game:
i just took it from the net ( i just needed a game to hide all the others processes )
