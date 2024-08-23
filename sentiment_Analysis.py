from textblob import TextBlob

def get_sentiment(tweets):
    sentiments = {'positive': 0, 'neutral': 0, 'negative': 0}
    neutralSet = []
    for tweet in tweets:
        print("this is the tweet: " + str(tweet))
        analysis = TextBlob(tweet)
        # Determine sentiment
        if analysis.sentiment.polarity > 0:
            sentiments['positive'] += 1
        elif analysis.sentiment.polarity == 0:
            sentiments['neutral'] += 1
            neutralSet.append(tweet)
        else:
            sentiments['negative'] += 1
    
    return (sentiments, neutralSet)