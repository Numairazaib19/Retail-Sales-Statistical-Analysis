import pandas as pd
data_path = 'Retail_Sales_Data.csv'
data = pd.read_csv(data_path)

rating_counts = data['Customer Rating'].value_counts(sort=False)  
print(rating_counts)

import pandas as pd
import numpy as np
from scipy.stats import chisquare

observed_frequencies = pd.Series([8, 8, 6, 6, 3], index=[1, 2, 3, 4, 5])
all_ratings = np.arange(1, 6) 
observed_frequencies = observed_frequencies.reindex(all_ratings, fill_value=0)
total_ratings = observed_frequencies.sum()
expected_frequencies = np.full(len(all_ratings), total_ratings / len(all_ratings))
expected_frequencies[-1] = total_ratings - expected_frequencies[:-1].sum()
chi_stat, p_value = chisquare(f_obs=observed_frequencies, f_exp=expected_frequencies)

print(f"Customer Ratings (1-5): {all_ratings}")
print(f"Observed Frequencies: {observed_frequencies.values}")
print(f"Expected Frequencies: {expected_frequencies}")
print(f"Chi-square Statistic: {chi_stat:.2f}")
print(f"P-value: {p_value:.3f}")
