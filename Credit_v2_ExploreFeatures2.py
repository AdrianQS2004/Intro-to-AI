# Introduction to Artificial Intelligence
# Credit Delinquency Dataset
# Exploration of variables in relation to Delinquency
# By Juan Carlos Rojas
# Copyright 2025, Texas Tech University - Costa Rica

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("credit_delinquency.csv", header=0)

# Go through all the columns
for col in df.columns:
    if col == "Delinquent":
        continue

    if df[col].dtype == 'object':
        lm = sns.barplot(data=df, x=col, y="Delinquent")
        lm.set_xticklabels(lm.get_xticklabels(),rotation=30)
        plt.title("Delinquent vs. {}".format(col))
        plt.show()
    else:
        # Numerical
        # If there are few unique values, treat as categorical
        if df[col].nunique() < 10:
            lm = sns.barplot(data=df, x=col, y="Delinquent")
            lm.set_xticklabels(lm.get_xticklabels())
            plt.title("Delinquent vs. {}".format(col))
            plt.show()
        else:
            # If numerical, do a discretized bar plot with 20 bins Using equal quantile bins
            df[col] = pd.qcut(df[col], 20, duplicates="drop")
            lm = sns.barplot(data=df, x=col, y="Delinquent")
            lm.set_xticklabels(lm.get_xticklabels(),rotation=30)
            plt.title("Delinquent vs. {}".format(col))
            plt.show()