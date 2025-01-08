import pandas as pd
import statsmodels.api as sm

# Load the dataset
data_path = 'Retail_Sales_Data.csv'
sales_data = pd.read_csv(data_path)

# Regression analysis
X = sales_data[['Units Sold', 'Customer Rating']]  # Independent variables
X = sm.add_constant(X)  # Adding a constant for the intercept
y = sales_data['Sales Revenue']  # Dependent variable
model = sm.OLS(y, X).fit()  # Fit linear regression model
regression_results = model.summary()  # Model summary

print(regression_results)
