from AbstractRandomCodePrinter import AbstractRandomCodePrinter
from pygments.formatters import terminal256
from pygments.console import ansiformat

class Terminal256RandomCodePrinter(AbstractRandomCodePrinter):
  def init_formatter(self, **kwargs):
    self.formatter = terminal256.Terminal256Formatter(**kwargs)

  def get_color(self, token):
    return self.formatter.style_string[str(token)]

  def get_colorized_symbol(self, symbol, color):
    return color[0] + symbol + color[1]