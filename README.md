# 🎬 Netflix Content EDA

Exploratory Data Analysis of Netflix's global content library — uncovering patterns in genres, countries, ratings and release trends.

## 📊 What's Inside

| Section | Description |
|---|---|
| Data Cleaning | Handle nulls, parse dates, extract numeric durations |
| Content Type | Movies vs TV Shows split |
| Time Trends | How Netflix's catalogue grew year-by-year |
| Seasonality | Which months Netflix adds the most content |
| Top Countries | Biggest content-producing nations |
| Ratings | Audience rating breakdown |
| Genres | Most common genres across the catalogue |
| Movie Duration | Runtime distribution and rating comparisons |
| TV Seasons | How many seasons shows run |
| Directors & Cast | Most prolific creators on the platform |

---

## 🗂 Dataset

[Netflix Movies and TV Shows](https://www.kaggle.com/datasets/shivamb/netflix-shows) — Kaggle  
~8,800 titles with title, type, director, cast, country, date added, rating, duration, and genre.

**Download options:**

```bash
# Option A — Kaggle CLI
kaggle datasets download -d shivamb/netflix-shows --unzip

# Option B — manual
# Download netflix_titles.csv from the link above and place it in this folder
```

---

## 🚀 Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/YOUR_USERNAME/netflix-eda.git
cd netflix-eda

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download dataset (see above)

# 4. Launch notebook
jupyter notebook netflix_eda.ipynb
```

---

## 📦 Requirements

```
pandas
numpy
matplotlib
seaborn
```

---

## 🔍 Key Findings

- **~70% Movies** — but TV Show additions have accelerated since 2018
- **USA dominates**, followed by India and the UK
- **TV-MA is the most common rating** — Netflix skews toward adult content
- **Most movies run 80–120 minutes** (median ~98 min)
- **70%+ of TV shows have only 1 season** on the platform
- **January & July** are the biggest content drop months

---

## 💡 Possible Extensions

- 🌍 Choropleth map of production by country with Plotly
- 📝 NLP clustering on descriptions with TF-IDF + KMeans
- 🤖 Content-based recommendation engine (cosine similarity)
- 📈 Time-series forecast of content additions with Prophet

---
