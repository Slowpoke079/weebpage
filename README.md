# weebpage
Weebpage.py is an automated webpage link finder.

What does it do?;
- It makes everything SUPER EASY for you
- It looks for robots.txt and scrapes it for xml sitemaps and links
- It looks for xml sitemaps and scrapes them for links
- It scrapes static html webpages for links
- It scrapes rendered javascript webpages for links
- It used Gobuster for directory bruteforcing to find links
- It uses Dirhunter for extending page finding
- It tries to make your day better with bad ascii art and a pun! Because a sad redteam is a bad redteam.

What it does not;
- It could crawl recursively, but i chose not to do so. Crawling recursively could impact your target negatively by accidentaly. For example doing a "GET" on a webpage url that triggers a SQL database reset etc.

How to use?

$ git clone https://github.com/Slowpoke079/weebpage.git

$ cd weebpage

$ chmod +x weebpage.py

$ python3 weebpage.py

#Now simply follow the script, trust me it is easy

#BuT i DoN't HaVe PyThOn3! -> sudo apt install -y python3 python3-pip

#The script was tested and build on kali-linux 23 July 2020

credits (for used tools/components)
wordlists:  https://raw.githubusercontent.com/danielmiessler/
gobuster:  https://github.com/OJ/gobuster
dirhunter:  https://github.com/Nekmo/dirhunt
And more! (tools like pip3 etc)

PS: please steal my code and make something better ;)
