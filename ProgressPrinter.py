import time
from random import randrange
from printer import print_l, clear_screen, print_l_colorized
from ShitPrintable import ShitPrintable
from ErrorCausable import ErrorCausable
from ErrorPrintable import ErrorPrintable
from ErrorPrinter import ErrorPrinter


class ProgressPrinter(ShitPrintable, ErrorCausable):

  def __init__(self, error_printable: ErrorPrintable):
    self.error_chance_num = 1400
    self.error_printable = error_printable

  def print_some_random_shit(self):
    with open('progress.txt', 'r') as file:
      for line in file:
        [d_prefix, d_suffix, d_fill, d_not_fill, d_length, d_completed_message] = line.split(',')
        self.print_progress(d_prefix, d_suffix, d_fill, d_not_fill, d_length, d_completed_message)

  def is_error_occurred(self):
    return randrange(self.error_chance_num) == 0

  def cause_error(self):
    self.error_printable.print_error()

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

  # Print iterations progress
  def print_progress_h(self, iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', not_fill = '-', printEnd = "\r", completed_message = ''):
      """
      Call in a loop to create terminal progress bar
      @params:
          iteration   - Required  : current iteration (Int)
          total       - Required  : total iterations (Int)
          prefix      - Optional  : prefix string (Str)
          suffix      - Optional  : suffix string (Str)
          decimals    - Optional  : positive number of decimals in percent complete (Int)
          length      - Optional  : character length of bar (Int)
          fill        - Optional  : bar fill character (Str)
          printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
      """
      percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
      filledLength = int(length * iteration // total)
      bar = fill * filledLength + not_fill * (length - filledLength)
      print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
      # Print New Line on Complete
      if iteration == total: 
          print()
          print(completed_message)

  def print_progress(self, prefix, suffix, fill, not_fill, length, completed_message):
    # A List of Items
    items = list(range(0, int(length)))
    l = len(items)
    # Initial call to print 0% progress
    self.print_progress_h(0, l, prefix=prefix, suffix=suffix, fill=fill, not_fill=not_fill, length=int(length), completed_message=completed_message)
    for i, item in enumerate(items):
      if self.is_error_occurred():
        print()
        return self.cause_error()
      sleep_acc = self.get_sleep_acc()
      sleep_time = self.get_sleep_time(0.1, sleep_acc)
      
      time.sleep(sleep_time)
      # Update Progress Bar
      self.print_progress_h(i + 1, l, prefix=prefix, suffix=suffix, fill=fill, not_fill=not_fill, length=int(length), completed_message=completed_message)
