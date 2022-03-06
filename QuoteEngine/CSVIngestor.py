from typing import List
import pandas as pd

from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    allowed_extensions = ['csv']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest extension.')
        
        out = []
        quotes = pd.read_csv(path)
        for index, row in quotes.iterrows():
            out.append(QuoteModel(row[0], row[1]))
        return out

    