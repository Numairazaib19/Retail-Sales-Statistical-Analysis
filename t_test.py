import pandas as pd
from scipy import stats

# Load the dataset
data_path = 'Retail_Sales_Data.csv'
sales_data = pd.read_csv(data_path)

# T-test
# Independent samples t-test for 'Clothing' and 'Electronics'
t_stat, p_value_t = stats.ttest_ind(
    sales_data[sales_data['Product Category'] == 'Clothing']['Sales Revenue'],
    sales_data[sales_data['Product Category'] == 'Electronics']['Sales Revenue'],
    equal_var=False  
)

print(f"T-test Results: t = {t_stat:.2f}, P-value = {p_value_t:.3f}")