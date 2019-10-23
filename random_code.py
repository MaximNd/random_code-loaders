import time
from random import randrange
import sys


CRED = '\033[91m'
CEND = '\033[0m'

def clear_screen():
  print("\033c", end="")

def print_l(text):
  print(text, end = '', flush=True)

def print_error_by_mode_and_type(error_text, mode, error_type):
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
    print_error_by_mode_and_type(CRED + "SOME RANDOM ERROR IS OCCURED ON YOUR COMPUTER!!! PLEASE STAND UP AND LOOK UNDER YOUR TABLE!! MAYBE YOUR COMPUTER IS NOT PLUGGED IN!! HAHA JEBAITED!!!! THE IS NO OUTLET UNDER THE TABLE!!!" + CEND, rand_error_mode, rand_error_type)
    print_error_by_mode_and_type(CRED + "LOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOL!!!" + CEND, rand_error_mode, rand_error_type)
  print()

def print_error():
  
  error_1 = CRED + "ERROR!, ERROR!, ERROR!" + CEND
  error_2 = CRED + "!!!!!!!!!!!!!!!!!!!!!!" + CEND
  error_3 = CRED + "FATAL ERROR!, YOUR LIFE IN DANGER!" + CEND
  for _ in range(15):
    mode = randrange(2)
    print_error_by_mode_and_type(error_1, mode, 1)
    print_error_by_mode_and_type(error_2, mode, 2)
    print_error_by_mode_and_type(error_1, mode, 1)
    print_error_by_mode_and_type(error_2, mode, 2)
    print_error_by_mode_and_type(error_3, mode, 3)
    print_error_by_mode_and_type(error_2, mode, 2)
    print()
    time.sleep(0.05)

def get_sleep_acc():
  sleep_acc_n = randrange(1, 100)
  sleep_acc = 0
  if sleep_acc_n >= 50:
    sleep_acc = sleep_acc_n / 150
  else:
    sleep_acc = -(sleep_acc_n / 150)
  return sleep_acc

def get_sleep_time(start_time, sleep_acc):
  sleep_time = abs(start_time + start_time * sleep_acc)
  if sleep_time <= 0:
    sleep_time = 0.05
  return sleep_time

def get_is_error(max_n=100):
  return randrange(max_n) == 0





def print_code(file):
  sleep_acc = get_sleep_acc()
  for line in file:
    is_error = get_is_error()
    if is_error:
      print_error()
      return
    for ch in line:
      print_l(ch)
      if ch == '\n':
        sleep_acc = get_sleep_acc()
        time.sleep(get_sleep_time(0.3, sleep_acc))
      elif ch == ' ':
        sleep_acc = get_sleep_acc()
        time.sleep(get_sleep_time(0.2, sleep_acc))
      else:
        time.sleep(get_sleep_time(0.05, sleep_acc))

# Print iterations progress
def print_progress_h(iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', not_fill = '-', printEnd = "\r", completed_message = ''):
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

def print_progress(prefix, suffix, fill, not_fill, length, completed_message):
  # A List of Items
  items = list(range(0, int(d_length)))
  l = len(items)
  # Initial call to print 0% progress
  print_progress_h(0, l, prefix=prefix, suffix=suffix, fill=fill, not_fill=not_fill, length=int(length), completed_message=completed_message)
  for i, item in enumerate(items):
    is_error = get_is_error(1000)
    if is_error:
      print()
      print_error()
      return
    sleep_acc = get_sleep_acc()
    sleep_time = get_sleep_time(0.1, sleep_acc)
    
    time.sleep(sleep_time)
    # Update Progress Bar
    print_progress_h(i + 1, l, prefix=prefix, suffix=suffix, fill=fill, not_fill=not_fill, length=int(length), completed_message=completed_message)



while True:
  mode = randrange(2)
  if mode == 0:
    file_number = randrange(20)
    with open('code' + str(file_number) + '.txt', 'r') as file:
      print_code(file)
    clear_screen()
  elif mode == 1:
    with open('progress.txt', 'r') as file:
      for line in file:
        [d_prefix, d_suffix, d_fill, d_not_fill, d_length, d_completed_message] = line.split(',')
        print_progress(d_prefix, d_suffix, d_fill, d_not_fill, d_length, d_completed_message)
    clear_screen()
