# imports the csv module
import csv
# opens the csv file in read mode --> Use abosule path if file doesn't open 
with open('FileIO//country.csv', 'r') as f:
    # creates a csv reader object
    csv_reader = csv.reader(f)
    # iterates over each line in the csv using reader object
    for line in csv_reader:
        # print each line of the CSV
        print(line)
    # prints datatype of line
    print(type(line))        
    
# to separate the header data from the rest of the data   
with open('FileIO//country.csv', 'r') as f:
    # creates a csv reader object
    csv_reader = csv.reader(f)
    # iterates over each line in the csv using reader object
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            # print the header title and then the header line of the CSV
            print('Header:')
            print(line)  # header data
            # print the data title and then goes to else statement to print the data
            print('Data:')
        else:
            # prints the csv data
            print(line)      

# to separate the header data and not include in the data
with open('FileIO//country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)

    # skip the first row
    next(csv_reader)

    # show the data
    for line in csv_reader:
        print(line)
        
        
# this will be used to figure out assignment 3-2
total_area = 0

# calculate the total area of all countries

with open('FileIO//country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)

    # skip the header
    next(csv_reader)

    # calculate total
    for line in csv_reader:
        total_area += float(line[1])

print(f"The total area is {total_area:.2f}") # use f string to have 2 decimal place with assignment

"""
Reading a CSV file using the DictReader class
First, the way to access the values from the CSV file is not so obvious. 
For example, the line[0] implicitly means the country name. It would be 
more expressive if you can access the country name like line['country_name'].
Second, when the order of columns from the CSV file is changed or new columns
are added, you need to modify the code to get the right data.
"""
print("\nTo print data as Dictionary")
with open('FileIO//country.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f)
    # skip the header
    next(csv_reader)
    # show the data
    for line in csv_reader:
        print(f"The area of {line['name']} is {line['area']} km2")
        
"""
Python Write CSV File
"""