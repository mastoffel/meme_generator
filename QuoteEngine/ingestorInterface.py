from abc import ABC, abstractmethod
from xmlrpc.client import boolean
from typing import List

from .quoteModel import QuoteModel

class IngestorInterface(ABC):
    
    allowed_extensions = []
    
    def __init_(self, path: str):
        self.path = path
    
    @classmethod
    def can_ingest(cls, path: str) -> boolean:
        extension = path.split('.')[-1]
        return extension in cls.allowed_extensions
    
    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
        
    