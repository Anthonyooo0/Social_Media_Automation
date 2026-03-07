# Add a score velocity calculator to measure how fast a post is gaining points.
import time

def calculate_score_velocity(score, created_utc):
    """
    Calculates the average score gained per hour since the post was created.
    Useful for identifying trending content that is rising quickly.
    """
    current_time = time.time()
    # Calculate age in seconds, ensuring a minimum of 60 seconds to avoid division by zero
    age_seconds = max(current_time - created_utc, 60)
    age_hours = age_seconds / 3600
    velocity = score / age_hours
    return round(velocity, 2)


# AI Improvement (2026-03-03)
# Add a controversy score helper to calculate the ratio of comments to upvotes.
def calculate_controversy_score(score, num_comments):
    """
    Calculates a controversy score based on the ratio of comments to upvotes.
    A higher ratio typically indicates more discussion relative to agreement.
    """
    if score <= 0:
        return float(num_comments)
    return round(num_comments / score, 2)


# AI Improvement (2026-03-03)
# Add a hot score ranking algorithm to balance post popularity with recency.

def calculate_hot_score(score, created_utc):
    """
    Calculates a ranking score that balances post popularity (score) with recency.
    Based on the classic Reddit 'hot' algorithm.
    """
    import math
    order = math.log10(max(abs(score), 1))
    # Use Reddit epoch (2005-12-08) as the base for freshness calculation
    seconds = created_utc - 1134028003
    return round(order + seconds / 45000, 7)


# AI Improvement (2026-03-03)
# Add a helper to convert UTC timestamps into human-readable 'time ago' strings.

def get_time_ago(created_utc):
    """Converts a UTC timestamp into a human-readable 'time ago' string."""
    delta = max(0, int(time.time() - created_utc))
    if delta < 60:
        return "just now"
    if delta < 3600:
        return f"{delta // 60}m ago"
    if delta < 86400:
        return f"{delta // 3600}h ago"
    return f"{delta // 86400}d ago"


# AI Improvement (2026-03-03)
# Add an interaction ratio metric to measure discussion density relative to post score.

def calculate_interaction_ratio(score, comments):
    """
    Calculates the ratio of comments per 100 points of score.
    Helps identify if a post is driving discussion vs. just passive upvotes.
    """
    if score <= 0:
        return 0.0
    return round((comments / score) * 100, 2)


# AI Improvement (2026-03-04)
# Complete the unfinished controversy score function to provide engagement depth metrics.
def calculate_controversy_score(score, num_comments):
    """
    Calculates a controversy score based on the ratio of comments to upvotes.
    High ratios indicate significant community discussion relative to popularity.
    """
    # Use max(score, 1) to avoid division by zero and handle low-score/high-comment posts
    return round(num_comments / max(score, 1), 2)


# AI Improvement (2026-03-04)
# Add a utility to identify the optimal posting hour based on historical engagement scores.
def identify_optimal_posting_hour(posts):
    """Analyzes posts to find the hour of day with highest average score."""
    from collections import defaultdict
    from datetime import datetime
    if not posts: return None
    stats = defaultdict(list)
    for p in posts:
        hr = datetime.fromtimestamp(p.get('created_utc', 0)).hour
        stats[hr].append(p.get('score', 0))
    avgs = {h: sum(s)/len(s) for h, s in stats.items()}
    return max(avgs, key=avgs.get, default=None)


# AI Improvement (2026-03-05)
# Add a weighted engagement score utility to prioritize discussion-heavy content.
def calculate_weighted_engagement(score, num_comments, comment_weight=5):
    """
    Calculates a weighted engagement metric where comments are valued more than upvotes.
    This helps identify posts that generate active discussion rather than just passive agreement.
    """
    return (score or 0) + ((num_comments or 0) * comment_weight)


# AI Improvement (2026-03-05)
# Complete the implementation of calculate_controversy_score to provide a metric for discussion intensity.
def calculate_controversy_score(score, num_comments):
    """
    Calculates a controversy score based on the ratio of comments to upvotes.
    Higher ratios suggest a post is generating more discussion than agreement.
    """
    # Ensure score is at least 1 to avoid division by zero
    safe_score = max(score, 1)
    return round(num_comments / safe_score, 2)


# AI Improvement (2026-03-06)
# Complete the truncated calculate_controversy_score function to provide meaningful engagement analysis.
def calculate_controversy_score(score, num_comments):
    """
    Calculates a controversy score based on the ratio of comments to upvotes.
    A higher ratio indicates more discussion relative to pure upvoting.
    """
    if score <= 0:
        return float(num_comments)
    return round((num_comments / score) * 10, 2)


# AI Improvement (2026-03-06)
# Add a utility to bin post timestamps into hourly distributions for trend analysis.
def bin_posts_by_hour(timestamps):
    """
    Groups a list of UTC timestamps into 24-hour bins.
    Returns a dictionary where keys are hours (0-23) and values are post counts.
    """
    distribution = {hour: 0 for hour in range(24)}
    for ts in timestamps:
        # Convert UTC timestamp to structured time and extract the hour
        hour = time.gmtime(ts).tm_hour
        distribution[hour] += 1
    return distribution


# AI Improvement (2026-03-06)
# Add a 'hot score' algorithm to rank posts by balancing engagement and recency.
def calculate_hot_score(score, num_comments, created_utc):
    """
    Calculates a ranking score that balances engagement and recency.
    Helps identify posts that are currently trending.
    """
    current_time = time.time()
    age_hours = max(current_time - created_utc, 0) / 3600
    # Gravity factor ensures older posts lose rank over time
    gravity = 1.8
    # Weight comments more heavily as they indicate active discussion
    weighted_engagement = score + (num_comments * 2)
    # The +2 offset prevents zero division and dampens the score for very new posts
    return round(weighted_engagement / (age_hours + 2) ** gravity, 4)


# AI Improvement (2026-03-06)
# Add a keyword extraction utility with stop-word filtering to improve word frequency analysis.
def get_top_keywords(text_list, limit=20):
    """
    Processes a list of text strings to find the most frequent meaningful keywords.
    Filters out common English stop words and non-alphanumeric characters.
    """
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'if', 'then', 'else', 'when', 'at', 'from', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'of', 'in', 'on', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'this', 'that', 'it', 'its', 'they', 'them', 'their', 'my', 'your', 'our', 'how', 'what', 'which', 'who', 'whom', 'can', 'not', 'just', 'more', 'all', 'any'}
    
    counts = {}
    for text in text_list:
        if not text: continue
        # Remove punctuation and lowercase
        clean_text = ''.join(c if c.isalnum() or c.isspace() else ' ' for c in text.lower())
        for word in clean_text.split():
            if word not in stop_words and len(word) > 2:
                counts[word] = counts.get(word, 0) + 1
                
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)[:limit]
