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
    Analysis Methodology
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
