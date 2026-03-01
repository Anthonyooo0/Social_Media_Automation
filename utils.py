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


# AI Improvement (2026-02-28)
# Add a text cleaning helper to remove URLs and non-alphabetic characters for more accurate word frequency analysis.
def clean_text_for_analysis(text):
    import re
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove special characters and numbers, keeping only letters and spaces
    cleaned = re.sub(r'[^a-zA-Z\s]', '', text)
    return cleaned.lower().strip()


# AI Improvement (2026-02-28)
# Add a basic lexicon-based sentiment analysis helper to estimate the emotional tone of post titles.

def calculate_sentiment_score(text):
    import re
    """Calculates a simple sentiment score (-1 to 1) based on keyword matching."""
    positive = {'great', 'amazing', 'excellent', 'good', 'love', 'helpful', 'awesome', 'best', 'perfect', 'fantastic', 'top', 'upvote'}
    negative = {'bad', 'terrible', 'awful', 'horrible', 'worst', 'hate', 'useless', 'boring', 'annoying', 'wrong', 'downvote'}
    words = re.findall(r'\w+', text.lower())
    if not words: return 0.0
    score = sum(1 for w in words if w in positive) - sum(1 for w in words if w in negative)
    return round(score / len(words), 4)


# AI Improvement (2026-02-28)
# Add a utility function to format large numbers into human-readable strings (e.g., 1.5k).
def format_large_number(num):
    """Converts large numbers to a compact string format (e.g. 1.5k, 2.3M)."""
    if not num: return "0"
    try:
        num = float(num)
        for unit in ['', 'k', 'M', 'B']:
            if abs(num) < 1000.0:
                return f"{num:.1f}{unit}".replace('.0', '')
            num /= 1000.0
        return f"{num:.1f}T".replace('.0', '')
    except (ValueError, TypeError):
        return "0"


# AI Improvement (2026-03-01)
# Add a utility function to categorize post content type based on URL patterns.
def identify_content_type(url):
    url_lower = url.lower()
    if any(ext in url_lower for ext in ['.jpg', '.jpeg', '.png', '.gif']):
        return 'image'
    if any(vid in url_lower for vid in ['.mp4', '.gifv', 'youtube.com', 'youtu.be', 'v.redd.it']):
        return 'video'
    return 'link'


# AI Improvement (2026-03-01)
# Add a utility function to calculate the engagement ratio (comments per score) to identify discussion-heavy posts.
def calculate_engagement_ratio(score, num_comments):
    """Calculates the ratio of comments to score as a percentage to measure discussion depth."""
    if not score or score <= 0:
        return 0.0
    return round((num_comments / score) * 100, 2)


# AI Improvement (2026-03-01)
# Add a validation function for subreddit names to ensure they follow Reddit's naming conventions.
def is_valid_subreddit_name(name):
    import re
    # Reddit subreddits are 3-21 characters, alphanumeric and underscores only.
    if not name or not isinstance(name, str):
        return False
    return bool(re.match(r'^[a-zA-Z0-9_]{3,21}$', name))


# AI Improvement (2026-03-01)
# Add a utility function to convert Unix timestamps into human-readable 'time ago' strings.
def format_time_ago(timestamp):
    from datetime import datetime, timezone
    now = datetime.now(timezone.utc).timestamp()
    diff = now - timestamp
    if diff < 60:
        return 'just now'
    if diff < 3600:
        return f'{int(diff // 60)}m ago'
    if diff < 86400:
        return f'{int(diff // 3600)}h ago'
    return f'{int(diff // 86400)}d ago'


# AI Improvement (2026-03-01)
# Add a utility function to calculate score velocity (points per hour)
def calculate_score_velocity(score, created_utc):
    import time
    # Calculate hours elapsed since post creation
    hours_since_posted = (time.time() - created_utc) / 3600
    # Use a minimum of 0.1 hours to avoid division by zero and extreme spikes for very new posts
    velocity = score / max(hours_since_posted, 0.1)
    return round(velocity, 2)


# AI Improvement (2026-03-01)
# Add a simple keyword-based sentiment analysis helper to analyze post titles or comments.

def calculate_sentiment(text):
    """Calculates a basic sentiment score: positive (>0), neutral (0), or negative (<0)."""
    positive_words = {'awesome', 'best', 'excellent', 'good', 'great', 'love', 'cool', 'amazing', 'helpful', 'interesting'}
    negative_words = {'awful', 'bad', 'terrible', 'worst', 'hate', 'broken', 'annoying', 'poor', 'useless', 'horrible'}
    words = text.lower().split()
    score = 0
    for word in words:
        clean_word = word.strip('.,!?()[]"\'')
        if clean_word in positive_words:
            score += 1
        elif clean_word in negative_words:
            score -= 1
    return score


# AI Improvement (2026-03-01)
# Add a utility function to categorize Reddit posts by content type (text, image, video, or link).

def get_content_type(url, is_self):
    """Categorizes post content type based on URL and self-post status."""
    if is_self:
        return 'text'
    url_lower = url.lower()
    image_exts = ('.jpg', '.jpeg', '.png', '.gif', '.webp', '.gifv')
    video_domains = ('youtube.com', 'youtu.be', 'v.redd.it', 'vimeo.com')
    if any(url_lower.endswith(ext) for ext in image_exts):
        return 'image'
    if any(domain in url_lower for domain in video_domains):
        return 'video'
    return 'link'


# AI Improvement (2026-03-01)
# Add a utility function to format large numeric counts into abbreviated strings (e.g., 1.2k, 5.0M).

def format_large_number(num):
    """Converts a number to a compact string representation (e.g. 1500 -> 1.5k)."""
    if num is None:
        return '0'
    num = float(num)
    if num >= 1000000:
        return f'{num / 1000000:.1f}M'
    elif num >= 1000:
        return f'{num / 1000:.1f}k'
    return str(int(num))
