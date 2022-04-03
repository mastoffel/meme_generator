from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine


print(Ingestor.parse("_data/DogQuotes/DogQuotesPDF.pdf")[1])
print(Ingestor.parse("_data/DogQuotes/DogQuotesDOCX.docx")[1])

quote = Ingestor.parse("_data/DogQuotes/DogQuotesPDF.pdf")[1]
quote.author
quote.body

meme = MemeEngine('tmp')
meme.output_dir
out = meme.make_meme('_data/photos/dog/xander_1.jpg', quote.body, quote.author, width = 300)

if __name__ == "__main__":
    print(Ingestor.parse("_data/DogQuotes/DogQuotesPDF.pdf")[1])
    print(Ingestor.parse("_data/DogQuotes/DogQuotesDOCX.docx")[1])
    

test = "hello"
type(test)