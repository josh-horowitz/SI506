# SI 506 Lecture 04

## Topics

1. Statements and expressions
2. Object behaviors (a gentle intro)
3. string formatting: f-string; `\n` newline escape sequence
4. In-class coding challenges

## Vocabulary

* __Expression__. An accumulation of values, operators, and/or function calls that return a value.
  `len(< some_list >)` is considered an expression.
* __f-string__. Formatted string literal prefixed with `f` or `F`.
* __Method__. A function defined by and bound to an object. For example the `str` type is
  provisioned with a number of methods including `str.lower()` and `str.strip()`.
* __Statement__. An instruction that the Python Interpreter can execute. For example, assigning a
  variable to a value such as `name = 'arwhyte'` is considered a statement.

## 1.0 Statements and expressions

A Python _statement_ is an instruction that performs some action. For example, a variable assignment
is considered a statement. Actions that evaluate one or more conditions (`if-else-if`) or involve
iteration over a sequence or a dictionary (`for`, `while`) are also considered statements.

A Python _expression_ is a combination of values, pointers (i.e., variables), operators, and/or
function or method calls that return a value.

:bulb: A statement can include one or more expressions (the reverse is not true).

```python
schools = [
    'Gerald R. Ford School of Public Policy',
    'School of Information',
    'School of Public Health',
    'Stamps School of Art & Design'
    ] # a statement

named_schools = [] # statement
for school in schools: # statement
    if ' school' in school.lower(): # statement that includes an expression (school.lower())
        named_schools.append(school) # expression (mutates the list)

print(f"\n1.0 named schools = {named_schools}") # expression
```

## 2.0 Object behaviors (a gentle intro)

The string (`str`) type or object can be said to exhibit behaviors that are expressed in the form of
_methods_ that you can call. For example, we can call `str.lower()` to convert a string to all
lower case characters:

```python
umich = 'University of Michigan'
umich_lowercase = umich.lower()

print(f"\nUMich lowercase = {umich_lowercase}")
```

Another `str` method that you will use frequently is the `str.split()` method. This method allows
you to return a list of character "chunks" after splitting the string on a specified delimiter
(the default delimiter is a space).

```python
umich_twitter = '@UMich @UMichiganNews @UMichResearch @UMSI'
umich_twitter_handles = umich_twitter.split()

print(f"\nTWITTER 01 = {umich_twitter_handles}")
```

When you split `umich_twitter` on a space the return value is a list:

`['@UMich', '@UMichiganNews', '@UMichResearch', '@UMSI']`

Note that you can pass a specified delimiter to the `str.split()` method, as in the following
example:

```python
umich_twitter = '@UMich,@UMichiganNews,@UMichResearch,@UMSI'
umich_twitter_handles = umich_twitter.split(',')

print(f"\nTWITTER 02 = {umich_twitter_handles}")
```

:exclamation: Consider carefully your choice of delimiter when splitting a string. In the following
example, specifing a comma as the sole delimiter upon which to split the string will lead to
unexpected results:

```python
umich_twitter = '@UMich, @UMichiganNews, @UMichResearch, @UMSI'
umich_twitter_handles = umich_twitter.split(',') # wrong delimiter

print(f"\nTWITTER 03 = {umich_twitter_handles}")
```

The list returned by the split operation will contain string elements with a leading space--usually
not the desired outcome.

`['@UMich', ' @UMichiganNews', ' @UMichResearch', ' @UMSI']`

:bulb: Instead specify a delimiter that also includes a trailing space (`', '`).

Over the course of the semester you will learn to use a number of `str` methods. For a complete
listing see w3schools' ["Python String Methods"](https://www.w3schools.com/python/python_ref_string.asp)

Other types such as lists, tuples, and dictionaries also include methods you can call. We will
explore those types and their methods in the coming weeks.

## 3.0 String formatting

The lectures, lab exercises, and problem sets will often include a number of pre-positioned
`print()` statements in which a _formatted string literal_ (a.k.a f-string) is passed in as an
argument.

The f-string syntax `f"some_string {some variable}"` is less verbose and easier to construct than
earlier string formatting approaches. You will learn how to write f-strings as well as format string
using the older approaches in the very near future.

```python
course = 'SI 506'
print(f"\nCourse = {course}")
```

:bulb: `\n` represents an escape sequence, specifically an ASCII linefeed (LF). Think of `\n` as
"newline". Passing `\n` in a string will insert a new line at the position of the escape sequence.

## 4.0 Challenges

__Meme stocks__: an emerging equities category in which company popularity and stock performance is
driven in large part by social sentiment rather than traditional economic or corporate indicators.

GameStop Corp.'s (GME) share price has risen dramatically since the beginning of the year. Earlier
in the year the stock price increased an astounding 1914.55 percent between 4 January 2021 ($17.25)
and 27 January 2021 ($347.51). Between 1 March and 8 September that stock price has ranged between
$120.40 and 198.80.

