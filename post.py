#!/usr/bin/env python

# Posts a random bark string to twitter

import random
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
    api = twitter.Api(consumer_key='rrMjgKHn8HSHrb4mJqbCpq3RP',
                      consumer_secret='l1SRjwtR3C7zrUuH4i37dFLkOonmRj07xo3oWvPck02dsFDSyu',
                      access_token_key='3345365117-5MlUzhUhedMVownUuqbZdAUyaesTwFV8LELhLnr',
                      access_token_secret='7QP3TlVJ84TagEQb0GnvFnHRZZj4WSI5LEXey9JQ3nBLB')
    api.PostUpdate(genPost()).text
    
