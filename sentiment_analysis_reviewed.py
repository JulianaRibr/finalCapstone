import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Removing the import above yields the following error:

#ValueError: [E002] Can't find factory for 'spacytextblob' for language English (en). This usually happens when spaCy calls `nlp.create_pipe` with a custom component name that's not registered on the current language class. If you're using a custom component, make sure you've added the decorator `@Language.component` (for function components) or `@Language.factory` (for class components).
#
#Available factories: attribute_ruler, tok2vec, merge_noun_chunks, merge_entities, merge_subtokens, token_splitter, doc_cleaner, parser, beam_parser, lemmatizer, trainable_lemmatizer, entity_linker, entity_ruler, tagger, morphologizer, ner, beam_ner, senter, sentencizer, spancat, spancat_singlelabel, span_finder, future_entity_ruler, span_ruler, textcat, textcat_multilabel, en.lemmatizer.

import pandas as pd

# Load the spaCy model.
nlp = spacy.load("en_core_web_lg")
nlp.add_pipe('spacytextblob')

# Data cleaning and review analysis functions.
def remove_stopwords(text):
    '''    
    Promote data cleaning.
    '''

    doc = nlp(text)
    tokens = [token.lemma_.lower().strip() for token in doc if not 
              token.is_stop and token.is_alpha]
    return " ".join(tokens)

def sentiment_analysis(text):
    '''
    Promote the review analysis
    '''

    doc = nlp(text)
    return doc._.blob.polarity


# Read the csv file from a local folder.
amazon_customer_reviews = pd.read_csv('amazon_product_reviews.csv',
                                       low_memory=False)


# Pieces of code that helps to know the dataset.
amazon_customer_reviews.head()
amazon_customer_reviews.info()
amazon_customer_reviews.isnull().sum()


# Select the columns with the review text that would be analysed.
reviews_data = amazon_customer_reviews['reviews.text']


# Preprocessing of the data, removing missing values and stop words.
reviews_clean_data = reviews_data.dropna()
reviews_clean_data = reviews_clean_data.apply(remove_stopwords)


# Perform sentiment analysis
sentiments = reviews_clean_data.apply(sentiment_analysis)


reviews_data.head()


# calculates the percentage of the positive and negative analysis.
positives = sentiments[sentiments>0]
negatives = sentiments[sentiments<0]

print(positives.count()/sentiments.count()*100)
print(negatives.count()/sentiments.count()*100)

# Test the accuracy of the sentiment analysis system.
print(f"{100} - {reviews_data[100]}. Score: {sentiments[100]}")
print(f"{4456} - {reviews_data[4456]}. Score: {sentiments[4456]}")
print(f"{919} - {reviews_data[919]}. Score: {sentiments[919]}")
print(f"{223} - {reviews_data[223]}. Score: {sentiments[223]}")
print(f"{4323} - {reviews_data[4323]}. Score: {sentiments[4323]}")