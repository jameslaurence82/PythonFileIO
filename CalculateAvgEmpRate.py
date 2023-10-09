"""
Assignment 3-2 Requirements

Economic growth and unemployment rate data from kaggle.com
Download the dataset
Create a code to import the csv and print average unemployment rate
Format your result to show only two decimal points.
Upload your screenshot and source code on Brightspace.
"""
#####################
#     Attempt 3     #
#####################
""" Updated code to include try/except for file check """

####### Pseudo Code ##########
# Try/Except for opening csv file (open file using with function to have file close automatically)
# create csv reader object
# display data of csv_reader
# calculate average unemployment rate
# display average unemployment rate with 2 decimal points if file is found
# display custom error message if file not found

import csv # imports csv library
import os # imports os library to clear screen
 
if __name__ == "__main__":
    
    ############## Inputs and Variables: ################
    
    # Variables
    unemploy_rate = 0 # set the unemployment rate variable to 0
    avg_unemploy_rate = 0 # set the average unemployment rate variable to 0
    
    ######### Processing and Outout: ################
    try:
        # open file in read mode to check data
        # with open("gdp_and_unemp1.csv",encoding="utf8") as gdpemploy: #testing try/except with wrong filename
        with open("gdp_and_unemp.csv",encoding="utf8") as gdpemploy:
            #create csv reader object
            csv_reader = csv.reader(gdpemploy)
            # skip the header row of the csv_reader
            next(csv_reader)
            rowcount = 0 # row count variable for the loop to calculate average
            # for loop to iterate through the csv_reader of the column index 3
            for csv_rows in csv_reader: 
                unemploy_rate += float(csv_rows[3]) # sums the total of the unemployment rate column
                rowcount += 1 # increase the row counter by 1 to calculate average
            # print(f"\nThe total sum of the unemployment rate is {unemploy_rate}") # display the sum of the unemployment rate
            avg_employ_rate = unemploy_rate/rowcount # calculate the average unemployment rate
            os.system('cls') # clear the screen before printing results
        print(f"Based on the CSV Data Provided:\nThe average unemployment rate is {avg_employ_rate:.2f} %\n") # display the average rate with 2 decimal points
    except FileNotFoundError:
        print(f"\nRequested file not found\nPlease verify the file name or folder location and try again.\n")


#####################
#     Attempt 2     #
#####################
"""
####### Pseudo Code ##########
# open csv file (use with function to have file close automatically)
# create csv reader object
# display data of csv_reader
# calculate average unemployment rate
# display average unemployment rate with 2 decimal points
# close csv file <-- not required as using with function


# imports csv library
import csv

if __name__ == "__main__":
    
    ############## Inputs: ################
    
    # Variables
    unemploy_rate = 0 # set the unemployment rate variable to 0
    avg_unemploy_rate = 0 # set the average unemployment rate variable to 0
    
    ############## Processing: ################
    
    #open file in read mode to check data
    with open("gdp_and_unemp.csv",encoding="utf8") as gdpemploy:
        #create csv reader object
        csv_reader = csv.reader(gdpemploy)
        # skip the header row of the csv_reader
        next(csv_reader)
        rowcount = 0 # row count variable for the loop to calculate average
        # for loop to iterate through the csv_reader of the column index 3
        for csv_rows in csv_reader: 
            unemploy_rate += float(csv_rows[3]) # sums the total of the unemployment rate column
            rowcount += 1 # increase the row counter by 1 to calculate average
        # print(f"\nThe total sum of the unemployment rate is {unemploy_rate}") # display the sum of the unemployment rate
        avg_employ_rate = unemploy_rate/rowcount # calculate the average unemployment rate
    print(f"\nBased on the Data Provided, the Unemployment Rate is {avg_employ_rate:.2f} %\n") # display the average rate with 2 decimal points

# Wanted to add Try/Except --> Refer Attempt 3 above to see my new attempt
"""

#####################
#     Attempt 1     #
#####################
"""
####### Pseudo Code ##########
# open csv file (use with function to have file close automatically)
# create csv reader object
# display data of csv_reader
# print csv data to check code
# modify code to complete next two steps
# calculate average unemployment rate
# display average unemployment rate with 2 decimal points
# close csv file <-- not required as using with function

# This Code block is executed only when this Python script is run directly,
# not executed when imported as a module in another script.
if __name__ == "__main__":
    
#     ############# Inputs: ################
    
    # Variables
    unemploy_rate = 0 # set the unemployment rate to float
    
    ############## Processing ################
    
    #open file in read mode to check data
    with open("gdp_and_unemp.csv",encoding="utf8") as gdpemploy:
        #create csv reader object
        csv_reader = csv.reader(gdpemploy)
        # display data type of csv_reader
        print(type(csv_reader))
        # head function can be use to display the top data of the csv 
        # print(csv_reader(gdpemploy).head) <--- this does not work
        # Display the csv data
        for csv_row in csv_reader:
            print(csv_row)
        #check data type of csv_row
        print(type(csv_row)) # prints the data type of csv_row
        
        # skips the first row (Header) of the csv file
        next(csv_reader)
        for csv_row in csv_reader:
            print(csv_row)

I can't modify the bottom part of my read csv file to calculate the average 
in the above code block. Refer Attempt 2 above to see my new attempt
"""
