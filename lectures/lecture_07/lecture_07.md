# SI 506 Lecture 07

## Topics

1. Control flow
2. Definite iteration: the `for` loop
3. The `if` statement
4. The accumulator pattern
5. Loop and slicing
6. `if-else` statements
7. `if-elif-else` statements

## Vocabulary

* __Argument__. A value passed to a function or method that corresponds to a parameter defined for
  the function or method.
* __Boolean__. A type (`bool`) or an expression that evaluates to either `True` or `False`.
* __Built-in Function__. A [function](https://docs.python.org/3/library/functions.html) defined by
  the Standard Library that is always available for use.
* __Conditional Statement__. A statement that determines a computer program's _control flow_ or the
  order in which particular computations are to be executed.
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
* __Immutable__. Object state cannot be modified following creation. Strings are immutable.
* __Iterable__. An object capable of returning its members one at a time. Both strings and lists are
  examples of an iterable.
* __Iteration__. Repetition of a computational procedure in order to generate a possible sequence of
  outcomes. Iterating over a `list` using a `for` loop is an example of iteration.
* __Method__. A function defined by and bound to an object. For example the `str` type is
  provisioned with a number of methods including `str.strip()`.
* __Mutable__. Object state can be modified following creation. Lists are mutable.
* __Operator__. A [symbol](https://www.w3schools.com/python/python_operators.asp) for performing
  operations on values and variables. The assignment operator (`=`) and arithmetic operators
  (`+`, `-`, `*`, `/`, `**`, `%`, `//`).
* __Parameter__. A named entity in a function or method definition that specifies an argument that
  the function or method accepts.
* __Sequence__. An ordered set such as `str`, `list`, or `tuple`, the members of which (e.g.,
  characters, elements, items) can be accessed.
* __Slice__. A subset of a sequence. A slice is created using the subscript notation `[]` with
  colons separating numbers when several are given, such as in `variable_name[1:3:5]`. The bracket
  notation uses slice objects internally.
* __Statement__. An instruction that the Python Interpreter can execute. For example, assigning a
  variable to a value such as `name = 'arwhyte'` is considered a statement.
* __Tuple__. An ordered sequence that cannot be modified once it is created.

## 1.0 Control flow

This week we focus on _control flow_ or the order in which a program or script executes. You will
learn how to iterate or loop over a sequence (`list`, `str`, `tuple`) using a `for` loop. You will
also learn how to use the `while` statement as well as manage the number of iterations to perform on
a sequence given some condition with the `continue` and `break` statements.

You will also learn how to write conditional statements in order to determine which computations
your code must perform. Conditional statements can be placed inside the body of a `for` or `while`
loop in order to act as data filters or terminate a looping operation if a particular condition has
been satisfied.

Conditional statements employ a variety of operators. As noted previously, Python operators are
organized into [groups](https://www.w3schools.com/python/python_operators.asp). We’ve touched on
arithmetic operators and assignment operators. Starting this week you will begin using other
operators when writing conditional statements, especially comparison, logical, and membership
operators.

## 2.0 Definite iteration: the `for` loop

Given a select list of model year 2021 electric passenger vehicles derived from the US Department of
Energy's [Fuel Economy](https://www.fueleconomy.gov/feg/ws/index.shtml) vehicle data (18.3 MB) and a
task to create a new list called `tesla_cars` that contains all Tesla vehicle data contained in
`elec_vehicles` how would you accomplish the task?

```python
elec_vehicles = [
    'Ford Mustang Mach-E AWD',
    'Kandi K27',
    'Chevrolet (GM) Bolt EV',
    'Audi (Volkswagen) e-tron',
    'Nissan Leaf (40 kW-hr battery pack)',
    'Tesla Model 3 Performance AWD',
    'Volvo XC40 AWD BEV',
    'Volkswagen ID.4 1st',
    'Polestar (Volvo) 2',
    'BMW i3s',
    'Mini (BMW) Cooper SE Hardtop 2 door',
    'Tesla Model S Performance (19in Wheels)'
]

# TODO Populate the list with Tesla vehicles
tesla_vehicles = [] # add elements
```

One solution would involve referencing each nested Tesla vehicle list by its index position and then
appending each vehicle to `tesla_vehicles` by calling the `list.append()` method and passing to it
a reference to the nested vehicle list. However, if the number of elements in the list were to grow,
calling the `list.append()` method repeatedly across multiple lines of code would prove both time
consuming and result in a series of repetitive statements that would prove difficult to maintain as
the number of model years and/or vehicle data increases.

Indeed, if the DOE `elec_vehicles` list covered the model years 2010-2021 it would include 245
elements (including the "header" element) and numerous Tesla vehicle nested lists. If you were
asked to analyze all the DOE's vehicle fuel economy data for the period 1994 to the present you
would confront 43255 records.

A more efficient approach is to utilize a `for` loop to traverse the sequence. Employing a
`for` loop that terminates automatically once the last character, element, or item in a
sequence is reached is known more generally as __definite iteration__.

The `for` loop employs the keywords `for` and `in` as in the expression
`for < element > in < sequence >:` and is terminated by a trailing colon (`:`) that indicates the
start of the loop's code block. The statement(s) that comprise the loop's code block _must_ be
indented four (4) spaces. The statements are _local_ to the loop and are only executed when the
loop is executed.

```commandline
for < element > in < sequence >:
    # indented block
    < statement A >
    < statement B >
    ...
```

```python
for vehicle in elec_vehicles:
    # indented block
    print(vehicle)
```

In order to find "Tesla" elements among our list of strings we can employ conditional logic to
evaluate each string encountered as we loop over the `elec_vehicles` list. Doing so involves
implementing an `if` statement.

### 2.2 The `if` statement

The rationale for writing a `for` loop is usually expressed in one or more conditional statements
defined within the body of the loop. The conditional statement determines which computations, if
any, are to be performed during the current iteration depending on whether the condition expressed
evaluates to true or false. More generally, conditional statements help determine a computer
program's _control flow_ or the order in which individual statements are executed.

The `if` statement is written as `if < condition >:` and is terminated with a trailing colon (`:`)
that indicates the start of the loop's code block. The statement(s) the `if` statement's code block
_must_ be indented four (4) spaces. The statements are _local_ to the `if statement` and are only
executed if the statement condition returns `True`.

```commandline
if < condition >:
    # indented block
    # < statement A.1 >
    # < statement A.2 >
    # ...
```

Below is a second example in which `elec_vehicles` elements are passed to the built-in `print()`
function if the string contains the substring "volvo".

```python
for vehicle in elec_vehicles:
    if vehicle[0].lower().find('volvo') > -1:
        print(vehicle)
```

:bulb: `str.find()` returns `-1` if no match is obtained; otherwise the method call returns the
index of the first occurence of the passed in substring.

For our "tesla" task, a conditional statement can be implemented in the loop's code block in order
to identify Tesla vehicles. In this scenario, the `if` statement acts as a filter, identifying
vehicles produced by Tesla whenever the condition evaluates to `True`. When an element satisfies the
condition it can be appended to a target list that acts as an "accumulator".

:exclamation: Failure to employ Python's indention rules can lead to unexpected computations and/or
trigger an `IndentionError`.

```python
tesla_vehicles = [] # accumulator
for vehicle in elec_vehicles:
    if vehicle.lower().startswith('tesla'):
        tesla_vehicles.append(vehicle)
```

:bulb: Note the use of `str.lower()` in the above conditional statements. Use of `str.lower()`
renders the `if` statement _case-insentive_ ensuring that possible variations in the manufacturer
name (e.g., "Tesla", "tesla", "TESLA"), will not result in skipping otherwise valid matches. This
is an example of "defensive" programming. When working with string data never assume that the data
is "clean" (i.e., uniform and consistent).

## 3.0 The accumulator pattern

One common programming “pattern” is to traverse a sequence (e.g., a `str`, `list`, or `tuple`),
_accumulating_ a value during each iteration of the loop and assigning it to another sequence
created and assigned to a variable _prior_ to implementing the `for` loop.

In the previous example, we created an empty "accumulator" list named `tesla_vehicles`. We then
looped over `elec_vehicles` accumulating string representations of Tesla vehicles that were
appended, each in turn, to the `tesla_vehicles` list.

Another variant of the accumulator pattern is to initialize an accumulator value, assigning it a
default value that is then updated in a subsequent `for` loop whenever a certain loop condition is
satisfied.

In the example below, two accumulator values are utilized in order to find the electric vehicle
with the greatest range in miles. The variable `num` is updated during a loop iteration whenever
a vehicle's range is greater than `num`. Likewise, the variable `vehicle_max_range` variable is
replaced with a new value if the condition is satisfied. When the loop terminates, the nested
vehicle list containing the best range value will have been assigned to `vehicle_max_range`.

:bulb: Conditional statements often compare two values using comparison operators
(`==`, `!=`, `>`, `<`, `>=`, `<=`). The return value of such expressions is either `True` or
`False`.

```python
# Manufacturer, Model, Year, Range (miles)
elec_vehicles = [
    ['Ford', 'Mustang Mach-E AWD', 2021, 211],
    ['Kandi', 'K27', 2021, 59],
    ['Chevrolet (GM)', 'Bolt EV', 2021, 259],
    ['Audi (Volkswagen)', 'e-tron', 2021, 222],
    ['Nissan', 'Leaf (40 kW-hr battery pack)', 2021, 149],
    ['Tesla', 'Model 3 Performance AWD', 2021, 315],
    ['Volvo', 'XC40 AWD BEV', 2021, 208],
    ['Volkswagen', 'ID.4 1st', 2021, 250],
    ['Polestar (Volvo)', '2', 2021, 233],
    ['BMW', 'i3s', 2021, 153],
    ['Mini (BMW)', 'Cooper SE Hardtop 2 door', 2021, 110],
    ['Tesla','Model S Performance (19in Wheels)', 2021, 387]
]

vehicle_max_range = None
num = 0
for vehicle in elec_vehicles:
    if vehicle[-1] > num:
        num = vehicle[-1] # ignores ties
        vehicle_max_range = vehicle
```

### 3.1 Challenge

Loop over `elec_vehicles` and leverage the accumulator pattern to return the electric vehicle with
the _shortest_ range and assign it to the variable `vehicle_min_range`.

```python
vehicle_min_range = None
num = None

# TODO Implement loop / conditional statement
```

## 4.0 Looping and slicing

You can also loop over slice expressions (recall that slicing a sequence returns a new sequence).
In the example below, the first element in `elec_vehicles` is not a representation of a vehicle but
a list containing the column names (headers) that describe the data contained in each nested
vehicle list. When working with the vehicle data you will want to exclude this element and you can
do so by looping over `elec_vehicles[1:]`.

:bulb: Later in the course you will work with CSV (comma-separated value) files. A header row of
column names is often included in the file in order to render it self-documenting (or nearly so). Be
sure to exclude the header row when analyzing the actual data imported from the CSV. You can also
extract the header row into its own list rather than simply ignoring or discarding it. The `headers`
list elements can then be used to look up corresponding values in the data as the example below
illustrates.

```python
elec_vehicles = [
    ['automaker', 'brand', 'model', 'year', 'range', 'range_hwy', 'range_city', 'highway_08_mpg', 'charge_240v_hrs'],
    ['Ford Motor Company', 'Ford', 'Mustang Mach-E AWD', 2021, 211, 193.7, 225.5, 86, 8.5],
    ['Kandi Technologies Group', 'Kandi', 'K27', 2021, 59, 51.6, 64.3, 102, 7.0],
    ['General Motors Co.', 'Chevrolet', 'Bolt EV', 2021, 259, 235.1, 277.7, 108, 9.3],
    ['Volkswagen AG', 'Audi', 'e-tron', 2021, 222, 221.9408, 222.74, 77, 10.0],
    ['Nissan Motor Co.', 'Nissan', 'Leaf (40 kW-hr battery pack)', 2021, 149, 131.3, 163.2, 99, 8.0],
    ['Tesla, Inc.', 'Tesla', 'Model 3 Performance AWD', 2021, 315, 299.0, 328.7, 107, 10.0],
    ['Volvo Group', 'Volvo', 'XC40 AWD BEV', 2021, 208, 188.0, 223.6, 72, 8.0],
    ['Volkswagen AG', 'Volkswagen', 'ID.4 1st', 2021, 250, 230.1587, 266.7659, 89, 7.5],
    ['Volvo Group', 'Polestar', '2', 2021, 233, 222.1, 241.9, 88, 8.0],
    ['Bayerische Motoren Werke AG', 'BMW', 'i3s', 2021, 153, 136.4, 166.5, 102, 7.0],
    ['Bayerische Motoren Werke AG', 'Mini', 'Cooper SE Hardtop 2 door', 2021, 110, 101.9, 116.9, 100, 4.0],
    ['Tesla, Inc.', 'Tesla','Model S Performance (19in Wheels)', 2021, 387, 373.2, 398.3, 106, 14.7]
]

headers = elec_vehicles[0] # column headers
vehicles_range = [] # accumulator
for vehicle in elec_vehicles[1:]:
    if vehicle[headers.index('range')] > 250: # lookup header row name
        vehicles_range.append(vehicle)
```

## 5.0 Counting

The built-in `len()` function provides us with the overall length or size of a list. But if you
want to return a count of a subset of a sequence in which slicing cannot be used, then consider
using an accumulating "counter" variable to hold a rolling count of the elements that satisfy a
given condition as in the example below where a count of the number of vehicles manufactured by
Volvo is accumulated.

A default value of zero (`0`) is assigned to the `volvo_count` variable. The variable is utilized to accumulate a count of the number of nested lists represents vehicles produced by the Swedish Volvo
Group.

:bulb: Note use of the "assignment addition" operator `+=` to _increment_ the count. The expression
`volvo_count += 1` is the equivalent to `volvo_count = volvo_count + 1`, an example of Python
"syntatic sugar" that I encourage you to use. You can also perform "assignment subtraction using the
`-=` operator to _decrement_ a count.

```python
volvo_count = 0
for vehicle in elec_vehicles[1:]:
    if vehicle[0].lower() == 'volvo group':
        volvo_count += 1 # assignment addition
```

### 5.1 Challenge

Return a count of the number of electric vehicles with a highway miles per gallon (mpg) rating
(`highway_08_mpg`) greater than or equal to 100 miles.

```python
mpg_count = 0

# TODO Implement loop / conditional statement
```

## 6.0 `if-else` conditions

Execution of an `if` statement's indented code block occurs _only_ if the condition to be tested
evaluates to `True`. If `False` is returned and a need exists to execute other statements in
response an `else` statement can be added togetther with an indented code block.

```commandline
if < condition >:
    < statement A >
    # ...
else:
    < statement B >
    # ...
```

The `if-else` block below evaluates an electric vehicle's battery charge period; if the period is
less than 8 hours it is considered a "short charge" and the element is appended to the
`short_charge` list; otherwise the vehicle is appended to the `long_charge` list.

```python
short_charge = []
long_charge = []
for vehicle in elec_vehicles[1:]:
    if vehicle[-1] < 8.0:
        short_charge.append(vehicle)
    else:
        long_charge.append(vehicle)
```

## 7.0 `if-elif-else` conditions

Multiple conditions can also be specified by specifying one or more `elif` conditions in between
an `if-else` block. The `if-elif-else` statement chain or ladder is executed from the top downwards.

```commandline
if < condition >:
    # < statement A >
    # ...
elif < condition >:
    < statement B >
    # ...
elif < condition >:
    < statement C >
    # ...
else:
    < statement D >
    # ...
```

The `else` statement is optional but recommended, especially for new programmers in order to render
explicit the conditional logic to be evaluated. You can also nest `if-elif-else` statement blocks.
We will explore nested conditional statements during a later lecture.

### 7.1 Challenge

Electric vehicle battery range remains a concern for consumers. Implement a `for` loop with an
`if-elif-else` block that assigns each vehicle in the list to one of three categories based on
their reported city range:

```python
range_city_high = [] # 300+ mpg (city)
range_city_med = []  # 150-299 mpg (city)
range_city_low = []  # 0 - 149 mpg (city)

# TODO Implement loop / conditional statements
```

However, do not append the vehicle `list` to the target accumulator list; instead assign a
string representation of the vehicle formatted as follows:

`< year brand model > range < range city > mpg (city)`

as in

```python
['2021 Kandi K27 range 64.3 mpg (city)', '2021 Mini Cooper SE Hardtop 2 door range 116.9 mpg (city)']
```
