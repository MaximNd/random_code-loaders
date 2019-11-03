#!/usr/bin/env python3
from random import randrange, choice
from printer import clear_screen
from TerminalRandomCodePrinter import TerminalRandomCodePrinter
from Terminal256RandomCodePrinter import Terminal256RandomCodePrinter
from ProgressPrinter import ProgressPrinter
from ErrorPrinter import ErrorPrinter
from pygments.formatters.terminal import TerminalFormatter
from pygments.formatters.terminal256 import Terminal256Formatter
from themes.dracula import dracula

error_printer = ErrorPrinter()

random_code_printer_default = TerminalRandomCodePrinter(error_printer)
random_code_printer_256 = Terminal256RandomCodePrinter(error_printer)
random_code_printer_256_dracula = Terminal256RandomCodePrinter(error_printer)
random_code_printer_256_dracula.init_formatter(style=dracula.DraculaStyle)

progress_printer = ProgressPrinter(error_printer)


random_code_printers = [ 
  random_code_printer_default,
  random_code_printer_256,
  random_code_printer_256_dracula
]

if __name__ == "__main__":
  clear_screen()
  while True:
    try:
      mode = randrange(10)
      if mode > 2:
        choice(random_code_printers).print_some_random_shit()
      else:
        pass
        progress_printer.print_some_random_shit()
      clear_screen()
    except KeyboardInterrupt:
      clear_screen()
      exit(0)
    except:
      clear_screen()
      error_printer.print_error()
