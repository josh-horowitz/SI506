# SI 506: Lecture 11

import csv
import os


def read_csv(filepath, delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list
    of lists, wherein each nested list represents a single row from the input file.

    Parameters:
        filepath (str): The location of the file to read.
        delimiter (str): delimiter that separates the row values

    Returns:
        list: contains nested "row" lists
    """

    with open(filepath, 'r', newline='', encoding='utf-8') as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)

        return data


def read_file(filepath, strip=True):
    """Read text file line by line. Remove whitespace and trailing newline
    escape character.

    Parameters:
        filepath (str): path to file
        strip (bool): remove white space, newline escape characters

    Returns
        list: list of lines in file
    """

    with open(filepath, 'r', encoding='utf-8') as file_obj:
        if strip:
            data = []
            for line in file_obj:
                # data.append(line) # includes trailing newline '\n'
                data.append(line.strip()) # strip leading/trailing whitespace including '\n'
            return data

            # return [line.strip() for line in file_obj] # list comprehension (single line)
        else:
            return file_obj.readlines() # list


def write_csv(filepath, data, headers=None):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): content to be written to the target file
        headers (seq): optional header row list or tuple.

    Returns:
        None
    """

    with open(filepath, 'w', newline='', encoding='utf-8') as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers) # add header row
            for row in data:
                writer.writerow(row) # iterable
        else:
            writer.writerows(data) # iterable


def write_file(filepath, data, newline=True):
    """Write content to a target file encoded as UTF-8. If optional newline is specified
    append each line with a newline escape sequence (`\n`).

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): list of strings comprising the content to be written to the target file
        newline (bool): add newline escape sequence to line

    Returns:
        None
    """

    with open(filepath, 'w', encoding='utf-8') as file_obj:
        if newline:
            for line in data:
                file_obj.write(f"{line}\n") # add newline
        else:
            file_obj.writelines(data) # write sequence to file


# 1.0 FILE PATHS WITH OS.PATH

# Absolute path to directory in which *.py is located.
abs_path = os.path.dirname(os.path.abspath(__file__))
print(f"\n1.0 Absolute directory path = {abs_path}")

# Current working directory
cwd = os.getcwd()
print(f"\n1.0 Current working directory = {cwd}")

# Construct macOS and Windows friendly paths
# faculty_path = os.path.join(abs_path, 'umsi-faculty.txt')
# resnick_path = os.path.join(abs_path, 'resnick-publications.csv')

faculty_path = './umsi-faculty.txt'
resnick_path = './resnick-publications.csv'

print(f"\n1.0 umsi-faculty.txt path = {faculty_path}")
print(f"\n1.0 resnick-publications.csv path = {resnick_path}")


# 2.1 OPEN/CLOSE FILE (YE OLDE WAY)

# TODO Implement

# print(f"\n2.1 faculty names .read()\n{data}")


# 2.2 WITH STATEMENT (RECOMMENDED WAY)

# TODO Implement with open()

# print(f"\n2.2 with open() statement)\n{data}")


# 2.3 FILE OPENING MODES

with open(faculty_path, 'r') as file_obj: # open in read mode
    data = file_obj.read()

# print(f"\n2.3 read mode ('r')\n{data}")

filepath = './umsi-faculty-v2.txt'
# filepath = os.path.join(abs_path, 'umsi-faculty-v2.txt')

# TODO Uncomment
# with open(filepath, 'w') as file_obj: # open in write mode
#     file_obj.write(data) # writes string to file


# 2.4 READ METHODS (READLINE(), READLINES())

# 2.4.1 READLINE()

with open(faculty_path, 'r') as file_obj: # open in read mode
    data = file_obj.readline()
    # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
    # data += file_obj.readline() # UNCOMMENT: call n times but not efficient
    # data += file_obj.readline() # UNCOMMENT: call n times but not efficient

# print(f"\n2.4.1 faculty names .readline()\n{data}")


# 2.4.2 READLINES()

with open(faculty_path, 'r') as file_obj: # open in read mode
    data = None # TODO Implement # returns list; elements include trailing '\n'

# print(f"\n2.4.2 faculty names .readlines() (type={type(data)}\n{data}")

# print(f"\n2.4.2 faculty .readlines(), .join()\n{''.join(data)}") # print string (pretty)


# 2.4.3 GOTCHA: READ(), READLINES() LIMITTED TO ONE CALL ONLY

