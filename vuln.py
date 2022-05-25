#!/usr/bin/python3
import requests
from bs4 import BeautifulSoup
from termcolor import colored
import os
import sys

def vuln():
    from axy import main    
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
    item = soup.find_all(find)
    print(item)
    chx = input('[Scraping] >>> ')
    soup = BeautifulSoup(rep.text, 'html.parser')
   

  elif chx == 'clear':
   os.system('clear')
   chx = input('[Scraping] >>> ')

   from axy import main  
  elif chx == 'axy':
   main()


  elif chx == '99':
   sys.exit()

  else:
   print(''+chx+': invalid command')
   chx = input('[Scraping] >>> ')
 