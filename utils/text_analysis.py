# Add a lexical diversity utility to measure the richness and variety of vocabulary in post titles.
import re

# AI Improvement (2026-03-10)
# Add a utility to measure vocabulary richness.
def calculate_lexical_diversity(texts):
    """
    Calculates the lexical diversity (unique words / total words).
    A higher ratio suggests more varied content and richer discussion.
    """
    if not texts:
        return 0.0
    
    all_text = " ".join(texts).lower()
    # Extract alphanumeric words only
    words = re.findall(r"\w+", all_text)
    
    if not words:
        return 0.0
        
    return round(len(set(words)) / len(words), 4)
