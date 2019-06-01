import nltk, string, numpy
from numpy import dot
from numpy.linalg import norm

d1 = "MATLAB is a program for solving engineering and mathematical problems. The basic MATLAB objects are vectors and matrices, so you must be familiar with these before making extensive use of this program."
d2 = "MATLAB works with essentially one kind of object, a rectangular numerical matrix. Here is some basic information on using MATLAB matrix commands."
documents = [d1, d2]

#Normalize by lemmatization
lemmer = nltk.stem.WordNetLemmatizer()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

#Turn text into vectors of term frequency
from sklearn.feature_extraction.text import CountVectorizer
LemVectorizer = CountVectorizer(tokenizer=LemNormalize, stop_words='english')
LemVectorizer.fit_transform(documents)
print(LemVectorizer.vocabulary_)

#Convert to frequency numeric vector
tf_matrix = LemVectorizer.transform(documents).toarray()
print(tf_matrix)

#Calculate cosing similarity
cos_similarity_matrix = dot(tf_matrix[0], tf_matrix[1])/(norm(tf_matrix[0])*norm(tf_matrix[1]))
print(cos_similarity_matrix)

