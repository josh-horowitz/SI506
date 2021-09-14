# SI 506: Data Structures: sequences

## 1.0 Topics

* Lecture 05
  * Sequences: strings and lists
  * Indexing
  * Slicing
  * A Look Ahead: select string and list methods

## 1.1 Vocabulary

* __Boolean__. A type (`bool`) or an expression that evaluates to either `True` or `False`.
* __Built-in Function__. A [function](https://docs.python.org/3/library/functions.html) defined by
  the Standard Library that is always available for use.
* __Dictionary__. An associative array or a map, wherein each specified value is associated with or
  mapped to a defined key that is used to access the value.
* __Expression__. An accumulation of values, operators, and/or function calls that return a value.
  `len(< some_list >)` is considered an expression.
* __Function__. A defined block of code that performs (ideally) a single task. Functions only run
  when they are explicitly called. A function can be defined with one or more _parameters_ that
  allow it to accept _arguments_ from the caller in order to perform a computation. A function can
  also be designed to return a computed value. Functions are considered "first-class" objects in the
  Python eco-system.
* __f-string__. Formatted string literal prefixed with `f` or `F`.
* __Iterable__. An object capable of returning its members one at a time. Both strings and lists are
  examples of an iterable.
* __Immutable__. Object state cannot be modified following creation. Strings are immutable.
* __Method__. A function defined by and bound to an object. For example the `str` type is
  provisioned with a number of methods including `str.strip()`.
* __Mutable__. Object state can be modified following creation. Lists are mutable.
* __Operator__. A [symbol](https://www.w3schools.com/python/python_operators.asp) for performing
  operations on values and variables. The assignment operator (`=`) and arithmetic operators
  (`+`, `-`, `*`, `/`, `**`, `%`, `//`).
* __Sequence__. An ordered set such as `str`, `list`, or `tuple`, the members of which (e.g.,
  characters, elements, items) can be accessed.
* __Slice__. A subset of a sequence. A slice is created using the subscript notation `[]` with
  colons separating numbers when several are given, such as in `variable_name[1:3:5]`. The bracket
  notation uses slice objects internally.
* __Statement__. An instruction that the Python Interpreter can execute. For example, assigning a
  variable to a value such as `name = 'arwhyte'` is considered a statement.
* __Tuple__. An ordered sequence that cannot be modified once it is created.

## 1.2 Lecture data

It is quite natural to assume that the Python programming language is named after the family of
snakes known as _Pythonidae_ or python. But you would be wrong.
[Guido van Rossum](https://gvanrossum.github.io/), the creator of the Python programming language
named it after the absurdist English comedy sketch series
[_Monty Python's Flying Circus_](https://en.wikipedia.org/wiki/Monty_Python%27s_Flying_Circus)
(1969-1974) which starred the "Pythons" Graham Chapman, John Cleese, Eric Idle, Terry Jones,
Michael Palin and the animator Terry Gilliam.

This week's lectures will feature data derived from the Pythons' famous
["Spam" sketch](https://en.wikipedia.org/wiki/Spam_(Monty_Python)) (1970) including the Spam
dominated cafe [menu](https://en.wikipedia.org/wiki/Spam_(Monty_Python)#/media/File:Monty_Python_Live_02-07-14_13_04_42_(14598710791).jpg). During the Second World
War and after Britain imposed rationing restrictions and, starting in 1941, imported massive
quantities of canned spam from the United States as a protein substitute for imports of beef, pork,
and poultry. The public, including my parents, grew to loathe it--which the sketch plays upon in
surrealist fashion.

:bulb: Have you ever wondered why unwanted email is referred to as "spam". Watch the
["Spam" sketch](https://vimeo.com/329001211) and you'll quickly understand why.

## 2.0 Sequences: strings and lists

This week we discuss Python data structures, focusing in particular on two sequence types: strings
and lists.

### 2.1 String basics

A string (type: `str`) is an ordered sequence of characters. Once created, the string is considered
_immutable_ and cannot be modified. The string is also an _iterable_, a type of object whose members
(in this case, characters), can be accessed.

String objects (an instance of the `str` class) are also provisioned with _methods_ that permit
operations to be performed on the string. These behaviors are discussed in greater detail during
the next lecture.

```python
# A string
comedy_series = 'Monty Python'

# The object's unique identifier in memory
print(f"\n2.1 comedy_series (id={id(comedy_series)}) = {comedy_series}")

# Return the object's type
comedy_series_type = type(comedy_series)

print(f"\n2.1 comedy_series type (id={id(comedy_series)}) = {comedy_series_type}")

# Return the object's length
comedy_series_len = len(comedy_series)

print(f"\n2.1 comedy_series length (id={id(comedy_series)}) = {comedy_series_len}")
```

You can confirm that a string is immutable by attempting to change one of its characters:

```python
# UNCOMMENT: Immutability check
# comedy_series[0] = 'm' # TypeError: 'str' object does not support item assignment
```

You can use the plus (`+`) operator to build a string. This is known as string concatenation.

In the example below the variable `comedy_series` is (re)assigned to a new string object comprising
the value of `comedy_series` plus the hard-coded string `"'s Flying Circus"`. The output of `print()`
demonstrates that the new concatenated string is assigned a new identity that remains unchanged for
the life of the object.

```python
comedy_series = comedy_series + "'s Flying Circus" # string concatenation (new object)

print(f"\n2.1 comedy_series (id={id(comedy_series)}) = {comedy_series}")
```

### 2.2 List basics

A list (type: `list`) represents an ordered sequence of elements (e.g., strings, lists, and/or other
object types). The list is also an _iterable_, a type of object whose members (in this case,
characters), can be accessed. Unlike a string a Python list is mutable and capable of modification.
Elements can be added or removed from lists and, if the element is mutable, (e.g., a nested list)
can be modified. List elements are accessed by position using a zero-based index value.

List objects are also provisioned with methods that permit operations to be performed on the
list. These behaviors are discussed in greater detail in a later section.

```python
# A list
pythons = [
    'Graham Chapman',
    'John Cleese',
    'Terry Jones',
    'Eric Idle',
    'Michael Palin'
    ]

# The object's unique identifier in memory
print(f"\n2.2 pythons (id={id(pythons)}) = {pythons}")

# Return the type
pythons_type = type(pythons)

print(f"\n2.2 pythons type (id={id(pythons)}) = {pythons_type}")

# Return the length
pythons_len = len(pythons)

print(f"\n2.2 pythons len (id={id(pythons)}) = {pythons_len}")
```

Unlike a string a list can be _mutated_ (i.e., modified) by adding, updating, substituting, and/or
removing elements. In the example below Terry Gilliam, the American animator (and later director),
was also a Python so let's add him to the list `pythons`. We can utilize a number of list methods
to accomplish the task. Each performs an in-place operation on the list. We will discuss list
methods in greater detail at our next meeting.

```python
# In-place list method calls mutate the list
pythons.append('Terry Gilliam')
# pythons.insert(-1, 'Terry Gilliam')
# pythons.extend(['Terry Gilliam'])
```

You can also create a _new_ list by concatenating two or more lists using the plus (`+`) operator.
In the example below a single element list containing the string 'Neil Innes' (considered by many
to be the seventh Python) is added to the `pythons` list. This results in a new list which is
assigned to the variable `python`.

```python
# Gotcha: list concatenation returns a new list
pythons = pythons + ['Neil Innes']

print(f"\n2.2 pythons (id={id(pythons)}) = {pythons}") # new identity
```

## 3.0 Indexing

You can access individual members of a sequence by their position or index value. Python's index
notation is __zero-based__. Individual characters in a string or individual elements in a list can
be accessed using either a positive or negative index operator. Index operator notation utilizes
two brackets `[]` together with the index value as in `var[0]`.

| &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; | &nbsp; |
|:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |:------ |
|   0    |   1    |   2    |   3    |   4    |   5    |   6    |   7    |   8    |   9    |   10   |   11   |
|   M    |   o    |   n    |   t    |   y    | &nbsp; |   P    |   y    |   t   |    h    |    o   |    n   |
|   -12  |   -11  |  -10   |   -9   |   -8   |   -7   |   -6   |   -5   |    -4  |   -3   |   -2   |   -1   |

### 3.1 Accessing a character in a string by position

```python
name = 'Monty Python'
letter = name[0] # first letter (zero-based index)

letter = name[4]

letter = name[-1]
```

:bulb: `name[0]` is considered an expression since it resolves to a value (e.g., "M").

### 3.2 Accessing a list element by position

```python
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

menu_item = menu[-2]
```

### 3.3 IndexError

If an index operator references a non-existent position in a sequence an `IndexError` will be
raised.

```python
# UNCOMMENT
# menu_item = menu[10] # IndexError: list index out of range
```

## 4.0 Slicing

You can access a `list` element, `tuple` item, or `str` character by position using an index
operator. You can also access a subset or _slice_ of elements, items, or characters using Python's
slicing notation.

To initate a slicing operation specify a range of index values by extending the index operator to
include an _optional_ integer `start` value, a _required_ integer `end` value that specifies the
position in which to end the slicing operation, and an _optional_ `stride` value that specifies the
slicing step (default = 1).

The slicing notation syntax simplifies referencing and/or extracting a subset of a given sequence.
List slicing can result in list traversal performance gains since slicing obviates the need to loop
over an entire list in order in order to operate on a targeted subset of elements. We will explore
this aspect of slicing when we explore list iteration in more detail starting next week.

```python
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
```

### 4.1 Slicing start/end range

:bulb: In the slicing example below the start value `1` is considered _inclusive_ while the end
value `3` is considered _exclusive_.

```python
# Return Mr and Mrs Bun.
cast_members = cast[1:3] # Returns ['Eric Idle, Mr Bun', 'Graham Chapman, Mrs Bun']
```

Negative slicing can also be employed to return the Buns:

```python
# Return Mr and Mrs Bun.
cast_members = cast[-11:-9]
```

Let's explore more examples.

### 4.2 slice from index 0 to index n (stride = 1)

```python
# Return named cast members.
cast_members = cast[:5] # or cast[0:5]
```

### 4.3 slice from index -n to end of list inclusive (stride = 1)

```python
# Return cast extras (i.e., Vikings 01-06, Police Constable) using negative slicing.
cast_members = cast[-7:] # warn: not the same as cast[-7:-1]
```

### 4.4 slice with a specified stride

You can set a stride value to increase the number of steps taken by each slice.

```python
# Return cast members in reverse order.
cast_members = cast[::-1]
```

```python
# Return every other cast member starting from the first element.
cast_members = cast[::2]
```

```python
# Return every other cast member starting from the last element (negative stride).
cast_members = cast[::-2] # reverse
```

```python
# Return every other Viking starting with Viking 01.
cast_members = cast[5:11:2]
```

```python
# Return every other Viking starting with Viking 01 in reverse order.
cast_members = cast[5:11:-2] # empty list returned

# Workaround
cast_members = cast[5:11]
cast_members = cast_members[::-2]
```

### 4.5 Slice Assignment

You can replace a subset of a list with another list or subset of a list using slice assignment.

```python
mounties = [
    'Extra, Canadian Mountie 01',
    'Extra, Canadian Mountie 02',
    'Extra, Canadian Mountie 03',
    'Extra, Canadian Mountie 04',
    'Extra, Canadian Mountie 05',
    'Extra, Canadian Mountie 06'
]
```

```python
# Replace part of a list (length unchanged).
cast[5:11] = mounties[0:] # replace Vikings with Mounties
```

```python
# Replace part of a list (length changes).
cast[5:11] = mounties[1:5] # replace Vikings with mounties 02-04 (negative slice)
```

### 4.6 Built-in del() function and slicing

You can employ slicing and the built-in `del()` function to remove subsets of a sequence.

```python
# Delete the Mounties (retain the Police Constable)
del(cast[-5:-1])
# del(cast[5:9]) # alternative
```

### 4.7 built-in slice() function

You can also use the built-in `slice()` function to return a slice object and apply it to a
sequence. `slice()` accepts three arguments: an optional integer `start` value
(default = 0), a required integer `end` value that specifies the position in which to end the
slicing operation, and an optional `step` value that specifies the slicing step (default = 1).

```python
# slice([start, ]end[, step]) object
s = slice(1, 4, 2)
cast_members = cast[s] # Returns Idle and Cleese
```

## 5.0 A Look Ahead to the next lecture: select string and list methods

The following is a short summary of select `str` and `list` methods that are relevant to this week's
lab exercise and problem. We will these and other `str` and `list` methods in more detail during our
next meeting.

### 5.1 str.join()

Returns a new string by joing each element in the passed in iterable to the specified string.

```python
items = ['Oatmeal', 'Fruit', 'Spam'] # a list
menu_item = ' '.join(items) # build a string by joining each element to an empty string

menu_item = ', '.join(items) # build a string by joining each element to a comma
```

### 5.2 str.replace()

Returns a new string by replacing the specified substring with a new value.

```python
menu_item = 'Egg, bacon and Spam'
menu_item = menu_item.replace('Spam', 'Pancakes')
```

### 5.3 str.split()

Splits a string into a list per the provided delimiter

```python
menu_item = 'Spam, bacon, sausage, Spam'
menu_items = menu_item.split(', ') # returns list
```

### 5.4 str.strip()

Returns a "trimmed" version of the string, removing leading and trailing spaces

```python
monty_python = " Monty Python's Flying Circus " # leading/trailing apostrophes
monty_python = monty_python.strip() # trims string
```

### 5.5 list.append()

Appends element to the end of a list (in-place operation, no variable assignment)

```python
menu_items.append('Red beans and rice') # adds new element to list
```

### 5.6 list.pop()

Returns the element at the specified position _after_ removing it from the list.

```python
popped = menu_items.pop(1) # removes the second element in the list
```
