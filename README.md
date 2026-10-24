# House Price Data Analysis using NumPy and Pandas

## Overview
This project explores a house-price dataset using Python, Pandas, NumPy, and Matplotlib. It focuses on inspecting the data, handling missing values, performing numerical operations, calculating descriptive statistics, grouping houses by bedroom count, and visualizing relationships in the dataset.

This project was completed as **Task 1: Data Handling with NumPy and Pandas** for the AI/ML volunteer recruitment task.

## Dataset
The project uses `Housing.csv` and selects these columns for analysis:

- `price` — house price
- `area` — house area
- `bedrooms` — number of bedrooms
- `parking` — number of parking spaces

The script loads the CSV using Pandas and creates a DataFrame containing only these columns.

> Keep `Housing.csv` in the same directory as `task_1.py` when running the script, or update the file path in the code.

## Tools and Libraries
- **Python** — programming language
- **Pandas** — loading, selecting, cleaning, summarizing, and grouping data
- **NumPy** — array operations, random missing-value generation, and numerical calculations
- **Matplotlib** — data visualization

## What the Script Does

### 1. Load and Inspect the Dataset
The script displays:
- Dataset shape (number of rows and columns)
- Column data types and DataFrame information
- The first seven rows
- Descriptive statistics using `describe()`

### 2. Create and Handle Missing Values
To practise data cleaning, the script randomly masks approximately 5% of the selected DataFrame's cells using NumPy's random number generator with seed `27`. It then fills missing numerical values in each column with that column's median and checks the missing-value counts after cleaning.

**Why use the median?** The median is less sensitive to unusually high or low values than the mean, making it a useful choice for numerical data that may contain outliers.

Note: the missing values are introduced by the script for practice; they are not necessarily missing values in the original CSV.

### 3. Perform NumPy Operations
The script:
- Converts the `area` and `price` columns to NumPy arrays.
- Calculates `price_per_sqft` by dividing price by area.
- Applies min-max normalization to the area column, producing values between 0 and 1 when the column has a non-zero range.
- Uses a Boolean mask to select houses with an area greater than 2,000.

### 4. Calculate Descriptive Statistics
For `price`, `area`, `bedrooms`, and `parking`, the script calculates:
- Mean
- Median
- Standard deviation
- Minimum
- Maximum

These calculations are currently performed on the selected DataFrame before the missing values are artificially introduced and cleaned.

### 5. Group Data by Number of Bedrooms
The script uses `groupby()` to calculate the average house price for each number of bedrooms. This can help compare average prices across bedroom groups.

### 6. Visualize the Data
The script creates:
- A histogram intended to explore the distribution of house area
- A scatter plot of house area against price

The scatter plot can help visually examine whether larger houses tend to have higher prices.

## How to Run

1. Install Python 3 if it is not already installed.
2. Place `task_1.py` and `Housing.csv` in the same folder.
3. Install the required libraries:

   ```bash
   pip install pandas numpy matplotlib
   ```

4. Run the script:

   ```bash
   python task_1.py
   ```

The script prints data-inspection and analysis results in the terminal and opens the plots in Matplotlib windows.

## Repository Structure

```text
.
├── task_1.py
├── Housing.csv
└── README.md
```

## Learning Outcomes
Through this task, I practised:
- Loading and inspecting tabular data with Pandas
- Identifying and handling missing values
- Converting Pandas columns to NumPy arrays
- Applying vectorized numerical operations and Boolean filtering
- Computing descriptive statistics
- Grouping data to compare average prices
- Creating basic plots to explore data relationships

## Current Scope and Possible Improvements
- Add a correlation matrix or correlation values for `area`, `bedrooms`, and `price`.
- Write 3–4 Markdown observations based on the actual output.
- Correct the histogram bin specification so it uses a suitable number of bins or explicit bin edges.
- Add axis titles that clearly distinguish house area from house price in each plot.
- Consider calculating statistics on the cleaned DataFrame as well, if the intention is to report statistics after cleaning.
- Guard against zero values in `area` before calculating price per square foot and against a zero range before min-max normalization.

## Data Source
The dataset is provided in `Housing.csv`. Add the original public dataset URL and attribution here if the file was obtained from an external source.
