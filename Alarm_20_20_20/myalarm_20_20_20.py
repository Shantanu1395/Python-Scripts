import datetime
import os
import vlc
stop = False
flag=True
while flag==True:
    while stop == False:
        rn = str(datetime.datetime.now().time())
        if rn[3:5] == "20" or rn[3:5] == "40" or rn[3:5] == "00":
            p=vlc.MediaPlayer("C:\\Users\Shantanu1395\Downloads\Moderator_Words_Remain.mp3")
            p.play()
            stop = True
        
    while stop == True:
        rn = str(datetime.datetime.now().time())
        if rn[3:5] == "21" or rn[3:5] == "41" or rn[3:5] == "01":
            p.stop()
            stop = False
