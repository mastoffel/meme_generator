from abc import abstractmethod
from tkinter import font
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

class MemeEngine():
    """Generate a meme."""
    def __init__(self, output_dir):
        self.output_dir = output_dir
    
    def make_meme(self, img, text, author, width=500): 
        """Create a meme.

        Args:
            img (str, optional): Path to img.
            text (str, optional): Meme body.
            author (str, optional): Meme author.
            width (int, optional): Width of meme. Defaults to 500 px.

        Returns:
        Path to meme.
        
        Raises:
            ValueError: _description_
        """
        print(self.output_dir)
        if width > 500:
            raise ValueError("Maximum width 500")
        with Image.open(img) as im:
            w_to_h = im.size[1] / im.size[0]
            new_height = int(width * w_to_h)
            new_im = im.resize((width, new_height))
        
        meme_text = text + "\n - " + author
            
        #check that text doesn't go outside
        for font_size in range(30, 1, -1):
            fnt = ImageFont.truetype("/Library/Fonts/Comic Sans MS.ttf", font_size)
            if fnt.getsize(meme_text)[0] < width-1:
                break
                    
        draw = ImageDraw.Draw(new_im)
        txt_coord1 = random.choice(range(1, width - fnt.getsize(meme_text)[0])) 
        txt_coord2 = random.choice(range(1 + fnt.getsize(meme_text)[1], new_height - fnt.getsize(meme_text)[1]))
            
        draw.text((txt_coord1, txt_coord2), meme_text, font = fnt)
        im_name = str(random.randrange(1e8)) + ".png"
        new_im.save(self.output_dir + "/" + im_name)
        outfile = self.output_dir + "/" + im_name
        return(outfile)

