import pandas as pd
import numpy as np
from scipy import stats
import statsmodels.api as sm

# Load the dataset
data_path = 'Retail_Sales_Data.csv'
sales_data = pd.read_csv(data_path)

# Z-test
# Known population mean
pop_mean = 500
sample_mean = sales_data['Sales Revenue'].mean()
print("Sample mean", sample_mean)
sample_std = sales_data['Sales Revenue'].std()
print("sample_standard deviation", sample_std)
n = len(sales_data)
sem = sample_std / np.sqrt(n)  # Standard error of the mean
z = (sample_mean - pop_mean) / sem  # Z-statistic
p_value_z = 2 * (1 - stats.norm.cdf(abs(z)))  # P-value

print(f"Z-test Results: Z = {z:.2f}, P-value = {p_value_z:.3f}")