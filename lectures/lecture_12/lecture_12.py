# SI 506: Lecture 12

import copy
import csv
import os


def get_attribute(publication, headers, attribute):
    """Returns publication attribute value based on passed in "header" look up value.

    Parameters:
        publication (list): represents a publication
        headers (list): column names sourced from CSV
        attribute (str): name of "header" attribute

    Returns:
        obj: str, int, list value sourced from publication list
    """

    pass # TODO implement


def format_title(string):
    """Converts all-caps string to mixed case. Reformats individual words using str.lower()
    and str.title(). Case conversion logic ignores < acronyms > and
    < stopwords > unless the stopword constitutes the first word in the string.

    Parameters:
        string (str): all-caps string to convert

    Returns:
        str: string converted to mixed case
    """

    acronyms = ('ACM', 'CHI', 'CIKM', 'ICER', 'ISDN', 'PLOS', 'RECSYS', 'SIGCHI', 'SIGIR', 'WWW')

    stopwords = (
        'a', 'an', 'and', 'as', 'do', 'for', 'from', 'how', 'in',
        'is', 'it', 'on', 'or', 'of', 'to', 'the', 'that', 'with'
        )

    pass # TODO Implement


def filter_authors(authors, filters=None):
    """Removes one or more authors from a list of publication authors per the passed
    in < filters > list of names. Filtering is case-insensitive. The filter is a list
    of strings employing the following format:

    [ '< Last Name >, < First Name >', '< Last Name >, < First Name >', ...]

    If no < filters > is passed in, the < authors > list is returned unchanged.
    Otherwise, nested loops are employed to loop over < filters > (outer loop) and
    < authors > (inner loop). For each filter string provided a case-insensitive
    string comparison is performed against each author. If a match is obtained
    the author is removed from < authors >.
    """

    pass # TODO implement


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


# 0.0 FILE PATHS WITH OS.PATH
# Absolute path to directory in which *.py is located.
abs_path = os.path.dirname(os.path.abspath(__file__))
print(f"\n Absolute directory path = {abs_path}")

# Construct macOS and Windows friendly paths
faculty_path = os.path.join(abs_path, 'umsi-faculty.csv')
resnick_path = os.path.join(abs_path, 'resnick-citations.csv')

# Relative paths
# faculty_path = './umsi-faculty.csv'
# resnick_path = './resnick-citations.csv'

print(f"\n0.0 umsi-faculty.csv path = {faculty_path}")
print(f"\n0.0 resnick-citations.csv path = {resnick_path}")


# 1.0 TUPLES

faculty = None # TODO Implement single item tuple
# faculty = 'Paul Resnick', # no parentheses (legal)
# faculty = ('Paul Resnick') # a string

# print(f"\n2.0 Single item tuple (type={type(faculty)}) = {faculty}")

faculty = ('Paul Resnick', 'TAWANNA DILLAHUNT', 'Barbara Ericson')

# TODO Uncomment
# print(f"\n2.1 Single item tuple (type={type(faculty)}) = {faculty}")

# TODO Uncomment (trigger TypeError)
# faculty[1] = 'Tawanna Dillahunt' # TypeError: 'tuple' object does not support item assignment

faculty = None # TODO Implment # each a single tuple

# print(f"\n2.2 Tuple concatenation (type={type(faculty)}) = {faculty}")

# TODO Uncomment
# tawanna = faculty[1] # returns string

# print(f"\n2.3 Tawanna (type={type(tawanna)}) = {tawanna}")

# TODO Uncomment
# tawanna_barb = faculty[-2:] # returns tuple

# print(f"\n2.3 Tawanna and Barb (type={type(tawanna_barb)}) = {tawanna_barb}")

# TODO Unpack
# ? = faculty

# TODO Uncomment
# print(f"\n2.4 Tuple unpacking = {paul}")
# print(f"\n2.4 Tuple unpacking = {tawanna}")
# print(f"\n2.4 Tuple unpacking = {barb}")

