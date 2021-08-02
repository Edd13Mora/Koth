#!/usr/bin/python3

import os
import sys
sys.path.append('__init__')
import get_ip as ad
import file_mg as file 
from art import *
from termcolor import colored

SEC_PATH = "/usr/bin/"


def main():
	try:	
		url =input("Please enter the URL : ")
		path_dir ="reports/" + url
		file.create_dir(path_dir)
		ip = ad.get(url)
		print('The IP Address is :',ip)
		os.system(SEC_PATH  + 'gnome-terminal -- bash -c "nmap -A '+ip+' -p- -o '+path_dir+'/nmap.txt && bash"') # This will call nmap to scan for open ports on the target!
		os.system(SEC_PATH  + 'gnome-terminal -- bash -c "nikto +h '+url+' -output '+path_dir+'/nikto.txt && bash"') # This will run nikto to scan the target from top 10 owasp vulns!
		os.system(SEC_PATH  + 'gnome-terminal -- bash -c "gobuster -u '+url+ ' -w /home/eddie/Bureau/tools/directory-list-2.3-medium.txt /dirsearch.txt && bash"') # This will run gobuster against the target to find hidden folders and files in the server (in will work if there is a web server) !
		os.system(SEC_PATH  + 'gnome-terminal -- bash -c "wpscan --url '+ip+' /wpscan.txt && bash"') # In case of testing on a Wordpress! this will run Wpscan tool and start enumiration on the target!
		os.system(SEC_PATH  + 'gnome-terminal -- bash -c "ftp '+ip+'"')  # this will open ftp connection with the target and u need to test for anonymous coneection!
        #you can add new lines here for other tools that you wanna call ... same syntax ^^
	except ValueError as e:
		print(e)
	except:
		print("Owh Shit!")
	
	


if __name__ == '__main__':

	print(colored(text2art ("koth 1.0.0"),'cyan'))
	print(colored('Coded by Edd13Mora! \n\n'.center(60),'green'))
	if sys.version_info.major < 3 :
		print("use python3" )
		exit(0)
	main()
