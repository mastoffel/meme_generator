from typing import List

from QuoteEngine.TXTIngestor import TXTIngestor

from .ingestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .TXTIngestor import TXTIngestor
from .DOCXingestor import DOCXIngestor
from .PDFIngestor import PDFIngestor
from .quoteModel import QuoteModel


class Ingestor(IngestorInterface):
    ingestors = [CSVIngestor, TXTIngestor, DOCXIngestor, PDFIngestor]
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)