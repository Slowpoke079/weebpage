#!/usr/bin/env python3
############################ PART 1 - CLEAR, BANNER, INSTALLER, FILE CLEANUP ############################
import os

def clear_terminal():
	os.system('cls' if os.name == 'nt' else 'clear')

def bad_joke_banner():
	print ("▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄ .▄▄▄▄·  ▄▄▄· ▄▄▄·  ▄▄ • ▄▄▄ ..▄▄ · ")
	print ("██· █▌▐█▀▄.▀·▀▄.▀·▐█ ▀█▪▐█ ▄█▐█ ▀█ ▐█ ▀ ▪▀▄.▀·▐█ ▀. ")
	print ("██▪▐█▐▐▌▐▀▀▪▄▐▀▀▪▄▐█▀▀█▄ ██▀·▄█▀▀█ ▄█ ▀█▄▐▀▀▪▄▄▀▀▀█▄")
	print ("▐█▌██▐█▌▐█▄▄▌▐█▄▄▌██▄▪▐█▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▄▌▐█▄▪▐█")
	print (" ▀▀▀▀ ▀▪ ▀▀▀  ▀▀▀ ·▀▀▀▀ .▀    ▀  ▀ ·▀▀▀▀  ▀▀▀  ▀▀▀▀ ")
	print ("\n")
	print (" ⣾⡇⣿⣿⡇⣾⣿⣿⣿⣿⣿⣿⣿⣿⣄⢻⣦⡀⠁⢸⡌⠻⣿⣿⣿⡽⣿⣿ ")
	print (" ⡇⣿⠹⣿⡇⡟⠛⣉⠁⠉⠉⠻⡿⣿⣿⣿⣿⣿⣦⣄⡉⠂⠈⠙⢿⣿⣝⣿ ")
	print (" ⠤⢿⡄⠹⣧⣷⣸⡇⠄⠄⠲⢰⣌⣾⣿⣿⣿⣿⣿⣿⣶⣤⣤⡀⠄⠈⠻⢮ ")
	print (" ⠄⢸⣧⠄⢘⢻⣿⡇⢀⣀⠄⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠄⢀ ")
	print (" ⠄⠈⣿⡆⢸⣿⣿⣿⣬⣭⣴⣿⣿⣿⣿⣿⣿⣿⣯⠝⠛⠛⠙⢿⡿⠃⠄⢸ ")
	print (" ⠄⠄⢿⣿⡀⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⡾⠁⢠⡇⢀ ")
	print (" ⠄⠄⢸⣿⡇⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⣫⣻⡟⢀⠄⣿⣷⣾ ")
	print (" ⠄⠄⢸⣿⡇⠄⠈⠙⠿⣿⣿⣿⣮⣿⣿⣿⣿⣿⣿⣿⣿⡿⢠⠊⢀⡇⣿⣿ ")
	print (" ⠒⠤⠄⣿⡇⢀⡲⠄⠄⠈⠙⠻⢿⣿⣿⠿⠿⠟⠛⠋⠁⣰⠇⠄⢸⣿⣿⣿ ")

def bad_joke_banner2():
	print ("\n")
	print ("Have fun and don't harm others!")
	print ("Feel free to re-use my code and make better things!")
	print ("Webpage turned into weebpage because i made a dyslectic fuck-up, ascii jokes followed.")
	print ("\n")

