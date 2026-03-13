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


# AI Improvement (2026-03-11)
# Add a utility to filter out common stop words for more meaningful word frequency analysis.


def filter_common_words(text):
    """
    Filters out common stop words from the input text to help identify meaningful trends.
    """
    if not text:
        return []
    
    stop_words = {"the", "and", "this", "that", "with", "from", "for", "was", "were", "about", "will", "can", "not", "your", "are", "have", "been", "has", "their", "there"}
    # Extract words of 3+ characters and filter stop words
    words = re.findall(r"\b\w{3,}\b", text.lower())
    return [w for w in words if w not in stop_words]


# AI Improvement (2026-03-13)
# Add a domain extraction utility to identify top external content sources.

def extract_top_domains(urls, limit=5):
    """
    Identifies the most common source domains from a list of external links.
    """
    from collections import Counter
    domains = []
    for url in urls:
        if isinstance(url, str):
            # Extract domain using regex (e.g., https://github.com/user -> github.com)
            match = re.search(r"https?://(?:www\.)?([^/:\s]+)", url)
            if match:
                domains.append(match.group(1).lower())
    
    return Counter(domains).most_common(limit)


# AI Improvement (2026-03-13)
# Implement bigram extraction to identify common two-word phrases for better topic context.
def extract_top_bigrams(texts, limit=10):
    """
    Identifies the most common two-word phrases (bigrams) to provide better context than single words.
    """
    from collections import Counter
    if not texts:
        return []
    
    bigram_counts = Counter()
    for text in texts:
        words = re.findall(r"\w+", text.lower())
        for i in range(len(words) - 1):
            bigram_counts[f"{words[i]} {words[i+1]}"] += 1
    
    return bigram_counts.most_common(limit)
