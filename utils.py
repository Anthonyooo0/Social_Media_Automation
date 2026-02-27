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
