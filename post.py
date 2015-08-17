#!/usr/bin/env python

# Posts a random bark string to twitter

import random

#Uses https://github.com/bear/python-twitter
import twitter

def genPost():
    words = ['bark','woof','ruff']
    upperWords = ['Bark', 'Woof', 'Ruff']
    punc = ['!', '.']
    numWords = random.randint(1, 10)
    s = ''
    sentenceBegin = True
    for x in range(numWords):
        if sentenceBegin:
            s += random.choice(upperWords)
            sentenceBegin = False
        else:
            s += random.choice(words)
        
        if random.random() > .5 or x == numWords-1:
            sentenceBegin = True
            s += random.choice(punc)
        s += ' '

    return s

if __name__ == "__main__":
    api = twitter.Api(consumer_key='Not',
                      consumer_secret='posting',
                      access_token_key='private',
                      access_token_secret='keys')
    api.PostUpdate(genPost()).text
    
