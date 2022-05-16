import requests
import errno
from bs4 import BeautifulSoup
import time
import sys
import os
from termcolor import colored
def vuln():
 print('')

ip = input('[Scraping -> Adress] >>> ')
chx = input('[Scraping] >>> ')

rep = requests.get(ip)
while True:
 if chx == 'text':
    soup = BeautifulSoup(rep.text, 'html.parser')
    print(soup)
    chx = input('[Scraping] >>> ')
 
 elif chx == 'finder':
    soup = BeautifulSoup(rep.text, 'html.parser')
    find = input('[Scraping -> Find element] >>> ')
    item = soup.findAll(find)
    print(item)
    chx = input('[Scraping] >>> ')
    soup = BeautifulSoup(rep.text, 'html.parser')

 elif chx == 'clear':
  os.system('clear')
  chx = input('[Scraping] >>> ')

 elif chx == 'axy':
  from axy import main


 elif chx == '99':
  sys.exit()

 else:
  print(''+chx+': invalid command')
  chx = input('[Scraping] >>> ')
 