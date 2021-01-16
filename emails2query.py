import pandas as pd
import numpy as np
import sys
import re
import os

current_path = os.getcwd()
input_path = current_path + "/input"
output_path = current_path + "/output"

os.chdir(input_path)

try:
    print("Reading and parsing template...")
    df = pd.read_excel("emails2query_template.xlsx")

except IndexError:
    print("Please, make sure you use and .xlsx file that it is saved as Excel Workbook and NOT as "
          "Strict Open XML Spreadsheet and try again. \n")
    sys.exit()

# Format null values to be easily manipulated
df.replace('nan', np.nan, inplace=True)
df.fillna("", inplace=True)

# Set regular expression to catch emails
regex = r"[a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+.[a-zA-Z\.]*"

# Initialise empty list to add query ready emails
emails_query_format = []

# Iterate over retailer_id / emails template rows and append formatted emails to list
for i, row in df.iterrows():
    # Put all emails in the row into a list
    emails = re.findall(regex, df['additional_emails'][i])
    emails = [email.strip() for email in emails]

    # Put all additional buyers into a list
    buyer_names = row['additional_buyers']
    buyers = re.split(r";", buyer_names)
    buyers = [buyer.strip() for buyer in buyers]

    # Empty list for buyer-email tuples
    buyer_emails_tuple_list = []

    # Pair emails and names even when buyer names are missing then use empty string...
    for idx in range(len(emails)):
        if idx <= len(buyers) - 1:
            buyer_emails_tuple_list.append((buyers[idx], emails[idx]))
        elif idx > len(buyers) - 1:
            buyer_emails_tuple_list.append(("", emails[idx]))

    # Sub the value pairs on each tuple in buyer-emails tuple list into query format and append to overall list...
    for tup in buyer_emails_tuple_list:
        query_format = "(" + str(row['retailer_id']) + "," + "'" + tup[0] + "'" + "," + "'" + tup[1] + "'" + ")" + ","
        emails_query_format.append(query_format)

# New DataFrame to input query ready emails
query_df = pd.DataFrame(emails_query_format, columns=['emails'])

# Export file with query ready additional emails
query_df.to_excel(output_path + "/emails2query_ready.xlsx")


print("The file is ready, please check the output folder and grab the emails2query_ready.xlsx file in: \n"
      + output_path)
