# SI 506 Lecture 05

# 2.1 STRING BASICS

comedy_series = 'Monty Python'

# TODO UNCOMMENT
print(f"\n2.1 comedy_series (id={id(comedy_series)}) = {comedy_series}")

# TODO UNCOMMENT
comedy_series_type = type(comedy_series)

print(f"\n2.1 comedy_series type (id={id(comedy_series)}) = {comedy_series_type}")

# TODO UNCOMMENT
comedy_series_len = len(comedy_series)

print(f"\n2.1 comedy_series length (id={id(comedy_series)}) = {comedy_series_len}")

# UNCOMMENT: Immutability check
# comedy_series[0] = 'm' # TypeError: 'str' object does not support item assignment

comedy_series = comedy_series + "'s Flying Circus" # string concatenation (new object)

print(f"\n2.1 comedy_series (id={id(comedy_series)}) = {comedy_series}")


# 2.2 LIST BASICS

pythons = [
    'Graham Chapman',
    'John Cleese',
    'Terry Jones',
    'Eric Idle',
    'Michael Palin'
    ]


print(f"\n2.2 pythons (id={id(pythons)}) = {pythons}")

pythons_type = type(pythons)

print(f"\n2.2 pythons type (id={id(pythons)}) = {pythons_type}")

pythons_len = len(pythons)

print(f"\n2.2 pythons len (id={id(pythons)}) = {pythons_len}")

# In-place list method calls mutate the list.

# TODO UNCOMMENT
pythons.append('Terry Gilliam')
# pythons.insert(-1, 'Terry Gilliam')
# pythons.extend(['Terry Gilliam'])

print(f"\n2.2 pythons (id={id(pythons)}) = {pythons}")

# Gotcha: list concatenation returns a new list
# TODO UNCOMMENT
pythons = pythons + ['Neil Innes'] # list concatenation (new list)

print(f"\n2.2 pythons (id={id(pythons)}) = {pythons}") # new identity


# 3.0 INDEX OPERATOR

### 3.1 Index position (string)

name = 'Monty Python'
letter = name[0] # first letter (zero-based index)

print(f"\n3.1 Letter = {letter}")

letter = name[4]

print(f"\n3.1 Letter = {letter}")

letter = name[-1]

print(f"\n3.1 Letter = {letter}")


### 3.2 Index operator (list)

menu = [
    'Egg and bacon',
    'Egg, sausage and bacon',
    'Egg and Spam',
    'Egg, bacon and Spam',
    'Egg, bacon, sausage and Spam',
    'Spam, bacon, sausage and Spam',
    'Spam, egg, Spam, Spam, bacon and Spam',
    'Spam, Spam, Spam, egg and Spam',
    'Spam, Spam, Spam, Spam, Spam, Spam, baked beans, Spam, Spam, Spam and Spam',
    'Lobster Thermidor aux crevettes with a Mornay sauce, garnished with truffle pâté, brandy and a fried egg on top and Spam'
    ]

menu_item = menu[1] # second element (zero-based index)

print(f"\n3.2 Menu item = {menu_item}")

menu_item = menu[9]

print(f"\n3.2 Menu item = {menu_item}")

# TODO UNCOMMENT
# menu_item = menu[10] # IndexError: list index out of range#


# 4.0 SLICING

cast = [
    'Terry Jones, Waitress',
    'Eric Idle, Mr Bun',
    'Graham Chapman, Mrs Bun',
    'John Cleese, The Hungarian',
    'Michael Palin, Historian',
    'Extra, Viking 01',
    'Extra, Viking 02',
    'Extra, Viking 03',
    'Extra, Viking 04',
    'Extra, Viking 05',
    'Extra, Viking 06',
    'Extra, Police Constable'
]

# 4.1 slice from index 0 to index n (stride = 1)

# Return Mr and Mrs Bun
cast_members = cast[1:3]

print(f"\n4.1 The Buns = {cast_members}")

# Return Mr and Mrs Bun (negative slice)
cast_members = cast[-11:-9]

print(f"\n4.1 The Buns (negative slice) = {cast_members}")


# 4.2 slice from index 0 to index n (stride = 1)
cast_members = cast[:5] # or cast[0:5]

print(f"\n4.2 Named cast members = {cast_members}")


