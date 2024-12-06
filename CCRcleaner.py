import pandas as pd

# Get the .csv file as a DataFrame
CR_df = pd.read_csv("CountyCrimeRate.csv")

# Check for NaN values in the DataFrame
nan_values = CR_df.isna().sum() # No NaN values in the DataFrame

# Split the 'county_name' column to move the state abbreviation to a new column
CR_df['State'] = CR_df['county_name'].str.split(',').str[1]
CR_df['county_name'] = CR_df['county_name'].str.split(',').str[0]

# Create a dictionary to map state names to their abbreviations (ty Carly)
state_abbrev = {
    'Alabama': 'AL', 'Alaska': 'AK', 'Arizona': 'AZ', 'Arkansas': 'AR', 'California': 'CA',
    'Colorado': 'CO', 'Connecticut': 'CT', 'Delaware': 'DE', 'Florida': 'FL', 'Georgia': 'GA',
    'Hawaii': 'HI', 'Idaho': 'ID', 'Illinois': 'IL', 'Indiana': 'IN', 'Iowa': 'IA', 'Kansas': 'KS',
    'Kentucky': 'KY', 'Louisiana': 'LA', 'Maine': 'ME', 'Maryland': 'MD', 'Massachusetts': 'MA',
    'Michigan': 'MI', 'Minnesota': 'MN', 'Mississippi': 'MS', 'Missouri': 'MO', 'Montana': 'MT',
    'Nebraska': 'NE', 'Nevada': 'NV', 'New Hampshire': 'NH', 'New Jersey': 'NJ', 'New Mexico': 'NM',
    'New York': 'NY', 'North Carolina': 'NC', 'North Dakota': 'ND', 'Ohio': 'OH', 'Oklahoma': 'OK',
    'Oregon': 'OR', 'Pennsylvania': 'PA', 'Rhode Island': 'RI', 'South Carolina': 'SC',
    'South Dakota': 'SD', 'Tennessee': 'TN', 'Texas': 'TX', 'Utah': 'UT', 'Vermont': 'VT',
    'Virginia': 'VA', 'Washington': 'WA', 'West Virginia': 'WV', 'Wisconsin': 'WI', 'Wyoming': 'WY',
    'Puerto Rico': 'PR'
}

# Rename some columns for clarity
CR_df.rename(columns={'county_name': 'County'}, inplace=True)

# Everything below this line is for the creation of the CountyCrimesMigration.csv file
# Take whatever information you need and adapt if you want something different
########################################################################################

# I only want to preserve crime rate per 100,000 people
# CR_simple = CR_df[['County', 'State', 'crime_rate_per_100000']]

# CM_df = pd.read_csv("CountyMigration.csv")
# CM_df['State'] = CM_df['State'].replace(state_abbrev)

# # Clean the data by stripping and setting to lowercase
# CR_simple.loc[:, 'County'] = CR_simple['County'].str.strip().str.lower()
# CR_simple.loc[:, 'State'] = CR_simple['State'].str.strip().str.lower()
# CM_df.loc[:, 'County'] = CM_df['County'].str.strip().str.lower()
# CM_df.loc[:, 'State'] = CM_df['State'].str.strip().str.lower()

# # Combine the dataframes based on the 'County' and 'State' columns, dropping any rows that don't match
# CCR_df = pd.merge(CR_simple, CM_df, on=['County', 'State'], how='inner')
# print(CCR_df['State'].unique().shape)

# # Save the cleaned and merged data to a new .csv file
# CCR_df.to_csv("CountyCrimesMigration.csv", index=False)