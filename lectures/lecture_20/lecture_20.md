# SI 506: Lecture 20

## Topics

1. Challenges

## Vocabulary

* __Class__: "A template for creating user-defined objects. Class definitions normally contain
  method definitions which operate on instances of the class."
  [Python Official Documentation](https://docs.python.org/3/glossary.html).
* __Composition__: Pattern that involves combining object types in order to create a _composite_
  type that models a "has a" relationship between the composite and one or more _component_ objects
  (e.g., `Automobile` has an `Engine`; `Bicycle` has a `Crankset`, `Handlebar`, `Wheelset`,
  `Pedal` (2x), `Seat`, etc.).
* __Instance__: An individual object whose type is defined by the class by which it was
  instantiated or created.
* __Instance variable__: An variable and value bound to a specific instance of a class.
* __Instance method__: A function defined by a class and bound to a specific instance of a class.
* __self__: A variable that represents an instance of a class.

### Previous

* __API__: Application Programming Interface that species a set of permitted interactions between
  systems.
* __Argument__. A value passed to a function or method that corresponds to a parameter defined for
  the function or method.
* __Boolean__. A type (`bool`) or an expression that evaluates to either `True` or `False`.
* __Built-in Function__. A [function](https://docs.python.org/3/library/functions.html) defined by
  the Standard Library that is always available for use.
* __Caller__. The initiator of a function call.
* __Conditional Statement__. A statement that determines a computer program's _control flow_ or the
  order in which particular computations are to be executed.
* __Deep copying__. For a given mutable object (e.g., `list`) constructs a new compound object and
  recursively _copies_ into it objects found in the original.
* __Dictionary__. An associative array or a map, wherein each specified value is associated with or
  mapped to a defined key that is used to access the value.
* __Expression__. An accumulation of values, operators, and/or function calls that return a value.
  `len(< some_list >)` is considered an expression.
* __f-string__. Formatted string literal prefixed with `f` or `F`.
* __File Object__. An object that provides a file-oriented application programming interface
  (API) to a either a text file, binary file (e.g., image file), or a buffered binary file. File
  objects include read and write methods for interacting with a file stored locally or remotely.
* __Flow of execution__. The order in which statements in a program are executed. Also referred to
   as _control flow_.
* __Function__. A defined block of code that performs (ideally) a single task. Functions only run
  when they are explicitly called. A function can be defined with one or more _parameters_ that
  allow it to accept _arguments_ from the caller in order to perform a computation. A function can
  also be designed to return a computed value. Functions are considered "first-class" objects in the
  Python eco-system.
* __HTTP__: The Hypertext Transport Protocol is an application layer protocol designed to facilitate
  the distributed transmission of hypermedia. Web data communications largely depends on HTTP.
* __Immutable__. Object state cannot be modified following creation. Strings are immutable.
* __Iterable__. An object capable of returning its members one at a time. Both strings and lists are
  examples of an iterable.
* __Iteration__. Repetition of a computational procedure in order to generate a possible sequence of
  outcomes. Iterating over a `list` using a `for` loop is an example of iteration.
* __JSON__: Javascript Object Notation, a lightweight data interchange format.
* __Method__. A function defined by and bound to an object. For example the `str` type is
  provisioned with a number of methods including `str.strip()`.
* __Mutable__. Object state can be modified following creation. Lists are mutable.
* __Nested Loop__. A `for` or `while` loop located within the code block of another loop.
* __Operator__. A [symbol](https://www.w3schools.com/python/python_operators.asp) for performing
  operations on values and variables. The assignment operator (`=`) and arithmetic operators
  (`+`, `-`, `*`, `/`, `**`, `%`, `//`).
* __Parameter__. A named entity in a function or method definition that specifies an argument that
  the function or method accepts.
* __Querystring__: That part of a Uniform Resouce Locator (URL) that assigns values to specified
  parameters.
* __Resource__: A named object (e.g., document, image, service, collection of objects) that is both
  addressable and accessible via an API.
* __Scope__. The part of a script or program in which a variable and the object to which it is
  assigned is visible and accessible.
* __Sequence__. An ordered set such as `str`, `list`, or `tuple`, the members of which (e.g.,
  characters, elements, items) can be accessed.
* __Shallow copying__. For a given mutable object (e.g., `list`) constructs a new compound object
  but inserts _references_ (rather than copies) into it of objects found in the original. The
  `list.copy()` returns a shallow copy of the original list.
* __Slice__. A subset of a sequence. A slice is created using the subscript notation `[]` with
  colons separating numbers when several are given, such as in `variable_name[1:3:5]`. The bracket
  notation uses slice objects internally.
* __Statement__. An instruction that the Python Interpreter can execute. For example, assigning a
  variable to a value such as `name = 'arwhyte'` is considered a statement.
* __Truth Value__. In Python any object can be tested for its
  [truth value](https://docs.python.org/3/library/stdtypes.html#truth-value-testing) using an `if`
  or `while` condition or when it is used as an operand in a
  [Boolean operation](https://docs.python.org/3/library/stdtypes.html#boolean-operations-and-or-not).
* __Tuple__. An ordered sequence that cannot be modified once it is created.
* __Tuple packing__. Assigning items to a tuple.
* __Tuple unpacking__. Assigning tuple items to an equal number of variables in a single assignment.
  A `list` can also be unpacked.
* __URI__: Uniform Resource Identifier that identifies unambiguously a particular resource.
* __URL__: Uniform Resource Locator is a type of URI that specifies the _location_ of a resource on
  a network and provides the means to retrieve it.
* __URN__: Uniform Resource Name is a type of URI that provides a unique identifier for a resource
  but does not specify its location on a network.

## 1.0 Challenges

## 1.1 Challenge 01

__Task__: Implement the `Film` class.

1. Call `read_json` and retrieve the list of Star Wars films from `swapi_films.json`. Assign the
   return value to a variable named `films_data`.

2. Implement the `Film` class. The `Film` class includes a __class variable__ named `franchise`
   with an assigned value of "Star Wars". You access class variables using dot notation (`.`)
   but unlike instance variables that are prefixed by `self` class variables are prefixed by the
   class name:

   ```python
   Film.franchise
   ```

3. Implement the "dunder" `__init__` method specifing the following parameters that _must_ be
   passed by the caller to initialize (e.g., create) a `Film` instance:

   * title
   * episode_id
   * release_date

   <br />

4. Add a fourth _optional_ instance variable named

   * audience_rating

   <br />

   This additional instance variable can only be set _after_ a `Film` instance is instantiated
   (in other words _do not_ include it in the function's parameter list). Assign it a value of
   `None`.

5. Implement the "dunder" `__str__` method. Return the following formatted string to the caller:

   ```commandline
   < franchise >: < title > (Episode < episode_id >)
   ```

6. Implement a `jsonable` method. Return a dictionary that includes the following key-value pairs:

    ```python
    {
        'title': < val >,
        'episode_id': < val >,
        'release_date': < val >,
        'audience_rating': < val >
    }
    ```

## 1.2 Challenge 02

__Task__: Read `swapi_films.json`. Convert dictionaries to `Film` instances and add each instance to
an accumulator dictionary.

1. Call `read_json` and retrieve the list of films in `swapi_films.json`. Assign the return value to
   a variable named `films_data`.

2. Create an "accumulator" dictionary named `films`. Loop over `films_data` and for each film
   dictionary use it's data to create a `Film` instance. Then assign each `Film` instance to the
   "accumulator" dictionary utilizing the film instance's title as the key and the film instance
   as the value.

   ```python
   {
        { '< title >': < Film >}
        . . .
   }
   ```

## 1.3 Challenge 03

__Task__: Read `rotten_tomatoes-star_wars.json`. Convert dictionaries to `Film` instances and add
each instance to an accumulator dictionary.

:exclamation: Given time constraints, the `AudienceRating` class is implemented fully.

1. Call `read_json` and retrieve the list of ratings in `rotten_tomatoes-star_wars.json`. Assign
   the return value to a variable named `ratings_data`.

2. Create an "accumulator" dictionary named `audience_ratings`. Loop over `ratings_data` and for
   each ratings dictionary use it's data to create a `AudienceRating` instance. Then assign each
   `AudienceRating` instance to the "accumulator" dictionary utilizing the audience rating
   instance's title as the key and the `AudienceRating` instance as the value.

   ```python
   {
        { '< title >': < AudienceRating >}
        . . .
   }
   ```

## 1.4 Challenge 04

__Task__: Loop over the `films` keys and assign to each `Film` instance the appropriate
`AudienceRating` instance in the `audience_ratings` dictionary.

1. Loop over the `film` keys. Inside this loop implement another loop that loops over the
   `audience_ratings` values. Utilize the outer loop's key value to assign each
   `AudienceRating` instance to the appropriate `Film.audience_rating` instance variable.

   :bulb: match on the title between the two dictionaries.

2. Create an accumulator listed named `writeable = []`. Loop over the `films` dictionary and
   append a JSON-friendly dictionary representation of each `Film` instance to `writeable`.

3. Call `write_json` and write `writeable` to a JSON file named `films_ratings.json`.

## 1.5 Challenge 05

__Task__: Add a method named `get_audience_positive_rating` to the `Film` class. Refactor
`Film.jsonable()` to ensure that a JSON-friendly dictionary representation of `AudienceRating`
if an instance has been assigned to `Film.audience_rating` instance variable. Return a list of
`Film` instances from `films` sorted by each film's positive audience rating. Serialize the list as
JSON and write it to a file.

1. Implement a new `Film` method named `get_audience_positive_rating`. The method defines no
   parameters (other than `self`) and returns the `Film` instance's `audience_rating`
   `positie_rating` value.

2. _Refactor_ (e.g., modify) `Film.jsonable()` so that a JSON-friendly dictionary representation
   of the `AudienceRating` instance assigned to `Film.audience_rating` can be returned _if_ an
   `AudienceRating` instance has been assigned to the instance variable.

3. Convert `films` dictionary values to a `list` and assign the return value to a variable named
   `film_rankings`.

4. __BONUS__: Sort the `film_rankings` list method employing an anonymous `lambda` function that
   sorts the list by each film's positive audience rating.

   A [`lambda`](https://docs.python.org/3/glossary.html) is

   > an anonymous inline function consisting of a single expression which is evaluated when the
   > function is called. The syntax to create a lambda function is `lambda [parameters]: expression`.

   :bulb: `lambda` functions assigned to the optional `key` argument can be passed to `list.sort()` or
   the built-in function `sorted()` in order to override the default sort order.

   ```python
   film_rankings.sort(key=lambda film: film.audience_rating.positive_rating, reverse=True)

   # Alternative (built-in sorted() function)
   film_rankings = sorted(
       film_rankings,
       key=lambda film: film.audience_rating.positive_rating,
       reverse=True
       )
   ```

5. Create an accumulator listed named `writeable = []`. Loop over the `film_rankings` list and
   append a JSON-friendly dictionary representation of each `Film` instance to `writeable`.

6. Call `write_json` and write `writeable` to a JSON file named `films_ranked.json`.
