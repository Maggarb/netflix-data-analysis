# ===============================
# Start the Analysis (Notebook Code)
# ===============================

# Import libraries

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")

# ===============================
# Load Data
# ===============================

df = pd.read_csv("../data/netflix_titles.csv")

print("First rows of dataset:")
display(df.head())

# ===============================
# Basic Exploration
# ===============================

print("\nDataset shape:")
print(df.shape)

print("\nDataset info:")
print(df.info())

print("\nMissing values:")
print(df.isnull().sum())

# ===============================
# Data Cleaning
# ===============================

df = df.dropna(subset=['country', 'rating'])
df['date_added'] = pd.to_datetime(df['date_added'])

# ===============================
# Analysis Tasks
# ===============================

# -------------------------------
# Movies vs TV Shows
# -------------------------------
plt.figure()
sns.countplot(data=df, x='type')
plt.title("Movies vs TV Shows on Netflix")

# Save figure
plt.savefig("../images/movies_vs_tvshows.png")

plt.show()

print("Insight: Netflix contains significantly more movies than TV shows.")

# -------------------------------
# Content Added Over Time
# -------------------------------
df['year_added'] = df['date_added'].dt.year

plt.figure()
df['year_added'].value_counts().sort_index().plot()
plt.title("Content Added Per Year")

plt.savefig("../images/content_per_year.png")

plt.show()

print("Insight: Netflix rapidly expanded content after 2016.")

# -------------------------------
# Top Producing Countries
# -------------------------------
plt.figure()
df['country'].value_counts().head(10).plot(kind='bar')
plt.title("Top Content Producing Countries")

plt.savefig("../images/top_countries.png")

plt.show()

# -------------------------------
# Most Popular Genres
# -------------------------------
genres = df['listed_in'].str.split(',', expand=True).stack()

plt.figure()
genres.value_counts().head(10).plot(kind='bar')
plt.title("Top Genres on Netflix")

plt.savefig("../images/top_genres.png")

plt.show()

# -------------------------------
# Ratings Distribution
# -------------------------------
plt.figure()
sns.countplot(data=df, y='rating',
              order=df['rating'].value_counts().index)
plt.title("Content Ratings Distribution")

plt.savefig("../images/ratings_distribution.png")

plt.show()

print("\nAnalysis complete ✅")
