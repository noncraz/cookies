import requests,os
P = '\x1b[1;97m'
M = '\x1b[1;91m'
H = '\x1b[1;92m'
K = '\x1b[1;93m'
B = '\x1b[1;94m'
U = '\x1b[1;95m' 
O = '\x1b[1;96m'
N = '\x1b[0m'    
Z = "\033[1;30m"
sir = '\033[41m\x1b[1;97m'
x = '\33[m' # DEFAULT
m = '\x1b[1;91m' #RED +
k = '\033[93m' # KUNING +
h = '\x1b[1;92m' # HIJAU +
hh = '\033[32m' # HIJAU -
u = '\033[95m' # UNGU
kk = '\033[33m' # KUNING -
b = '\33[1;96m' # BIRU -
p = '\x1b[0;34m' # BIRU +
ses = requests.Session()
session = requests.Session()
cok=input('Enter Cookie : ')
#cok='c_user=100009040303803;datr=1CnBZPBG4Cp6DzWq_g5807XK;fr=0u5JRafNeRU9jFnle.AWX5QtpjOjeCAc4zrP8ZUtpbxug.BkwSnV.ow.AAA.0.0.BkwSnV.AWUh1x0Wiys; sb=1CnBZHM3_-YHTRJiA595T_uA;xs=31%3AdJktYzgNd-Q6-g%3A2%3A1690380757%3A-1%3A6439'
headapp={"user-agent":"SupportsFresco=1 Dalvik/2.1.0 (Linux; U; Android 6.0.1; SM-J210F Build/MMB29Q) Source/1 [FBAN/EMA;UNITY_PACKAGE/342;FBBV/107586706;FBAV/172.0.0.8.182;FBDV/SM-J210F;FBLC/id_ID;FBOP/20]"}
w =session.get("https://m.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+cok}).text
sop = bs4.BeautifulSoup(w,"html.parser")
x = sop.find("form",method="post")
game = [i.text for i in x.find_all("h3")]
try:
	for i in range(len(game)):
		print ("\r%s\033[0m%s%s"%(P,H,game[i].replace("Ditambahkan pada"," Ditambahkan pada")))
except AttributeError:
		print ("\r%s\033[0m cookie invalid"%(M))
w=session.get("https://m.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+cok}).text
sop = bs4.BeautifulSoup(w,"html.parser")
x = sop.find("form",method="post")
game = [i.text for i in x.find_all("h3")]
try:
	for i in range(len(game)):
			print ("\r%s\033[0m%s"%(P,game[i].replace("Kedaluwarsa"," Kedaluwarsa")))
except AttributeError:
		print ("\r%s\033[0mcookie invalid"%(M))
