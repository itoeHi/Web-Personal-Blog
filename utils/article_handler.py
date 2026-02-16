import os
import json
from datetime import datetime

ARTICLES_DIR = 'articles'

def get_article_path(article_id):
    """Aquired article file path"""
    return os.path.join(ARTICLES_DIR, f'article_{article_id}.json')

def get_all_articles():
    """Aquried all articles"""
    articles = []

    if not os.path.exists(ARTICLES_DIR):
        return articles
    
    for filename in os.listdir(ARTICLES_DIR):
        if filename.endswith('.json'):
            filepath = os.path.join(ARTICLES_DIR, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    article = json.load(f)
                    articles.append(article)
            except:
                continue
            
    return articles

def get_article_by_id(article_id):
    """Aqurired article by ID"""
    filepath = get_article_path(article_id)

    if os.path.exists(filepath):
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return None
    return None

def get_next_id():
    """Aqurired next usable article ID"""
    articles = get_all_articles()
    if not articles:
        return 1
    
    # Aquired max ID and add 1
    max_id = max(article['id'] for article in articles)
    return max_id + 1

def create_article(article_data):
    """Create new article"""
    try:
        filepath = get_article_path(article_data['id'])
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(article_data, f, ensure_ascii=False, indent=2)
        return True
    except:
        return False
    
def update_article(article_id, article_data):
    """Update article"""
    filepath = get_article_path(article_id)

    if os.path.exists(filepath):
        try:
            # Save origin publish date
            old_article = get_article_by_id(article_id)
            if old_article and 'created_at' in old_article:
                article_data['created_at'] = old_article['created_at']
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(article_data, f, ensure_ascii=False, indent=2)
            return True
        except:
            return False
    return False
    
def delete_article(article_id):
    """Delete article"""
    filepath = get_article_path(article_id)

    if os.path.exists(filepath):
        try:
            os.remove(filepath)
            return True
        except:
            return False
    return False
