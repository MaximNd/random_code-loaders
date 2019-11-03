from AbstractRandomCodePrinter import AbstractRandomCodePrinter
from pygments.formatters import terminal
from pygments.console import ansiformat

class TerminalRandomCodePrinter(AbstractRandomCodePrinter):
  def init_formatter(self, **kwargs):
    self.formatter = terminal.TerminalFormatter(**kwargs)

  def get_color(self, token):
    return self.formatter._get_color(token)

  def get_colorized_symbol(self, symbol, color):
    return ansiformat(color, symbol)