# emails2query Tool (v2.0.0)

This script takes a template with the columns retailer_id, additional_names, and additional_emails, and generates an excel file with each of the rows transforment in query-ready format.

**Version 2.0.0**: incorporates a new column with additional buyer names and parses them together with their respective email into query format.

A complex environment is not needed here as long as you got Python3, pandas, and NumPy. Errors may occur if some excel packages are not installed. In this case set up the environment or just follow the error an will tell you which ones are missing. It should even tell you what command to run (i.e., `conda install openpyxl` or `pip3 install openpyxl` depending on your environment). 

Slack Toni if you are having issues with the installation process.


## Instructions

1. Pull or download the zip for this package and place it wherever you want that you can easily navigate to later on to execute the script.

2. Fill in the template which you can find either on the input or template directories using the required fields.

	* **retailer_id**: the corresponding id for the connection you are adding the additional names and emails to.
	* **additional_names**: additional buyer names concatenate by ";" (semicolon)
	* **additional_emails**: additional emails concatenated by ";" (semicolon)


3. Place the **.xlsx** template, without changing its name, in the input directory. Make sure it's the only file there, and run the following commands on your terminal:

```
# Activate the environment if you don't have the basic packages installed (pandas, numpy, and some excel readers: openpyxl, xlrd, or xlwt)

$ conda activate cd-cleaner-conda-env

# Navigate to the folder with the script

$ cd ~path/to/emails2query

# Run the script

$ python3 emails2query.py
```

4. If no errors are thrown then you should see a message directing you to check output folder for the file with the emails in query-ready format. Drag this file out to avoid confusion next time you use it, although it overwrites everytime so not to worry otherwise.


5. Slack Toni if any issues.


## Important Notes ⚠️

The tool does no magic so please **make sure buyer names are set in the same order as their corresponding emails**.

**Emails with NO buyer names should:**

1. Be **at the end** of the emails concatenation, so that they are not matched to a wrong name.

**OR** 

2. You can **write names as name1;;name3** (this will consider the value inside semicolons as ""). In this case the only thing you need to make sure is that email2 has no buyer name, for example. Normally, if you concatenate them in the order given by additional columns 1, 2, 3... and put a ";" in between, empty names will be already in ;; format.


You can concatenate both buyers and emails separately by copying all the additional buyer name / email column to a separate worksheet, use concatenate and then simply insert ";" between elements in the excel formula.

**Please slack Toni if this is not 100% clear.**


## Updates 📡

I will be updating the script when we review errors, please either pull from your IDE connecting to this remote repository or simply replace the tool folder with a new unzipped download of the repository. If additional **functionalities OR requirements** are added I will make it clear in a new section above instructions.
