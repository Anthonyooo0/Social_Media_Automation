#!/usr/bin/env python3
"""
Social Media Analytics - Reddit & Twitter Data Analyzer
Analyzes posts, engagement, trends, and sentiment from social media
"""

from flask import Flask, render_template, request, jsonify
import praw
import sqlite3
from datetime import datetime, timedelta
from collections import Counter
import re
import json

app = Flask(__name__)

# Database setup
def init_db():
    """Initialize SQLite database"""
    conn = sqlite3.connect('analytics.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS reddit_posts
                 (id TEXT PRIMARY KEY,
                  subreddit TEXT,
                  title TEXT,
                  author TEXT,
                  score INTEGER,
                  num_comments INTEGER,
                  created_utc INTEGER,
                  url TEXT,
                  selftext TEXT,
                  fetched_at TIMESTAMP)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS analytics
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  source TEXT,
                  query TEXT,
                  total_posts INTEGER,
                  avg_score REAL,
                  top_words TEXT,
                  created_at TIMESTAMP)''')
    
    conn.commit()
    conn.close()

init_db()

def get_reddit_client():
    """Create Reddit client (read-only mode)"""
    # Using read-only mode - no authentication needed
    reddit = praw.Reddit(
        client_id='read_only_mode',
        client_secret=None,
        user_agent='Social Media Analytics v1.0'
    )
    return reddit

def analyze_reddit(subreddit_name, limit=100):
    """Fetch and analyze Reddit posts"""
    try:
        reddit = get_reddit_client()
        subreddit = reddit.subreddit(subreddit_name)
        
        posts = []
        word_counter = Counter()
        hour_counter = Counter()
        
        for post in subreddit.hot(limit=limit):
            # Store post data
            post_data = {
                'id': post.id,
                'title': post.title,
                'author': str(post.author),
                'score': post.score,
                'num_comments': post.num_comments,
                'created_utc': post.created_utc,
                'url': post.url,
                'selftext': post.selftext[:500] if post.selftext else ''
            }
            posts.append(post_data)
            
            # Word frequency analysis
            text = f"{post.title} {post.selftext}".lower()
            words = re.findall(r'\b[a-z]{3,}\b', text)
            word_counter.update(words)
            
            # Posts by hour
            hour = datetime.fromtimestamp(post.created_utc).hour
            hour_counter[hour] += 1
            
            # Save to database
            save_post(post_data, subreddit_name)
        
        # Get top words (exclude common words)
        stop_words = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 
                      'can', 'her', 'was', 'one', 'our', 'out', 'this', 'that',
                      'with', 'have', 'from', 'they', 'been', 'what', 'which'}
        top_words = [(word, count) for word, count in word_counter.most_common(50) 
                     if word not in stop_words][:20]
        
        # Calculate stats
        avg_score = sum(p['score'] for p in posts) / len(posts) if posts else 0
        avg_comments = sum(p['num_comments'] for p in posts) / len(posts) if posts else 0
        
        return {
            'success': True,
            'subreddit': subreddit_name,
            'total_posts': len(posts),
            'posts': sorted(posts, key=lambda x: x['score'], reverse=True)[:10],
            'top_words': top_words,
            'posts_by_hour': dict(sorted(hour_counter.items())),
            'avg_score': round(avg_score, 2),
            'avg_comments': round(avg_comments, 2)
        }
        
    except Exception as e:
        return {'success': False, 'error': str(e)}

def save_post(post_data, subreddit):
    """Save post to database"""
    conn = sqlite3.connect('analytics.db')
    c = conn.cursor()
    
    try:
        c.execute('''INSERT OR REPLACE INTO reddit_posts 
                     (id, subreddit, title, author, score, num_comments, 
                      created_utc, url, selftext, fetched_at)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                  (post_data['id'], subreddit, post_data['title'], 
                   post_data['author'], post_data['score'], 
                   post_data['num_comments'], post_data['created_utc'],
                   post_data['url'], post_data['selftext'], 
                   datetime.now()))
        conn.commit()
    except Exception as e:
        print(f"Error saving post: {e}")
    finally:
        conn.close()