with open(faculty_path, 'r') as file_obj: # open in read mode
    data = None # TODO Implement
    data_lines = None # TODO Implement # WARN: does not execute

# print(f"\n2.4.3 data_lines list is empty = {data_lines}\n")


# 2.5 WRITE METHODS (WRITE(), WRITELINES())

# 2.5.1 WRITE STR TO FILE WITH WRITE()

with open(faculty_path, 'r') as file_obj: # open in read mode
    data = file_obj.read() # returns a single multiline string

filepath = './umsi-faculty-v3.txt'
# filepath = os.path.join(abs_path, 'umsi-faculty-v3.txt')

# TODO Uncomment
# with open(filepath, 'w') as file_obj: # open in write mode
#     file_obj.write(data)


# 2.5.2 WRITE SEQUENCE TO FILE WITH WRITELINES()

with open(faculty_path, 'r') as file_obj: # open in read mode
    data = file_obj.readlines() # returns a list

# Reverse names

# TODO Implement loop

# WARN: does not update string
# for faculty_member in data:
#     name = faculty_member.strip().split(', ') # strip \n
#     faculty_member = f"{name[1]} {name[0]}\n" # does not update string element

filepath = './umsi-faculty-v4.txt'
# filepath = os.path.join(abs_path, 'umsi-faculty-v4.txt')

# TODO Uncomment
# with open(filepath, 'w') as file_obj: # open in write mode
#     file_obj.writelines(data)


# 2.5.3 WRITE SEQUENCE TO FILE WITH WRITE()

with open(faculty_path, 'r') as file_obj: # open in read mode
    data = None # TODO Implement

filepath = './umsi-faculty-v5.txt'
# filepath = os.path.join(abs_path, 'umsi-faculty-v5.txt')

# TODO Uncomment
# with open(filepath, 'w') as file_obj: # open in write mode
#     pass # TODO Implement loop

# 2.5.4 CALL READ_FILE() / WRITE_FILE() INSTEAD

# Get data
data = None # TODO call function

# Access surnames first before calling function
surnames = []

# TODO Implement loop

# Bonus: List comprehension (elegant list creation in a single line)
# surnames = [row.split(', ')[0] for row in data]

# Write surnames to file
filepath = './umsi-faculty-v6.txt'

# TODO Uncomment
# write_file(filepath, surnames)


# 3.0 CSV FILES

# 3.3 RESNICK RECOMMENDER SYSTEMS

# 1.0 Read CSV file and retrieve data
filepath = './resnick-publications.csv'
publications = read_csv(filepath)

# print(f"\n3.0: Total publications (rows) = {len(publications)}")

# 2.0 Get headers
headers = publications[0] # header row

# print(f"\n3.0: Total elements (columns) = {len(headers)}")

# 3.0 Filter title on "recommender"; accumulate results
recommender_publications = []

for publication in publications[1:]:
    if 'recommender' in publication[headers.index('title')].lower():
        recommender_publications.append(publication)

# 4.0 Write CSV file
filepath = './resnick-recommender_publications.csv'

# TODO Uncomment
# write_csv(filepath, recommender_publications, headers)


# 4.0 NESTED LISTSs

faculty = read_file(faculty_path)

# Normalize the strings (all lower case)

# TODO Implement loop

# for member in faculty:
#     member = member.lower() # WARN: this does not mutate the underlying string

# print(f"4.0: UMSI faculty (lower case) sample\n{faculty[:3]}")

# Find UMSI coathured publications
umsi_coauthor_publications = []

# TODO Implement

# Write CSV file (order of publications determined by publications loop)
filepath = './umsi_coauthor_publications.csv'
# filepath = os.path.join(abs_path, 'umsi_coauthor_publications.csv')

# TODO Uncomment
# write_csv(filepath, umsi_coauthor_publications, headers)

# Loop over faculty, publications, authors (less efficient)
# Guard against appending duplicate publications (due to multiple
# coauthors in faculty) with a compound if statement
umsi_coauthor_publications.clear()

# TODO Implement

# Write CSV file (order of publications determined by faculty loop)
filepath = './umsi_coauthor_publications-v2.csv'
# filepath = os.path.join(abs_path, 'uumsi_coauthor_publications-v2.csv')

# TODO Uncomment
# write_csv(filepath, umsi_coauthor_publications, headers)