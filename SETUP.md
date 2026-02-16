# Setup Guide for Social Media Analytics

## Quick Setup

### 1. Install Dependencies
```bash
pip install flask praw --break-system-packages
```

### 2. Run the App
```bash
python app.py
```

### 3. Open Browser
Navigate to: `http://localhost:5000`

### 4. Try It Out
- Enter a subreddit: `python`, `programming`, `technology`, `worldnews`
- Click Analyze
- View the analytics!

## Example Subreddits to Try

**Tech:**
- `python` - Python programming
- `programming` - General programming
- `webdev` - Web development
- `MachineLearning` - ML discussions

**News:**
- `worldnews` - World news
- `technology` - Tech news
- `science` - Science news

**Fun:**
- `memes` - Memes
- `funny` - Funny content
- `aww` - Cute animals

**Sports:**
- `nba` - Basketball
- `soccer` - Football/Soccer
- `nfl` - American Football

## Troubleshooting

### "Module not found"
```bash
pip install flask praw --break-system-packages
```

### "Address already in use"
Change port in `app.py`:
```python
app.run(debug=True, host='0.0.0.0', port=5001)  # Changed to 5001
```

### Reddit API Limits
The app uses read-only mode which has limits. For more requests:

1. Go to https://www.reddit.com/prefs/apps
2. Click "Create App"
3. Choose "script"
4. Add credentials to `app.py`

## Using with Gemini Bot

1. **Initialize Git**
```bash
cd social-media-analytics
git init
git add .
git commit -m "Initial commit: Social Media Analytics app"
```

2. **Create GitHub Repo**
- Go to https://github.com/new
- Create repo named `social-media-analytics`

3. **Push to GitHub**
```bash
git remote add origin https://github.com/YOUR_USERNAME/social-media-analytics.git
git branch -M main
git push -u origin main
```

4. **Point Gemini Bot**
Edit `gemini_github_bot.py`:
```python
REPO_PATH = os.path.expanduser("~/social-media-analytics")
```

5. **Let Gemini Improve It!**
```bash
python3 gemini_github_bot.py
```

## What Gemini Can Add

Gemini will continuously improve your project:

**Week 1:**
- Better error handling
- Loading states
- Input validation

**Week 2:**
- Sentiment analysis
- Export to CSV
- More charts

**Week 3:**
- Date range filters
- Multi-subreddit comparison
- Advanced analytics

**Month 1:**
- User authentication
- Saved searches
- Email alerts
- API endpoints

**Month 2:**
- Machine learning predictions
- Trend forecasting
- Network analysis
- Real-time updates

## Next Steps

1. ✅ Test the app locally
2. ✅ Push to GitHub
3. ✅ Set up Gemini bot
4. ✅ Let AI improve it daily
5. ✅ Review and merge improvements
6. ✅ Watch your GitHub graph turn green!

## Tips

- Start with small subreddits (faster analysis)
- Try different subreddits to test variety
- Check the database file (`analytics.db`) to see stored data
- Monitor Gemini's improvements to learn new techniques

Enjoy your automated code improvements! 🚀
