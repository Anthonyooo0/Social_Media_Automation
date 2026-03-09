# Add a controversy index utility that measures the ratio of comments to score.
def calculate_controversy_index(num_comments, score):
    """
    Calculates a controversy index.
    A higher ratio of comments relative to the score suggests a polarizing or high-discussion topic.
    """
    if score < 1:
        return float(num_comments)
    return round((num_comments / score), 4)


# AI Improvement (2026-03-09)
# Add an engagement velocity utility to calculate score growth per hour.
def calculate_engagement_velocity(score, created_utc):
    import time
    # Calculate age in hours, using a minimum of 1 hour to prevent extreme values for brand new posts
    age_in_hours = (time.time() - created_utc) / 3600
    return round(score / max(age_in_hours, 1.0), 2)
