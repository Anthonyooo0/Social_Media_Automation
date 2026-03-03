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


# AI Improvement (2026-03-03)
# Add a basic sentiment analysis utility to estimate post tone.

def estimate_sentiment(text):
    """Provides a rudimentary sentiment score (-1 to 1) based on keyword matching."""
    pos_terms = {'amazing', 'best', 'excellent', 'good', 'great', 'helpful', 'love', 'perfect', 'thanks', 'wonderful'}
    neg_terms = {'awful', 'bad', 'broken', 'error', 'fail', 'hate', 'issue', 'problem', 'terrible', 'worst'}
    words = re.findall(r'\w+', (text or "").lower())
    if not words: return 0.0
    score = sum(1 for w in words if w in pos_terms) - sum(1 for w in words if w in neg_terms)
    # Normalize by square root of length to dampen the effect of long posts
    return round(max(min(score / (len(words)**0.5), 1.0), -1.0), 2)


# AI Improvement (2026-03-03)
# Add a keyword extraction helper that filters out stop words.

def extract_keywords(text):
    """Extracts meaningful keywords from text by removing common stop words and punctuation."""
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were', 'to', 'for', 'in', 'on', 'at', 'by', 'with', 'from', 'as', 'it', 'its', 'that', 'this', 'of', 'be', 'has', 'have', 'do', 'if', 'then', 'which', 'who', 'where', 'when', 'how'}
    # Extract alphanumeric words of at least 3 characters and filter against stop words
    words = re.findall(r'[a-z]{3,}', text.lower())
    return [w for w in words if w not in stop_words]


# AI Improvement (2026-03-03)
# Add a reading time estimation utility
def estimate_reading_time(text, words_per_minute=200):
    """Estimates the reading time in minutes for a given text content."""
    if not text:
        return 0
    words = text.split()
    # Ensure at least 1 minute is returned for any non-empty text
    return max(1, round(len(words) / words_per_minute))
