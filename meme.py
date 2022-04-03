import argparse
import os
import random
from xml.dom.expatbuilder import parseString
from QuoteEngine import Ingestor, QuoteModel
from MemeGenerator import MemeEngine


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/hamster/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/HamsterQuotes/HamsterQuotes.txt']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine('./tmp')
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
  
    parser = argparse.ArgumentParser(description="Make a meme.")
    parser.add_argument('--path', type=str, 
                        help='Path to image (png or jpg)')
    parser.add_argument('--body', type=str, 
                        help = 'Meme text body')
    parser.add_argument('--author', type=str,
                        help='Meme text author')
    args = parser.parse_args()
    print(args.path)
    print(generate_meme(args.path, args.body, args.author))
