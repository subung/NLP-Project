#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup

url = 'https://insights.blackcoffer.com/what-if-the-creation-is-taking-over-the-creator/'
response = requests.get(url)
html = response.text


soup = BeautifulSoup(html, 'html.parser')


text = soup.article.get_text()
print(text)


# In[2]:


import chardet

def get_encoding(file_path):
    with open(file_path, 'rb') as f:
        result = chardet.detect(f.read())
        return result['encoding']

file_encoding = get_encoding('C:\\Program Files\\Python310\\Project\\URL_ID1.txt')

from textblob import TextBlob

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()
    
blob = TextBlob(text)

print(blob.sentiment)


# In[3]:


from textblob import TextBlob

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()

blob = TextBlob(text)
sentiment = blob.sentiment

positive_score = sentiment.polarity

print("Positive Score:", positive_score)


# In[4]:


from textblob import TextBlob

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()
blob = TextBlob(text)
sentiment = blob.sentiment

negative_score = sentiment.polarity

print("negative_score:", negative_score)


# In[5]:


with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()

sentences = text.split(".")
total_words = 0
for sentence in sentences:
    words = sentence.split()
    total_words += len(words)

average_sentence_length = total_words / len(sentences)

print("Average Sentence Length:", average_sentence_length)


# In[6]:


import nltk
from nltk.tokenize import word_tokenize

def is_complex(word):
    if len(word) >= 6:
        return True
    else:
        return False

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()

tokens = word_tokenize(text)

complex_words = [word for word in tokens if is_complex(word)]

percentage_complex_words = (len(complex_words) / len(tokens)) * 100

print("Percentage of Complex Words:", percentage_complex_words, "%")


# In[ ]:


import nltk
from nltk.tokenize import word_tokenize

def fog_index(text):
    tokens = word_tokenize(text)
    words_per_sentence = len(tokens) / len(text.split("."))
    syllables_per_word = 0
    for word in tokens:
        syllables = nltk.corpus.cmudict.dict().get(word.lower(), [])
        if len(syllables) > 0:
            syllables_per_word += len([syl for syl in syllables[0] if syl[-1].isdigit()])
    fog = 0.4 * ((words_per_sentence) + 100 * (syllables_per_word / len(tokens)))
    return fog

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()
    
fog = fog_index(text)

print("FOG Index:", fog)


# In[7]:


import nltk
from nltk.tokenize import word_tokenize

def avg_words_per_sentence(text):
    tokens = word_tokenize(text)
    sentences = nltk.sent_tokenize(text)
    avg_words = len(tokens) / len(sentences)
    return avg_words

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()

avg_words = avg_words_per_sentence(text)

print("Average Number of Words per Sentence:", avg_words)


# In[8]:


import nltk
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize

def complex_word_count(text):
    d = cmudict.dict()
    tokens = word_tokenize(text)
    complex_word_count = 0
    for word in tokens:
        syllables = d.get(word.lower(), [])
        if len(syllables) > 0:
            syllable_count = len([syl for syl in syllables[0] if syl[-1].isdigit()])
            if syllable_count >= 3:
                complex_word_count += 1
    return complex_word_count

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()
    
complex_word_count = complex_word_count(text)

print("Complex Word Count:", complex_word_count)


# In[9]:


import nltk
from nltk.tokenize import word_tokenize

def word_count(text):
    tokens = word_tokenize(text)
    return len(tokens)

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()

word_count = word_count(text)

print("Word Count:", word_count)


# In[10]:


import nltk
from nltk.corpus import cmudict
from nltk.tokenize import word_tokenize

def avg_syllables_per_word(text):
    d = cmudict.dict()
    tokens = word_tokenize(text)
    syllable_count = 0
    for word in tokens:
        syllables = d.get(word.lower(), [])
        if len(syllables) > 0:
            syllable_count += len([syl for syl in syllables[0] if syl[-1].isdigit()])
    avg_syllables = syllable_count / len(tokens)
    return avg_syllables

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()

avg_syllables = avg_syllables_per_word(text)

print("Average Number of Syllables per Word:", avg_syllables)


# In[11]:


import re

pronouns = ['I', 'me', 'my', 'mine', 'you', 'your', 'yours', 'he', 'him', 'his', 'she', 'her', 'hers', 'it', 'its', 'we', 'us', 'our', 'ours', 'they', 'them', 'their', 'theirs']
pronoun_pattern = re.compile('|'.join(pronouns), re.IGNORECASE)

def count_pronouns(text):
  return len(re.findall(pronoun_pattern, text))

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()

pronoun_count = count_pronouns(text)
print(f'Number of personal pronouns: {pronoun_count}')


# In[12]:


def avg_word_length(text):
  words = text.split()
  word_lengths = [len(word) for word in words]
  avg_length = sum(word_lengths) / len(words)
  return avg_length

with open('C:\\Program Files\\Python310\\Project\\URL_ID1.txt', 'r', encoding=file_encoding) as f:
    text = f.read()
    
avg_length = avg_word_length(text)
print(f'Average word length: {avg_length:.2f}')


# In[ ]:




