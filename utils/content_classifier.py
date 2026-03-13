# Add a content classification utility to categorize posts into types like Questions, Links, or Media.
# AI Improvement (2026-03-11)
def classify_post_type(title):
    """
    Categorizes a post title to help analyze what content formats perform best.
    """
    if not title:
        return "Unknown"

    t = title.lower().strip()
    # Detect questions based on punctuation or common starting interrogatives
    if "?" in t or any(t.startswith(w) for w in ["how", "why", "what", "can", "is "]):
        return "Question"
    # Detect media-based posts
    if any(x in t for x in ["[img]", "[video]", ".jpg", ".png", ".gif", "v.redd.it"]):
        return "Media"
    # Detect external news or source links
    if "http" in t or "www." in t:
        return "Link"

    return "Discussion"


# AI Improvement (2026-03-13)
# Add a utility to detect potential clickbait patterns in post titles.


# AI Improvement (2026-03-14)
def is_potential_clickbait(title):
    """
    Detects if a title exhibits common clickbait patterns such as 
    excessive capitalization, cliffhanger phrases, or repetitive punctuation.
    """
    if not title:
        return False

    # Check for excessive capitalization (e.g., >50% of words are ALL CAPS)
    words = title.split()
    if len(words) >= 3:
        caps_count = sum(1 for w in words if w.isupper() and len(w) > 1)
        if caps_count / len(words) > 0.5:
            return True

    # Common clickbait phrases and patterns
    clickbait_triggers = ["won't believe", "this happens", "reasons why", "secret to", "top 10", "shocking"]
    t_lower = title.lower()
    if any(trigger in t_lower for trigger in clickbait_triggers):
        return True

    # Excessive punctuation patterns
    if "!!!" in title or "???" in title:
        return True

    return False
