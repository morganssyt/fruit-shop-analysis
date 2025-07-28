import pandas as pd 
import matplotlib.pyplot as plt
# Load the dataset
df = pd.read_csv('Fruit-Sales-Analysis/data/daily_fruit_sales_2024-06-01.csv')
df['DateTime'] = pd.to_datetime(df['DateTime'])  # Convert 'Date' column to datetime
total_sales = df.groupby('Fruit')['Quantity'].sum()  # Total Sales by 'Fruit' 
print(total_sales)  # Print total sales for each fruit

# Rapresenting thw total sales by fruit in a bar chart
total_sales.plot(kind='bar', title='Total Sales by Fruit') 
plt.xlabel('Fruit')
plt.ylabel('Quantity Sold')
plt.tight_layout()
plt.show()  # Show the plot 

# Let's analyse the sales over time
df['Hour'] = df['DateTime'].dt.hour  # Extract hour from 'DateTime'
sales_by_hour = df.groupby('Hour')['Quantity'].sum()  # Total sales by hour
plt.xlabel('Hour of the Day')
plt.ylabel('Quantity Sold')
sales_by_hour.plot(kind='line', title='Sales by Hour of the Day')  # Plot sales by hour
plt.tight_layout() 
plt.grid(True)  # Add grid for better readability 
plt.show()  # Show the plot
plt.savefig('Fruit-Sales-Analysis/sales_by_hour.png')  # Save the plot as an image
