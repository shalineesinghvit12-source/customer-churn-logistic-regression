# Customer Churn Prediction Using Logistic Regression

## Overview

This project develops an interpretable logistic regression model to predict customer churn using subscription length, complaints filed, satisfaction score, and discount usage.

The original model achieved **86% accuracy** and **0.861 ROC-AUC** on the test set. Although overall discrimination was good, churn recall was **46%**, showing that the default threshold missed more than half of actual churners.

## Business objective

The goal is to help a business:

- identify customers at risk of churn
- understand the factors associated with churn
- prioritize retention interventions
- balance precision and recall based on intervention cost

## Dataset

The original dataset contains 1,000 customer records and 12 columns. The model uses:

| Feature | Description |
|---|---|
| `SubscriptionLength` | Length of the customer subscription |
| `ComplaintsFiled` | Number of complaints filed |
| `SatisfactionScore` | Customer satisfaction rating |
| `DiscountUsed` | Whether a discount was used |
| `Churn` | Target variable, where 1 indicates churn |

The dataset is not included in this repository. Add `customer_sales_churn.csv` to the `data/` folder or upload it when prompted in Google Colab.

## Workflow

1. Load and validate the data
2. Check missing values and duplicates
3. Explore target balance and feature relationships
4. Create a stratified train/test split
5. Train a logistic regression model
6. Evaluate accuracy, precision, recall, F1-score, confusion matrix, and ROC-AUC
7. Interpret coefficients and odds ratios
8. Analyze alternative classification thresholds
9. Translate results into business recommendations

## Verified original results

| Metric | Score |
|---|---:|
| Accuracy | 0.86 |
| ROC-AUC | 0.861 |
| Churn precision | 0.66 |
| Churn recall | 0.46 |
| Churn F1-score | 0.54 |

## Key insights

- `ComplaintsFiled` had the strongest positive coefficient, indicating higher churn odds as complaints increased.
- `SatisfactionScore` was negatively associated with churn.
- `SubscriptionLength` was negatively associated with churn.
- `DiscountUsed` was positively associated with churn, but this should not be interpreted as causal.
- Churn recall was substantially lower than overall accuracy, so threshold selection is important for retention use cases.

## Business recommendations

- Escalate repeated complaints and proactively contact high-risk customers.
- Follow up on low satisfaction scores.
- Test loyalty and renewal incentives.
- Review whether discounts are targeted toward customers who are already at risk.
- Consider lowering the classification threshold when the cost of missing a churner is high.

## Repository structure

```text
customer-churn-logistic-regression/
├── customer_churn_logistic_regression.ipynb
├── README.md
├── requirements.txt
├── .gitignore
├── LICENSE
├── data/
│   └── README.md
└── images/
```

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Google Colab / Jupyter Notebook

## How to run

### Google Colab

1. Open the notebook in Colab.
2. Run all cells.
3. Upload `customer_sales_churn.csv` when prompted.

### Local environment

```bash
git clone YOUR_REPOSITORY_URL
cd customer-churn-logistic-regression
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

On Windows, activate the environment with:

```bash
.venv\Scripts\activate
```

Place the CSV file in `data/customer_sales_churn.csv`, open the notebook, and run all cells.

## Limitations

- The model uses only four predictors.
- The results are based on one train/test split.
- Logistic regression assumes a linear relationship in log-odds.
- Coefficients indicate association rather than causation.
- The cleaned notebook uses a stratified split, so rerun results may differ slightly from the original assignment.

## Author

**Shalinee Singh**

Connect through the LinkedIn and GitHub links provided on my resume.
