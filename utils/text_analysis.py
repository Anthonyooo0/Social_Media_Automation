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


# AI Improvement (2026-03-11)
# Add a bigram extraction utility to identify common two-word phrases for better topic context.

# AI Improvement (2026-03-12)
def extract_top_bigrams(texts, limit=10):
    """
    Extracts the most frequent two-word sequences (bigrams) from titles.
    Helps identify specific topics like 'machine learning' vs just 'learning'.
    """
    from collections import Counter
    if not texts:
        return []
    
    bigrams = []
    for text in texts:
        # Clean and tokenize into alphanumeric words
        words = re.findall(r"\w+", text.lower())
        # Generate pairs of consecutive words
        bigrams.extend([f"{words[i]} {words[i+1]}" for i in range(len(words) - 1)])
    
    return Counter(bigrams).most_common(limit)
