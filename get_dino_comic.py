import random
import HTMLParser

from bs4 import BeautifulSoup


class DinoComics(object):

    def __init__(self):
        with open('everywordindinosaurcomicsOHGOD_cleaned.xml') as f:
            soup = BeautifulSoup(f)
        self.transcriptions = [x for x in list(soup.transcriptions)
                          if len(x) > 1]
        self.numcomics = len(self.transcriptions)
        self.htmlparse = HTMLParser.HTMLParser()

    def get_random_dino_comic(self):
        return self.get_dino_comic_by_index(random.randrange(self.numcomics))

    def get_dino_comic_by_index(self, dino_index):
        if dino_index >= self.numcomics:
            dino_index = 0
        return [self.htmlparse.unescape(line.string)
                for line in self.transcriptions[dino_index].panel
                if ':' in line.string]


if __name__ == "__main__":
    dinocomics = DinoComics()
    print dinocomics.get_random_dino_comic()
