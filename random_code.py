from random import randrange
from printer import clear_screen
from RandomCodePrinter import RandomCodePrinter
from ProgressPrinter import ProgressPrinter
from ErrorPrinter import ErrorPrinter


error_printer = ErrorPrinter()

random_code_printer = RandomCodePrinter(error_printer)
progress_printer = ProgressPrinter(error_printer)

if __name__ == "__main__":
  while True:
    try:
      mode = randrange(10)
      if mode > 2:
        random_code_printer.print_some_random_shit()
      else:
        progress_printer.print_some_random_shit()
      clear_screen()
    except:
      clear_screen()
      error_printer.print_error()
