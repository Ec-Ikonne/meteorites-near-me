'''import math

print(math.pi)
math.e
math.log(math.e)

math.floor(15.8)
math.ceil(15.8)

import random

random.random()
random.randint(10, 500)

random.choice(["happy", "sad", "unemotional"])

moods = ("happy", "sad", "unemotional")

/*random includes the start and last numbers while range does not include the last and first numbers  */


values = range(1, 14)
list(values)

cards = []

for mood in moods:
    for v in values:
        cards.append("{0} of {1}".format(v, mood))

random.choice(cards)


from random import shuffle
shuffle(cards)


import itertools as iter
for num in iter.chain([1,2,3], [4,5,6]):
    print(num)

import time
time.localtime()

now = time.strftime("%H:%M::%S")
now

import zipfile
from zipfile import ZipFile

'''
import requests
resp = requests.get('https://nasa.gov')

resp.status_code
len(resp.text)


meteor_resp = requests.get('https://data.nasa.gov/resource/y77d-th95.json')

meteor_resp.status_code
meteor_resp.text
meteor_data = meteor_resp.json()

type(meteor_data)

meteor_data[0]

for meteor in meteor_data:
    type(meteor) 
