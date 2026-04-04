## Exploratory Data Analysis of Netflix's global content library 

## What's Inside

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

##  Dataset

This project uses the *Netflix Movies and TV Shows* dataset available on Kaggle:
Available at: https://www.kaggle.com/datasets/shivamb/netflix-shows

A copy of the dataset is provided in the `data/` directory to ensure reproducibility of the analysis.

---

##  Getting Started

```bash
# 1. Clone the repo
git clone https://github.com/Maggarb/netflix-data-analysis.git
cd netflix-eda

# 2. Install dependencies
pip install -r requirements.txt

```

---


##  Key Findings

- **~70% Movies** — but TV Show additions have accelerated since 2018
- **USA dominates**, followed by India and the UK
- **TV-MA is the most common rating** — Netflix skews toward adult content
- **Most movies run 80–120 minutes** (median ~98 min)
- **70%+ of TV shows have only 1 season** on the platform
- **January & July** are the biggest content drop months

---

