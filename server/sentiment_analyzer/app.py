"""
Sentiment Analysis Microservice
Flask-based REST API that analyzes the sentiment of a review text.
"""

from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def analyze_sentiment(text: str) -> str:
    """
    Simple rule-based sentiment analysis.
    Returns 'positive', 'negative', or 'neutral'.
    In production, replace with a real NLP model (e.g., NLTK VADER, transformers).
    """
    if not text:
        return 'neutral'

    text_lower = text.lower()

    positive_words = [
        'great', 'excellent', 'fantastic', 'amazing', 'wonderful', 'awesome',
        'outstanding', 'superb', 'perfect', 'best', 'love', 'happy', 'satisfied',
        'recommend', 'helpful', 'friendly', 'professional', 'efficient', 'smooth',
        'quick', 'honest', 'fair', 'nice', 'good', 'pleased', 'delighted',
        'impressive', 'top', 'exceptional', 'incredible', 'brilliant', 'terrific',
    ]

    negative_words = [
        'bad', 'terrible', 'awful', 'horrible', 'worst', 'poor', 'disappointed',
        'disappointing', 'unhappy', 'upset', 'rude', 'unprofessional', 'slow',
        'overpriced', 'expensive', 'waste', 'avoid', 'never', 'problem', 'issue',
        'wrong', 'broken', 'defective', 'frustrating', 'annoying', 'dishonest',
        'scam', 'fraud', 'lied', 'deceived', 'regret', 'mistake',
    ]

    pos_score = sum(1 for w in positive_words if w in text_lower)
    neg_score = sum(1 for w in negative_words if w in text_lower)

    if pos_score > neg_score:
        return 'positive'
    elif neg_score > pos_score:
        return 'negative'
    else:
        return 'neutral'


@app.route('/analyze/<path:review_text>', methods=['GET'])
def analyze(review_text):
    """GET /analyze/<review_text> — returns sentiment analysis result."""
    sentiment = analyze_sentiment(review_text)
    return jsonify({
        'sentiment': sentiment,
        'text': review_text,
        'status': 200,
    })


@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok', 'service': 'sentiment-analyzer'})


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5050))
    app.run(host='0.0.0.0', port=port, debug=False)