def cleanup():
	filepath = ("list.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("list2.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("output_dirhunter.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("output_gobuster.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("output_filter_gobuster.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("output_gobuster_common.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("output_gobuster_big.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("webpages.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("sitemaps")
	if os.path.exists(filepath):
		os.system("rm -rf sitemaps")
	else:
		None
	filepath = ("robots.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("sitemap_files.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("grep.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("passed.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("output2.txt")
	if os.path.exists(filepath):
		os.system("rm -rf " + filepath)
	else:
		None
	filepath = ("robotics.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("filter_file1.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("filter_file2.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None
	filepath = ("checked.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None

def install_requirements():
	os.system("sudo apt install -y git")
	os.system("sudo apt install -y wget")
	os.system("sudo apt install -y python3")
	os.system("sudo apt install -y python3-pip")
	os.system("sudo apt install -y gobuster")
	os.system("pip3 install dirhunt")
	os.system("pip3 install http.client")
	os.system("pip3 install tqdm")
	os.system("rm common.txt")
	os.system("rm big.txt")
	os.system("wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/common.txt")
	os.system("wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/big.txt")
	os.system("mkdir wordlists")
	os.system("mv common.txt wordlists/")
	os.system("mv big.txt wordlists/")
	os.system("pip3 install selenium")
	os.system("sudo wget https://github.com/mozilla/geckodriver/releases/download/v0.24.0/geckodriver-v0.24.0-linux64.tar.gz -O /usr/local/bin/geckodriver.tar.gz")
	os.system("sudo tar -zxvf /usr/local/bin/geckodriver*.tar.gz -C /usr/local/bin/")
	os.system("sudo rm /usr/local/bin/geckodriver.tar.gz")
	os.system("sudo chmod +x /usr/local/bin/geckodriver")
	os.system("sudo apt install firefox")

def already_installed():
	clear_terminal()
	bad_joke_banner()
	bad_joke_banner2()
	print ("Do you want to install the requirements, run the script or clean up previously left files?")
	print ("enter: [run], [install] or [clean]")
	print ("\n")
	install = ("install", "INSTALL")
	run = ("run", "RUN", "ayayaya")
	clean = ("clean", "CLEAN", "ewh, weebs")
	choice = input()
	if choice in install:
		install_requirements()
		print ("requirements are now installed!")
	if choice in run:
		return True
	if choice in clean:
		cleanup()
		filepath = ("output.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("target.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		clear_terminal()
		bad_joke_banner()
		print ("\n")
		print ("The leftover files have been cleaned up!")
		exit()
	else:
		already_installed()

already_installed()
filepath = ("output.txt")
if os.path.exists(filepath):
	os.remove(filepath)
else:
	None

############################ PART 2 - NEW IMPORTS ############################
import os
from time import sleep
from tqdm import tqdm
from tqdm import trange
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
import urllib.request

############################ PART 3 - SET TARGET FILES ############################
def target():	
	clear_terminal()
	bad_joke_banner()
	print("\n")
	print ("Enter target webpage, use format: https://www.yourwebsite.com or http://www.yourwebsite.com")
	webpage = input("Enter target webpage: ")
	file = open("target.txt", "w")
	file.write(webpage)
	file.close()

############################ PART 4 - ROBOTS AND SITEMAPS #########################
def robots_and_sitemaps():
	
	def robots():
		clear_terminal()
		bad_joke_banner()
		print ("\n")
		print ("Scanning for robots.txt and xml sitemaps, please wait!")
		print ("\n")
		filepath = ("robots.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		filepath2 = ("sitemaps/")
		if os.path.exists(filepath2):
			os.system("rm -rf " + filepath2)
		with open ("target.txt") as domainfile:
			for line in domainfile:
				domain = str(line.strip("\n"))
		if os.path.exists("sitemaps"):
			os.system("rm -rf sitemaps")
			os.system("mkdir sitemaps")
		else:
			os.system("mkdir sitemaps")
			None
		filepath = ("robotics.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
			os.system("touch robotics.txt")
		else:
			os.system("touch robotics.txt")
		wget = ("wget " + domain + "/robots.txt")
		os.system(wget)
		filepath = ("robots.txt")
		if os.path.exists(filepath):		
			os.system('cat robots.txt | grep -Eo "(/)[a-zA-Z0-9./?=_%:-]*" > filter_file1.txt')
			os.system("sed '/www/d;/http/d' filter_file1.txt > filter_file2.txt")
			do1 = domain.replace("https://www.", "")
			do2 = do1.replace("http://www.", "")
			do3 = (domain + do2)
			with open ("filter_file2.txt") as uwu:
				for line in uwu:
					if line.startswith("/"):
						robottxtlinks = (str(domain + line).strip("\n"))
						if domain in robottxtlinks:
							print(robottxtlinks)
							file = open ("robotics.txt", "a")
							file.write(robottxtlinks + "\n")
							file.close()
		if os.path.exists(filepath):
			file = open("robotics.txt", "a")
			file.write(domain + "/robots.txt" + "\n")
			file.close()
			downloaded_robot = open ("robots.txt")
			robot = downloaded_robot.readlines()
			robots = str(robot).split()
			for text in robots:
				if ("http") in text:
					sexy_strippers = ("\n']", "\n")
					robolinks = (str(text).strip(str(sexy_strippers)))
					if robolinks.startswith("http") and robolinks.endswith("sitemap.xml"):
						if domain in robolinks:
							os.system("wget " + robolinks + " -P sitemaps/")
							file = open("robotics.txt", "a")
							file.write(robolinks + "\n")
							file.close()

	robots()

	def sitemaps():
		clear_terminal()
		bad_joke_banner()
		print ("\n")
		print ("Scanning xml sitemaps for webpages, please wait!")
		print ("\n")
		with open ("target.txt") as domainfile:
			for line in domainfile:
				domain = str(line.strip("\n"))
		filepath = ("sitemaps/")
		os.system("ls sitemaps > sitemap_files.txt")
		with open ("sitemap_files.txt") as goodies:
			for line in goodies:
				filepath = ("sitemaps/" + line)
				pudding = (str(filepath).strip("\n"))
				os.system("cat " + pudding + " | grep http > grep.txt")
				with open ("grep.txt") as victim:
					for line in victim:
						stripper1 = (str(line).strip("\n"))
						stripper2 = (str(stripper1).replace("<loc>", ""))
						stripper3 = (str(stripper2).replace("</loc>", ""))
						stripper4 = (str(stripper3).replace("<sitemapindex xmlns='", ""))
						stripper5 = (str(stripper4).replace("    ", ""))
						stripper6 = (str(stripper5).replace("'>", ""))
						stripper7 = (str(stripper6).replace("<xhtml:link href=", ""))
						stripper8 = (str(stripper7).replace(" hreflang=", ""))
						stripper9 = (str(stripper8).replace(">", ""))
						stripper10 = (str(stripper9).replace(" rel=", ""))
						stripper11 = (str(stripper10).replace("alternate", ""))
						stripper12 = (str(stripper11).replace("/>", ""))
						stripper13 = (str(stripper12).replace(" xmlns:xhtml=", ""))
						stripper14 = (str(stripper13).replace("<urlset xmlns=", ""))
						stripper15 = (str(stripper14).replace("x-default", ""))
						file = open ("robotics.txt", "a")
						file.write(stripper15 + "\n")
						file.close()
						if domain in stripper6 and stripper15.endswith(".xml"):
							os.system("wget " + stripper15 + " -P sitemaps/")
		os.system("ls sitemaps > sitemap_files.txt")
		with open ("sitemap_files.txt") as goodies:
			for line in goodies:
				filepath = ("sitemaps/" + line)
				pudding = (str(filepath).strip("\n"))
				os.system("cat " + pudding + " | grep http > grep.txt")
				with open ("grep.txt") as victim:
					for line in victim:
						stripper1 = (str(line).strip("\n"))
						stripper2 = (str(stripper1).replace("<loc>", ""))
						stripper3 = (str(stripper2).replace("</loc>", ""))
						stripper4 = (str(stripper3).replace("<sitemapindex xmlns='", ""))
						stripper5 = (str(stripper4).replace("    ", ""))
						stripper6 = (str(stripper5).replace("'>", ""))
						stripper7 = (str(stripper6).replace("<xhtml:link href=", ""))
						stripper8 = (str(stripper7).replace(" hreflang=", ""))
						stripper9 = (str(stripper8).replace(">", ""))
						stripper10 = (str(stripper9).replace(" rel=", ""))
						stripper11 = (str(stripper10).replace("alternate", ""))
						stripper12 = (str(stripper11).replace("/>", ""))
						stripper13 = (str(stripper12).replace(" xmlns:xhtml=", ""))
						stripper14 = (str(stripper13).replace("<urlset xmlns=", ""))
						stripper15 = (str(stripper14).replace("x-default", ""))
						print (stripper15)
						if domain in stripper15:
							file = open ("sm1.txt", "a")
							file.write(stripper15 + "\n")
							file.close()
			filepath = ("sm1.txt")
			if os.path.exists(filepath):
				os.system('cat sm1.txt | grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" | sort -u > output.txt')

	sitemaps()

############################ PART 5 - ONE TIME ENUMERATORS ############################
def enumerator():

	def dirhunter():
		clear_terminal()
		bad_joke_banner()
		print ("\n")
		print ("Scanning with dirhunter, please wait!")
		print ("\n")
		with open ("target.txt") as domainfile:
			for line in domainfile:
				domain = str(line.strip("\n"))
				webpage = domain
		os.system('echo "#!/bin/bash" > dir.sh')
		os.system('echo "dirhunt ' +(webpage)+ ' --not-follow-subdomains |& tee -a list.txt" >> dir.sh')
		os.system('chmod +100 dir.sh')
		import subprocess
		from subprocess import call
		subprocess.call(['./dir.sh'])
		os.system('grep -Eo "(http|https)://[a-zA-Z0-9./?=_%:-]*" list.txt >> list2.txt')
		os.system("cat list2.txt > list.txt")

	def gobuster():
		clear_terminal()
		bad_joke_banner()
		print ("\n")
		print ("Scanning with dirbuster, please wait! (this can take some time)")
		print ("\n")
		with open ("target.txt") as domainfile:
			for line in domainfile:
				domain = str(line.strip("\n"))
				webpage = domain
		os.system("gobuster dir -u " +(webpage)+ " -w wordlists/common.txt -o output_gobuster_common.txt")
		os.system("gobuster dir -u " +(webpage)+ " -w wordlists/big.txt -o output_gobuster_big.txt")
		os.system("grep -Eo '^[^ ]+' output_gobuster_common.txt >> output_filter_gobuster.txt")
		os.system("grep -Eo '^[^ ]+' output_gobuster_big.txt >> output_filter_gobuster.txt")
		webpage_unstripped = open("target.txt").read()
		webpage = webpage_unstripped.strip("\n")
		with open ("output_filter_gobuster.txt") as origin:
			for line in origin:
				if webpage in line:
					file = open("output_gobuster.txt", "a")
					file.write(line)
					file.close()
				if line.startswith("/"):
					file = open("output_gobuster.txt", "a")
					file.write(webpage + line)
					file.close()
		os.system("grep -Eo '^[^ ]+' output_gobuster.txt >> list.txt")

	def list2target():
		os.system("cat list.txt >> output.txt")

	def minicleanup():
		filepath = ("output_gobuster_common.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("output_gobuster_big.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("output_filter_gobuster.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("output_gobuster.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("dirhunttemp.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("dir.sh")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("list2.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None

	dirhunter()
	gobuster()
	list2target()
	minicleanup()

############################ PART 6 - CRAWLERS ############################
def crawlers():
	
	def Selenium_Crawler():
		clear_terminal()
		bad_joke_banner()
		amount = sum(1 for line in open("target.txt","r"))
		print ("\n")
		print ("Crawling " +(str(amount))+ " webpages to find new pages for you, please wait!")
		print ("\n")
		with open("target.txt","r") as f:
			for line in tqdm(f, total=amount):
				try:
					domain = str(line.strip("\n"))
					options = FirefoxOptions()
					options.add_argument("--headless")
					driver = webdriver.Firefox(options=options)
					driver.get(domain)
					elems = driver.find_elements_by_xpath("//a[@href]")
					for elem in elems:
						href = (elem.get_attribute("href"))
						if href is not None:
							if href.startswith(domain):
								file = open("list.txt", "a")
								file.write(href + "\n")
								file.close()
					driver.quit()
				except (Exception):
					pass

		os.system("sort -u list.txt > sorted_output.txt")

	def write_output():
		filepath = ("list.txt")
		if os.path.exists(filepath):
			os.system("cat sorted_output.txt >> output.txt")
			os.system("cat sorted_output.txt >> target.txt")
		else:
			None

	def minicleanup():
		filepath = ("webpages.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("geckodriver.log")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("list.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("output_selenium.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("sorted_output.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None

	Selenium_Crawler()
	write_output()
	minicleanup()
############################ PART 7 - OUTPUT CLEANERS ############################
def sorting_and_cleaning():
	os.system("sort -u output.txt > output2.txt")
	os.system("sort -u output2.txt > output.txt")
	os.system("sort -u target.txt > target2.txt")
	os.system("sort -u target2.txt > target.txt")
		
	def minicleanup():
		filepath = ("target2.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
		filepath = ("output2.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
	minicleanup()

############################ PART 8 - HTTP LINK CHECKER ############################
def http200_checker():
	os.system('cls' if os.name == 'nt' else 'clear')
	filepath = ("checked.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
		os.system("touch checked.txt")
	else:
		os.system("touch checked.txt")
	filepath = ("output.txt")
	if os.path.exists(filepath):
		None
	else:
		os.system("touch output.txt")	

	clear_terminal()
	bad_joke_banner()
	print ("\n")
	print ("Checking if found links are dead-or-alive (lol) please wait, it won't take long!")
	print ("\n")
	with open("output.txt","r") as f:
		for line in f:
			try:
				webpage = str(line.strip("\n"))
				req = urllib.request.urlopen(webpage).getcode()
				print (webpage, "HTTP", req)
				os.system("echo " + webpage + " >> checked.txt")
				sleep(0.010)
			except Exception:
				webpage = str(line.strip("\n"))
				print (webpage + " ", "DEAD")
				sleep(0.010)

	os.system("cat checked.txt > target.txt")
	os.system("cat checked.txt > output.txt")
	sorting_and_cleaning()

	def minicleanup():
		filepath = ("checked.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None
	minicleanup()
http200_checker()

############################ PART 9 - SHOW OUTPUT ############################
def show_found_webpages():
	clear_terminal()
	bad_joke_banner()
	print ("\n")
	print ("Found webpages: ")
	print ("\n")
	sorting_and_cleaning()
	with open ("target.txt") as domainfile:
		for line in domainfile:
			target0 = (str(line.strip("\n")))
			target = (target0 + "/")
			os.system("cat output.txt | grep " +(target)+ " >> target.txt")
	
	sorting_and_cleaning()
	os.system("cat target.txt >> output.txt")
	sorting_and_cleaning()
		
	filepath = ("target.txt")
	if os.path.exists(filepath):
		os.remove(filepath)
	else:
		None

	os.system("cat output.txt")
	print ("\n")	
	print ("output is saved in output.txt!")
	print ("\n")

############################ PART 10 - EXECUTION FLOW - ENUMERATION ############################
target()					#target.txt holds single http/s link
robots_and_sitemaps()				#output.txt is created and filled with found links.
cleanup()					#cleans not used files up (except for target.txt and output.txt)

enumerator()					#output is appended into output.txt
cleanup()					#cleans not used files up (except for target.txt and output.txt)
sorting_and_cleaning()				#sorts and removes duplicates from output.txt

crawlers()					#webcrawlers and cleaners, output is in output.txt
sorting_and_cleaning()				#sorts and removes duplicates from target.txt
http200_checker()				#checks if found links are alive or dead/bogus links


############################ PART 11 - EXECUTION FLOW - CRAWLER ############################
#(Can be duped to do deeper scans, but the crawler will become slow af.) 
crawlers()					#webcrawlers and cleaners, output is in output.txt
sorting_and_cleaning()				#sorts and removes duplicates from target.txt
http200_checker()				#checks if found links are alive or dead/bogus links

crawlers()					#webcrawlers and cleaners, output is in output.txt
sorting_and_cleaning()				#sorts and removes duplicates from target.txt
http200_checker()				#checks if found links are alive or dead/bogus links

############################ PART 12 - EXECUTION FLOW - RESULTS ############################
cleanup()					#cleans up all created files (excluding output.txt)
show_found_webpages()				#shows found webpage urls



