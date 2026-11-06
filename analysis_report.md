# Sales Data Analysis Report

## 1. Introduction
The Sales Data Analysis project is developed using Python and Pandas. The main objective is to analyze sales data, clean the dataset, and calculate useful sales statistics.

## 2. Tools and Technologies
- Python
- Pandas
- CSV Dataset
- VS Code

## 3. Dataset Description

The dataset contains 100 records and 5 columns.

| Column Name | Description |
|---|---|
| Order_ID | Unique order identification |
| Product | Product name |
| Quantity | Number of products sold |
| Unit_Price | Price of one product |
| Total_Sales | Total sales amount |

## 4. Data Cleaning
The following operations were performed:
- Checked missing values.
- Replaced missing product names with "Unknown".
- Replaced missing numerical values using median.
- Removed duplicate records.
- Recalculated Total_Sales.
- Saved the cleaned dataset as `cleaned_sales_data.csv`.

## 5. Analysis
The following metrics are calculated:
- Total Revenue
- Average Sales
- Highest Sales
- Lowest Sales
- Best-Selling Product

## 6. Conclusion
This project demonstrates how Python and Pandas can be used to load, clean, and analyze sales data. It helps understand basic data analysis techniques and generate useful business insights.

## 7. Future Enhancements
- Add graphical charts.
- Create an interactive dashboard.
- Analyze monthly and yearly sales.
- Generate automated sales reports.
