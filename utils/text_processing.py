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
