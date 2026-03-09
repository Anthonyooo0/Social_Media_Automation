# Add a utility to track user engagement and contribution concentration.
from collections import Counter

def calculate_user_contribution_stats(authors):
    """
    Analyzes user contribution patterns to determine community diversity.
    Returns the number of unique authors and the percentage of content from the top 5 users.
    """
    if not authors:
        return {"unique_authors": 0, "top_5_contribution_pct": 0}
    
    counts = Counter(authors)
    total_posts = len(authors)
    top_5_count = sum(count for _, count in counts.most_common(5))
    
    return {
        "unique_authors": len(counts),
        "top_5_contribution_pct": round((top_5_count / total_posts) * 100, 2)
    }
