import nmap
import time
import os
import sys
from bs4 import BeautifoulSoup
from termcolor import colored

def scan():
 print('')


chx = input('[Scan] >>> ')
if chx == 'scan -si':
 ip = input('[Scan -> Adress] >>> ')
  print('----------')
  print(colored('Stats', 'red'))
  print('----------')

  print('Title ')
  title = ip.BeautifoulSoup('title')
  print(title)
  print('HTML balises ')
  balises = ip.BeautifoulSoup.herf(a)
  print('balises')

