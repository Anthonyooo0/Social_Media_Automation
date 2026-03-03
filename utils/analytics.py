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
