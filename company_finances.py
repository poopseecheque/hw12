import numpy as np
import pandas as pd
income = np.array([12000, 15000, 13000, 16000, 17000, 15500, 14000, 16500, 15800, 14500])
income_without_tax = income * 0.7

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct']
expenses = np.array([8000, 9000, 9500, 11000, 12000, 11500, 10000, 10800, 10200, 9500])
data = {
    'Month': months,
    'Income_without_tax': income_without_tax,
    'Expenses': expenses
}
df = pd.DataFrame(data)
print("Company Finances:")
print(df)

q1 = df.iloc[0:3,]
print('\n1st quarter')
print(q1)