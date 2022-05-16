#!/usr/bin/python3

import os
import sys
from termcolor import colored
from art import *



sys.path.append('__init__')

 
def main():
 print('')
tprint('Axy')
print(colored('  By FrenchCamp (BETA VERSION)', 'green'))
print(colored('-------------------------------------------', 'red'))



print(colored('Use "help" for list of commands ', 'cyan'))


chx = input('>>> ')


while True: 
 if chx == 'scraping':
   from vuln import vuln
 


 elif chx == 'scan':
   from scan import scan

 

 elif chx == 'cls':
  os.system('clear')
  chx = input('>>> ')

  
  

 elif chx == 'help':
  print('----------')
  print(colored('Help', 'red'))
  print('----------')
  print(colored('1.Commands', 'yellow'))
  print('help: show help\nscraping: Launch the Web Scraping interface\nScan: launches the Website Scraping scanner menu\n99: Exit Application')
  print(colored('2.About Developper', 'yellow'))
  print('The developer named Frenchcamp is a French child who is passionate about programming and cyberseurity, he is currently 11 years old.\nWebsite: https://frenchcamp.github.io/fr/')
  print(colored('2.About Axy', 'yellow'))
  print('Axy is a Web Scraping application developed by FrenchCamp.\nWebsite : https://frenchcamp.github.io/fr/axy.html ')
  chx = input('>>> ')

 elif chx == '99':
   sys.exit()

 elif chx == 'clear':
  os.system('clear')
  chx = input('>>> ')
 
 elif chx == 'report':
  print('A bug, a problem? you can report it with the following email address:')
  print(colored('frenchcamp.axy.bug@gmail.com', 'blue'))
  chx = input('>>> ')


 else:
  print(''+chx+': invalid command')
  chx = input('>>> ')


