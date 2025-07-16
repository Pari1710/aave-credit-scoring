# 🧠 Aave Credit Scoring Engine

This project builds a credit scoring model for DeFi wallets using transaction-level data from the Aave V2 protocol. The goal is to assign each wallet a credit score between **0 and 1000**, where:

- **Higher scores** indicate more reliable and responsible usage.
- **Lower scores** may reflect risky, bot-like, or exploitative behavior.

---

## 📂 Folder Structure

```mermaid
graph TD
    A[Start] --> B(user-wallet-transactions.json);
    B --> C{generate_scores.py};
    C -- Computes Scores --> D(wallet_scores.csv);
    C -- Generates Plot --> E(score_distribution.png);
    D --> F[Analysis];
    E --> F[Analysis];
    F --> G[End];


---

## ⚙️ How It Works

1. **Input**: A JSON file containing raw user transactions (deposits, borrows, repays, etc.).
2. **Feature Engineering**:
   - Repay-to-borrow ratio
   - Redeem-to-deposit ratio
   - Wallet active time (based on first and last transaction)
   - Liquidation penalty
3. **Scoring Logic**:
   - +300 for repay/borrow ratio
   - +100 for redeem/deposit ratio
   - +100 for longer activity period
   - -200 for any liquidation event
4. **Output**: Each wallet is assigned a score between 0 and 1000 and saved to `wallet_scores.csv`.

---

## 📊 Example Output

A sample of the final output looks like:

| userWallet                                 | creditScore |
|-------------------------------------------|-------------|
| 0x00000000001accfa9cef68cf5371a23025b6d4b6 | 400         |
| 0x0000000000e189dd664b9ab08a33c4839953852c | 450         |
| 0x000000000a38444e0a6e37d3b630d7e855a7cb13 | 600         |

The accompanying chart (`score_distribution.png`) provides a visual breakdown of wallet scores.

---

## 🖥️ How to Run

1.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

2.  **Run the Script**

    ```bash
    python src/generate_scores.py
    ```

    **Output:** `wallet_scores.csv` and `score_distribution.png`

---

## 📈 Analysis

See [`analysis.md`](analysis.md) for:

* Score distribution breakdown
* Behavioral insights across credit ranges (0–1000)
* Observations on trustworthy vs risky wallets

---

## 🧪 Sample Use Cases

* Building DeFi-native credit systems
* Identifying trustworthy wallets for airdrops
* Filtering out bot or exploitative behaviors

---

## 🛠️ Built With

* Python 3.12
* Pandas
* Matplotlib

---

## 📫 Contact

For questions or collaboration, feel free to reach out via GitHub Issues or connect at [@Pari1710](https://github.com/Pari1710).

---

### ✅ Instructions to Add It

1.  Open your GitHub repo
2.  Click `README.md` → then ✏️ (Edit this file)
3.  Paste the above content
4.  Click **Commit changes**

---
