# Introduction to Artificial Intelligence
# Credit Delinquency Dataset
# Exploration of variables
# By Juan Carlos Rojas
# Copyright 2025, Texas Tech University - Costa Rica

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("credit_delinquency.csv", header=0)

# Print the dataframe info
print(df.info())

# Plot histograms of all numerical columns
for col in df.select_dtypes(exclude='object').columns:

    # If the colum is binary, or has few unique values, plot a bar chart instead
    if df[col].nunique() < 10:
        pd.value_counts(df[col]).plot.barh()
        plt.title(col)
        plt.show()
    else:
        # Plot a full histogram
        df.hist(column=[col], bins=50)
        plt.title(col)
        plt.show()

# Plot bar chart of counts in categorical columns
for col in df.select_dtypes(include='object').columns:
    pd.value_counts(df[col]).plot.barh()
    plt.title(col)
    plt.show()