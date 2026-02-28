# Add a text preprocessing helper to filter out common stop words for more meaningful word frequency analysis.
def filter_stop_words(text):
    import re
    # Set of common English stop words to filter out
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'in', 'on', 'at', 'to', 'for', 'with', 'by', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'from', 'up', 'down', 'out', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'don', 'should', 'now'}
    # Extract words using regex, converting to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    # Return only non-stop words with length > 2 to remove noise
    return [w for w in words if w not in stop_words and len(w) > 2]


# AI Improvement (2026-02-24)
# Add a text cleaning helper to remove URLs and Markdown formatting from Reddit content
def clean_social_text(text):
    import re
    # Remove URLs (http, https, www)
    text = re.sub(r'http\S+|www\S+', '', text)
    # Remove markdown links: [label](url) -> label
    text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', text)
    # Remove basic markdown formatting characters like bold, italics, headers
    text = re.sub(r'[*_~#>`\-]', '', text)
    # Normalize whitespace
    return ' '.join(text.split())


# AI Improvement (2026-02-24)
# Add a helper function to calculate post velocity (score per hour).
def calculate_post_velocity(score, created_utc):
    """Calculates the score accumulation rate per hour to identify trending content."""
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).timestamp()
    age_hours = (now - created_utc) / 3600
    # Use 0.1 hours as a minimum age to avoid extreme values for very new posts
    return round(score / max(age_hours, 0.1), 2)


# AI Improvement (2026-02-24)
# Add a helper function to perform basic keyword-based sentiment analysis on post titles or content.

def calculate_sentiment(text):
    """Performs basic keyword-based sentiment analysis to categorize text as positive, negative, or neutral."""
    import re
    pos_words = {'great', 'awesome', 'excellent', 'good', 'love', 'amazing', 'best', 'helpful', 'useful', 'cool'}
    neg_words = {'bad', 'terrible', 'worst', 'awful', 'hate', 'horrible', 'useless', 'broken', 'annoying', 'boring'}
    # Remove punctuation and lowercase
    clean_text = re.sub(r'[^\w\s]', '', str(text).lower())
    tokens = clean_text.split()
    # Calculate score
    score = sum(1 for word in tokens if word in pos_words) - sum(1 for word in tokens if word in neg_words)
    return 'positive' if score > 0 else ('negative' if score < 0 else 'neutral')


# AI Improvement (2026-02-25)
# Add a helper function to categorize post hours into time-of-day segments.
def get_time_of_day_category(hour):
    """Categorize an hour (0-23) into Morning, Afternoon, Evening, or Night segments."""
    if 5 <= hour < 12:
        return 'Morning'
    elif 12 <= hour < 17:
        return 'Afternoon'
    elif 17 <= hour < 21:
        return 'Evening'
    return 'Night'


# AI Improvement (2026-02-27)
# Add a helper function to sanitize subreddit name inputs safely.
def sanitize_subreddit(name):
    """
    Cleans subreddit input by removing 'r/' prefixes and leading/trailing slashes.
    """
    if not name:
        return ""
    name = name.strip().lower()
    if name.startswith('r/'):
        name = name[2:]
    elif name.startswith('/r/'):
        name = name[3:]
    return name.strip('/')


# AI Improvement (2026-02-27)
# Add a helper function to calculate engagement density (comments-to-score ratio).
def calculate_engagement_density(score, num_comments):
    """Calculates the ratio of comments per score to measure discussion intensity."""
    if not score or score <= 0:
        return 0.0
    return round((num_comments / score) * 100, 2)


# AI Improvement (2026-02-27)
# Add a helper function to extract the source domain from post URLs for source-based analytics.

def extract_domain(url):
    from urllib.parse import urlparse
    try:
        domain = urlparse(url).netloc
        return domain.lower().replace('www.', '') if domain else 'self'
    except Exception:
        return 'unknown'


# AI Improvement (2026-02-27)
# Add a text cleaning helper to remove URLs and special characters for cleaner word frequency analysis.
def clean_text(text):
    import re
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove special characters and numbers, keep only letters and spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return " ".join(text.lower().split())


# AI Improvement (2026-02-27)
# Add a basic sentiment analysis helper to categorize post titles.
def analyze_sentiment(text):
    """Categorizes text as positive, negative, or neutral based on keyword polarity."""
    positive_words = {'great', 'awesome', 'excellent', 'happy', 'good', 'best', 'cool', 'love', 'amazing', 'useful', 'helpful'}
    negative_words = {'bad', 'terrible', 'awful', 'horrible', 'worst', 'sad', 'hate', 'poor', 'annoying', 'wrong', 'broken'}
    words = str(text).lower().split()
    score = sum(1 for word in words if word in positive_words) - sum(1 for word in words if word in negative_words)
    return 'positive' if score > 0 else ('negative' if score < 0 else 'neutral')


# AI Improvement (2026-02-27)
# Add a helper function to format large engagement counts into human-readable strings like '1.2k' or '4.5M'.
def format_count(num):
    if num >= 1000000:
        return f'{num / 1000000:.1f}M'
    if num >= 1000:
        return f'{num / 1000:.1f}k'
    return str(num)


# AI Improvement (2026-02-27)
# Add a trend score helper that calculates post 'hotness' using engagement and time decay.
def calculate_trend_score(score, comment_count, created_utc):
    from datetime import datetime
    # Calculate age in hours, ensuring a minimum of 1 to avoid division errors or extreme weight
    age_hours = max((datetime.now().timestamp() - created_utc) / 3600, 1)
    # Gravity-based ranking formula (Score + Weighted Comments) / Age^Gravity
    # Higher gravity (1.5) ensures that older posts fall off the 'trending' list quickly
    return round((score + (comment_count * 2)) / (age_hours ** 1.5), 2)


# AI Improvement (2026-02-28)
# Add a subreddit name validation helper to verify naming conventions before API requests.

def validate_subreddit_name(name):
    import re
    if not name or not isinstance(name, str):
        return False
    # Reddit subreddits are 3-21 characters, alphanumeric and underscores only
    return bool(re.match(r'^[A-Za-z0-9_]{3,21}$', name))


# AI Improvement (2026-02-28)
# Add a helper function to extract the source domain from post URLs.
def extract_domain(url):
    from urllib.parse import urlparse
    if not url or 'reddit.com' in url or not url.startswith('http'):
        return 'self'
    domain = urlparse(url).netloc
    return domain.replace('www.', '') if domain else 'self'
