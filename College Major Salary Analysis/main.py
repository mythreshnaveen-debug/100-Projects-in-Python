import pandas as pd

d = pd.read_csv('data.csv')
df = d.dropna()
um_table = df["Undergraduate Major"]

#Finding the HIGHEST Starting Median Salary/Major
sms = df['Starting Median Salary'].idxmax()
print(f"Highest Starting Median Salary: {um_table[sms]}")
print(f"Earns a median of: {df['Starting Median Salary'][sms]}")

print("\n")
#Finding the Highest Mid-Career Median Salary/Major

mms = df['Mid-Career Median Salary'].idxmax()
print(f"Highest Mid-Career Median Salary: {um_table[mms]}")
print(f"Earns a median of: {df['Starting Median Salary'][mms]}")

print("\n")
#Finding the Lowest Starting Median Salary/Major

lsms = df['Starting Median Salary'].idxmin()
print(f"Lowest Starting Median Salary: {um_table[lsms]}.")
print(f"Earns a median of: {df['Starting Median Salary'][lsms]}")

print("\n")
#Finding the Lowest Risk Major
spread = df["Mid-Career 90th Percentile Salary"] - df["Starting Median Salary"]
df.insert(1, "Spread", spread)


print("Top 5 Lowest Risk Majors:")
low_risk = df.sort_values('Spread')
low_risk_top5 = low_risk.head()
for i in range(5):
    max_id = low_risk_top5["Spread"].idxmin()
    print(low_risk_top5["Undergraduate Major"].loc[max_id] + " - Up to $" + str(low_risk_top5["Spread"].loc[max_id]) + " change in salary")
    low_risk_top5 = low_risk_top5.drop(max_id)

print("\n")
#Finding the Highest Potential Majors
print("Top 5 Highest Potential Majors:")
high_risk_top5 = low_risk.tail()
for i in range(5):
    max_id = high_risk_top5["Spread"].idxmax()
    print(high_risk_top5["Undergraduate Major"].loc[max_id] + " - Up to $" + str(high_risk_top5["Spread"].loc[max_id]) + " change in salary")
    high_risk_top5 = high_risk_top5.drop(max_id)