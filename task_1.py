import pandas as pd
import numpy as np
import matplotlib.pyplot as pl

complex_df = pd.read_csv("Housing.csv")
df = complex_df[["price","area","bedrooms","parking"]]

#Load and inspect

# Display the shape (rows, columns)
print(df.shape)

# Display column names and data types
print(df.dtypes)
print(df.info())

# Display the first n rows
n = 7
print(df.head(n))

# Display describe output
print(df.describe())


# Handle missing values

# Randomly replace approximately 5% of all data cells with NaN
rng = np.random.default_rng(27)

df_missing = df.copy()
mask = rng.random(df_missing.shape) < 0.05
df_missing = df_missing.mask(mask)

# Check the number of missing values in each column
print("Missing values per column:")
print(df_missing.isnull().sum())

# Create a cleaned copy
df_clean = df_missing.copy()

# Fill missing numerical values with their respective column medians
for col in df_clean.columns:
    df_clean[col] = df_clean[col].fillna(df_clean[col].median())

# Verify that all missing values have been handled
print("Missing values after cleaning:")
print(df_clean.isnull().sum())

print("\nCleaned dataset shape:", df_clean.shape)


# NumPy operations

# Convert Pandas columns into NumPy arrays
area_array = df_clean["area"].to_numpy()
price_array = df_clean["price"].to_numpy()

# Calculate price per square foot
df_clean["price_per_sqft"] = price_array / area_array

# Normalize area using min-max normalization
area_min = np.min(area_array)
area_max = np.max(area_array)

df_clean["area_normalized"] = (
    (area_array - area_min) / (area_max - area_min)
)

# Use a Boolean mask to find houses larger than 2000 square feet
large_houses = df_clean[area_array > 2000]

print("First five price-per-square-foot values:")
print(df_clean["price_per_sqft"].head())

print("\nFirst five normalized area values:")
print(df_clean["area_normalized"].head())

print("\nNumber of houses with area greater than 2000:")
print(len(large_houses))

print("\nLarge-house sample:")
print(large_houses.head())

# Statistics
key_columns = ["price","area","bedrooms","parking"]

for column in key_columns:
    print(df[column].mean())
    print(df[column].median())
    print(df[column].std())
    print(df[column].min())
    print(df[column].max())

df.groupby("bedrooms")["price"].mean()

pl.hist(df["area"], list(df["price"]).sort())
pl.xlabel("Area")
pl.ylabel("Prices")

pl.show()

pl.scatter(df["area"],df["price"] )
pl.xlabel("Area")
pl.ylabel("Prices")

pl.show()