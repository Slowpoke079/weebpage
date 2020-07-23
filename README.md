# weebpage
Weebpage.py is an automated webpage link finder. What does it do?; It looks for robots.txt and scrapes it for xml sitemaps and urls, It looks for xml sitemaps and scrapes them, It scrapes static html webpages, It scrapes rendered javascript webpages, It used Dirbuster for directory bruteforcing, It uses Dirhunter for extending page finding, It tries to make your day better with bad ascii art and a pun.
It could crawl recursivly, but i chose not to use this, since this could impact your target negatively by accidentaly doing a "GET" on a webpage url that triggers a SQL databse reset (etc).

How to use?

$ git clone https://github.com/Slowpoke079/weebpage.git

$ cd weebpage

$ chmod +x weebpage.py

$ python3 weebpage.py

#I don't have python3! -> sudo apt install -y python3 python3-pip

credits (for used tools/components)
wordlists:  https://raw.githubusercontent.com/danielmiessler/
gobuster:  https://github.com/OJ/gobuster
dirhunter:  https://github.com/Nekmo/dirhunt
