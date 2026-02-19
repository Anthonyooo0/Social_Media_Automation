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


# AI Improvement (2026-02-19)
# Add a helper function to identify the most active authors/contributors from a list of posts.


def get_top_contributors(posts, limit=5):
    """Identifies the most frequent authors in the provided list of posts."""
    authors = {}
    for post in posts:
        author = str(post.get('author', '[deleted]'))
        authors[author] = authors.get(author, 0) + 1
    return sorted(authors.items(), key=lambda x: x[1], reverse=True)[:limit]


# AI Improvement (2026-02-19)
# Add a helper function to extract the most frequent two-word phrases (bigrams) from titles to help identify trending topics.
def get_top_phrases(titles, n=2, limit=10):
    """Extracts the most frequent n-word phrases (bigrams) from titles to identify trends."""
    import re
    from collections import Counter
    phrases = []
    for title in titles:
        words = re.findall(r'\w+', str(title).lower())
        for i in range(len(words) - n + 1):
            phrases.append(" ".join(words[i:i + n]))
    return Counter(phrases).most_common(limit)


# AI Improvement (2026-02-19)
# Add a helper function to calculate a controversy index (comment-to-score ratio) to identify highly debated posts.


def calculate_controversy_index(posts):
    """Identifies controversial posts where the number of comments is high relative to the score."""
    results = []
    for post in posts:
        score = post.get('score', 0)
        num_comments = post.get('num_comments', 0)
        # A high ratio of comments to upvotes often indicates a heated discussion or 'ratioing'
        index = round(num_comments / max(score, 1), 2)
        results.append({"title": post.get('title', 'Untitled'), "controversy_index": index})
    return sorted(results, key=lambda x: x['controversy_index'], reverse=True)
