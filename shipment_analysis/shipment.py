import pandas as pd
import matplotlib.pyplot as plt  
import seaborn as sns  

# load cv
df = pd.read_csv("shipment_data.csv")

#display first rows
print(df.head())

# check missing values
print(df.isnull().sum())

# converts date to datetime
df['Ship Date'] = pd.to_datetime(df['Ship Date'])
df['Delivery Date'] = pd.to_datetime(df['Delivery Date'])

# calculate shipping duration
df['Shipping Duration'] = (df['Delivery Date'] - df['Ship Date']).dt.days  

print(df[['Order ID', 'Shipping Duration']])

# Get only delayed shipments
delayed = df[df['Status'] == 'Delayed']  

# Average shipping cost
avg_cost = df['Cost ($)'].mean()  
print(f"Average Shipping Cost: ${avg_cost:.2f}")  

# Bar chart of shipping status
sns.countplot(data=df, x='Status')  
plt.title("Shipping Status Distribution")  
plt.show()