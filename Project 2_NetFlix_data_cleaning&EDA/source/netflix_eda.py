import pandas as pd
import matplotlib.pyplot as plt


# Load the dataset from csv
df = pd.read_csv("data/netflix_titles.csv")
print(df.head())

# Dataset checks
# Basic datset information
df.info()
print(f"Rows and columns of NetFlix dataset: \n{df.shape}")
print(df.describe())
print(f"No. of missing data points per each column: \n{df.isnull().sum()}")

#--------------------------------------------------
# Step 1: Handling missing values
#--------------------------------------------------
# Handling missing values
print(f"Percentage of no. of missing data points per each column: \n{df.isnull().sum() * 100/ (df.shape[0])}")

# Filling all the missing data points in the director, cast and country as "Unknown"
df["director"] = df["director"].fillna('Unknown')
df["cast"] = df["cast"].fillna('Unknown')
df["country"] = df["country"].fillna('Unknown')

# Filling the missing data points in date_added as "ffill" and rating as "mode[0]"
df["date_added"] = df["date_added"].ffill()
df["rating"] = df["rating"].fillna(df["rating"].mode()[0])

# Fixing datatypes for necessary columns
df["date_added"] = pd.to_datetime(df["date_added"], errors = 'coerce')

#--------------------------------------------------
# Step 2: Remove duplicates
#--------------------------------------------------
# Removing duplicates
df = df.drop_duplicates()

#--------------------------------------------------
# Step 3: Stripping unwanted spaces
#--------------------------------------------------
# Clean "type" and "country" text columns
df["type"] = df["type"].str.strip()
df["country"] = df["country"].str.strip()

#---------------------------------------------------
# Step 4: Feature Engineering
#---------------------------------------------------
# Feature Engineering
df["year_added"] = df["date_added"].dt.year

df["duration"] = df["duration"].astype(str)
df["duration_num"] = df["duration"].str.extract('(\d+)').astype(float)

# Dataset cleaning completed
print("Data Cleaning completed successfully!")

# Save the cleaned dataset
df.to_csv("data/cleaned_netflix_dataset.csv", index = False)


#---------------------------------------------------
# Exploratory Data Analysis (EDA)
#---------------------------------------------------
# 1. Content Type Distribution
plt.figure(figsize = (6,4))
type_counts = df["type"].value_counts()
type_counts.plot(kind = 'bar', color = ['#4CAF50', '#2196F3'])
# Add Text labels 
for i, v in enumerate(type_counts):
    plt.text(i, v + max(type_counts)*0.01, str(v), ha = 'center')
plt.title("Movies vs TV Shows Distribution", fontsize  = 14)
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.xticks(rotation = 0)
plt.legend(["Count"], loc = "upper right")
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.tight_layout()
# Saving the plots
plt.savefig("plots/chart1_content_type_distribution.png")
plt.show()

# 2. Content Over Years
plt.figure(figsize = (8,5))
year_counts = df["year_added"].value_counts().sort_index()
year_counts.plot(kind = 'line', marker = 'o', linewidth = 2)
plt.title("Content Added Over Years", fontsize = 14)
plt.xlabel("Year")
plt.ylabel("Number of Titles")
plt.grid(True, linestyle = '--', alpha = 0.6)
plt.legend(["Titles Added"])
plt.tight_layout()
# Saving the plots
plt.savefig("plots/chart2_content_over_years.png")
plt.show()

# 3. Top 10 content producing countries
plt.figure(figsize = (10,5))
country_counts = df["country"].value_counts().head(10)
country_counts.plot(kind = 'bar', color = 'orange')
# Add Text labels
for i, v in enumerate(country_counts):
    plt.text(i, v + max(country_counts)*0.01, str(v), ha = 'center')
plt.title("Top 10 Content producing Countries", fontsize = 14)
plt.xlabel("Country")
plt.ylabel("Number of Titles")
plt.xticks(rotation = 90)
plt.legend(["Titles Count"])
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.tight_layout()
# Saving the plots
plt.savefig("plots/chart3_top_content_producing_countries.png")
plt.show()

# 4. Content rating distribution
plt.figure(figsize = (10,5))
rating_counts = df["rating"].value_counts()
rating_counts.plot(kind = 'bar', color = 'purple')
# Add Text labels
for i, v in enumerate(rating_counts):
    plt.text(i, v + max(rating_counts)*0.01, str(v), ha = 'center')
plt.title("Content rating distribution", fontsize = 14)
plt.xlabel("Rating")
plt.ylabel("Number of Titles")
plt.xticks(rotation = 90)
plt.legend(["Count"])
plt.grid(axis = 'y', linestyle = '--', alpha = 0.7)
plt.tight_layout()
# Saving the plots
plt.savefig("plots/chart4_content_rating_distribution.png")
plt.show()