# 4.3 slice from index -n to end of list inclusive (stride = 1)
cast_members = cast[-7:] # warn: not the same as cast[-7:-1]

print(f"\n4.3 Extras = {cast_members}")


# 4.4 slice with a specified stride

# Return cast members in reverse order
cast_members = cast[::-1]

print(f"\n4.4 Cast members reverse order = {cast_members}")

# Return every other cast member starting from the first element
cast_members = cast[0::2]

print(f"\n4.4 Every other cast member = {cast_members}")

# Return every other cast member starting from the last element (negative stride)
cast_members = cast[::-2] # reverse

print(f"\n4.4 Every other cast member (negative stride) = {cast_members}")

# Return every other Viking starting with Viking 01.
cast_members = cast[5::2]

print(f"\n4.4 Every other Viking = {cast_members}")

# Return every other Viking starting with Viking 01 in reverse order.
cast_members = cast[5:11:-2] # Fails: empty list returned

print(f"\n4.4 Every other Viking reverse order = {cast_members}")

# Workaround
cast_members = None # slice with default stride
cast_members = None # slice all with reverse stride

# print(f"\n4.4 Every other Viking reverse order workaround = {cast_members}")


# 4.5 Slice Assignment

mounties = [
    'Extra, Canadian Mountie 01',
    'Extra, Canadian Mountie 02',
    'Extra, Canadian Mountie 03',
    'Extra, Canadian Mountie 04',
    'Extra, Canadian Mountie 05',
    'Extra, Canadian Mountie 06'
]


# 4.5.1 Replace part of a list (length unchanged)

# TODO UNCOMMENT
cast[5:11] = mounties[0:] # replace Vikings with Mounties

print(f"\n4.5.1 Replace Vikings with Canadian Mounties = {cast}")

# 4.5.2 Replace part of a list (length changes)
# TODO UNCOMMENT
# cast[?] = mounties[?] # replace Vikings with mounties 02-04 (negative slice)

# print(f"\n4.5.2 Replace Vikings with mounties 02-04 = {cast}")


# 4.6 Built-in del() function and slicing

# 4.6.1 Delete a slice with built-in del() function

# Delete the Mounties (retain the Police Constable)
# TODO UNCOMMENT
# del(cast[?)

# print(f"\n4.6.1 Delete Mounties = {cast}")

# 4.6.2 built-in slice() function

# slice([start, ]end[, step]) object
s = slice(1, 4, 2) # Returns Idle and Cleese
# TODO UNCOMMENT
cast_members = None

# print(f"\n4.6.2 slice() example = {cast_members}")


## 5.0 SELECT STRING AND LIST METHODS

# 5.1 str.join()

# Returns a new string by joing each element in the passed in iterable to the specified string.

items = ['Oatmeal', 'Fruit', 'Spam'] # a list
menu_item = ' '.join(items) # build a string by joining each element to an empty string

# print(f"\n5.1 Menu item (space) = {menu_item}")

menu_item = ', '.join(items) # build a string by joining each element to a comma

# print(f"\n5.1 Menu item (comma) = {menu_item}")


# 5.2 str.replace()

# Returns a new string by replacing the specified substring with a new value.

menu_item = 'Egg, bacon and Spam'
menu_item = menu_item.replace('Spam', 'Pancakes')

# print(f"\n5.2 Menu item = {menu_item}")


# 5.3 str.split()

# Splits a string into a list per the provided delimiter

menu_item = 'Spam, bacon, sausage, Spam'
menu_items = menu_item.split(', ') # returns list

# print(f"\n5.3 Menu items = {menu_items}")


# 5.4 str.strip()

# Returns a "trimmed" version of the string, removing leading and trailing spaces

monty_python = " Monty Python's Flying Circus " # leading/trailing apostrophes
monty_python = monty_python.strip()

# print(f"\n5.5 Monty Python (stripped) = {monty_python}")


# 5.5 list.append()

# Appends element to the end of a list (in-place operation, no variable assignment)

menu_items.append('Red beans and rice')

# print(f"\n5.6 Menu items = {menu_items}")


# 5.6 list.pop()

# Returns the element at the specified position _after_ removing it from the list.

popped = menu_items.pop(1)

# print(f"\n5.6 Menu items = {menu_items}")

print('\n') # padding
