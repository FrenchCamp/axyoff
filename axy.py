#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
import os
import sys
from termcolor import colored
from art import *

sys.path.append('__init__')

ip = input('[Scraping -> Adress] >>> ')
os.system('clear')
def main():
 chx = input('>>> ')
tprint('Axy')
print(colored('  By FrenchCamp (BETA VERSION)', 'green'))
print(colored('-------------------------------------------', 'red'))



print(colored('Use "help" for list of commands ', 'cyan'))

rep = requests.get(ip)
chx = input('>>> ')



while True:

 if chx == 'text':
    soup = BeautifulSoup(rep.text, 'html.parser')
    print(soup)
    chx = input('>>> ')
    

 

 elif chx == 'cls':
  os.system('clear')
  chx = input('>>> ')


 elif chx == 'finder':
    soup = BeautifulSoup(rep.text, 'html.parser')
    find = input('[Scraping -> Find element] >>> ')
    item = soup.find_all(find)
    print(item)
    chx = input('>>> ')
    

 elif chx == 'help':
  print('----------')
  print(colored('Help', 'red'))
  print('----------')
  print(colored('1/2.Commands : (Basic commands)', 'yellow'))
  print('help: show help\ncls : clear\nreport : report a bug\n99: Exit Application')
  print(colored('2/2.Commands : (Scraping commands)', 'yellow'))
  print('text : displays the code of the page in question\nfinder : search for an element on the page in question')
  print(colored('About Developper', 'yellow'))
  print('The developer named Frenchcamp is a French child who is passionate about programming and cyberseurity, he is currently 11 years old.\nWebsite: https://frenchcamp.github.io/fr/')
  print(colored('About Axy', 'yellow'))
  print('Axy is a Web Scraping application developed by FrenchCamp.\nWebsite : https://frenchcamp.github.io/fr/axy.html ')
  chx = input('>>> ')

 elif chx == '99':
   sys.exit()
 
 elif chx == 'report':
  print('A bug, a problem? you can report it with the following email address:')
  print(colored('frenchcamp.axy.bug@gmail.com', 'blue'))
  chx = input('>>> ')


 else:
  print(''+chx+': invalid command')
  chx = input('>>> ')