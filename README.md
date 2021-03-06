# Weebpage.py
Weebpage.py is an automated webpage finder. 
Specify a single target web URL and it will automate finding new webpages for you.


What does it do?;
- It makes everything SUPER EASY for you
- It looks for robots.txt and scrapes it for xml sitemaps and links
- It looks for xml sitemaps and scrapes them for links
- It scrapes static html webpages for links
- It scrapes rendered javascript webpages for links
- It used Gobuster for directory bruteforcing to find links (on the first page only)
- It uses Dirhunter for extending page finding (on the first page only)
- It tries to make your day better with bad ascii art and a pun! Because a sad redteam is a bad redteam.
- It stays on domain. (It won't crawl other domain names then the initial specified "seed url".) So you will stay in your costumers scope!
- weebpages.py (not weebpage.py) will scan recursively, found links will be reused for scanning for new pages.


What it does not;
- It could crawl recursively, but i chose not to do so. Crawling recursively could impact your target/costumer negatively on accident. For example doing an accidental "GET" on a automated and newly found webpage url that triggers an SQL database modification like a DB reset or deleting a user.



# How to use?


```console
my@pc:~$ sudo apt install -y python3
```

```console
my@pc:~$ git clone https://github.com/Slowpoke079/weebpage.git
```

```console
my@pc:~$ cd weebpage
```

```console
my@pc:~$ chmod +100 weebpage.py
```

```console
my@pc:~$ python3 weebpage.py
```


Now simply follow the script;
![github-small](https://github.com/Slowpoke079/weebpage/blob/master/image.png)
```
Enter a web url like; http://192.68.56.1 or https://192.68.56.1 or http://192.68.56.1:65524 or http://192.68.56.1:80 or http://192.68.56.1:80/whatever/
```
![github-small](https://github.com/Slowpoke079/weebpage/blob/master/image2.png)



# How to scan webpages recursively?
For this i made a small clone of weebpage.py with some small edits called weebpages.py. The process of using the tool is the same as with weebpage.py If you already did a gitclone you don't need to do that again ;).


```console
my@pc:~$ sudo apt install -y python3
```

```console
my@pc:~$ git clone https://github.com/Slowpoke079/weebpage.git
```

```console
my@pc:~$ cd weebpage
```

```console
my@pc:~$ chmod +100 weebpages.py
```

```console
my@pc:~$ python3 weebpages.py
```



# Output
- Output (found webpage links) will be shown in the terminal.
- Output will also be saved to "output.txt" like this small list example.
![github-small](https://github.com/Slowpoke079/weebpage/blob/master/image3.png)



# Other
The script was tested and build on kali-linux 31 July 2020


credits (for used tools/components)
- Wordlists:  https://raw.githubusercontent.com/danielmiessler/
- Gobuster:  https://github.com/OJ/gobuster
- Dirhunter:  https://github.com/Nekmo/dirhunt
- And more! (tools like pip3 etc)
