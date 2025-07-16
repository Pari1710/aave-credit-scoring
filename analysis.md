# 📊 Wallet Score Analysis

This document provides insights into the distribution and behavior of DeFi wallets after applying the credit scoring model to Aave V2 transaction data.

---

## 🧮 Score Distribution

The wallet scores were grouped into the following bands:

- **0–100**
- **100–200**
- **200–300**
- **300–400**
- **400–500**
- **500–600**
- **600–700**
- **700–800**
- **800–900**
- **900–1000**

### 📈 Bar Chart: Score Distribution

A bar chart (`score_distribution.png`) was generated to visualize the count of wallets in each score band.

**Key Observations:**
- 🔵 **Most wallets fall in the 400–499 range**, with this band containing the **highest number of wallets** (~2500+).
- 🟢 The **600–699 band** is the second most populated, suggesting moderate credit behavior.
- 🟠 The **500–599 band** shows a smaller but still relevant count.
- 🔴 Very few wallets fall below 300 or above 700, indicating **extremely poor or extremely good behavior is rare**.

---

## 🔍 Behavior by Score Range

### 🟥 Low Score Range (0–300)
- Wallets in this range often:
  - Had **liquidations**
  - Showed **poor repay-to-borrow** or **redeem-to-deposit ratios**
  - Were active for **very short durations**
- Likely to be **bots, risky actors, or abusers of the system**

### 🟡 Mid Score Range (400–600)
- Majority of wallets fall here.
- These wallets show:
  - **Moderate or good repayment behavior**
  - Some red flags but generally consistent participation
  - Healthy ratios but **shorter active windows**

### 🟢 High Score Range (600–800+)
- Wallets in this group:
  - Showed **excellent repayment and redemption behavior**
  - Had **no liquidation calls**
  - Were active over a **longer time period**
- Ideal candidates for **credit delegation** or **future DeFi airdrops**

---

## ✅ Summary

The score distribution highlights the **effectiveness of transaction behavior as a proxy for creditworthiness**. By combining multiple on-chain features, we created a system that distinguishes between:

- Trustworthy and consistent users
- Irregular or bot-like patterns
- Abusive or high-risk behavior

---

📁 For further details, check the scoring logic in [`src/generate_scores.py`](./src/generate_scores.py).
