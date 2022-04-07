class QuoteModel():
    """Quote encapsulator
    
    Parameters
    ----------
    body: str
        The body of the quote
    author: str
        The author of the quote
    
    """
    def __init__(self, body, author):
        self.body = body
        self.author = author
    def __str__(self):
        return f'"{self.body}" - {self.author}'
