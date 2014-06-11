'''
Program works for current directory
just be sure to have .txt data there
and to output results to a file or somewhere
'''

import os
import codecs
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer


def include_ext(ext):
    def compare(fn):
        return os.path.splitext(fn)[1] == ext
    return compare


def search_for_max(maax):
    max = 0
    item = None
    for z in maax.keys():
        if maax[z] > max:
            item = z
            max = maax[z]
    return item

#print 'Test............'
'''
vect = TfidfVectorizer(min_df=1)
tfidf = vect.fit_transform(["I'd like an apple",
                            "An apple a day keeps the doctor away",
                            "Never compare an apple to an orange",
                            "I prefer scikit-learn to Orange"])
'''
#print (tfidf * tfidf.T).A
#print 'End of test.................'

text_files = filter(os.path.isfile, os.listdir(os.curdir))  # files only
text_files = filter(include_ext(".txt"), text_files)

#print '................................................................'
print text_files
#print '................................................................'
documents = [codecs.open(f, 'r', encoding='utf-8', errors='ignore').read() for f in text_files]
#print documents
#print '................................................................'
#tfidf = TfidfVectorizer(tokenizer=lambda doc: doc, lowercase=False).fit_transform(documents)
tfidf = TfidfVectorizer(min_df=1).fit_transform(documents)
# no need to normalize, since Vectorizer will return normalized tf-idf
#pairwise_similarity = tfidf * tfidf.T
#pairwise_similarity = (tfidf * tfidf.T).A
#print tfidf
#print '.....................'
#print tfidf.T
#print '.....................'
#print tfidf.A
#print '.....................'
#print (tfidf * tfidf.T)
#print '.....................'
#print (tfidf * tfidf.T).A
#print '.....................'

cosine_sim = (tfidf * tfidf.T).toarray()
#print cosine_sim
ms = []
for i in range(0, len(text_files)):
    most_similar = np.argsort(cosine_sim[:, i])[::-1]
    print most_similar
    ms.append(most_similar)
#candicates = ms[:100]  # or however many you desire
#print candicates

counts = dict()
results = []

for y in reversed(range(1, len(ms))):  # kolumny
    for x in range(0, len(ms)):  # wpisy (wystapienia, wiersze)
        counts[str(ms[x][y])] = counts[str(ms[x][y])] + 1 if str(ms[x][y]) in counts else 1
    results.append(search_for_max(counts))
    counts = dict()

print results[0:1999]  # this is guaranted to have insert order
zz = [text_files[int(x)] for x in results[0:1999]]  # same here
print zz
print set(zz)
