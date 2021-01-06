'''
 Simple wikipedia scraper using python
Code by Awok ID
'''
#Import
import os, sys, time
try:
  import requests
  from bs4 import BeautifulSoup as bs
except ImportError:
  os.system("pip install requests")
  os.system("pip install bs4")

#Url and searching
try:
  os.system("cls" if os.name == "nt" else "clear")
  cari = input("\033[1;37mQuery: ")
  spasi = cari.replace(" ", "_")
  url_jadi = "https://id.m.wikipedia.org/wiki/"+spasi
  req = requests.get(url_jadi)
  soup = bs(req.content, 'html.parser')

  if req.status_code == 200:
    #title
    os.system("cls" if os.name == "nt" else "clear")
    title = soup.find("title")
    print("\033[0;41m"+title.text+"\033[0m")
    print('')

    #Konten
    konten = soup.find("p")
    print("\033[1;37m"+konten.text+"\033[0m\n")
  else:
    print("\n\033[0;41mNOT FOUND\033[0m\n")
except KeyboardInterrupt:
  print("\n\033[0;41mEXIT PROGRAM\033[0m\n ")
except Exception as e:
  print("\n\033[0;41mE R R O R\033[0m\n")
