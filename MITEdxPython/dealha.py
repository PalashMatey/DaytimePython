import random
import numpy as np
hand = {}
vowels = 'aeiou'
numVowels = 7/3
for i in range(numVowels):
	x = vowels[random.randrange(0,len(vowels))]
	hand[x] = hand.get(x,0)+1

