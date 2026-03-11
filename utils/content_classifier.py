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
