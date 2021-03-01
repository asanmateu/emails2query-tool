# emails2query Tool (v3.0.0)

This script takes a template with the columns retailer_id, additional_names, and additional_emails, and generates an excel file with each of the rows transformed into query-ready format.

**Version 3.0.0**: Modular design to fit main source code.

Only needs Python3, pandas, and NumPy. Errors may occur if some excel packages are not installed. In this case set up the environment or just follow the error an will tell you which ones are missing. It should even tell you what command to run (i.e., `conda install openpyxl` or `pip3 install openpyxl` depending on your environment). 


## Instructions 📋

1. Pull or download the zip for this package and place it wherever you want that you can easily navigate to later on to execute the script.

2. Fill in the template which you can find either on the input or template directories using the required fields.

	* **retailer_id**: the corresponding id for the connection you are adding the additional names and emails to.
	* **additional_names**: additional buyer names concatenate by ";" (semicolon) or "," (comma)
	* **additional_emails**: additional emails concatenated by any non alpha-numerical char.


3. Place the **.xlsx** template, without changing its name, in the input directory. Make sure it's the only file there, and run the following commands on your terminal:

```
# Activate the environment if you don't have the basic packages installed (pandas, numpy, and some excel readers: openpyxl, xlrd, or xlwt)

$ conda activate cd-cleaner-conda-env

# Navigate to the folder with the script

$ cd ~path/to/emails2query

# Run the script

$ python3 main.py
```

4. If no errors are thrown then you should see a message directing you to check output folder for the file with the emails in query-ready format. Drag this file out to avoid confusion next time you use it, although it overwrites everytime so not to worry otherwise.


## Important Notes ⚠️

Please **make sure buyer names are set in the same order as their corresponding emails**.

**Emails with NO buyer names should:**

1. Be **at the end** of the emails concatenation, so that they are not matched to a wrong name.

**OR** 

2. You can **write names as name1;;name3** (this will consider the value inside semicolons as ""). In this case the only thing you need to make sure is that email2 has no buyer name, for example. Normally, if you concatenate them in the order given by additional columns 1, 2, 3... and put a ";" in between, empty names will be already in ;; format.

You can have as many leading or ending ";" in the email concatenation since empty emails won't be included.

You can concatenate both buyers and emails separately by copying all the additional buyer name / email column to a separate worksheet, use concatenate and then simply insert ";" between elements in the excel formula.
