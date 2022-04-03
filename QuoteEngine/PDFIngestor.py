import subprocess
from typing import List
import os
import random

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class PDFIngestor(IngestorInterface):
    """A class to read quotes from PDF files."""
    allowed_extensions = ['pdf']
    
    @classmethod
    def parse(cls, path: str):
        """Parse a PDF file and return a list of QuoteModels.
        
        Args:
            path (str): The path to the PDF file.
        """
        
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
                    quote = [x.replace('"',"").strip() for x in line.split("-")]
                    quotes.append(QuoteModel(quote[0], quote[1]))
        
        os.remove(tmp)
        return quotes
