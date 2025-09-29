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
df = pd.read_csv("credit_delinquency_v2.csv", header=0)

# Print the dataframe info
print(df.info())

# Show histograms of the “C”, “0” and “1” ratio columns
ratio_cols = ['Frac_C', 'Frac_0', 'Frac_1']
for col in ratio_cols:
    if col in df.columns:
        df.hist(column=[col], bins=30)
        plt.title(f'Histogram of {col}')
        plt.xlabel(col)
        plt.show()

# Show bar plots of the delinquency rate for customers in different intervals of these ratio columns
for col in ratio_cols:
    if col in df.columns:
        # Bin the ratio column into intervals
        bins = np.linspace(0, 1, 11)  # 10 bins from 0 to 1
        df[f'{col}_bin'] = pd.cut(df[col], bins=bins, include_lowest=True)
        # Calculate mean delinquency rate per bin
        delinquency_rate = df.groupby(f'{col}_bin')['Delinquent'].mean()
        delinquency_rate.plot.bar()
        plt.title(f'Delinquency Rate by {col} Interval')
        plt.xlabel(f'{col} Interval')
        plt.ylabel('Delinquency Rate')
        plt.xticks(rotation=30)
        plt.show()
        df.drop(columns=[f'{col}_bin'], inplace=True)

