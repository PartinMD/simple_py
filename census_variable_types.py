# Import pandas with alias
import pandas as pd

# Read in the census dataframe
census = pd.read_csv('census_data.csv', index_col=0)

# Print the first 5 rows
print(census.head())

# Check data types
print(census.dtypes)

# Unique dtypes of birth_year
print(census.birth_year.unique())

# Correct missing values and change the dtype to int64
census.birth_year = census.birth_year.replace('missing', 1967)
census.birth_year = census.birth_year.astype('int64')
print(census.dtypes)

# Average birth year?
avg_birth = census.birth_year.mean()
print(avg_birth)

# Convert high_tax to Ordinal Categorical data
census.higher_tax = pd.Categorical(census.higher_tax, ['strongly disagree', 'disagree', 'neutral', 'agree', 'strongly agree'], ordered = True)
print(census.higher_tax.unique())

# Median response of higher_tax?
census.higher_tax = census.higher_tax.cat.codes
median_tax = census.higher_tax.median()
print(median_tax)

# One-Hot Encode marital_status
census = pd.get_dummies(data = census, columns=['marital_status'])
print(census.head())
