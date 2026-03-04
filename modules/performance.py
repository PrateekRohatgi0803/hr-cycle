from nltk.sentiment import SentimentIntensityAnalyzer

def analyze_feedback(feedback):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(feedback)
    return sentiment