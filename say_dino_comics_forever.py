from get_dino_comic import DinoComics
from say_dino_comic import DinoComicSayer

dinocomics = DinoComics()
sayer = DinoComicSayer()
sayer.say('i am about to start reading dinosaur comics forever')

while True:
    try:
        comic = dinocomics.get_random_dino_comic()
        print comic
        for line in comic:
            sayer.say_as(line)
    except:
        pass
