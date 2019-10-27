from abc import ABC, ABCMeta, abstractmethod

class ErrorPrintable(ABC):
  __metaclass__ = ABCMeta
  
  @abstractmethod
  def print_error(self): raise NotImplementedError