@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze endpoint"""
    data = request.json
    source = data.get('source', 'reddit')
    query = data.get('query', '')
    limit = int(data.get('limit', 100))
    
    if source == 'reddit':
        result = analyze_reddit(query, limit)
        return jsonify(result)
    else:
        return jsonify({'success': False, 'error': 'Unsupported source'})

@app.route('/history')
def history():
    """Get analysis history"""
    conn = sqlite3.connect('analytics.db')
    c = conn.cursor()
    
    c.execute('SELECT * FROM analytics ORDER BY created_at DESC LIMIT 10')
    history = c.fetchall()
    conn.close()
    
    return jsonify({'history': history})

if __name__ == '__main__':
    print("🚀 Social Media Analytics Server Starting...")
    print("📊 Navigate to: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)


# AI Improvement (2026-02-16)
# Add a text cleaning helper function for word frequency analysis
def clean_text(text):
    """Clean text by removing URLs, punctuation, and converting to lowercase"""
    if not text:
        return ""
    # Remove URLs
    text = re.sub(r'http\S+', '', text)
    # Remove punctuation and numbers, keep only letters and spaces
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    return text.lower().strip()


# AI Improvement (2026-02-16)
# Add a rule-based sentiment analysis helper function
def analyze_sentiment(text):
    """
    Perform basic sentiment analysis on a string.
    Returns a string: 'positive', 'negative', or 'neutral'
    """
    pos_words = {'good', 'great', 'excellent', 'amazing', 'cool', 'love', 'best', 'awesome', 'helpful', 'interesting'}
    neg_words = {'bad', 'terrible', 'awful', 'worst', 'hate', 'boring', 'useless', 'wrong', 'broken', 'issue'}
    
    words = re.findall(r'\w+', text.lower())
    score = sum(1 for word in words if word in pos_words) - sum(1 for word in words if word in neg_words)
    
    return 'positive' if score > 0 else 'negative' if score < 0 else 'neutral'


# AI Improvement (2026-02-16)
# Add a helper function to sanitize subreddit name inputs
def sanitize_subreddit(name):
    """Standardize subreddit input (handles 'r/python', URLs, etc.)"""
    if not name:
        return ''
    return name.strip().rstrip('/').split('/')[-1]



# AI Improvement (2026-02-16)
# Expand the database schema to include a sentiment_score column for persisting analysis results
                  score INTEGER,
                  num_comments INTEGER,
                  created_utc INTEGER,
                  sentiment_score REAL)''')


# AI Improvement (2026-02-16)
# Add a helper function to calculate 'post velocity' (score per hour)
def calculate_post_velocity(score, created_utc):
    """Calculates score accumulation per hour to identify trending content regardless of age"""
    age_in_hours = (datetime.now().timestamp() - created_utc) / 3600
    return round(score / max(age_in_hours, 0.1), 2)



# AI Improvement (2026-02-17)
# Add a stop-word filtering helper to improve the quality of word frequency analysis
def filter_stop_words(words):
    """Remove common English stop words to ensure word frequency analysis highlights meaningful terms"""
    stop_words = {'the', 'and', 'for', 'this', 'that', 'with', 'from', 'was', 'are', 'they', 'their', 'have', 'has', 'not', 'but', 'what', 'who', 'how', 'where', 'your', 'about', 'will', 'just', 'can'}
    return [w for w in words if w.lower() not in stop_words and len(w) > 2]


# AI Improvement (2026-02-17)
# Add a helper function to identify the peak posting hour from a collection of posts.
def get_peak_activity_hour(posts):
    """Identify the hour of the day with the highest frequency of posts"""
    if not posts:
        return None
    hours = [datetime.fromtimestamp(p.get('created_utc', 0)).hour for p in posts]
    most_common = Counter(hours).most_common(1)
    return most_common[0][0] if most_common else None


# AI Improvement (2026-02-17)
# Add a basic keyword-based sentiment analysis helper function to process post titles
def analyze_sentiment(text):
    """Perform basic keyword-based sentiment analysis on a string."""
    pos = {'upvote', 'good', 'great', 'awesome', 'interesting', 'cool', 'best', 'love', 'helpful'}
    neg = {'downvote', 'bad', 'terrible', 'awful', 'boring', 'worst', 'hate', 'annoying', 'useless'}
    words = re.findall(r'\w+', text.lower())
    return sum(1 for w in words if w in pos) - sum(1 for w in words if w in neg)


# AI Improvement (2026-02-17)
# Add a helper function to identify the most frequent contributors in a set of posts
def get_top_contributors(posts, limit=5):
    """Identify the most active authors in the provided dataset"""
    authors = [p.get('author') for p in posts if p.get('author')]
    return Counter(authors).most_common(limit)


# AI Improvement (2026-02-17)
# Add a helper function to calculate the engagement ratio (comments per upvote).
def calculate_engagement_ratio(score, num_comments):
    """
    Calculates the ratio of comments to upvotes.
    High ratios often indicate controversial or highly engaging discussion-based content.
    """
    return round(num_comments / max(score, 1), 4)


# AI Improvement (2026-02-17)
# Add a trending score helper function to calculate post momentum using time decay
def calculate_trending_score(score, num_comments, created_utc):
    """
    Calculates a trending score using a gravity-based decay formula.
    Higher values indicate content gaining traction quickly relative to its age.
    """
    age_hours = max(0.1, (datetime.now().timestamp() - created_utc) / 3600)
    # Weighting: Score + (Comments * 2) / (Age + 2)^1.5
    return round((score + (num_comments * 2)) / (age_hours + 2)**1.5, 3)


# AI Improvement (2026-02-17)
# Add a helper function to extract meaningful keywords by filtering out common stop words.
def get_filtered_keywords(titles, limit=20):
    """Extracts significant keywords from titles by filtering out common stop words."""
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'is', 'are', 'was', 'were', 'to', 'of', 'in', 'for', 'with', 'on', 'at', 'by', 'from', 'up', 'about', 'into', 'over', 'after', 'that', 'this', 'who', 'what', 'where', 'when', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 'can', 'will', 'just', 'should', 'now', 'my', 'your', 'his', 'her', 'its', 'our', 'their', 'me', 'him', 'them', 'us'}
    all_words = []
    for title in titles:
        if not title: continue
        words = re.findall(r'\\w+', title.lower())
        all_words.extend([w for w in words if w not in stop_words and len(w) > 2])
    return Counter(all_words).most_common(limit)


# AI Improvement (2026-02-17)
# Add a helper function to calculate the Jaccard similarity between two sets of keywords for subreddit comparison.
def calculate_subreddit_similarity(keywords_one, keywords_two):
    """
    Computes the similarity score between two subreddits based on their top keywords.
    Uses Jaccard Similarity: (Intersection / Union)
    """
    set1, set2 = set(keywords_one), set(keywords_two)
    if not set1 or not set2:
        return 0.0
    return round(len(set1 & set2) / len(set1 | set2), 4)


# AI Improvement (2026-02-18)
# Add a helper function to perform basic lexicon-based sentiment analysis on post titles.
def get_sentiment_label(text):
    """Categorizes text as Positive, Negative, or Neutral based on a predefined word list."""
    pos_words = {'excellent', 'great', 'good', 'amazing', 'love', 'best', 'awesome', 'incredible', 'positive', 'win'}
    neg_words = {'terrible', 'bad', 'awful', 'worst', 'hate', 'poor', 'negative', 'fail', 'disappointing', 'horrible'}
    tokens = [w.strip('.,!?:;') for w in text.lower().split()]
    score = sum(1 for word in tokens if word in pos_words) - sum(1 for word in tokens if word in neg_words)
    return 'Positive' if score > 0 else 'Negative' if score < 0 else 'Neutral'
