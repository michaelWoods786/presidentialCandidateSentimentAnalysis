import matplotlib.pyplot as plt

def plot_sentiment_comparison(harris_sentiments, trump_sentiments):
    categories = ['positive', 'neutral', 'negative']
    harris_values = [harris_sentiments[category] for category in categories]
    trump_values = [trump_sentiments[category] for category in categories]

    bar_width = 0.35
    index = np.arange(len(categories))

    fig, ax = plt.subplots()
    bar1 = ax.bar(index, harris_values, bar_width, label='Kamala Harris')
    bar2 = ax.bar(index + bar_width, trump_values, bar_width, label='Donald Trump')

    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Number of Tweets')
    ax.set_title('Sentiment Comparison between Kamala Harris and Donald Trump')
    ax.set_xticks(index + bar_width / 2)
    ax.set_xticklabels(categories)
    ax.legend()

    plt.show()