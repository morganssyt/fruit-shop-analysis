# 🍎 Fruit Sales Analysis – June 1, 2024

This project analyzes fruit sales data from a single day using Python.
It includes data cleaning, grouping, and visualizations to understand what fruit was sold the most and at what time.

## 🔍 Goals
- Analyze which fruits had the highest total sales
- Identify the peak sales hours during the day
- Practice working with pandas and matplotlib

## 📁 Project Structure

fruit-sales-analysis/

├── data/                         ← CSV dataset

├── plots/                        ← Auto-generated graphs

├── analysis.py                   ← Python script

├── requirements.txt              ← Dependencies

└── README.md                     ← Project description (this file)



## ▶️ How to Run

1. **Install the required libraries** (Python 3.8+ recommended):

```bash
pip install -r requirements.txt
 
2. Run the Script from the terminal

📊 Output


This project generates:

total_sales_per_fruit.png: Bar chart of total fruit sales

sales_by_hour.png: Line chart showing quantity sold by hour of day



All plots are saved inside the plots/ folder.



📦 Dataset


The dataset (daily_fruit_sales_2024-06-01.csv) contains fruit sales recorded every 30 minutes on June 1st, 2024. Each row represents a single sale with timestamp, fruit type, and quantity sold.



🚀 Future Ideas
Extend to multiple days of sales

Add price and calculate revenue

Export a PDF report with charts and summary

Build a dashboard using Streamlit or Flask



👤 Author


Morgan Germinario, Computer science student is building his portfolio project in Python and data analysis.

Built with Visual Studio Code, Git, pandas and matplotlib.