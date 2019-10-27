import time
from random import randrange
from printer import print_l
from ErrorPrintable import ErrorPrintable

CRED = '\033[91m'
CEND = '\033[0m'

class ErrorPrinter(ErrorPrintable):
  def print_error_by_mode_and_type(self, error_text, mode, error_type):
    if mode == 0:
      if error_type == 1:
        for ch in error_text:
          print_l(ch)
          time.sleep(0.02)
      elif error_type == 2:
        for ch in error_text:
          print_l(ch)
          time.sleep(0.01)
      elif error_type == 3:
        for ch in error_text:
          print_l(ch)
          time.sleep(0.03)
      else:
        for ch in error_text:
          print_l(ch)
          time.sleep(0.009)
    elif mode == 1:
      print_l(error_text)
    random_error_n = randrange(30)
    if random_error_n == 0:
      print()
      rand_error_mode = randrange(2)
      rand_error_type = randrange(4) + 1
      self.print_error_by_mode_and_type(CRED + "SOME RANDOM ERROR IS OCCURRED ON YOUR COMPUTER!!! PLEASE STAND UP AND LOOK UNDER YOUR TABLE!! MAYBE YOUR COMPUTER IS NOT PLUGGED IN!! HAHA JEBAITED!!!! THERE IS NO OUTLET UNDER THE TABLE!!!" + CEND, rand_error_mode, rand_error_type)
      self.print_error_by_mode_and_type(CRED + "LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL!!!" + CEND, rand_error_mode, rand_error_type)
    print()

  def print_error(self):
    error_1 = CRED + "ERROR!, ERROR!, ERROR!" + CEND
    error_2 = CRED + "!!!!!!!!!!!!!!!!!!!!!!" + CEND
    error_3 = CRED + "FATAL ERROR!, YOUR LIFE IN DANGER!" + CEND
    for _ in range(15):
      mode = randrange(2)
      self.print_error_by_mode_and_type(error_1, mode, 1)
      self.print_error_by_mode_and_type(error_2, mode, 2)
      self.print_error_by_mode_and_type(error_1, mode, 1)
      self.print_error_by_mode_and_type(error_2, mode, 2)
      self.print_error_by_mode_and_type(error_3, mode, 3)
      self.print_error_by_mode_and_type(error_2, mode, 2)
      print()
      time.sleep(0.05)