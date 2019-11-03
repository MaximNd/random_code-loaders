import time
import math
from random import randrange
from printer import print_l, clear_screen, print_l_colorized
from ShitPrintable import ShitPrintable
from ErrorCausable import ErrorCausable
from ErrorPrintable import ErrorPrintable
from ErrorPrinter import ErrorPrinter
from pygments.formatter import Formatter
from pygments.lexers import python as py_l
from pygments.lexers import c_cpp as cpp_l
from pygments.lexers import javascript as js_l
from pygments.lexers import asm as asm_l
from pygments.lexers import haskell as hs_l
from pygments.lexers import data as data_l
from pygments.lexers import dotnet as dnet_l
from pygments.lexer import Lexer
from pygments.lexers import python as pl
from pygments.formatters import terminal as tf

lexers = {
  'py': py_l.PythonLexer,
  'cpp': cpp_l.CppLexer,
  'js': js_l.JavascriptLexer,
  'ts': js_l.TypeScriptLexer,
  'asm': asm_l.GasLexer,
  'haskell': hs_l.HaskellLexer,
  'json': data_l.JsonLexer,
  'cs': dnet_l.CSharpLexer
}

langs = {
  'python': 'py',
  'cpp': 'cpp',
  'javascript': 'js',
  'typescript': 'ts',
  'assembly': 'asm',
  'haskell': 'haskell',
  'json': 'json',
  'cs': 'cs'
}

files_types = [
  langs['cpp'],
  langs['cpp'],
  langs['javascript'],
  langs['cpp'],
  langs['typescript'],
  langs['typescript'],
  langs['typescript'],
  langs['python'],
  langs['python'],
  langs['cpp'],
  langs['python'],
  langs['assembly'],
  langs['assembly'],
  langs['assembly'],
  langs['assembly'],
  langs['json'],
  langs['cs'],
  langs['cs'],
  langs['haskell'],
  langs['haskell']
]

class AbstractRandomCodePrinter(ShitPrintable, ErrorCausable):
  def __init__(self, error_printable: ErrorPrintable):
    self.sleep_acc = 0
    self.error_chance_num = 400
    self.error_printable = error_printable
    self.formatter = None

  def init_formatter(self, **kwargs): raise NotImplementedError

  def get_color(self, token): raise NotImplementedError

  def get_colorized_symbol(self, symbol, color): raise NotImplementedError

  def print_some_random_shit(self):
    file_number = randrange(20)
    file_type = files_types[file_number]
    with open('code' + str(file_number) + '.txt', 'r') as file:
      lexer = lexers[file_type]()
      self.print_code(file, lexer)

  def print_code(self, file, lexer: Lexer):
    if (not self.formatter):
      self.init_formatter()
    code = file.read()
    colors_indices = []
    color_idx = 0
    char_idx = 0
    for index, token, text in lexer.get_tokens_unprocessed(code):
      colors_indices.append({ 'index': index, 'text': text, 'color': self.get_color(token) })
    
    file.seek(0)
    self.sleep_acc = self.get_sleep_acc()
    for line in file:
      if self.is_error_occurred():
        return self.cause_error()

      for i, ch in enumerate(line):
        if ch == '\n':
          self.sleep_acc = self.get_sleep_acc()
          time.sleep(self.get_sleep_time(0.3, self.sleep_acc))
        elif ch == ' ' and i < len(line) and line[i + 1] != ' ':
          self.sleep_acc = self.get_sleep_acc()
          time.sleep(self.get_sleep_time(0.2, self.sleep_acc))
        elif ch == ' ' and i < len(line) and line[i + 1] == ' ':
          time.sleep(self.get_sleep_time(0.01, self.sleep_acc))
        else:
          time.sleep(self.get_sleep_time(0.05, self.sleep_acc))
        
        
        color_data = colors_indices[color_idx]
        next_color_data = colors_indices[color_idx + 1] if color_idx + 1 < len(colors_indices) else {'index': math.inf}
        
        if char_idx >= next_color_data['index'] - 1:
          color_idx += 1
          
        print_l(self.get_colorized_symbol(ch, color_data['color']))
        char_idx += 1
  
  def get_sleep_acc(self):
    sleep_acc_n = randrange(1, 100)
    sleep_acc = 0
    if sleep_acc_n >= 50:
      sleep_acc = sleep_acc_n / 150
    else:
      sleep_acc = -(sleep_acc_n / 150)
    return sleep_acc

  def get_sleep_time(self, start_time, sleep_acc):
    sleep_time = abs(start_time + start_time * sleep_acc)
    if sleep_time <= 0:
      sleep_time = 0.05
    return sleep_time

  def is_error_occurred(self):
    return randrange(self.error_chance_num) == 0

  def cause_error(self):
    self.error_printable.print_error()
