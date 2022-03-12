from typing import List
import docx

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel

class DOCXIngestor(IngestorInterface):
    """A class to read quotes from .docx files."""
    
    allowed_extensions = ['docx']
    
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('Cannot ingest extension.')
        
        out = []
        
        doc = docx.Document(path)
        
        for line in doc.paragraphs:
            if line.text != "":
                quote = [x.replace('"',"").strip() for x in line.text.rstrip('\n').split("-")]
            out.append(QuoteModel(quote[0], quote[1]))
        
        return out
