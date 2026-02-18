# Add a helper function to analyze and rank the primary domains (content sources) from a list of post URLs.
from urllib.parse import urlparse

def get_source_distribution(urls):
    """Analyzes a list of URLs to determine the distribution of content sources (domains)."""
    counts = {}
    for url in urls:
        domain = urlparse(url).netloc.lower().replace('www.', '')
        if domain:
            counts[domain] = counts.get(domain, 0) + 1
    return sorted(counts.items(), key=lambda x: x[1], reverse=True)
