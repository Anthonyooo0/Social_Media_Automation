# Add a text cleaning utility to strip Markdown syntax and URLs from post content.
import re

def sanitize_post_text(text):
    """Removes Markdown syntax and URLs to provide clean text for word frequency analysis."""
    if not text:
        return ""
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove common Markdown formatting characters (bold, italic, headers, blockquotes)
    text = re.sub(r'[*_~`#>]', '', text)
    # Clean extra whitespace and normalize to single spaces
    return ' '.join(text.split())


# AI Improvement (2026-03-03)
# Add a utility to normalize subreddit names for consistent API queries.
def normalize_subreddit_name(name):
    """Cleans subreddit input by removing 'r/' or '/r/' prefixes and whitespace."""
    if not name:
        return ""
    clean_name = name.strip().lower().lstrip('/')
    return clean_name[2:] if clean_name.startswith('r/') else clean_name


# AI Improvement (2026-03-03)
# Add a word frequency counter with stopword filtering to extract meaningful insights from post content.
from collections import Counter

def get_word_frequencies(texts, top_n=20):
    """Extracts the most frequent words from a list of strings, filtering out common stopwords."""
    stopwords = {'the', 'and', 'this', 'that', 'with', 'from', 'for', 'was', 'were', 'about', 'would', 'could', 'their', 'there'}
    all_words = []
    for text in texts:
        clean_text = sanitize_post_text(text)
        # Extract words with 3+ characters and convert to lowercase
        words = re.findall(r'\b\w{3,}\b', clean_text.lower())
        all_words.extend([w for w in words if w not in stopwords])
    return Counter(all_words).most_common(top_n)


# AI Improvement (2026-03-03)
# Add HTML entity unescaping to the text sanitization utility.
import re
import html

def sanitize_post_text(text):
    """Removes Markdown syntax, URLs, and HTML entities to provide clean text for analysis."""
    if not text:
        return ""
    # Unescape HTML entities (e.g., &amp; to &)
    text = html.unescape(text)
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove common Markdown formatting characters (bold, italic, headers, blockquotes)
    text = re.sub(r'[*_~`#>]', '', text)
    # Clean extra whitespace and normalize to single spaces
    return ' '.join(text.split())
