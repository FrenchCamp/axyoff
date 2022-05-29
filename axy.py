#!/usr/bin/python3

 # Importation des modules
from bs4 import BeautifulSoup
import requests
import os
import sys
from termcolor import colored
from art import *

sys.path.append('__init__')

 # Rensaignement de l'adresse
ip = input('[Scraping -> Adress] >>> ')
os.system('clear')

 # Main
def main():
 chx = input('>>> ')
tprint('Axy')
print(colored('  By FrenchCamp (BETA VERSION)', 'green'))
print(colored('-------------------------------------------', 'red'))

print(colored('Use "help" for list of commands ', 'cyan'))

 # Composants pour faire fonctionner l'application
rep = requests.get(ip)
soup = BeautifulSoup(rep.text, 'html.parser')
chx = input('>>> ')

 # Boucle infinie
while True:
 
  # 1 : Affiche le code
 if chx == 'text':
    print(soup)
    chx = input('>>> ')

  # 2 : Rechercher un élément dans le code
 elif chx == 'finder':
   find = input('[Scraping -> Find element] >>> ')
    item = soup.find_all(find)
    print(item)
    chx = input('>>> ')

  # 3 : Efface 
 elif chx == 'cls':
    os.system('clear')

  # 4 : Affiche l'aide et autres informations
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

  # 5 : Quitter l'application
 elif chx == '99':
   sys.exit()

  # 6 : Rapporter un bug
 elif chx == 'report':
  print('A bug, a problem? you can report it with the following email address:')
  print(colored('frenchcamp.axy.bug@gmail.com', 'blue'))
  chx = input('>>> ')

  # Si autre commande éffectuée
 else:
  print(''+chx+': invalid command')
  chx = input('>>> ')



