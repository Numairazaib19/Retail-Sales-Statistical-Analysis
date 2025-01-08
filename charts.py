import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data_path = 'Retail_Sales_Data.csv'
sales_data = pd.read_csv(data_path)

# T-test data bar chart: Average Sales Revenue by Product Category
avg_sales_by_category = sales_data.groupby('Product Category')['Sales Revenue'].mean()
plt.figure(figsize=(8, 6))
avg_sales_by_category.plot(kind='bar', color='green', alpha=0.7)
plt.title('Average Sales Revenue by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Average Sales Revenue')
plt.xticks(rotation=0)
plt.grid(True, axis='y')
plt.savefig('BarChart_Sales_By_Category.png')

# Chi-square test data pie chart: Customer Ratings distribution
ratings_distribution = sales_data['Customer Rating'].value_counts()
plt.figure(figsize=(8, 6))
ratings_distribution.plot(kind='pie', autopct='%1.10f%%', startangle=90, colors=plt.cm.Pastel1.colors)
plt.title('Distribution of Customer Ratings')
plt.ylabel('')  # Remove the y-label for the pie chart
plt.savefig('PieChart_Customer_Ratings_1.png')

# Regression analysis scatter plot: Units Sold vs. Sales Revenue
plt.figure(figsize=(8, 6))
plt.scatter(sales_data['Units Sold'], sales_data['Sales Revenue'], alpha=0.7, c='red', label='Units Sold vs Sales Revenue')
plt.title('Scatter Plot: Units Sold vs. Sales Revenue')
plt.xlabel('Units Sold')
plt.ylabel('Sales Revenue')
plt.grid(True)
plt.legend()
plt.savefig('ScatterPlot_Units_Sold_vs_Sales_Revenue.png')

