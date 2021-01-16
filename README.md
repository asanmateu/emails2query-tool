# emails2query Tool (v2.0.0)

This script takes a template with the columns retailer_id, additional_names, and additional_emails, and generates an excel file with a all each of the rows transforment in query-ready format.

Follow python and conda environment installation from joor-cd-cleaner repository (if you need to): https://github.com/asanmateu/joor-cd-cleaner

An complex environment is not needed here as long as you got Python3, pandas, and NumPy. Errors may occur if some excel packages are not installed. In this case set up the environment. Slack Toni if you are having issues with the installation process.

## Instructions

1. Pull or download the zip for this package and place it wherever you want that you can easily navigate to later on to execute the script.

2. Fill in the template which you can find either on the input or template directories using the required fields.

	* **retailer_id**: the corresponding id for the connection you are adding the additional names and emails to.
	* **additional_names**: additional buyer names concatenate by ";" (semicolon)
	* **additional_emails**: additional emails concatenated by ";" (semicolon)


**IMPORTANT: The tool does no magic so please make sure buyer names are set in the same order as their corresponding emails. Emails with no buyer names should go EITHER at the end OR otherwise you can write names as name1;;name3 (this will consider the value inside semicolons as "", in this case the only thing you need to make sure is that email2 has no buyer name for example. Normally, if you concatenate them in order and put a ";" in between, empty names will be already in ;; format.**

**Please slack Toni if this is not 100% clear.**


3. Place the **.xlsx** template, without changing its name, in the input directory. Make sure it's the only file there, and run the following commands on your terminal:

```
# Activate the environment if you don't have the basic packages installed (pandas, numpy, and some excel readers if errors happen)

$ conda activate cd-cleaner-conda-env

# Navigate to the folder with the script

$ cd ~path/to/emails2query

# Run the script

$ python3 emails2query.py
```

4. If no errors are thrown then you should see a message directing you to check output folder for the file with the emails in query-ready format. Drag this file out to avoid confusion next time you use it, although it overwrites everytime so not to worry otherwise.


5. Slack Toni if any issues.


## Updates

I will be updating the script when we review errors, please either pull from your IDE connecting to this remote repository or simply replace the tool folder with a new unzipped download of the repository. If additional **functionalities OR requirements** are added I will make it clear in a new section above instructions.
