from typing import List
import pandas as pd

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class CSVIngestor(IngestorInterface):
    """A class to read quotes from CSV files."""
    allowed_extensions = ['csv']
            
    @classmethod
    def parse(cls, path: str):
        """Parse a CSV file and return a list of QuoteModels.
        
        Args:
            path(str): The path to the .csv file to be parsed.
        """

        if not cls.can_ingest(path):
            raise Exception('Cannot ingest extension.')
        
        out = []
        quotes = pd.read_csv(path)
        for index, row in quotes.iterrows():
            out.append(QuoteModel(row[0], row[1]))
        return out

    