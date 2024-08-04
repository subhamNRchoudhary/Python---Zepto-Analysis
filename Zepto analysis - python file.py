import pandas as pd

# Load the data
file_path = r"C:\Users\sunny\OneDrive\Desktop\All the projects\19. zepto\Zepto Dairy, Bread & Batter.xlsx"
df = pd.read_excel(file_path)

# Display the first few rows of the DataFrame
print(df.head())


import matplotlib.pyplot as plt
import seaborn as sns

# Bar plot of MRP for each product
plt.figure(figsize=(10, 6))
sns.barplot(x='name', y='mrp', data=df)
plt.xticks(rotation=90)
plt.title('MRP of Each Product')
plt.xlabel('Product Name')
plt.ylabel('MRP')
plt.show()


# Scatter plot of MRP vs Discounted Selling Price
plt.figure(figsize=(10, 6))
sns.scatterplot(x='mrp', y='discountedSellingPrice', hue='name', data=df)
plt.title('MRP vs Discounted Selling Price')
plt.xlabel('MRP')
plt.ylabel('Discounted Selling Price')
plt.show()

# Pie chart of Available Quantity
plt.figure(figsize=(10, 6))
df.groupby('name')['availableQuantity'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title('Available Quantity Distribution')
plt.ylabel('')
plt.show()
