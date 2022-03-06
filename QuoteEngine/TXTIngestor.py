from typing import List

from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel

class TXTIngestor(IngestorInterface):
    allowed_extensions = ['txt']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest extension.')
        
        out = []
        with open(path, 'r', encoding='utf-8-sig') as f:
            for line in f:
                quote = line.rstrip('\n').split("-")
                out.append(QuoteModel(quote[0], quote[1]))
        return out
