import pandas as pd
# Sample dataset
data = {
'Area': [750, 800, 850, 900, 950, 1000], # in square feet
'Price': [150000, 160000, 170000, 180000, 190000, 200000] # in USD
}
# Load the dataset into a DataFrame
df = pd.DataFrame(data)
# Display the dataset
print(df)

import matplotlib.pyplot as plt
# Plot the data
plt.scatter(df['Area'], df['Price'], color='blue')
plt.xlabel('Area (sq ft)')
plt.ylabel('Price (USD)')
plt.title('Area vs Price')
plt.show()

from sklearn.linear_model import LinearRegression
# Reshape the data for the model
X = df[['Area']] # Feature (Area)
y = df['Price'] # Target (Price)
# Create and train the model
model = LinearRegression()
model.fit(X, y)
# Display the model's coefficients
print("Slope (Coefficient):", model.coef_)
print("Intercept:", model.intercept_)

# Predict the price for a house with an area of 925 sq ft
area = 925
predicted_price = model.predict([[area]])
print(f"The predicted price for a house with {area} sq ft is${predicted_price[0]:.2f}.")
