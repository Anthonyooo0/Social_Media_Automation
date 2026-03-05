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


# AI Improvement (2026-03-04)
# Complete the normalize_subreddit_name function to robustly handle various subreddit input formats.
def normalize_subreddit_name(name):
    """Cleans subreddit input by removing 'r/' or '/r/' prefixes and whitespace."""
    if not name:
        return ""
    # Strip whitespace and normalize to lowercase
    clean_name = name.strip().lower()
    # Remove 'r/' or '/r/' prefixes using regex
    clean_name = re.sub(r'^/?r/', '', clean_name)
    # Ensure no trailing slashes remain
    return clean_name.strip('/')


# AI Improvement (2026-03-04)
# Add a utility to extract multi-word phrases (n-grams) from text.
def extract_phrases(text, n=2):
    """
    Extracts n-gram phrases (default bigrams) from the text.
    Helpful for identifying trending topics that consist of multiple words.
    """
    if not text:
        return []
    words = re.findall(r'\w+', text.lower())
    if len(words) < n:
        return []
    return [' '.join(words[i:i+n]) for i in range(len(words)-n+1)]


# AI Improvement (2026-03-04)
# Add a basic sentiment analysis helper to estimate the emotional tone of post content.
def estimate_sentiment(text):
    """
    Estimates text sentiment from -1.0 (negative) to 1.0 (positive) using keyword analysis.
    This provides a foundation for the roadmap's sentiment analysis feature.
    """
    pos_words = {'excellent', 'great', 'good', 'amazing', 'helpful', 'love', 'best', 'cool', 'upvote'}
    neg_words = {'terrible', 'bad', 'awful', 'boring', 'useless', 'hate', 'worst', 'issue', 'wrong'}
    
    words = re.findall(r'\w+', (text or "").lower())
    if not words:
        return 0.0
    
    score = sum(1 for w in words if w in pos_words) - sum(1 for w in words if w in neg_words)
    # Normalize by word density to keep score within -1 to 1 range
    normalized_score = score / (len(words) * 0.1 + 1)
    return round(max(min(normalized_score, 1.0), -1.0), 2)


# AI Improvement (2026-03-05)
# Add a stopword removal utility to filter out common filler words from text analysis.

# AI Improvement (2026-03-05)
# Add a utility to remove common English stopwords for more meaningful frequency analysis.
def remove_stopwords(text, extra_words=None):
    """Removes common English stopwords to highlight meaningful keywords in word frequency analysis."""
    stopwords = {"the", "a", "an", "and", "or", "but", "if", "then", "else", "when", "at", "from", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "of", "in", "on", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "do", "does", "did", "this", "that", "it", "they", "them", "their", "we", "us", "our", "i", "me", "my", "you", "your"}
    if extra_words:
        stopwords.update(extra_words)
    
    words = text.lower().split()
    filtered_words = [word for word in words if word.isalnum() and word not in stopwords]
    return " ".join(filtered_words)


# AI Improvement (2026-03-05)
# Complete the unfinished normalize_subreddit_name function to handle various user input formats correctly.
    # Remove whitespace and convert to lowercase for consistency
    clean_name = name.strip().lower()
    # Remove common prefixes 'r/' or '/r/' using regex for robustness
    clean_name = re.sub(r'^/?r/', '', clean_name)
    # Remove any surrounding slashes and return
    return clean_name.strip('/')


# AI Improvement (2026-03-05)
# Add a basic sentiment analysis helper to evaluate the emotional tone of post content.

def calculate_sentiment_score(text):
    """
    Calculates a simple sentiment polarity score based on positive and negative word matches.
    Returns a float where > 0 is positive and < 0 is negative.
    """
    if not text:
        return 0.0
    
    pos_words = {'great', 'good', 'excellent', 'amazing', 'helpful', 'awesome', 'best', 'happy'}
    neg_words = {'bad', 'awful', 'terrible', 'worst', 'horrible', 'useless', 'wrong', 'sad'}
    
    tokens = re.findall(r'\w+', text.lower())
    if not tokens:
        return 0.0
        
    score = sum(1 for word in tokens if word in pos_words) - sum(1 for word in tokens if word in neg_words)
    return round(score / len(tokens), 4)


# AI Improvement (2026-03-05)
# Add a utility to extract and normalize the domain from URLs for content source analysis.
def extract_domain(url):
    """
    Extracts the base domain from a URL to identify content sources.
    Returns 'self' for text posts and 'reddit_media' for internal uploads.
    """
    from urllib.parse import urlparse
    if not url or not isinstance(url, str):
        return "self"
    domain = urlparse(url).netloc.lower()
    if not domain:
        return "self"
    if 'redd.it' in domain:
        return "reddit_media"
    return domain.replace('www.', '')


# AI Improvement (2026-03-05)
# Add a stopword removal utility to filter common English words from text analysis.
def remove_stopwords(text):
    """Removes common English stopwords to refine word frequency analysis."""
    stopwords = {'a', 'an', 'the', 'and', 'or', 'but', 'if', 'because', 'as', 'of', 'at', 'by', 'for', 'with', 'about', 'into', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'do', 'does', 'did', 'this', 'that', 'these', 'those', 'i', 'me', 'my', 'we', 'our', 'you', 'your', 'he', 'him', 'his', 'she', 'her', 'it', 'its', 'they', 'them', 'their'}
    return ' '.join([w for w in text.lower().split() if w not in stopwords and w.isalnum()])
