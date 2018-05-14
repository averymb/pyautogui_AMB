import pyautogui as pg
import time

points = 0

answer = pg.prompt (
"""
Which would you rather do

a)go shopping
b)play tennis
c)write news reports
d)DJ a party

"""
    )

if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer =="d":
    points +=4

answer = pg.prompt(
"""
What is your ideal outfit

a)A fancy dress
b)swim trunks
c)a button down and pants
d)shorts and a tee

"""
    )
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer =="d":
    points +=4

answer = pg.prompt(
"""
Which accessory would you most likely wear

a)necklace
b)sweat headband
c)scarf
d)fedora

"""
    )
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer =="d":
    points +=4

answer = pg.prompt(
"""
Where would you rather be

a)the mall
b)a sports court/field
c)a computer lab
d)the beach club

"""
    )
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer =="d":
    points +=4

answer = pg.prompt(
"""
In what industry is your dream job

a)fashion
b)sports
c)technology
d)music

"""
)
if answer == "a":
    points +=1
elif answer == "b":
    points +=2
elif answer == "c":
    points +=3
elif answer =="d":
    points +=4



#END OF SURVEY
pg.alert("you are...")

#Naomi
if points < 7:
    pg.alert("Naomi")
    webbrowser.open ("https://media.giphy.com/media/bQZVMxgODgluU/giphy.gif")
#Teddy
if points >=7 and points <13:
    pg.alert("Teddy")
    webbrowser.open ("https://i.imgur.com/0YXmz.jpg")
#Navid
if points >=12 and points <18:
    pg.alert("Navid")
    webbrowser.open ("https://vignette.wikia.nocookie.net/90210/images/0/03/511navid.jpeg/revision/latest?cb=20160923005340")
#Dixon
if points >=17 and points <23:
    pg.alert("Dixon")
    webbrowser.open("http://coolspotters.com/files/photos/184031/dixon-wilson-profile.jpg")
