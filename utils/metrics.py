# Add a controversy index utility that measures the ratio of comments to score.
def calculate_controversy_index(num_comments, score):
    """
    Calculates a controversy index.
    A higher ratio of comments relative to the score suggests a polarizing or high-discussion topic.
    """
    if score < 1:
        return float(num_comments)
    return round((num_comments / score), 4)
