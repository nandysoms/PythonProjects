import random
import urllib.request

def get_image(url):
    name = random.randrange(1,500)
    fname = str(name)+".mp4"
    urllib.request.urlretrieve(url,fname)

get_image('https://www.facebook.com/shamji.raj.3/videos/227613168043564/')