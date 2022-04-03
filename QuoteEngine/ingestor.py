from typing import List

from QuoteEngine.TXTIngestor import TXTIngestor

from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .DOCXIngestor import DOCXIngestor
from .PDFIngestor import PDFIngestor
from .QuoteModel import QuoteModel


class Ingestor(IngestorInterface):
    """A class to read quotes from files of different types."""
    
    ingestors = [CSVIngestor, TXTIngestor, DOCXIngestor, PDFIngestor]
    
    @classmethod
    def parse(cls, path: str):
        """Parse a file and return a list of QuoteModels."""
        
        for ingestor in cls.ingestors:
            try:
                if ingestor.can_ingest(path):
                    return ingestor.parse(path)
            except TypeError:
                print("Fileformat not readable.")