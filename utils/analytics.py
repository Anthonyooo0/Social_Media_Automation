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
