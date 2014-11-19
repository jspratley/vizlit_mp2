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

#My own stopwords, in addition to nltk's
my_stopwords = open('docs\my_stopwords.txt').read()
my_stopwords = nltk.word_tokenize(my_stopwords)
porter = nltk.PorterStemmer()

#Processing each paragraph (removes unnecessary data & formats it)
p_words = []
s_words = []
for pa in paragraphs:
    pa = nltk.sent_tokenize(pa)
    for p in pa:
        p = nltk.wordpunct_tokenize(p)
        p = [s.lower() for s in p]
        p = [s for s in p if not s in stopwords.words('english')]
        p = [s for s in p if not s in my_stopwords]
        p = [re.sub('\.', '', s) for s in p]
        p = [s for s in p if s.isalpha()]
        p = [porter.stem(s) for s in p]
        #Clean up words that will appear on surface (too many for leaves)
        p = ['country' if s=='countri' else s for s in p]
        p = ['arrive' if s=='arriv' else s for s in p]
        s_words.append(p)
    p_words.append(s_words)
    s_words = []

out_data = {'word': 'time', 'children': []}

temp_p = []
temp_data = {'word': '', 'children': []}
temp_s = []
#Placing the data into the correct format for json
for p in p_words:
    for s in p:
        temp_p += s
        if s != []:
            #If there is no most frequent word, use the first word.
            freqdist = nltk.FreqDist(s);
            if freqdist.most_common(1) != []:
                word = freqdist.most_common(1)[0][0]
            else:
                word = s[0]
        #Give a size of 5, so that circle packing works.
        temp_dict_s = {'word': word, 'size': 5}
        temp_s.append(temp_dict_s)
    freq_dist = nltk.FreqDist(temp_p)
    needed_word = freq_dist.most_common(1)[0][0]
    temp_dict = {'word': needed_word, 'children': temp_s}
    if temp_dict not in out_data['children']:
        out_data['children'].append(temp_dict)
    temp_s = []

with open('data/data.json','w') as outfile:
    json.dump(out_data, outfile, sort_keys=True, indent=4, ensure_ascii=False)
