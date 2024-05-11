# app.py
import streamlit as st
import pickle
import tweepy
import numpy as np
#from sklearn.feature_extraction.text import TfidfVectorizer
#Vectorizer=TfidfVectorizer()
# Twitter API credentials
consumer_key = 'oaC21eodbyaCB6sHTrIdRtfpH'
consumer_secret = 'zi0174zb76Hhjoh5HXnTE08LpHMkMFiS1kMXytu3M2n7Ljs6In'
access_token = '986230220-PHjEbG4PuMUksorV4ksXwUaVN1oDYSKQ3PxhPLr3'
access_token_secret = 'L5wiRTiKwIIGCui6rxFFjHP3v9VSpH4ZTUuaLrUptGlJQ'


# Load the model
with open(r'C:\Users\UTKARSH\Desktop\programming\projects\data analytics\sentiment analysis\trainedtwitter_model.sav', 'rb') as model_file:
    model = pickle.load(model_file)

def extract_tweet_text(tweet_link):
    # Authenticate with Twitter API
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Extract tweet ID from the link
    tweet_id = tweet_link.split('/')[-1]
    
    # Retrieve tweet content
    try:
        tweet = api.get_status(tweet_id)
        tweet_text = tweet.text
        return tweet_text
    except tweepy.TweepError as e:
        print("Error: ", e)
        return None    

# Function to analyze sentiment
def analyze_sentiment(tweet_text):
    #transformed_tweet = Vectorizer.transform([tweet_text])
    prediction = model.predict(np.array([tweet_text]).reshape(1, -1))[0]
    return prediction

# Streamlit UI
st.title('Twitter Sentiment Analysis')

tweet_text = st.text_input('Enter a tweet:')
if st.button('Analyze'):
    if tweet_text:
        st.write('Tweet:', tweet_text)
        st.write('Sentiment:', analyze_sentiment(tweet_text))
    else:
        st.warning('Please enter a tweet!')
