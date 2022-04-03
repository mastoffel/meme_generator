import random
import os
import requests
from QuoteEngine import Ingestor
from MemeGenerator import MemeEngine
from flask import Flask, render_template, abort, request

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    def flatten(t):
        return [item for sublist in t for item in sublist]
    
    quotes = flatten([Ingestor.parse(quote) for quote in quote_files])

    images_path = "./_data/photos/dog/"

    imgs = []
    for file in os.listdir(images_path):
        if file.endswith(('.jpg', 'jpeg', 'png')):
            imgs.append(images_path + file)
      
    return quotes, imgs

quotes, imgs = setup()

@app.route('/')
def meme_rand():
    """ Generate a random meme """

    quotes, imgs = setup()
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    # 1. Use requests to save the image from the image_url
    #    form param to a temp local file.
    # 2. Use the meme object to generate a meme using this temp
    #    file and the body and author form paramaters.
    # 3. Remove the temporary saved image.
    image_url = request.form.get('image_url')
    img_content = requests.get(image_url, stream=True).content
    tmp_name = str(random.randint(0,100000000))
    tmp = f'./tmp/{tmp_name}.png'
    with open(tmp, 'wb') as img:
        img.write(img_content)
    # save image to temp file
    body = request.form.get('body')
    author = request.form.get('author')
    
    meme = MemeEngine('./static')
    path = meme.make_meme(tmp, body, author)
    os.remove(tmp)
    
    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
