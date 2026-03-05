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
