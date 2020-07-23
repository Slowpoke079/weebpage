#!/usr/bin/env python3
############################ PART 1 - CLEAR, BANNER, INSTALLER, FILE CLEANUP ############################
import os

def clear_terminal():
	os.system('cls' if os.name == 'nt' else 'clear')

def bad_joke_banner():
	print ("▄▄▌ ▐ ▄▌▄▄▄ .▄▄▄ .▄▄▄▄·  ▄▄▄· ▄▄▄·  ▄▄ • ▄▄▄ .")
	print ("██· █▌▐█▀▄.▀·▀▄.▀·▐█ ▀█▪▐█ ▄█▐█ ▀█ ▐█ ▀ ▪▀▄.▀·")
	print ("██▪▐█▐▐▌▐▀▀▪▄▐▀▀▪▄▐█▀▀█▄ ██▀·▄█▀▀█ ▄█ ▀█▄▐▀▀▪▄")
	print ("▐█▌██▐█▌▐█▄▄▌▐█▄▄▌██▄▪▐█▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▄▌")
	print (" ▀▀▀▀ ▀▪ ▀▀▀  ▀▀▀ ·▀▀▀▀ .▀    ▀  ▀ ·▀▀▀▀  ▀▀▀ ")
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

def install_requirements():
	os.system("sudo apt install -y git")
	os.system("sudo apt install -y wget")
	os.system("sudo apt install -y python3")
	os.system("sudo apt install -y python3-pip")
	os.system("sudo apt install -y gobuster")
	os.system("sudo pip3 install dirhunt")
	os.system("sudo pip3 install bs4")
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
	print("Do you want to install the requirements, run the script or clean up previously left files?")
	print("enter: [run], [install] or [clean]")
	print("\n")
	install = ("install", "INSTALL")
	run = ("run", "RUN", "ayayaya")
	clean = ("clean", "CLEAN", "ewh, weebs")
	choice = input()
	if choice in install:
		install_requirements()
		print("requirements are now installed!")
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
		print("\n")
		print("The leftover files have been cleaned up!")
		exit()
	else:
		already_installed()

already_installed()
filepath = ("output.txt")
if os.path.exists(filepath):
	os.remove(filepath)
else:
	None

from bs4 import BeautifulSoup
import requests

############################ PART 2 - SET TARGET FILES ############################
def target():	
	clear_terminal()
	bad_joke_banner()
	print("\n")
	print ("Enter target webpage, use format: https://www.yourwebsite.com or http://www.yourwebsite.com")
	webpage = input("Enter target webpage: ")
	file = open("target.txt", "w")
	file.write(webpage)
	file.close()

############################ PART 3 - ROBOTS AND SITEMAPS #########################
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

############################ PART 4 - ONE TIME ENUMERATORS ############################
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

############################ PART 5 - CRAWLERS ############################
from bs4 import BeautifulSoup
import requests

def crawlers():
	
	def rendered_webpage_crawler():
		clear_terminal()
		bad_joke_banner()
		print ("\n")
		print ("crawling javascript rendered webpages with selenium, please wait!")
		print ("\n")
		from selenium import webdriver
		from selenium.webdriver.firefox.options import Options as FirefoxOptions
		with open ("target.txt") as domainfile:
			for line in domainfile:
				domain = domain = str(line.strip("\n"))
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

	def static_webpage_crawler():
		clear_terminal()
		bad_joke_banner()
		print ("\n")
		print ("crawling static html webpages with beautifulsoup, please wait!")
		print ("\n")
		with open ("target.txt") as domainfile:
			for line in domainfile:
				domain = line
		webpage = (str(domain).strip("\n"))
		page = requests.get(webpage)
		data = page.text
		soup = BeautifulSoup(data, "html.parser")
		for link in soup.find_all("a"):
			links = link.get("href")
			if links is not None:
				file = open("webpages.txt", "a")
				file.write(links+"\n")
				file.close()
		with open ("webpages.txt") as origin:
			for line in origin:
				if webpage in line:
					file = open("list.txt", "a")
					file.write(line)
					file.close()
				if line.startswith("/"):
					file = open("list.txt", "a")
					file.write(webpage + line)
					file.close()

	def write_output():
		filepath = ("list.txt")
		if os.path.exists(filepath):
			os.system("cat list.txt >> output.txt")
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

	rendered_webpage_crawler()
	static_webpage_crawler()
	write_output()
	minicleanup()

############################ PART X1 - OUTPUT CLEANERS ############################
def sorting_and_cleaning():

	def remove_duplicates():
		with open ("output.txt") as read:
			uniqlines = set(read.readlines())
			with open("output2.txt", "w") as write:
				write.writelines(set(uniqlines))

	def sorting():
		with open ("output2.txt") as input_file:
			lines = input_file.readlines()
			sortedfile = (sorted(lines))
			with open("output.txt", "w") as output_file:
				output_file.writelines(sortedfile)

	def minicleanup():
		filepath = ("output2.txt")
		if os.path.exists(filepath):
			os.remove(filepath)
		else:
			None

	remove_duplicates()
	sorting()						

############################ PART X3 - SHOW OUTPUT ############################
def show_found_webpages():
	cleanup()
	clear_terminal()
	bad_joke_banner()
	print("\n")
	print("found webpages: ")
	sorting_and_cleaning()
	os.system("cat output.txt")
	print("\n")	
	print ("output is saved in output.txt!")
	print("\n")

############################ EXECUTION FLOW ############################
target()					#target.txt holds single http/s link
robots_and_sitemaps()				#output.txt is created and filled with found links.
cleanup()					#cleans not used files up (exept for target.txt and output.txt)
enumerator()					#output is appended into output.txt
cleanup()					#cleans not used files up (exept for target.txt and output.txt)
sorting_and_cleaning()				#sorts and removes duplicates from output.txt
crawlers()					#webcrawlers and cleaners, output is in output.txt
sorting_and_cleaning()				#sorts and removes duplicates from target.txt
cleanup()					#cleans up all created files (excluding output.txt)
show_found_webpages()				#shows found webpage urls
cleanup()					#cleans up all created files (excluding output.txt)
