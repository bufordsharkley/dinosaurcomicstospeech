import time
import sys

import pyttsx

_VOICES = {
    't-rex': 'com.apple.speech.synthesis.voice.Alex',
    't-rex off-panel': 'com.apple.speech.synthesis.voice.Alex',
    'dromiceiomimus': 'com.apple.speech.synthesis.voice.Victoria',
    'utahraptor': 'com.apple.speech.synthesis.voice.Bruce',
    'narrator': 'com.apple.speech.synthesis.voice.Ralph',
    'god': 'com.apple.speech.synthesis.voice.Fred',
    'the devil': 'com.apple.speech.synthesis.voice.Whisper',
    'devil': 'com.apple.speech.synthesis.voice.Whisper',
    'default': 'com.apple.speech.synthesis.voice.Fred'
    }


class DinoComicSayer(object):

    def __init__(self):
        self.engine = pyttsx.init()

    def say(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def say_as(self, text):
        # for this case, the text should be in form : 'T-Rex: I am saying something')
        speaker, utterance = text.split(': ', 1)
        try:
            speaker_id = _VOICES[speaker.lower()]
        except KeyError:
            print >> sys.stderr, 'ERROR WE DONT HAVE ANYBODY FOR: {}'.format(speaker)
            speaker_id = _VOICES['default']
        self.engine.setProperty('voice', speaker_id)
        self.say(utterance)

if __name__ == "__main__":
    sayer = DinoComicSayer()
    sayer.say('hello world')
    sayer.say_as('T-Rex: I know, right?')
