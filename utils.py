import pandas as pd
import numpy as np
import sys
import re


def read_excel_template(input_file_name):
    try:
        print("Reading and parsing template...")
        return pd.read_excel(input_file_name, converters={'retailer_id': str})
    except IndexError:
        print("Error: make sure you use and .xlsx file that it is saved as Excel Workbook and NOT as "
              "Strict Open XML Spreadsheet and try again.")
        sys.exit()


def format_null_values(df):
    # Format null values to be easily manipulated
    df.replace('nan', np.nan, inplace=True)
    df.fillna("", inplace=True)

    return df


def extract_additional_emails(df_row):
    regex = r"[a-zA-Z0-9_.+-]*@[a-zA-Z0-9-]+.[a-zA-Z\.]*"
    emails = re.findall(regex, df_row)
    emails = [email.strip() for email in emails]

    return emails


def split_additional_buyer_names(df_row):
    buyer_names = re.split(r"[,;]", df_row)
    buyer_names = [buyer.strip() for buyer in buyer_names]

    return buyer_names


def pair_buyers_and_emails(buyer_names, emails):
    buyer_emails_tuple_list = []

    for i in range(len(emails)):
        if i <= len(buyer_names) - 1:
            buyer_emails_tuple_list.append((buyer_names[i], emails[i]))
        elif i > len(buyer_names) - 1:
            buyer_names.append(("", emails[j]))

    return buyer_emails_tuple_list


def transform_tuples_to_query_format(retailer_id_row, tuple_list, empty_list):
    for tup in tuple_list:
        query_format = "(" + str(retailer_id_row) + "," + "'" + tup[0] + "'" + "," + "'" + tup[1] + "'" + ")" + ","
        empty_list.append(query_format)


def get_all_pairs(df):

    try:
        print("Transforming additional buyer names and emails into query format...")

        emails_query_format = []

        for i, row in df.iterrows():
            emails_list = extract_additional_emails(row['additional_emails'])
            buyers_list = split_additional_buyer_names(row['additional_buyers'])
            pairs_tuple_list = pair_buyers_and_emails(buyers_list, emails_list)
            transform_tuples_to_query_format(row['retailer_id'], pairs_tuple_list, emails_query_format)

        return emails_query_format

    except KeyError:
        print("Error: please check that you template contains the right columns (retailer_id, additional_buyers, \
              additional_emails) and try again.")
        sys.exit()


def list_to_df(query_format_list):
    return pd.DataFrame(query_format_list, columns=['emails'])


def extract_df_to_excel(df, path, filename):
    return df.to_excel(path + filename)


def export_results(query_format_list, output_path, filename):
    export_df = list_to_df(query_format_list)
    extract_df_to_excel(export_df, output_path, filename)
    print("The file is ready, please check the output folder and grab the emails2query_ready.xlsx file in: \n"
          + output_path)
