# presidentialCandidateSentimentAnalysis
Project Overview

This project aims to perform sentiment analysis on tweets mentioning two prominent political figures, Donald Trump and Kamala Harris. The analysis helps understand the public's sentiment towards these figures over a specific period, providing insights into public opinion, trends, and possible changes in perception.
Objectives

    Collect tweets mentioning Donald Trump and Kamala Harris.
    Clean and preprocess the tweet data for analysis.
    Apply sentiment analysis using various NLP techniques and models.
    Visualize and interpret the sentiment distribution for each political figure.

Table of Contents

    Project Overview
    Dataset
    Installation
    Usage

    Results and Visualization
    Contributing
    License

Dataset
Data Collection

The tweets are collected using the Twitter API (via Tweepy or another scraping method). The dataset consists of tweets mentioning "Donald Trump" or "Kamala Harris" during a specified period.
Data Fields

Each tweet in the dataset contains the following fields:

    id: Unique identifier for the tweet.
    text: The full text of the tweet.
    created_at: Timestamp when the tweet was created.
    user_id: Identifier for the user who posted the tweet.
    user_location: The location of the user (if available).
    retweet_count: Number of retweets.
    favorite_count: Number of likes.

Installation

To run this project, you'll need to install the necessary Python packages. Use the following steps to set up your environment:
Prerequisites

    Python 3.7 or higher
    Twitter API credentials (API key, API secret key, Access token, Access token secret)

Step-by-Step Installation

1)Clone the Repository:git clone https://github.com/yourusername/sentiment-analysis-trump-harris.git
cd sentiment-analysis-trump-harris

2)Set Up a Virtual Environment:python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3)Install Required Packages:
pip install -r requirements.txt


Usage

    Configure Twitter API Credentials
    Create a .env file in the project root and add your Twitter API credentials:

    TWITTER_API_KEY=your_api_key
    TWITTER_API_SECRET_KEY=your_api_secret_key
    TWITTER_ACCESS_TOKEN=your_access_token
    TWITTER_ACCESS_TOKEN_SECRET=your_access_token_secret

Run the Data Collection Script:
    python collect_tweets.py

Run the Sentiment Analysis Script:
    python sentiment_analysis.py


Results and Visualization

    Sentiment Distribution: The sentiment distribution for each political figure is visualized using histograms. These histograms display the count of positive, negative, and neutral tweets, providing a clear overview of public sentiment.

    (Include an example histogram image if available)

Contributing

Contributions are welcome! Please follow these steps to contribute:

    Fork the repository.
    Create a new branch: git checkout -b feature/your-feature-name.
    Commit your changes: git commit -m 'Add your feature'.
    Push to the branch: git push origin feature/your-feature-name.
    Open a pull request.
