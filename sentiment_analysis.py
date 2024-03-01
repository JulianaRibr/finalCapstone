import spacy
from spacytextblob.spacytextblob import SpacyTextBlob
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
    tokens = [token.lemma_.lower().strip() for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def sentiment_analysis(text):
    '''
    Promote the review analysis
    '''

    doc = nlp(text)
    return doc._.blob.polarity


# Read the csv file from a local folder.
amazon_customer_reviews = pd.read_csv('amazon_product_reviews.csv', low_memory = False)


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