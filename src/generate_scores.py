# generate_scores.py

import json
import pandas as pd
import numpy as np
from datetime import datetime
from collections import defaultdict
import matplotlib.pyplot as plt
import os

# Load JSON data
def load_data(path):
    with open(path, 'r') as f:
        return json.load(f)

# Convert amount to float USD value
def calculate_usd(row):
    try:
        amount = float(row['actionData']['amount']) / 1e18  # assume 18 decimals typical for DeFi
        price = float(row['actionData']['assetPriceUSD'])
        return amount * price
    except:
        return 0.0

# Feature Engineering
def build_wallet_features(data):
    wallets = defaultdict(lambda: defaultdict(float))
    timestamps = defaultdict(list)

    for tx in data:
        wallet = tx['userWallet']
        action = tx['action'].lower()
        usd_value = calculate_usd(tx)
        timestamp = tx['timestamp']

        wallets[wallet][f"count_{action}"] += 1
        wallets[wallet][f"usd_{action}"] += usd_value
        timestamps[wallet].append(timestamp)

        if action == 'liquidationcall':
            wallets[wallet]['was_liquidated'] = 1

    # Derived features
    for wallet in wallets:
        t_list = timestamps[wallet]
        if t_list:
            t_min = min(t_list)
            t_max = max(t_list)
            wallets[wallet]['active_days'] = (t_max - t_min) / (60 * 60 * 24)

        borrow = wallets[wallet]['usd_borrow']
        repay = wallets[wallet]['usd_repay']
        deposit = wallets[wallet]['usd_deposit']
        redeem = wallets[wallet]['usd_redeemunderlying']

        wallets[wallet]['repay_borrow_ratio'] = repay / borrow if borrow else 0
        wallets[wallet]['redeem_deposit_ratio'] = redeem / deposit if deposit else 0

    df = pd.DataFrame(wallets).T.reset_index().rename(columns={"index": "userWallet"})
    return df.fillna(0)

# Score Calculation (Heuristic Model)
def score_wallets(df):
    scores = []
    for _, row in df.iterrows():
        score = 500  # base

        if row['repay_borrow_ratio'] > 0.9:
            score += 100
        elif row['repay_borrow_ratio'] < 0.3:
            score -= 100

        if row['redeem_deposit_ratio'] > 0.5:
            score += 50

        if row['was_liquidated']:
            score -= 200

        if row['active_days'] > 90:
            score += 50

        score = max(0, min(1000, score))
        scores.append(score)

    df['creditScore'] = scores
    return df[['userWallet', 'creditScore']]

# Plot Score Distribution
def plot_distribution(df):
    df['score_band'] = (df['creditScore'] // 100) * 100
    dist = df['score_band'].value_counts().sort_index()
    dist.plot(kind='bar', title='Score Distribution', xlabel='Score Range', ylabel='Wallet Count')
    plt.tight_layout()
    plt.savefig('score_distribution.png')
    plt.close()

# Main Execution
def main():
    input_path = 'data/user-wallet-transactions.json'
    os.makedirs('data', exist_ok=True)
    
    data = load_data(input_path)
    features_df = build_wallet_features(data)
    scored_df = score_wallets(features_df)

    scored_df.to_csv('wallet_scores.csv', index=False)
    plot_distribution(scored_df)

if __name__ == '__main__':
    main()
