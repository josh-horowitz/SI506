# SI 506 Lecture 04

# 1.0 STATEMENTS AND EXPRESSIONS

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


# 2.0 OBJECT BEHAVIORS (GENTLE INTRO)

umich = 'University of Michigan'
umich_lowercase = umich.lower()

print(f"\n2.0 UMich lowercase = {umich_lowercase}")

umich_twitter = '@UMich @UMichiganNews @UMichResearch @UMSI'

umich_twitter_handles = umich_twitter.split()

print(f"\n2.0 TWITTER 01 = {umich_twitter_handles}")

umich_twitter = '@UMich,@UMichiganNews,@UMichResearch,@UMSI'
umich_twitter_handles = umich_twitter.split(',')

print(f"\n2.0 TWITTER 02 = {umich_twitter_handles}")

umich_twitter = '@UMich, @UMichiganNews, @UMichResearch, @UMSI'
umich_twitter_handles = umich_twitter.split(', ')

print(f"\n2.0 TWITTER 03 = {umich_twitter_handles}")


# 4.0 CHALLENGES


# CHALLENGE 01

# !ticker_symbol = 'GME'
# ticker-symbol = 'GME'
ticker_symbol = 'GME'
# @ticker_symbol = 'GME'
# TickerSymbol = 'GME'

# TODO COMMENT AND ADD VARIABLE
print(f"\nChallenge 01 = {ticker_symbol}")


# CHALLENGE 02

obj_type = type(ticker_symbol)

print(f"\nChallenge 02 type = {obj_type}")

obj_length = len(ticker_symbol)

print(f"\nChallenge 02 length = {obj_length}")


# CHALLENGE 03

string = "GameStop AMC BlackBerry Macy's" # note single quote surrounded by double quotes

companies = string.split() # default delimiter is blank space

print(f"\nChallenge 03 = {companies}")


# CHALLENGE 04

string = "GameStop, AMC, BlackBerry, Macy's" # note single quote surrounded by double quotes

companies = string.split(", ")

print(f"\nChallenge 04 = {companies}")


# CHALLENGE 05

jan_04_open_price = 17.25 # 4 Jan 2021
sep_08_close_price = 198.80 # 8 Sep 2021
percent_change = ((sep_08_close_price - jan_04_open_price)/jan_04_open_price)*100

print(f"\nChallenge 05 (ytd return) = {percent_change}")

# Bonus: str.format()
# Formatting types: see https://www.w3schools.com/python/ref_string_format.asp

percent_change_formatted = str.format(f"{percent_change:.2f}")

print(f"\nChallenge 05 (ytd return formatted) = {percent_change_formatted}")


# CHALLENGE 06

aug_04_open_price = 146.80
gamestop_shares = 5

purchase_price = aug_04_open_price * gamestop_shares

print(f"\nChallenge 06 stock purchase price = {purchase_price}")

sep_08_close_price = 198.80

sell_price = sep_08_close_price * gamestop_shares

print(f"\nChallenge 06 stock sale price = {sell_price}")

percent_change = ((sell_price - purchase_price)/purchase_price) * 100

print(f"\nChallenge 06 percent_change = {percent_change}")

fee = sell_price * .01

print(f"\nChallenge 06 fee = {fee}")

profit = sell_price - fee

print(f"\nChallenge 06 profit = {profit}")

# Bonus: profit formatted
# See https://www.w3schools.com/python/ref_string_format.asp
print(f"\nChallenge 06 profit formatted = ${profit:.2f}") # fixed point number format


## CHALLENGE 07

ny_times = """
No one knows how this ends. Some analysts say the intense activity could eventually prompt a wider
sell-off in the market by forcing hedge funds on the losing side of these trades to sell parts of
their portfolios to raise cash to cover their losses. While this speculative frenzy played out on
the market’s sidelines, the S&P 500 fell more than 2.5 percent on Wednesday, its worst day since
late October, as the Federal Reserve gave a glum assessment of the economy and before a number of
big tech companies announced their earnings.
"""

char_count = None

print(f"\nChallenge 07 (char count) = {char_count}")

chunks = None
chunk_count = None

print(f"\nChallenge 07 (chunk count) = {chunk_count}")

avg_chunk_size = None

print(f"\nChallenge 07 (avg chunk size) = {avg_chunk_size}")
