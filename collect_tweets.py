import requests

bearer_token = 'YOUR_BEARER_TOKEN'  # Replace with your actual bearer token

headers = {
    'Authorization': f'Bearer {bearer_token}',
}

def create_url(query, max_results=100):
    search_url = "https://api.twitter.com/2/tweets/search/recent"
    query_params = {
        'query': query,
        'max_results': max_results,
        'tweet.fields': 'text,id',  # Include 'id' field to track duplicates
    }
    return search_url, query_params

def connect_to_endpoint(url, headers, params):
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(f"Request returned an error: {response.status_code} {response.text}")
    return response.json()

def fetch_tweets(query, max_tweets):
    headers = {"Authorization": f"Bearer {bearer_token}"}
    all_tweets = []
    tweet_ids = set()
    next_token = None

    while len(all_tweets) < max_tweets:
        url, params = create_url(query)
        if next_token:
            params['next_token'] = next_token
        
        json_response = connect_to_endpoint(url, headers, params)
        tweets = json_response.get('data', [])
        
        for tweet in tweets:
            if tweet['id'] not in tweet_ids:
                tweet_ids.add(tweet['id'])
                all_tweets.append(tweet)
        
        # Check if there's a next_token to continue pagination
        if 'meta' in json_response and 'next_token' in json_response['meta']:
            next_token = json_response['meta']['next_token']
        else:
            break  # No more tweets available

        if len(all_tweets) >= max_tweets:
            break

    return all_tweets[:max_tweets]  # Return only the max_tweets requested

def write_tweets_to_file(tweets, filename):
    """Writes the list of tweets to a file, one tweet per line."""
    with open(filename, 'w', encoding='utf-8') as f:
        for tweet in tweets:
            f.write(tweet['text'] + '\n')

# Example usage

tweetsTrump = fetch_tweets("Donald Trump", 2000)
tweetsHarris = fetch_tweets("KamalaHarris", 2000)

# Write the fetched tweets to files
write_tweets_to_file(tweetsTrump, 'tweets_trump.txt')
write_tweets_to_file(tweetsHarris, 'tweets_harris.txt')

print("Tweets have been written to files.")
