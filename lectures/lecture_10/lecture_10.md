# SI 506 Lecture 10

## TOPICS

1. Variable scope
2. Challenges

## Vocabulary

### This week

* __Argument__. A value passed to a function or method that corresponds to a parameter defined for
  the function or method.
* __Caller__. The initiator of a function call.
* __Function__. A defined block of code that performs (ideally) a single task. Functions only run
  when they are explicitly called. A function can be defined with one or more _parameters_ that
  allow it to accept _arguments_ from the caller in order to perform a computation. A function can
  also be designed to return a computed value. Functions are considered "first-class" objects in the
  Python eco-system.
* __Parameter__. A named entity in a function or method definition that specifies an argument that
  the function or method accepts.
* __Scope__. The part of a script or program in which a variable and the object to which it is
  assigned is visible and accessible.

### Previous

* __Boolean__. A type (`bool`) or an expression that evaluates to either `True` or `False`.
* __Built-in Function__. A [function](https://docs.python.org/3/library/functions.html) defined by
  the Standard Library that is always available for use.
* __Conditional Statement__. A statement that determines a computer program's _control flow_ or the
  order in which particular computations are to be executed.
* __Dictionary__. An associative array or a map, wherein each specified value is associated with or
  mapped to a defined key that is used to access the value.
* __Expression__. An accumulation of values, operators, and/or function calls that return a value.
  `len(< some_list >)` is considered an expression.
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
* __Sequence__. An ordered set such as `str`, `list`, or `tuple`, the members of which (e.g.,
  characters, elements, items) can be accessed.
* __Slice__. A subset of a sequence. A slice is created using the subscript notation `[]` with
  colons separating numbers when several are given, such as in `variable_name[1:3:5]`. The bracket
  notation uses slice objects internally.
* __Statement__. An instruction that the Python Interpreter can execute. For example, assigning a
  variable to a value such as `name = 'arwhyte'` is considered a statement.
* __Tuple__. An ordered sequence that cannot be modified once it is created.

## Data

```python
scale = [('5 stars', 5), ('4 stars', 4), ('3 stars', 3), ('2 stars', 2), ('1 star', 1)]

# Walmart customer reviews (2 March 2021)
data = [
    ["Apple Jacks", 'Kellogg Company', (5, 185), (4, 21), (3, 10), (2, 4), (1, 2)],
    ["Cap'n Crunch", 'Quaker Oats Company', (5, 49), (4, 5), (3, 3), (2, 1), (1, 1)],
    ["Cap'n Crunch's Crunch Berries", 'Quaker Oats Company', (5, 196), (4, 15), (3, 6), (2, 2), (1, 4)],
    ['Cheerios', 'General Mills', (5, 1310), (4, 95), (3, 14), (2, 11), (1, 28)],
    ['Cinnamon Toast Crunch', 'General Mills', (5, 577), (4, 46), (3, 10), (2, 5), (1, 19)],
    ['Cocoa Puffs', 'General Mills', (5, 147), (4, 9), (3, 1), (2, 2), (1, 5)],
    ['Corn Flakes', 'Kellogg Company', (5, 467), (4, 45), (3, 9), (2, 3), (1, 10)],
    ['Frosted Flakes', 'Kellogg Company', (5, 1465), (4, 116), (3, 37), (2, 11), (1, 35)],
    ['Frosted Mini-Wheats', 'Kellogg Company', (5, 883), (4, 95), (3, 18), (2, 6), (1, 26)],
    ['Fruit Loops', 'Kellogg Company', (5, 750), (4, 84), (3, 14), (2, 6), (1, 8)],
    ['Fruity Pebbles', 'Post consumer Brands', (5, 170), (4, 23), (3, 8), (2, 2), (1, 7)],
    ['Grape-nuts', 'post Consumer Brands', (5, 322), (4, 25), (3, 3), (2, 1), (1, 15)],
    ['Honey Bunches of Oats', 'Post Consumer brands', (5, 95), (4, 7), (3, 3), (2, 1), (1, 2)],
    ['Honey-nut Cheerios', 'General Mills', (5, 814), (4, 64), (3, 22), (2, 8), (1, 22)],
    ['Lucky Charms', 'General Mills', (5, 388), (4, 38), (3, 12), (2, 3), (1, 7)],
    ['Raisin Bran', 'Kellogg Company', (5, 946), (4, 79), (3, 21), (2, 14), (1, 30)],
    ["Reese's Puffs", 'General Mills', (5, 184), (4, 14), (3, 10), (2, 4), (1, 3)],
    ['Rice Krispies', 'Kellogg Company', (5, 429), (4, 31), (3, 11), (2, 5), (1, 13)],
    ['Shredded Wheat', 'post consumer brands', (5, 208), (4, 13), (3, 6), (2, 5), (1, 11)],
    ['Wheaties', 'General Mills', (5, 215), (4, 18), (3, 5), (2, 2), (1, 12)],
]
```

## 1.0 Variable scope

Now that you have begun to write functions it's time to discuss Python's rules for resolving name
references (i.e., variables). Accessing a variable and the object to which it is assigned depends in
large part on _where_ the variable is defined in your program. An object's duration or lifetime also
depends in part on _where_ in your program it is assigned. A variable's _scope_ is limited to those
parts of a program in which the variable is visible and can be accessed.

A variable defined _inside_ a function is considered _local_ to that function. In other words, a
local variable can only be accessed from inside the function's code block. On the other hand, a
variable defined outside a function in the main part of a program file or module possesses top level
or _global_ scope. Such a variable is visible throughout the program from the point in which it was
first defined. Treat _global_ variables carefully. Referencing _global_ variables inside functions
can have unintended effects.

Python keywords and built-in functions possess a special _built-in_ scope and are also
available whenever you execute a script or run your program.

In the following example referencing the local variable `name` outside the function `format_name`
will trigger a `NameError` runtime exception.

```python
cereal = ('General Mills', 'Cocoa Puffs', 4.8, 164) # global scope

if cereal: # truth value
    cereal_exists = True # available globally

def format_name(cereal):
    name = f"{cereal[0]} {cereal[1]}" # local scope only
    return name

print(f"\n1.0: Cereal exists = {cereal_exists}")

cereal_name = format_name(cereal) # call function

print(f"\n1.0: Cereal name = {cereal_name}")

print(f"\n1.0: Local variable name = {name}") # Triggers NameError: name 'name' is not defined
```

## 2.0 Challenges

### Challenge 01

1. Implement a function named `get_cereal` that defines two parameters:

   * `cereals` (`list`): list of nested lists, each representing a cereal product
   * `name` (`str`): name of the cereal

2. The function _must_ check each cereal element's name value in the `cereals` list. If a
   _case insensitive_ name match is obtained return the cereal to the caller.

3. Call the function and pass it the following arguments:

   1. the `cereals` list
   2. the string "Lucky Charms".

4. Assign the return value to a variable named `lucky_charms`.

### Challenge 02

1. Implement a function named `get_cereals_by_company` that defines two parameters:

   * `cereals` (`list`): list of nested lists, each representing a cereal product
   * `company` (`str`): name of the product owner.

2. The function _must_ check each cereal element's company value in the `cereals` list. If a
   case-insensitive name match is obtained add the cereal element (a `list`) to a local accumulator
   list in the function code block.

3. The function _must_ compute case-insensitive, "near" matches on the company name. For example
   passing in the argument "Post" or "post" will match "Post Consumer Brands"; passing in "Kellogg" or "kellogg" will match the "Kellogg" Company.

4. Once every cereal element is checked, return the accumulated list of cereal matches.

5. Call the function and pass it the following argument using __keyword arguments__:

   1. the `cereals` list
   2. the string "post".

6. Assign the return value to a variable named `cereal`.

### Challenge 03

1. Implement a function named `count_ratings` that defines a single parameter:

   * `ratings` (`list`): list of 1 to 5 star rating tuples.

2. The function _must_ return the _sum_ of all rating counts across the five tuples
   `( < star value >, < rating count >)`.

3. To obtain the desired cereal you _must_ first call the function `get_cereal` in order to obtain
   the specified cereal, then pass the relevant list slice to `count_ratings` in order to obtain a
   list of the cereal's ratings.

4. To obtain the cereal call the function `get_cereal` and pass to it the argument(s) using
   __keyword arguments in reverse order__:

   1. the `cereals` list
   2. the string "Frosted Flakes".

5. Assign the return value of `get_cereal` to a variable name `frosted_flakes`.

6. Then call `count_ratings` and pass to it as the argument the _slice_ of `frosted_flakes`
   "ratings".

7. Assign the return value to a variable named `ratings_count`.

### Challenge 04

1. Use a `for` loop and `range()` to loop over the `cereals` list.

2. During each loop iteration return a count of the cereal's ratings and then _insert_ the count
   into each cereal list as the new third (3rd) element.

### Challenge 05

1. Implement a function named `get_ratings` that defines a single parameter:

   * `cereal` (list): represents a cereal product and its 1 to 5 star ratings.

2. The function _must_ return a list of the cereal's 1 to 5 star rating tuples.

3. After implementing the function return the Raisin Bran's five (5) and four (4) star
   "ratings" (e.g. the positive ratings).

4. To obtain the desired cereal you _must_ first call the function `get_cereal` and pass to it the
following argument(s):

   1. the `cereals` list
   2. the string "Raisin Bran".

5. Assign the return value to a variable named `raisin_bran`.

6. Call `get_ratings` and pass to it the argument `raisin_bran`.

7. Assign the return value to a variable named `raisin_bran_ratings`.

8. Call `count_ratings` and pass to it the _slice_ of cereal's five (5) and four (4) star
   "ratings".

9. Assign the return value to a variable named `favorable_count`.

### Challenge 06

1. Implement a function named `favorite_cereal` that defines two parameters:

   * `cereals` (`list`): list of nested lists, each representing a cereal product
   * `slice` (slice): slice object that defaults to some_list[:2]

2. The function will evaluate the `cereals` list and identify the cereal with the most
   favorable ratings (5 star and 4 star counts only).

3. In the function block create a list named `selection` to hold the "current" favorable cereal
   name (`str`) and the rating count (`int`). Seed the list with default values `None` and `0`. The list will be updated whenever a new contender for "favorite cereal" is identified.

4. For each cereal in `cereals` call the functions `get_ratings` and `count_ratings` in order to
   return the 5 star and 4 star counts (ignore all other ratings). Assign the return values to
   local variables.

5. Write a conditional statement that checks if the cereal's favorable ratings count is greater
   than the count stored in the `selection` list. If `True` update `selection` with the
   cereal name and ratings count.

6. After all cereals are checked return `selection` to the caller.

7. After implementing the function, call it and pass to it the `cereals` list as the argument.

8. Assign the return value to a variable named `favorite`.

### Challenge 07

5-star rankings systems typically exhibit a J-shaped distribution that tends to favor higher product
valuations due to the presence of two biases: _purchasing bias_ and _under-reporting bias_. People
who view a product unfavorably tend not to purchase it, thus decreasing the number of negative
reviews that might otherwise be written. Those who purchase the product and regard it as average
tend not to bother rating it. Thus, product ratings systems tend to reflect purchasers who are
either extremely satisfied (5-star) or extremely unsatisfied (1-star) with a product. And
satisfaction/disatisfaction may reflect criteria beyond the product itself (e.g., Walmart's grocery
delivery service) which further degrades the rankings utility.

In our case, let's write a function that filters out the "extreme" ratings for each cereal opting by
removing the 5-star and 1-star ratings for each cereal.

1. Implement a function named `exclude_extreme_ratings` that defines a single parameter:

   * `cereal` (list): represents a cereal product and its 1 to 5 star ratings.

2. The function _must_ return a new representation of the cereal that excludes the 5-star and 1-star
   tuples. The function _must_ delegate retrieval of the cereal's ratings and a count of the ratings
   to other functions previously implemented.

   `[< name >, < company >, < count >, (< 4-star tuple>), (< 3-star tuple>), (< 2-star tuple>)]`

   :bulb: Use the list concatenation to assemble the new list.

3. After `exclude_extreme_ratings` is implemented, create an empty accumulator list named
    `cereals_trimmed`. Loop over the `cereals` list. During each loop iteration call the `exclude_extreme_ratings` function and pass to it the cereal element as the argument. Append the function's return value to the `cereals_trimmed` list.

4. Then call the function `favorite_cereal` and pass to it the `cereals_trimmed` list and the slice
   object `slice(0, 4)` as arguments. Assign the return value to the variable `favorite_trimmed`.

### Challenge 08 (Bonus)

Now let's see if we can write a function to compute a
[weighted average](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean) for each cereal ranking
as Walmart does.

1. Implement a function named `calculate_weighted_mean` with a single parameter:

   * `cereal` (list): represents a cereal product and its 1 to 5 star ratings.

2. The function _must_ calculate a weighted mean for the ratings earned by a given cereal.

3. Create local "accumulator" variables `dividend` and `divisor` in the function block. Assign each
   the default value of zero (`0`).

4. Calculate the weighted mean by assigning a "weight" to each star based on the number of votes
   it received. The following equation will suffice:

   `(5 * < 5 star count > + 4 * < 4 start count > + 3 * < 3 star count > + 2 * < 2 star count > + 1 * < 1 star count >)` \
   divided by (`/`) \
   `(< 5 star count > + < 4 star count > + < 3 star count > + < 2 start count > + < 1 start count >)`

   Example (Frosted Mini-Wheats): `(5 * 883 + 4 * 95 + 3 * 18 + 2 * 6 + 1 * 26) / (883 + 95 + 18 + 6 + 26)`

5. Loop over the cereal's five rating tuples. For each star rating tuple encountered, multiply the
   star rating number (e.g., 5 for the 5 star rating) by the number of ratings the star received
   (e.g., the rating count) and add the product to `dividend`. Then add the rating count to `divisor`.

6. Ater the loop terminates divide `dividend` by `divisor` and assign the return value (round to 2
   decimal points) to a variable named `weighted_mean`. Return `weighted_mean` to the caller.

7. Test the function by first calling `get_cereal` and passing to it the nested `cereals` list and
   a cereal name (e.g., "Corn Flakes"). Assign the return value to a variable named `cereal`
   and then call `calculate_weighted_mean` passing in `cereal` as the argument. Assign the return
   value to `weighted_mean`.

    :bulb: For more info on weighted means see _Wikipedia_,
    ['Weighted Arithmetic Mean"](https://en.wikipedia.org/wiki/Weighted_arithmetic_mean).

8. Then loop over the nested `cereals` list, calculate the rating weighted mean for each cereal, and
   print the result using an f-string employing the format
   `< cereal name >, < rating weighted mean > (n=< total ratings count >))`

:bulb: _Out of scope_ for SI 506: If you wanted to sort the cereals by weighted mean
(descending order) you can call the `list.sort()` method specifying a `lambda` function assigned to
the `key` parameter along with an option sort order. A list comprehension is employed to create a
new `ratings` list. The anonymous `lambda` function provides the sort algorithmn to be applied to
the list.

```python
print(f"\nChallenge 07 Sorted: Cereal, Weighted mean, Total ratings\n")

# List comprehension
ratings = [
    (cereal[0], calculate_weighted_mean(cereal), count_ratings(get_ratings(cereal)))
    for cereal in cereals
    # for cereal in cereals if count_cereal_reviews(cereal) > 100
    ]

# Sort list using a lambda expression
ratings.sort(key=lambda cereal: cereal[1], reverse=True) # sort by rating, reverse order

for cereal in ratings:
    print(f"{cereal[0]}, {cereal[1]} (n={cereal[2]})")
```
