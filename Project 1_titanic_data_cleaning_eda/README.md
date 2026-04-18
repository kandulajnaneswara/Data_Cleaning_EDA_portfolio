# Titanic Data Cleaning & Exploratory Data Analysis

## 📌 Project Overview
This project focuses on cleaning and analyzing the Titanic dataset from Kaggle. The goal is to transform raw data into an analysis-ready format and extract meaningful insights about passenger survival.

## 💡 Skills Demonstrated
- Data Cleaning
- Handling Missing Values
- Exploratory Data Analysis (EDA)
- Data Visualization
- Feature Engineering

## 🎯 Objectives
- Handle missing values and inconsistencies.
- Perform exploratory data analysis.
- Generate actionable insights.
- Create a clean dataset for future modeling.

## 🛠️ Tools & Technologies
- Python
- Pandas & NumPy
- Matplotlib & Seaborn
- Jupyter Notebook

## 🧹 Data Cleaning Steps
- Filled missing values in `Age` and `Embarked`.
- Dropped the `Cabin` column due to excessive missing data.
- Removed duplicate records.
- Standardized categorical variables.
- Engineered new features such as `FamilySize` and `Title`.

## ❗ Problem Statement
The dataset contains missing values, inconsistent data, and requires preprocessing before analysis.

## ✅ Solution
- Filled missing values in Age and Embarked
- Removed duplicates
- Standardized categorical columns
- Created new features for better analysis

## 📊 Key Insights
- Female passengers had a significantly higher survival rate.
- First-class passengers were more likely to survive.
- Higher fares were associated with increased survival.
- Larger family sizes showed varying survival patterns.

## 📦 Deliverables

- Cleaned dataset (CSV)
- Python script
- Visualizations
- Insight summary

## 📂 Project Structure
```text
titanic-data-cleaning-eda/
│
├── plots/
│  ├── chart1_survival_distribution.png
│  └── chart2_survival_by_gender.png
│  └── chart3_age_distribution.png
│  └── chart4_correlation_heatmap.png
│  └── chart5_fare_vs_survival.png
│── train.csv
│── cleaned_titanic_dataset.csv
├── titanic_eda.py
└── README.md
└── How_to_run.md




