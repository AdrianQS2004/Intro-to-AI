# Introduction to AI Homework 4
# Part A
# By Keisy Nunez and Adrian Quiros

import pandas as pd

# Read the CSV files
app_df = pd.read_csv('application_record_clean1.csv')
credit_df = pd.read_csv('credit_record.csv')

# Ensure ID columns are named the same for merging
app_id_col = 'ID'
credit_id_col = 'ID'

print("Filtering application records with no matching credit records and removing customers with STATUS 'X'...")
# Remove credit records with STATUS 'X'
filtered_credit_df = credit_df[credit_df['STATUS'] != 'X']
matched_ids = set(filtered_credit_df[credit_id_col].unique())
app_df = app_df[app_df[app_id_col].isin(matched_ids)].copy()
print("Done filtering.  Found {} matching records.".format(len(app_df)))

# Compute the total number of "C", "0" and "1" statuses for each ID

status_counts = filtered_credit_df.groupby(credit_id_col)['STATUS'].value_counts().unstack(fill_value=0)

# Total observations per customer (excluding "X")
total_obs = status_counts.sum(axis=1)

# Calculate fractions
frac_C = status_counts.get('C', 0) / total_obs
frac_0 = status_counts.get('0', 0) / total_obs
frac_1 = status_counts.get('1', 0) / total_obs

# Add these as columns to app_df
app_df['Frac_C'] = app_df[app_id_col].map(frac_C)
app_df['Frac_0'] = app_df[app_id_col].map(frac_0)
app_df['Frac_1'] = app_df[app_id_col].map(frac_1)
app_df['Total_Obs'] = app_df[app_id_col].map(total_obs)


# Function to determine delinquency
def is_delinquent(id_):
    statuses = filtered_credit_df.loc[filtered_credit_df[credit_id_col] == id_, 'STATUS']
    return int(any(status in ['2', '3', '4', '5'] for status in statuses))

# Apply the function to each record
print("Creating delinquency labels...")
app_df['Delinquent'] = app_df[app_id_col].apply(is_delinquent)

print("Delinquency labels created.")
print("Delinquent counts:\n", app_df['Delinquent'].value_counts())

# Drop the ID column (no longer needed)
app_df.drop(columns=[app_id_col], inplace=True)

# Save the result
app_df.to_csv('credit_delinquency_v2.csv', index=False)

print(app_df.head())


