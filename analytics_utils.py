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


# AI Improvement (2026-02-19)
# Add a helper function to calculate the hour of the day with the highest average engagement from a list of hour-score pairs.


def get_peak_engagement_hour(hour_score_pairs):
    """Calculates the hour of the day with the highest average engagement from (hour, score) tuples."""
    hour_metrics = {}
    for hour, score in hour_score_pairs:
        if hour not in hour_metrics:
            hour_metrics[hour] = []
        hour_metrics[hour].append(score)
    
    if not hour_metrics:
        return None
            
    avg_scores = {hour: sum(scores) / len(scores) for hour, scores in hour_metrics.items()}
    return max(avg_scores, key=avg_scores.get)


# AI Improvement (2026-02-19)
# Add a function to categorize URLs into content types like Image, Video, and Discussion.


def get_content_type_distribution(urls):
    """Categorizes a list of URLs into content types (Image, Video, Discussion, Article)."""
    stats = {"Image": 0, "Video": 0, "Discussion": 0, "Article": 0}
    img_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp')
    vid_domains = ('youtube.com', 'vimeo.com', 'youtu.be', 'v.redd.it')
    for url in urls:
        parsed = urlparse(url)
        path, domain = parsed.path.lower(), parsed.netloc.lower()
        if path.endswith(img_exts):
            stats["Image"] += 1
        elif any(vd in domain for vd in vid_domains):
            stats["Video"] += 1
        elif 'reddit.com' in domain and '/comments/' in path:
            stats["Discussion"] += 1
        else:
            stats["Article"] += 1
    return stats


# AI Improvement (2026-02-20)
# Complete the sentiment analysis helper function using a keyword-based scoring system.
def analyze_sentiment(texts):
    """Categorizes text content into positive, negative, or neutral buckets based on keyword matching."""
    pos_words = {'excellent', 'good', 'great', 'awesome', 'amazing', 'love', 'perfect', 'best', 'positive', 'cool'}
    neg_words = {'bad', 'awful', 'terrible', 'horrible', 'worst', 'hate', 'negative', 'poor', 'wrong', 'boring'}
    
    stats = {'positive': 0, 'neutral': 0, 'negative': 0}
    for text in texts:
        words = set(text.lower().split())
        pos_score = len(words.intersection(pos_words))
        neg_score = len(words.intersection(neg_words))
        
        if pos_score > neg_score:
            stats['positive'] += 1
        elif neg_score > pos_score:
            stats['negative'] += 1
        else:
            stats['neutral'] += 1
    return stats


# AI Improvement (2026-02-20)
# Add a helper function to extract top keywords, filtering out common stop words and punctuation.
def get_top_keywords(texts, limit=20):
    """Extracts the most frequent meaningful keywords from a list of strings."""
    stops = {'the', 'and', 'for', 'with', 'this', 'that', 'from', 'was', 'are', 'but', 'not', 'have', 'has', 'they', 'what', 'who', 'how', 'about', 'will', 'your', 'their', 'can', 'all', 'more', 'just', 'when'}
    counts = {}
    for text in texts:
        for word in text.lower().split():
            w = word.strip('.,!?:;"()')
            if w not in stops and len(w) > 2:
                counts[w] = counts.get(w, 0) + 1
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:limit]


# AI Improvement (2026-02-22)
# Add a trending score calculator using a time-decay formula to identify 'hot' content.

def calculate_trending_score(score, hours_old):
    """Calculates a trending score using a time-decay formula to surface 'hot' content."""
    # Gravity formula: Score / (Age + 2)^1.5
    return round(score / pow((max(0, hours_old) + 2), 1.5), 4)


# AI Improvement (2026-02-22)
# Add a helper function to extract top phrases (n-grams) for more contextual trending topic detection.
def get_top_phrases(texts, n=2, limit=10):
    """Extracts the most common n-word phrases (n-grams) to identify context-rich trends."""
    import re
    from collections import Counter
    phrases = []
    for text in texts:
        # Find all words with at least 3 characters
        words = re.findall(r'\b\w{3,}\b', text.lower())
        for i in range(len(words) - n + 1):
            phrase = " ".join(words[i:i+n])
            phrases.append(phrase)
    return Counter(phrases).most_common(limit)


# AI Improvement (2026-02-22)
# Add a helper function to format large engagement metrics into human-readable strings.
def format_short_number(num):
    """Formats large numbers into human-readable strings (e.g., 1500 -> 1.5k)."""
    if num >= 1000000:
        return f"{num / 1000000:.1f}M"
    if num >= 1000:
        return f"{num / 1000:.1f}k"
    return str(num)


# AI Improvement (2026-02-22)
# Add a helper function to categorize post URLs into media types (Image, Video, Self-post, or Article).
def identify_content_type(url):
    """Categorizes a URL into media types: Image, Video, Self-post, or Article."""
    u = url.lower()
    if any(x in u for x in ['.jpg', '.jpeg', '.png', '.gif', 'imgur.com', 'i.redd.it']):
        return 'Image'
    elif any(x in u for x in ['youtube.com', 'youtu.be', 'v.redd.it', 'vimeo.com']):
        return 'Video'
    elif 'reddit.com' in u and '/comments/' in u:
        return 'Self-post'
    return 'Article'


# AI Improvement (2026-02-22)
# Complete the basic sentiment analysis helper function to categorize text into positive, negative, and neutral buckets.
def analyze_sentiment(texts):
    """Categorizes text content into positive, negative, or neutral buckets."""
    pos_words = {'excellent', 'good', 'great', 'best', 'amazing', 'useful', 'helpful', 'positive', 'success', 'win'}
    neg_words = {'bad', 'worst', 'terrible', 'awful', 'negative', 'failure', 'fail', 'problem', 'broken', 'sad'}
    
    counts = {'positive': 0, 'neutral': 0, 'negative': 0}
    for text in texts:
        words = set(str(text).lower().split())
        p_score = len(words & pos_words)
        n_score = len(words & neg_words)
        if p_score > n_score:
            counts['positive'] += 1
        elif n_score > p_score:
            counts['negative'] += 1
        else:
            counts['neutral'] += 1
    return counts


# AI Improvement (2026-02-22)
# Add a helper function to aggregate timestamps into a 24-hour frequency distribution.
def get_hourly_distribution(timestamps):
    """Aggregates Unix timestamps into a fixed 24-hour distribution (0-23) for charting."""
    from datetime import datetime
    counts = {i: 0 for i in range(24)}
    for ts in timestamps:
        hour = datetime.fromtimestamp(float(ts)).hour
        counts[hour] += 1
    return [counts[i] for i in range(24)]
