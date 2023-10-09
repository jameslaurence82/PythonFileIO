# should work with just the file name if it is in the same folder
# if not it worked with just the containing folder name
with open("FileIO\\the-zen-of-python.txt") as f:
    contents = f.read()
    print(contents)
    print(type(contents))
print("\nWith file path")
# if it has an error the path might be required
with open('E:\\4-Data Analytics Fall 2023\\DBAS3018 - Data Movement and Integration\\Demo\\FileIO\\the-zen-of-python.txt') as f:
    contents = f.read()
    print(contents)
    print(type(contents))
    
# more precise way to read a text file line by line is by for loop
with open("FileIO\\the-zen-of-python.txt") as f:
    for line in f:
        print(line.strip())
        
# UTF-8
# when trying to read different langauge characters it will have an error unless set as UTF 8 
"""
with open("FileIO\\quotes.txt") as f:
    contents = f.read()
    print(contents)
    print(type(contents))
"""
print("\nUTF8 encoding to write different characters")
with open("FileIO\\quotes.txt",encoding="utf8") as f:
    for line in f:
        print(line.strip())
    
# writing to a file
print("\nWrite to a file readme.txt")
lines = ['Readme', 'How to write text files in Python']
print(type(lines))
with open('FileIO\\readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')
print("\nAppend lines to readme.txt file")
more_lines = ['', 'Append text files', 'The End']

with open('FileIO\\readme.txt', 'a') as f:
    f.write('\n'.join(more_lines))

# write to a file with UTF-8 encoding
print("\nWrite UTF8 encoding lines to quotes.txt file") 
quote = 'English and 成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'

with open('FileIO\\quotes.txt', 'w', encoding='utf-8') as f:
    f.write(quote)

print("\this will overwrite or create new readme.txt file")
# will overwrite or create new readme.txt file
with open('FileIO\\readme.txt', 'w') as f:
    f.write('Create a new text file!')
    
print("\nThis section of code will have errors") 
# # this will give an error if the file already exists using mode 'x'    
# with open('FileIO\\readme.txt', 'x') as f:
#     f.write('Create a new text file!')    
# This code won't work because IDE cannot create a folder. set folder manually or 
# create a new folder     
# with open('FileIO\\test\\readme.txt', 'x') as f:
#     f.write('Create a new text file!')    

print("\nTry catch exception to catch the folder error") 
try:
    with open('docs/readme.txt', 'w') as f:
        f.write('Create a new text file!')
except FileNotFoundError:
    print("Error: The 'docs' directory does not exist")


print("\nPython Check If File Exists - Non-OOP method with an existing file")
# Imports the os.path exists module
from os.path import exists
file_exists1 = exists("FileIO//readme.txt")
print(f"True if the file exists and False if it doesn't exist: Answer is --> {file_exists1}")

print("\nPython Check If File Exists - Non-OOP method with a file that doesn't exist")
# Imports the os.path exists module
from os.path import exists
file_exists2 = exists("FileIO//read.txt")
print(f"True if the file exists and False if it doesn't exist: Answer is --> {file_exists2}")

print("\nPython Check If File Exists - OOP method with an existing file")
# Imports the path module from pathLib
from pathlib import Path
path = Path("FILEIO//readme.txt")
print(f"True if the file exists and False if it doesn't exist: Answer is --> {path.is_file()}")

print("\nPython Check If File Exists - OOP method - with a file that does not exist")
# Imports the path module from pathLib
from pathlib import Path
path = Path("FILEIO//read.txt")
print(f"True if the file exists and False if it doesn't exist: Answer is --> {path.is_file()}")
    
print("\nPython Check If File Exists - OOP method with an existing file")
# Imports the path module from pathLib
from pathlib import Path
path = Path("FILEIO//readme.txt")
if path.is_file():
    print(f"The file {path} exists")
else:
    print(f'The file {path} does not exist')

print("\nPython Check If File Exists - OOP method - with a file that does not exist")
# Imports the path module from pathLib
from pathlib import Path
path = Path("FILEIO//read.txt")
if path.is_file():
    print(f'The file {path} exists')
else:
    print(f'The file {path} does not exist')
    
