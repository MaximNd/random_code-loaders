from abc import ABC, ABCMeta, abstractmethod

class ErrorCausable(ABC):
  __metaclass__ = ABCMeta
  
  @abstractmethod
  def cause_error(self): raise NotImplementedError

  @abstractmethod
  def is_error_occurred(self): raise NotImplementedError