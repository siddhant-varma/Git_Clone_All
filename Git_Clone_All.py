"""
    
    Git-Clone-All is a clonning tool that clones all public github repositories of a User or organization with a single command.

    Author: SpeedCuber (@yogendrasinghx)
 
    Special Thanks to @tirthapriya12 ;)


"""



from bs4 import BeautifulSoup
import urllib2
import re
import os
import socket


# Console colors
G = '\033[32m'  # green
Y = '\033[33m'  #Yellow
B = '\033[34m'  # blue
C = '\033[36m'  # cyan
GR ='\033[37m'  # gray
R = '\033[31m'  # red



"""
Display ASCII art to make it cool ;)
"""
print B +" _____ _ _          _____ _                          ___  _ _ "
print B +"|  __ (_) |        /  __ \ |                        / _ \| | |"
print B +"| |  \/_| |_ ______| /  \/ | ___  _ __   ___ ______/ /_\ \ | |"
print B +"| | __| | __|______| |   | |/ _ \| '_ \ / _ \______|  _  | | |"
print B +"| |_\ \ | |_       | \__/\ | (_) | | | |  __/      | | | | | |"
print B +" \____/_|\__|       \____/_|\___/|_| |_|\___|      \_| |_/_|_|\n"
print C +"                                                    Ver.1.0\n"
print C +"                                         Author: SpeedCuber\n"
                                                              


#Check internet connection

def internet_on():
  try:
  	print (Y+"\r[.]Checking Internet Connection...\r")
  	host = socket.gethostbyname("www.google.com")
  	s = socket.create_connection((host, 80), 2)
  	return True
  except:
     pass
  return False

if internet_on():
	print G+"[OK] Connected\n"
	username= raw_input(Y+'Enter Github Username : '+GR)
	if not os.path.exists(username):
		os.makedirs(username)
	os.chdir(username)

	#Count number of pages for repositories

	html_page = urllib2.urlopen("https://github.com/"+username+"?page=1&tab=repositories")
	soup = BeautifulSoup(html_page,"lxml")
	for child in soup.find(class_=re.compile("Counter")):
		count=int(child)
	print G+"\n\n[+]"+str(count) + " Repositories Found!!\n"
	nop=(count/30)+1; #Number of pages
	#print nop


	#Dump git URL and execute git clone command
	for i in range(nop):
		#print "https://github.com/"+username+"?page="+str(i+1)+"&tab=repositories"
		html_page = urllib2.urlopen("https://github.com/"+username+"?page="+str(i+1)+"&tab=repositories")
		stoup = BeautifulSoup(html_page,"lxml")
		for link in soup.findAll(itemprop="name codeRepository"):
			print B+"\n=================================================================="+GR+"\n"
			catch="git clone https://github.com"+link.get('href')+".git"
			os.system(catch)
			print('\x1b[6;30;42m' + '\nSuccess!' + '\x1b[0m')

  	
else:
	print R+"\nINTERNET IS NOT WORKING :( "
