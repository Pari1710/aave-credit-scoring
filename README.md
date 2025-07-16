# DeFi Credit Scoring - Aave V2

This project assigns credit scores (0–1000) to wallets interacting with the Aave V2 protocol based on their transaction history.

---

## 📊 Objective

To develop a one-step machine learning or heuristic model that:
- Reads raw Aave V2 transaction data in JSON format.
- Extracts key behavioral features for each wallet.
- Assigns a credit score from 0 (risky) to 1000 (reliable).

---

## 🛠️ Features Engineered

For each wallet:
- Number and USD value of actions: `deposit`, `borrow`, `repay`, `redeem`, `liquidationcall`
- Ratios like `repay/borrow`, `redeem/deposit`
- Liquidation flag
- Activity duration (first to last transaction)

---

## 🧠 Scoring Logic

Heuristic scoring based on behavioral traits:
- +100 if repay/borrow ratio > 0.9
- -100 if repay/borrow ratio < 0.3
- -200 if liquidation occurred
- +50 for activity > 90 days
- +50 if redeem/deposit ratio > 0.5

Final score is clipped between **0 and 1000**.

---

## ▶️ How to Run

1. **Install Requirements**
   ```bash
   pip install -r requirements.txt

---

2. **Place your JSON file at data/user-wallet-transactions.json**

---

3. **Run the script**

---

4. **OUTPUT**
   wallet_scores.csv — Credit scores for each wallet
   score_distribution.png — Visual distribution of scores
