# emails2query Script

MAIN USE: split and stack concatenated additional emails with its corresponding retailer ID in query format.


This script takes a specific format template which is provided in the folder named exactly emails2query_template.xls and returns a .csv file with the data transformed into tuples ready for copy pasting into the "add_buyers_and_logins" query. MIND THE ENDING COMMA.

This script can be used when additional emails require no name.

You will different cases, judge by yourself if you might want to leave the first email to go with the connections and buyer name or if you want to add them all through query. If you want to add first one with the connections then parse it and then concat the rest again to use this template... Every case is different.



# INSTRUCTIONS 

=====================================================================================================================================

### FIRST TIME:

1. Place the file on Desktop.

2. Install python3 and use pip/pip3/conda to setup an environment with numpy and pandas.


=====================================================================================================================================

### EVERYTIME YOU USE:

1. Drop the specific template which is provided in the folder with .xls format and exact name in the input folder. MAKE SURE THERE IS ONLY ONE FILE AT A TIME.

2. Open terminal, make sure you've activated the correct environment if you need to and run:

	$ cd ~/Desktop/emails2query
	$ python emails2query.py 
	
Note: do not include the dollar symbol this is just saying "terminal command"...

3. A file should have been generated on the output folder which contains a column with the emails ready to copy and paste into query template. Check that the last comma is deleted so that it matches the format that the template requires.

4. Make sure to remove templates from input and output to avoid confusion next time you use it as it can mess up results if theres several files in input especially.

=====================================================================================================================================


## NOTES

There is a copy of the environment I use (file: .yml) in case you want to clone it although its faster to just set up your own since it's only NumPy and pandas you need and the version is pretty recent. Save the environment in the folder in case of major future updates on the packages.