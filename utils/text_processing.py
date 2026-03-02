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
