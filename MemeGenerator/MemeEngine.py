from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

class MemeEngine():
    
    def __init__(self, output_dir):
        self.output_dir = output_dir
    
    @classmethod
    def make_meme(cls, img, text, author, width):
        with Image.open(img) as im:
            w_to_h = im.size[0] / im.size[1]
            new_height = int(width * w_to_h)
            new_im = im.resize((width, new_height))
            
            draw = ImageDraw.Draw(new_im)
            txt_coord1 = random.choice(range(1, width))
            txt_coord2 = random.choice(range(1, new_height))
            
            draw.text((txt_coord1, txt_coord2), "hello")
            new_im.save(output_dir + "/mymeme.png")