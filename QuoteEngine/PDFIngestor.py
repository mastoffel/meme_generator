import subprocess
from typing import List
import os
import random

from .ingestorInterface import IngestorInterface
from .quoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest extension.')
        
        os.makedirs('tmp', exist_ok=True)
        tmp = f'./tmp/{random.randint(0, 1000000000)}.txt'
        call = subprocess.call(['pdftotext', path, tmp])

        quotes = []

        with open(tmp, 'r', encoding='utf-8-sig') as f:
            for line in f:
                line = line.strip('\n\r').strip()
                if len(line) > 0:
                    #print(line)
                    quote = [x.strip() for x in line.split("-")]
                    quotes.append(QuoteModel(quote[0], quote[1]))
        
        os.remove(tmp)
        return quotes
