import pandas as pd
from pandasql import sqldf 
#clean Census Data
censusDF = pd.read_csv('CensusData.csv')
censusDF['zip'] = censusDF['zip'].str[6:]
censusDF = censusDF[censusDF['Amount'] != '-']
censusDF.loc[censusDF['Amount'] == '250,000+'] = '250000'
censusDF.loc[censusDF['Amount'] == '2,500-'] = '2500'
censusDF['Amount'] = censusDF['Amount'].astype(int)
#clean CMS Data
cmsDF = pd.read_csv('CMS_PSI_6_decimal_file.csv')
cmsDF = cmsDF[cmsDF['Measure'] == 'PSI_90']
#query to join the datasets based on zip code
query = """
select c.zip, c.rate, cd.amount from cmsDF c 
left join censusDF cd 
on cd.zip = c.zip
"""
#create output data frame with sql
output_df = sqldf(query)
#clean output data frame where the rate or amount is not populated
output_df = output_df[output_df['Rate'] != 'Not Available']
output_df = output_df[output_df['Amount'] > 0]
#export the data frame as a CSV file so we can load that into SAS
output_df.to_csv('combined_data.csv', index=None)
