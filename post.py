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
    hashTag = False
    sentenceBegin = True
    for x in range(numWords):
        if sentenceBegin:
            if random.random() > .66:
                hashTag = True
                s += '#'
            s += random.choice(upperWords)
            sentenceBegin = False
        else:
            if hashTag:
                s += random.choice(upperWords)
            else:
                s += random.choice(words)
        
        if random.random() > .5 or x == numWords-1:
            sentenceBegin = True
            if not hashTag: 
                s += random.choice(punc)
            hashTag = False
        if not hashTag:
            s += ' '

    return s

import ConfigParser

if __name__ == "__main__":
    config = ConfigParser.RawConfigParser()
    config.read('private.conf')
    api = twitter.Api(consumer_key=config.get('TwitterKeys','consumer_key'),
                      consumer_secret=config.get('TwitterKeys','consumer_secret'),
                      access_token_key=config.get('TwitterKeys','access_token'),
                      access_token_secret=config.get('TwitterKeys', 'access_token_secret'))
    api.PostUpdate(genPost())
    
