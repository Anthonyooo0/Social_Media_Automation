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


# AI Improvement (2026-03-09)
# Add a normalization utility to calculate engagement per thousand subscribers.
def calculate_normalized_engagement(score, comments, subscriber_count):
    """
    Calculates engagement per 1,000 subscribers to allow comparison between subreddits.
    Weights comments more heavily than scores to reflect deeper engagement.
    """
    if not subscriber_count or subscriber_count == 0:
        return 0.0
    
    # Score + weighted comments (comments represent higher interaction effort)
    total_engagement = score + (comments * 2)
    engagement_rate = (total_engagement / subscriber_count) * 1000
    return round(engagement_rate, 4)


# AI Improvement (2026-03-10)
# Add a discussion intensity utility to measure comment frequency over time.


# AI Improvement (2026-03-11)
# Add a discussion intensity utility to measure comment frequency over time.
def calculate_discussion_intensity(num_comments, created_utc):
    """
    Calculates the rate of comments per hour since the post was created.
    High intensity suggests an active, ongoing discussion.
    """
    import time
    age_in_hours = (time.time() - created_utc) / 3600
    return round(num_comments / max(age_in_hours, 1.0), 2)


# AI Improvement (2026-03-10)
# Add an engagement outlier detection utility to identify viral posts using the Interquartile Range (IQR) method.


def identify_engagement_outliers(scores):
    """
    Identifies scores that are statistical outliers using the Interquartile Range (IQR) method.
    Useful for highlighting viral posts that significantly outperform the average.
    """
    if len(scores) < 4:
        return []
    
    sorted_scores = sorted(scores)
    q1 = sorted_scores[len(sorted_scores) // 4]
    q3 = sorted_scores[(len(sorted_scores) * 3) // 4]
    iqr = q3 - q1
    upper_bound = q3 + (1.5 * iqr)
    
    return [score for score in scores if score > upper_bound]


# AI Improvement (2026-03-10)
# Add a Gini coefficient utility to measure engagement inequality within a subreddit.


# AI Improvement (2026-03-10)
# Calculate the Gini coefficient to measure engagement distribution inequality.
def calculate_engagement_concentration(scores):
    """
    Calculates the Gini coefficient for post scores.
    Values close to 0 indicate even engagement, while values close to 1 indicate a few posts dominate.
    """
    if not scores or len(scores) < 2:
        return 0.0
    
    sorted_scores = sorted(scores)
    n = len(scores)
    sum_of_scores = sum(sorted_scores)
    
    if sum_of_scores == 0:
        return 0.0
        
    # Calculate Gini coefficient using the simplified rank-based formula
    index_sum = sum((i + 1) * score for i, score in enumerate(sorted_scores))
    gini = (2 * index_sum) / (n * sum_of_scores) - (n + 1) / n
    return round(max(0, gini), 3)
