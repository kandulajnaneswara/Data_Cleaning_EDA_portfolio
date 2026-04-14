import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("data/train.csv")

# Preview data
print(df.head())

# Volume of dataset
print(df.shape)

# Dataset information
print(df.info())

# Statistical summary
print(df.describe())

# Check missing values
print(df.isnull().sum())


# Data Cleaning
#--------------------------------------------------
# Step 1: Handling missing values
#--------------------------------------------------
# Fill missing age with median
df.loc[:, "Age"] = df["Age"].fillna(df["Age"].median())

# Fill missing embarked with mode
df.loc[:, "Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Dropping cabin column due to excessive missing values
df = df.drop(columns = ["Cabin"])

#--------------------------------------------------
# Step 2: Remove duplicates
#--------------------------------------------------
df = df.drop_duplicates()

#--------------------------------------------------
# Step 3: Standardize categorical variables
#--------------------------------------------------
# Standardize text columns
df["Sex"] = df["Sex"].str.strip().str.lower()
df["Embarked"] = df["Embarked"].str.strip().str.upper()

#--------------------------------------------------
# Step 4: Family size Feature
#--------------------------------------------------
# Create Family size feature
df["Family_size"] = df["SibSp"] + df["Parch"] + 1

# Extract title from name
df["title"] = df["Name"].str.extract(' ([A-Za-z]+)\.', expand = False)

# Dataset cleaning completed
print("Data Cleaning completed successfully!")

# Save the cleaned dataset
df.to_csv("data/cleaned_titanic_dataset.csv", index = False)


#---------------------------------------------------
# Exploratory Data Analysis (EDA)
#---------------------------------------------------

# 1. Survival Distribution
sns.countplot(data = df, x = "Survived")
plt.title("Survival Distribution")
# Saving the plots
plt.savefig("plots/chart1_survival_distribution.png", dpi = 300)
plt.show()

# 2. Survival by gender
sns.countplot(data = df, x = "Sex", hue = "Survived")
plt.title("Survival by Gender")
# Saving the plots
plt.savefig("plots/chart2_survival_by_gender.png", dpi = 300)
plt.show()

# 3. Age Distribution
sns.histplot(df["Age"], bins = 20, kde = True)
plt.title("Age Distribution")
# Saving the plots
plt.savefig("plots/chart3_age_distribution.png", dpi = 300)
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize = (10,6))
sns.heatmap(df.corr(numeric_only = True), annot = True, cmap = "coolwarm")
plt.title("Correlation Heatmap")
# Saving the plots
plt.savefig("plots/chart4_correlation_heatmap.png", dpi = 300)
plt.show()

# 5. Fare vs Survival
sns.boxplot(data = df, x = "Survived", y = "Fare")
plt.title("Fare vs Survival")
# Saving the plots
plt.savefig("plots/chart5_fare_vs_survival.png", dpi = 300)
plt.show()




