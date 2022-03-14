import random
from english_words import english_words_lower_alpha_set
words=[]
for i in english_words_lower_alpha_set:
    if len(i)==5:
        words.append(i)
print(random.choice(words))