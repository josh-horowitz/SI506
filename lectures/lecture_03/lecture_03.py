# SI 506 Lecture 03

# 1.0 COMMENTS

# A single line comment <-- commences with hash (#) character

"""
This is a block comment comprising a multi-line string. This is actually a string
constant that is denoted by the use of triple quotation marks.
"""

# 3.0 VARIABLES

num = 506
print(num)
print(type(num))

welcome_message = 'Welcome to SI 506'

teaching_team = ['arwhyte', 'amjaha', 'dsewhite','raynez','torchont', 'ykamat']

chorus = """
Hail! to the victors valiant
Hail! to the conquering heroes
Hail! Hail! to Michigan
the leaders and best!
"""

# 4.0 VARIABLE NAMING RULES AND CONVENTIONS

# 4.1 Good

# Choose lowercase

# TODO variable assignment

# Separate words with underscore (_)

# TODO variable assignment

# Use plural form to indicate a set or sequence

# TODO variable assignment

# Ok to use recognizable abbreviations like num[ber], val[ue] or var[iable].

# TODO variable assignment

# "is_", "has_" Boolean true/false

# TODO variable assignment

# All caps designates a module level constant (special case)
BASE_URL = 'https://si506.org/'

# Function definition specifying two parameters x and y (a foreshadowing of the weeks ahead)
def multiply(x, y):
    return x * y # arithmetic

# Call the function and pass two numeric arguments
product = multiply(14, 27)

print(f"\n4.2: function return value = {product}\n") # formatted string literal (f-string)

# Built-in enumerate() function adds a counter < i > when looping over < course_codes >
course_codes = ['SI 564', 'SI 574', 'SI 579', 'SI 582']
for i, code in enumerate(course_codes, 1):
    print(f"{i}. {code}")


# 4.2 Bad (but legal)

# Opaque
c = 'SI 506'
cc = 'SI 506'

# Reserve CamelCase for class names.
CourseCode = 'SI 506'

# Unnecessarily verbose; difficult to read.
c_o_u_r_s_e_c_o_d_e = 'SI 506'

# Difficult to read; guaranteed to annoy.
cOUrsE_cOdE = 'SI 506'


# 4.3 Ugly (illegal)

# Illegal: keyword used as a variable name (language-specific identifiers reserved by Python)

# class = 'SI 506' # use clazz # TODO UNCOMMENT

# Illegal: variable name commences with a numeric value.

# 506_umsi = 'SI 506' # TODO UNCOMMENT

# Illegal: variable name commences with a special character (e.g., `@`, `%`, `$`, `&`, `!`)

# $number = 506 # TODO UNCOMMENT

# Illegal: variable name includes a dash (`-`).

# course-list = ['SI 506', 'SI 507', 'SI 618'] # TODO UNCOMMENT

# Illegal: variable name includes whitespace.

# course name = 'SI 506' # illegal; uncomment to test

# Avoid: built-in function names (a few examples) # TODO UNCOMMENT

# Shadowing; risk name clash with built-in functions
# id = 506
# str = 'Go Blue'
# min = 0
# max = 27
# len = 6 # See example TypeError below

# Alternative names
id_ = 506

str_ = 'Go Blue'
val = 'Go Blue'

min_ = 0
min_val = 0

max_ = 27
max_val = 27

len_ = 6
length = 6


# 5.0 BUILT-IN FUNCTIONS (print(), type(), len())

# 5.1 print(): print passed in object to the screen

# Passing a hard-coded string.
print('\n5.1: SI 506 rocks!') # \n = newline escape character

# Passing a variable name which points to a string.
print(f"\n5.1: print welcome_message = {welcome_message}") # formatted string literal

# Passing a variable name which points to a multiline string.
print(f"\n5.1: print multiline str = {chorus}")


# 5.2 type(): determine object's data type

data_type = type(num)
print(f"\n5.2: num type = {data_type}") # returns <class 'int'>

data_type = type(welcome_message)
print(f"\n5.2: welcome_message type = {data_type}") # returns <class 'str'>

data_type = type(teaching_team)
print(f"\n5.2: teaching_team type = {data_type}") # returns <class 'list'>


# 5.3 len(): check length of sequence (i.e., number of elements)

# TODO UNCOMMENT
# len = 10 # Shadowing built-in function name (avoid)
# Generates TypeError: 'int' object is not callable when len() is called below.

# Count characters in string (including whitespace).
char_count = len(welcome_message)
print(f"\n5.3: welcome_message length = {char_count}")

# Count number of elements in list.
team_count = len(teaching_team)
print(f"\n5.3: team_count length = {team_count}")


# 6.0. BASIC ARITHMETIC (addition, subtraction, multiplication, division)

# Counts
lecturer_count = 1
gsi_count = 5
ia_count = 2
lab_section_count = 8
student_count = 250

# Addition (+ operator)
teaching_team_count = lecturer_count+gsi_count+ia_count
print(f"\n6.0: teaching_team_count = {teaching_team_count}")

# Subtraction (- operator)
instructor_count = teaching_team_count-gsi_count-ia_count
print(f"\n6.0: instructor_count = {instructor_count}")

# Multiplication (* operator)
max_enrollment = None
print(f"\n6.0: max_enrollment = {max_enrollment}")

# Floating point division (/ operator)
avg_lab_size = student_count/lab_section_count
print(f"\n6.0: average lab size = {avg_lab_size}")

# Floor division a.k.a integer division (//)
avg_lab_size = student_count//lab_section_count
print(f"\n6.0: average lab size = {avg_lab_size}")