The still bouyant stock price is driven in large part by otherwise small-scale "retail" investors
using social media platforms to coordinate activities and force the more traditional private equity
firms, hedge funds and wealthy investors who had bet against the stock rise via short-selling to
cover their losses by repurchasing GME shares that they had previously borrowed in order to return
them and exit their trades, a response further contributing to the rise in the share price.

We'll use the GameStop share price surge as the "theme" for today's set of challenges.

### Challenge 01

Uncomment the variable name that is both syntatically _and_ stylistically correct from the list
below:

```python
# !ticker_symbol = 'GME'
# ticker-symbol = 'GME'
# ticker_symbol = 'GME'
# @ticker_symbol = 'GME'
# TickerSymbol = 'GME'
```

### Challenge 02

Return the type and length of the "ticker symbol" object using the appropriate built-in functions
and assign the return values to the appropriate variable.

```python
obj_type = None
obj_length = None
```

### Challenge 03

GameStop is not the only company that has seen a jump in its share price due, in part, to coordinated
retail investor activity. AMC Entertainment Holdings Inc. (NYSE: AMC), BlackBerry Ltd (NYSE; BB),
and Macy's Inc. have also experienced share price surges during January 2021.

Use the `str.split()` method to split `string` into a `list`. Assign the return value to the variable
`companies`.

:exclamation: The presence of a single quote in the string requires the use of double quotes to
denote the `str` object.

```python
string = "GameStop AMC BlackBerry Macy's"
companies = None
```

### Challenge 04

Again, use the `str.split()` method to split `string` into a `list`. Assign the return value to
the variable `companies`.

:bulb: this challenge requires that you pass to `str.split(< argument >)` the appropriate
_delimiter_ argument.

```python
string = "GameStop, AMC, BlackBerry, Macy's"
companies = None
```

### Challenge 05

According to [Google Finance](https://www.google.com/finance/quote/GME:NYSE?sa=X&ved=2ahUKEwjX3Mm2_-_yAhW5MlkFHfKBBQUQ3ecFegQIGBAS&window=YTD) GameStop's YTD (Year to date) price
change is an astounding 1,052.46 percent. Write an equation that returns this value and assign it to
the variable `percent_change`.

```python
jan_04_open_price = 17.25 # 4 Jan 2021
sep_08_close_price = 198.80 # 8 Sep 2021
percent_change = None
```

### Challenge 06

Let's say you decided to speculate in GameStop shares. You purchase five (5) shares at the opening
price on Wednesday, 4 August 2021 ($146.80 per share) commission-free. You sell all five (5) shares
on Wednesday, 8 Sept 2021 ($198.80 per share), incurring a transaction fee of one percent (1%) on
the sell price. Use Python to answer the following questions.

1. How much did it cost you to purchase the five shares?
2. What was the sell price of the five shares?
3. What was the percent change in price between 4 August and 8 September?
4. How much profit did you make on the sale of the five shares?

```python
aug_04_open_price = 146.80
gamestop_shares = 5

purchase_price = None
sell_price = None
percent_change = None
fee = None
profit = None
```

### Challenge 07

The coordinated trading activity of "retail" investors rattled the market during the early part of
the year. The Security and Exchange Commission (SEC) issued a statement on Wednesday, 27 January
2021, noting that it is "actively monitoring" the current volitility in the options and equities
markets. The NY Times reports that "[n]o one knows how this ends."

First, return a count of the characters in the following multi-line string and assign to the variable
`char_count`.

Then split the string into a list of character "chunks" using the blank spaces in the string as the
delimiter. Then calculate the average chunk size and assign to the variable `avg_chunk_size`.

```python
ny_times = """
No one knows how this ends. Some analysts say the intense activity could eventually prompt a wider
sell-off in the market by forcing hedge funds on the losing side of these trades to sell parts of
their portfolios to raise cash to cover their losses. While this speculative frenzy played out on
the market’s sidelines, the S&P 500 fell more than 2.5 percent on Wednesday, its worst day since
late October, as the Federal Reserve gave a glum assessment of the economy and before a number of
big tech companies announced their earnings.
"""

char_count = None

chunks = None
chunk_count = None

avg_chunk_size = None
```

## Sources

* New York Times, ["‘Dumb Money’ Is on GameStop, and It’s Beating Wall Street at Its Own Game"](https://www.nytimes.com/2021/01/27/business/gamestop-wall-street-bets.html), 27 January 2021.
* GamesStop Inc., ["Historical Price Lookup"](https://news.gamestop.com/stock-information/historical-price-lookup)
* finbox.com, ["1 Year Stock Price Total Return for GameStop Corp."](https://finbox.com/NYSE:GME/explorer/asset_price_return_1y)
