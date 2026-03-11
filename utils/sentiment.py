# Add a basic sentiment analysis utility to quantify the emotional tone of post titles.
def calculate_sentiment_score(text):
    """
    Performs a basic sentiment analysis using keyword matching.
    Returns a normalized score where positive values indicate positive sentiment.
    """
    pos_words = {'good', 'great', 'awesome', 'excellent', 'happy', 'positive', 'success', 'love', 'best', 'upvote', 'interesting'}
    neg_words = {'bad', 'terrible', 'worst', 'sad', 'negative', 'fail', 'hate', 'poor', 'issue', 'downvote', 'boring'}
    
    words = text.lower().split()
    if not words:
        return 0.0
        
    score = 0
    for word in words:
        clean_word = "".join(c for c in word if c.isalnum())
        if clean_word in pos_words:
            score += 1
        elif clean_word in neg_words:
            score -= 1
    
    return round(score / len(words), 4)
