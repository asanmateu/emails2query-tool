import pandas as pd
import numpy as np
import re
import os

current_path = os.getcwd()
input_path = current_path + "/input"
output_path = current_path + "/output"

os.chdir(input_path)
df = pd.read_excel("emails2query_template.xls")
df.replace('nan', np.nan, inplace=True)
df.fillna("", inplace=True)

# Set regular expression to catch emails
regex = r"[a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+.[a-zA-Z\.]*"

# Initialise empty list to add query ready emails
emails_qf = []

# Iterate over retailer_id / emails template rows and append formatted emails to list
for i, row in df.iterrows():
    # Put all emails in the row into a list
    emails = re.findall(regex, df['additional_emails'][i])
    for email in emails:
        qf = "(" + str(row['retailer_id']) + "," + "''" + "," + "'" + email + "'" + ")" + ","
        emails_qf.append(qf)

# New dataframe to input query ready emails
query_df = pd.DataFrame(emails_qf, columns=['emails'])

# Export file with query ready additional emails
query_df.to_csv(output_path + "/emails2query_ready.csv")
