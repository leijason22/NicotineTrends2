import pandas as pd
import matplotlib.pyplot as plt


#cdc path
cdc_data_path = '../data/cdc_data.csv'
cdc_data = pd.read_csv(cdc_data_path)

#who path
who_data_path = '../data/who_tobacco_data.csv'
who_data = pd.read_csv(who_data_path)

#kaggle path
kaggle_data_path = '../data/kaggle_data.csv'
kaggle_data = pd.read_csv(kaggle_data_path)

# Handling missing values
cdc_data.fillna(0, inplace=True)
#who_data.fillna("", inplace=True)
kaggle_data.fillna("", inplace=True)

# Plotting CDC data
plt.figure(figsize=(12, 6))
for state in cdc_data['locationdesc'].unique():
    state_data = cdc_data[cdc_data['locationdesc'] == state]
    plt.plot(state_data['ffy_year'], state_data['data_value'], label=state)

plt.title('Trend of Tobacco Sales to Minors by State')
plt.xlabel('Year')
plt.ylabel('Sales to Minors (%)')
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.show()

# Age distribution in Kaggle data
plt.figure(figsize=(10, 6))
kaggle_data['age'].hist(bins=30)
plt.title('Number of Smokers by Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Data for visualizations using WHO Article
deaths_data = {
    'Direct Tobacco Use': 7,
    'Second-Hand Smoke': 1.3
}

income_level_data = {
    'Low- and Middle-Income Countries': 80,
    'Other Countries': 20
}

gender_data = {
    'Men': 36.7,
    'Women': 7.8
}

#Pie Chart for Deaths Due to Tobacco Use
plt.figure(figsize=(8, 8))
plt.pie(deaths_data.values(), labels=deaths_data.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Deaths Due to Tobacco Use')
plt.show()

#Pie Chart for Tobacco Use by Income Level
plt.figure(figsize=(8, 8))
plt.pie(income_level_data.values(), labels=income_level_data.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Tobacco Use by Income Level')
plt.show()

#Pie Chart for Tobacco Use by Gender
plt.figure(figsize=(8, 8))
plt.pie(gender_data.values(), labels=gender_data.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Tobacco Use by Gender')
plt.show()

# Basic statistics for the 'age' and 'smoking' columns
age_mean = kaggle_data['age'].mean()
age_median = kaggle_data['age'].median()
age_mode = kaggle_data['age'].mode()[0]
age_std = kaggle_data['age'].std()

smoking_mean = kaggle_data['smoking'].mean()
smoking_median = kaggle_data['smoking'].median()
smoking_mode = kaggle_data['smoking'].mode()[0]
smoking_std = kaggle_data['smoking'].std()

# Display the statistics for the kaggle dataset
print("Age Statistics:")
print(f"Mean: {age_mean}")
print(f"Median: {age_median}")
print(f"Mode: {age_mode}")
print(f"Standard Deviation: {age_std}")

print("\nSmoking Statistics:")
print(f"Mean: {smoking_mean}")
print(f"Median: {smoking_median}")
print(f"Mode: {smoking_mode}")
print(f"Standard Deviation: {smoking_std}")

state_avg_sales_to_minors = cdc_data.groupby('locationdesc')['data_value'].mean().reset_index()
state_avg_sales_to_minors.columns = ['State', 'Average Sale Percentage']

# Display the average sales to minors by state
print(state_avg_sales_to_minors)

# Plot the average sales to minors by state
plt.figure(figsize=(14, 8))
plt.barh(state_avg_sales_to_minors['State'], state_avg_sales_to_minors['Average Sale Percentage'], color='skyblue')
plt.title('Average Percentage of Tobacco Sales to Minors by State')
plt.xlabel('Average Percentage of Sales to Minors (%)')
plt.ylabel('State')
plt.grid(True)
plt.show()
