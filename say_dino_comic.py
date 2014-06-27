import time

import pyttsx

class DinoComicSayer(object):

    def __init__(self):
        self.engine = pyttsx.init()

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        self.engine.endloop()
