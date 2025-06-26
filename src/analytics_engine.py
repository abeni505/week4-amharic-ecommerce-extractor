# src/analytics_engine.py
import pandas as pd
import numpy as np
import re
from tqdm import tqdm

def calculate_vendor_metrics(df: pd.DataFrame, ner_pipeline):
    """Calculates all key performance metrics for each vendor."""
    df['date'] = pd.to_datetime(df['date']).dt.tz_localize(None)
    total_weeks = max(1, (df['date'].max() - df['date'].min()).days / 7)
    
    posts_per_channel = df.groupby('channel')['message_id'].count()
    posting_frequency = posts_per_channel / total_weeks
    avg_views_per_post = df.groupby('channel')['views'].mean().fillna(0)
    
    def extract_avg_price(text_series):
        all_prices = []
        # Use tqdm to show a progress bar for this long-running process
        for text in tqdm(text_series, desc="Extracting Prices"):
            try:
                entities = ner_pipeline(text)
                for ent in entities:
                    if ent['entity'].endswith('PRICE'):
                        price_str = re.sub(r'[^\d.]', '', ent['word'])
                        if price_str:
                            all_prices.append(float(price_str))
            except Exception:
                continue
        return np.mean(all_prices) if all_prices else 0

    print("Extracting average price points for each vendor...")
    avg_price_point = df.groupby('channel')['processed_text'].apply(extract_avg_price)
    
    scorecard = pd.DataFrame({
        'Posts/Week': posting_frequency,
        'Avg. Views/Post': avg_views_per_post,
        'Avg. Price (ETB)': avg_price_point
    }).fillna(0)
    
    return scorecard

def create_lending_score(scorecard: pd.DataFrame):
    """Creates a simple, weighted lending score based on vendor metrics."""
    # Normalize metrics to a 0-1 scale to allow fair comparison
    normalized_card = scorecard.apply(lambda x: (x - x.min()) / (x.max() - x.min()) if (x.max() - x.min()) > 0 else 0)
    
    # Define weights as per the project prompt example
    scorecard['Lending Score'] = (normalized_card['Avg. Views/Post'] * 0.5 + normalized_card['Posts/Week'] * 0.5) * 100
    
    return scorecard.sort_values('Lending Score', ascending=False)