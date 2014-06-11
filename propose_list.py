import os
import codecs
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer


def include_ext(ext):
    def compare(fn):
        return os.path.splitext(fn)[1] == ext
    return compare


print 'Test............'
vect = TfidfVectorizer(min_df=1)
tfidf = vect.fit_transform(["I'd like an apple",
                            "An apple a day keeps the doctor away",
                            "Never compare an apple to an orange",
                            "I prefer scikit-learn to Orange"])
print (tfidf * tfidf.T).A
print 'End of test.................'

text_files = filter(os.path.isfile, os.listdir( os.curdir ) )  # files only
text_files = filter(include_ext(".txt"), text_files)

print '................................................................'
print text_files
print '................................................................'
documents = [codecs.open(f, 'r', encoding='utf-8', errors='ignore').read() for f in text_files]
print documents
print '................................................................'
#tfidf = TfidfVectorizer(tokenizer=lambda doc: doc, lowercase=False).fit_transform(documents)
tfidf = TfidfVectorizer(min_df=1).fit_transform(documents)
# no need to normalize, since Vectorizer will return normalized tf-idf
#pairwise_similarity = tfidf * tfidf.T
#pairwise_similarity = (tfidf * tfidf.T).A
print tfidf
print '.....................'
print tfidf.T
print '.....................'
print tfidf.A
print '.....................'
print (tfidf * tfidf.T)
print '.....................'
print (tfidf * tfidf.T).A
print '.....................'

cosine_sim = (tfidf * tfidf.T).toarray()
print cosine_sim
ms = []
for i in range (0, 4):
    most_similar = np.argsort(cosine_sim[:, i])[::-1]
    print most_similar
    ms.append(most_similar)
candicates = ms[:100]  # or however many you desire
print candicates
