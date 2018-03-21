from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy.sparse import save_npz
import json

newsgroups = fetch_20newsgroups(subset='all',
                                remove=['headers', 'footers', 'quotes'])

vectorizer = TfidfVectorizer()
vectors = vectorizer.fit_transform(newsgroups.data)

save_npz('20groups-tfidf.npz', vectors)
with open('20groups-tfidf-names.json', 'w') as f:
    json.dump(vectorizer.get_feature_names(), f)
with open('20groups.json', 'w') as f:
    json.dump(newsgroups.data, f)
