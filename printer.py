import os
from pygments.console import ansiformat

def clear_screen():
  os.system('cls' if os.name == 'nt' else 'clear')

def print_l(text):
  print(text, end = '', flush=True)

def print_l_colorized(text, color):
  print(ansiformat(color, text), end = '', flush=True)