# TODO Uncomment (triggers ValueError)
# paul, tawanna, barb = faculty[1:] # triggers a runtime exception
# paul, tawanna, barb, chris = faculty # triggers a runtime exception


# 3.0 CHALLENGES

# CHALLENGE 01: CSV READER / WRITER AND DEEP COPYING

# Read CSV file and retrieve data
data = None # TODO call function

# Obtain a deep copy of publications
publications = None # TODO call function  # no references to data object

# Get headers
headers = None # TODO get headers # header row

# TODO Uncomment
# print(f"\n2.1 Headers\n{headers}")

# TODO Uncomment
# print(f"\n2.2 Publications (select examples)\n")
# for publication in publications[1:3]:
#     print(publication)


# CHALLENGE 02 CLEAN DATA

# Note the duplication
# for publication in publications[1:]:
#     title_idx = headers.index('Title')
#     authors_idx = headers.index('Authors')
#     source_idx = headers.index('Source Title')

#     if publication[title_idx].isupper():
#         publication[title_idx] = format_title(publication[title_idx])
#     if publication[authors_idx].isupper():
#         publication[authors_idx] = format_title(publication[authors_idx])
#     if publication[source_idx].isupper():
#         publication[source_idx] = format_title(publication[source_idx])


# Refactor: put columns in a sequence and loop over them

# TODO Implement solution

# Write to file
filepath = './resnick-citations-cleaned.csv'
# filepath = os.path.join(abs_path, 'resnick-citations-cleaned.csv')

# TODO Uncomment
# write_csv(filepath, publications, headers)


# CHALLENGE 03 TOTAL CITATIONS PER YEAR

# Slice out the years
idx = None # TODO assign header # first column with annual citation counts
years = None # TODO slice # slice
annual_counts = []

# TODO Implement loop

# Write to file
filepath = './resnick-citations-annual_counts.csv'
# filepath = os.path.join(abs_path, 'resnick-citations-annual_counts.csv')

# TODO Uncomment
# write_csv(filepath, annual_counts, ['year', 'citations'])


# CHALLENGE 04 GET UMSI COAUTHORS (REMOVE RESNICK; AVIOD WRITING DUPLICATE NAMES TO LIST)

filepath = './umsi-faculty.csv'
# input_path = os.path.join(abs_path, 'umsi-faculty.csv')
faculty = read_csv(filepath)

# TODO implement loop

# BONUS: lambda sort (anonymous function)
# Sort case insensitive otherwise ALL CAPS names sorted ahead of mixed case names

# TODO Uncomment (first sort)
# umsi_coauthors.sort(key=lambda x: (x[0].lower(), x[1].lower()))
# umsi_coauthors.sort(key=lambda x: (x[0], x[1])) # ALL CAPS names sorted ahead of mixed case names

# Write to file
filepath = './resnick-citations-umsi_coauthors.csv'
# filepath = os.path.join(abs_path, 'resnick-citations-umsi_coauthors.csv')

# TODO Uncomment
# write_csv(filepath, umsi_coauthors, ['last_name', 'first_name'])


# CHALLENGE 05 GET UMSI COAUTHORED PUBLICATIONS

# Find UMSI coathured publications

# TODO Implement loop

# Write to file
filepath = './resnick-citations-umsi_coauthored.csv'
# filepath = os.path.join(abs_path, 'resnick-citations-umsi_coauthored.csv')

# TODO Implement
# write_csv(filepath, umsi_coauthored, headers)


# CHALLENGE 06 MOST CITATIONS (TIES PERMITTED)

# TODO Implement loop

# Write to file
filepath = './resnick-citations-max_citations.csv'
# filepath = os.path.join(abs_path, 'resnick-citations-max_citations.csv')

# TODO Uncomment
# write_csv(filepath, max_citations, headers)
