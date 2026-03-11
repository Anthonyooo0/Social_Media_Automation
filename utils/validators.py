# Add a utility to validate subreddit names against Reddit's official naming rules
import re

# AI Improvement (2026-03-11)
def is_valid_subreddit_name(name):
    """
    Validates if a string follows Reddit's subreddit naming rules:
    - 3 to 21 characters
    - Only alphanumeric characters and underscores
    - Does not start with an underscore
    """
    if not name or not (3 <= len(name) <= 21):
        return False
    return bool(re.match(r"^[A-Za-z0-9][A-Za-z0-9_]*$", name))
