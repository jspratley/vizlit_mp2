import nltk, pprint, re
import json
from nltk import word_tokenize
from urllib import request
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords

raw = open('docs\stoker-dracula.txt').read()

words = nltk.wordpunct_tokenize(raw)
sentences = nltk.sent_tokenize(raw)
paragraphs = str.split(raw, "\n\n")

my_stopwords = open('docs\my_stopwords.txt').read()
my_stopwords = nltk.word_tokenize(my_stopwords)
porter = nltk.PorterStemmer()

#Processing each paragraph
p_words = []
s_words = []
for pa in paragraphs:
    pa = nltk.sent_tokenize(pa)
    for p in pa:
        p = nltk.wordpunct_tokenize(p)
        p = [s.lower() for s in p]
        p = sorted(p)
        p = [s for s in p if not s in stopwords.words('english')]
        p = [s for s in p if not s in my_stopwords]
        p = [re.sub('\.', '', s) for s in p]
        p = [s for s in p if s.isalpha()]
        p = [porter.stem(s) for s in p]
        s_words.append(p)
    p_words.append(s_words)
    s_words = []

out_data = {'word': 'time', 'children': []}

temp_p = []
temp_data = {'word': '', 'children': []}
temp_s = []
for p in p_words:
    for s in p:
        temp_p += s
        if s != []:
            word = s[0]
        temp_dict_s = {'word': word}
        temp_s.append(temp_dict_s)
    freq_dist = nltk.FreqDist(temp_p)
    needed_word = freq_dist.most_common(1)[0][0]
    temp_dict = {'word': needed_word, 'children': [temp_s]}
    if temp_dict not in out_data['children']:
        out_data['children'].append(temp_dict)
    temp_s = []

with open('data/data.json','w') as outfile:
    json.dump(out_data, outfile, sort_keys=True, indent=4, ensure_ascii=False)
