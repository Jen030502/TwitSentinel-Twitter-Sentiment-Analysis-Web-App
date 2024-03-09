import pandas as pd
import regex
  # for mathematical calculation
import seaborn as sns  # for data visualiztion
import pickle
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_extraction.text import TfidfVectorizer

import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import Word
import re
import xgboost as xgb




def preprocess(processed_data):
    
    
    # make all word into lower case and whitespace inbetween 
    processed_data = " ".join([word.lower() for word in processed_data.split()])
    # processed_data = lambda x: " ".join(x.lower() for x in processed_data.split());
    
    # replace all non-charachter and whitespace from the tweet 
    processed_data = re.sub(r'[^a-zA-Z]', " ", processed_data)
    # processed_data = processed_data.replace('/W+','',regex=True)
    # processed_data = processed_data.replace('/s','',regex=True)
    
    # delete all the numbers and stop words from the tweet 
    
    
    # processed_data = processed_data.replace('[0-9]+','',regex=True)
    
    sw = stopwords.words("english")
    processed_data = " ".join([Word(word).lemmatize() for word in processed_data.split() if word not in sw])
    # processed_data = lambda x: " "join(x for x in processed_data.split() if processed_data not in sw)
    

    
    # lemaaatize the roots words from the tweet
    
    # processed_data =lambda x: " ".join([Word(word).lemmatize() for word in processed_data.split()]);

   
    processed_data = pd.Series(processed_data)
    
    # load the tf-idf vectorixer model 
    with open('./savedModels/tfidf_vectorizer.pkl', 'rb') as file:
        model = pickle.load(file)
    preprocessed_data = model.transform(processed_data)
    

    return preprocessed_data


def prediction(processed_data):
    # load the model

    with open('./savedModels/xgb_model.pkl', 'rb') as file2:
        model = pickle.load(file2)

    ypred = model.predict(processed_data)
    
    return ypred
