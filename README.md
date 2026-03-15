# 📊 Social Media Analytic

**Analyze Reddit posts, trends, and engagement metrics in real-time!**

A data-driven web application that fetches and analyzes social media content, providing insights into:
- Top trending posts
- Word frequency analysis
- Posting patterns by hour
- Engagement metrics
- Historical data tracking

## 🎯 Features

### Current Features
- ✅ Reddit post analysis (any subreddit)
- ✅ Top 10 most popular posts
- ✅ Word frequency analysis (top 20 words)
- ✅ Post distribution by hour
- ✅ Average score and comments
- ✅ SQLite database storage
- ✅ Beautiful web interface
- ✅ Interactive charts

### 🚀 Coming Soon (Perfect for AI to add!)
- [ ] Sentiment analysis on posts/comments
- [ ] Multi-subreddit comparison
- [ ] Trending topics detection
- [ ] User engagement tracking
- [ ] Export to CSV/PDF
- [ ] Twitter integration
- [ ] Historical trend analysis
- [ ] Predictive analytics
- [ ] Keyword tracking over time
- [ ] Bot detection
- [ ] Engagement heat maps
- [ ] Network analysis
- [ ] Real-time updates
- [ ] Custom date ranges
- [ ] API endpoints
- [ ] User authentication
- [ ] Saved searches
- [ ] Email alerts for trends

## 📸 Screenshots

![Dashboard](https://via.placeholder.com/800x400?text=Social+Media+Analytics+Dashboard)

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/social-media-analytics.git
cd social-media-analytics
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open your browser**
```
http://localhost:5000
```

## 📖 Usage

1. Select platform (Reddit currently supported)
2. Enter subreddit name (without "r/")
   - Examples: `python`, `datascience`, `technology`
3. Choose number of posts to analyze (50-200)
4. Click **Analyze**
5. View results:
   - Overall statistics
   - Hourly post distribution chart
   - Top trending words
   - Most popular posts with scores

## 🗄️ Database

The app uses SQLite to store:
- All fetched posts
- Analysis history
- Cached results

Database file: `analytics.db`

## 📊 What Gets Analyzed

### Reddit Analysis
- **Post metrics**: Score (upvotes), comments, author
- **Timing**: When posts are made (hourly distribution)
- **Content**: Word frequency in titles and text
- **Trends**: Top performing posts
- **Engagement**: Average scores and comment counts

## 🛠️ Tech Stack

- **Backend**: Python, Flask
- **Data**: PRAW (Reddit API), SQLite
- **Frontend**: HTML, CSS, JavaScript
- **Visualizations**: Chart.js
- **Analysis**: Python collections, regex

## 🔑 API Configuration

Currently uses PRAW in **read-only mode** (no authentication needed).

For higher rate limits, add Reddit API credentials:

1. Create app at: https://www.reddit.com/prefs/apps
2. Update `app.py`:
```python
reddit = praw.Reddit(
    client_id='YOUR_CLIENT_ID',
    client_secret='YOUR_CLIENT_SECRET',
    user_agent='Social Media Analytics v1.0'
)
```

## 📈 Future Improvements (AI-Ready!)

This project is **perfect for AI-assisted development**. Here are areas for improvement:

### Data Analysis
- Sentiment analysis using NLP
- Trend prediction models
- Anomaly detection
- Topic modeling (LDA)
- Network analysis of user interactions

### Features
- Compare multiple subreddits
- Track keywords over time
- User behavior analysis
- Bot detection algorithms
- Viral content prediction

### Visualizations
- Heat maps
- Network graphs
- Time series analysis
- Interactive dashboards
- Word clouds with better styling

### Performance
- Caching layer
- Background job processing
- API rate limit handling
- Pagination for large datasets
- Database optimization

### User Experience
- Dark mode
- Mobile responsive design
- Export functionality
- Saved searches
- User accounts
- Custom alerts

## 🤝 Contributing

Contributions welcome! This project is designed to be improved by:
- Manual contributions
- AI-assisted development (Gemini, Claude, etc.)
- Student projects
- Portfolio showcases

## 📝 License

MIT License - feel free to use for personal or commercial projects!

## 🎓 Learning Opportunities

Great project for learning:
- Web scraping and APIs
- Data analysis and visualization
- Flask web development
- Database design
- Frontend development
- Async programming
- NLP and sentiment analysis

## 🐛 Known Issues

- Reddit API rate limits in read-only mode
- Word analysis doesn't filter all stop words
- No error handling for deleted posts
- Limited to hot posts only (not new/top/controversial)

## 📞 Support

- 🐛 Issues: [GitHub Issues](https://github.com/YOUR_USERNAME/social-media-analytics/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/YOUR_USERNAME/social-media-analytics/discussions)

## 🌟 Star History

If you find this useful, please ⭐ star the repo!

## 📚 Resources

- [PRAW Documentation](https://praw.readthedocs.io/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [Chart.js Documentation](https://www.chartjs.org/)
- [Reddit API](https://www.reddit.com/dev/api/)

---

**Made with ❤️ and data**

Perfect for AI improvement via Gemini! 🤖
