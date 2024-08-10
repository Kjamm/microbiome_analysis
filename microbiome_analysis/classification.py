import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import make_pipeline


def classify_sequences(data, classifier):
    predictions = classifier.predict(data)
    return predictions


def train_classifier(sequences, labels):
    vectorizer = CountVectorizer(analyzer='char', ngram_range=(3, 3))
    classifier = MultinomialNB()
    pipeline = make_pipeline(vectorizer, classifier)
    pipeline.fit(sequences, labels)
    return pipeline


def classify_new_samples(new_samples, trained_classifier):
    predictions = trained_classifier.predict(new_samples)
    return predictions
