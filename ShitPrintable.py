from abc import ABC, ABCMeta, abstractmethod

class ShitPrintable(ABC):
  __metaclass__ = ABCMeta

  @abstractmethod
  def print_some_random_shit(self): raise NotImplementedError
    