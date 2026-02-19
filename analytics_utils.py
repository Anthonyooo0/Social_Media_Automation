# Add a helper function to analyze and rank the primary domains (content sources) from a list of post URLs.
from urllib.parse import urlparse

def get_source_distribution(urls):
    """Analyzes a list of URLs to determine the distribution of content sources (domains)."""
    counts = {}
    for url in urls:
        domain = urlparse(url).netloc.lower().replace('www.', '')
        if domain:
            counts[domain] = counts.get(domain, 0) + 1
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)


# AI Improvement (2026-02-19)
# Add a basic sentiment analysis helper to categorize post titles into positive, negative, and neutral sentiments.

def analyze_sentiment(texts):
    """Categorizes text content into positive, negative, or neutral buckets."""
    pos_set = {'excellent', 'good', 'great', 'awesome', 'amazing', 'love', 'perfect', 'best', 'success'}
    neg_set = {'bad', 'worst', 'awful', 'terrible', 'hate', 'issue', 'problem', 'fail', 'error', 'poor'}
    sentiment_counts = {'positive': 0, 'neutral': 0, 'negative': 0}
    for text in texts:
        words = set(text.lower().split())
        score = len(words & pos_set) - len(words & neg_set)
        if score > 0:
            sentiment_counts['positive'] += 1
        elif score < 0:
            sentiment_counts['negative'] += 1
        else:
            sentiment_counts['neutral'] += 1
    return sentiment_counts
