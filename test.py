from QuoteEngine import Ingestor

print(Ingestor.parse("_data/DogQuotes/DogQuotesPDF.pdf")[1])
print(Ingestor.parse("_data/DogQuotes/DogQuotesDOCX.docx")[1])

if __name__ == "__main__":
    print(Ingestor.parse("_data/DogQuotes/DogQuotesPDF.pdf")[1])
    print(Ingestor.parse("_data/DogQuotes/DogQuotesDOCX.docx")[1])