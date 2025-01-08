import pandas as pd

data_path = 'Retail_Sales_Data.csv'
data = pd.read_csv(data_path)

#for clothing
clothing_data = data[data['Product Category'] == 'Clothing']
mean_sales_revenue = clothing_data['Sales Revenue'].mean()
std_sales_revenue = clothing_data['Sales Revenue'].std()
print("----For Clothing----")
print("mean_sales_revenue", mean_sales_revenue)
print("std_sales_revenue", std_sales_revenue)
mean_sales_revenue, std_sales_revenue
clothing_count = clothing_data.shape[0]
print("Count", clothing_count)

#for electronics
Electronics_data = data[data['Product Category'] == 'Electronics']
mean_sales_revenue = Electronics_data['Sales Revenue'].mean()
std_sales_revenue = Electronics_data['Sales Revenue'].std()
print("----For Electronics----")
print("mean_sales_revenue", mean_sales_revenue)
print("std_sales_revenue", std_sales_revenue)
mean_sales_revenue, std_sales_revenue
Electronics_count = Electronics_data.shape[0]
print("Count", Electronics_count)

