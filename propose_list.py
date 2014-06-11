import os

from sklearn.feature_extraction.text import TfidfVectorizer

print 'Test............'
vect = TfidfVectorizer(min_df=1)
tfidf = vect.fit_transform(["I'd like an apple",
                            "An apple a day keeps the doctor away",
                            "Never compare an apple to an orange",
                            "I prefer scikit-learn to Orange"])
print (tfidf * tfidf.T).A
print 'End of test.................'

def include_ext(ext):
    def compare(fn): return os.path.splitext(fn)[1] == ext
    return compare

text_files = filter(os.path.isfile, os.listdir( os.curdir ) )  # files only
text_files = filter(include_ext(".txt"), text_files)

print text_files
print '................................................................'

documents = [open(f) for f in text_files]
tfidf = TfidfVectorizer(tokenizer=lambda doc: doc, lowercase=False).fit_transform(documents)
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
