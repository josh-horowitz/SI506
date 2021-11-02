# SI 506 Lecture 10

# SETUP

scale = [('5 stars', 5), ('4 stars', 4), ('3 stars', 3), ('2 stars', 2), ('1 star', 1)]

cereals = [
    ['Apple Jacks', 'Kellogg Company', (5, 185), (4, 21), (3, 10), (2, 4), (1, 2)],
    ["Cap'n Crunch", 'Quaker Oats Company', (5, 49), (4, 5), (3, 3), (2, 1), (1, 1)],
    ["Cap'n Crunch's Crunch Berries", 'Quaker Oats Company', (5, 196), (4, 15), (3, 6), (2, 2), (1, 4)],
    ['Cheerios', 'General Mills', (5, 1310), (4, 95), (3, 14), (2, 11), (1, 28)],
    ['Cinnamon Toast Crunch', 'General Mills', (5, 577), (4, 46), (3, 10), (2, 5), (1, 19)],
    ['Cocoa Puffs', 'General Mills', (5, 147), (4, 9), (3, 1), (2, 2), (1, 5)],
    ['Corn Flakes', 'Kellogg Company', (5, 467), (4, 45), (3, 9), (2, 3), (1, 10)],
    ['Frosted Flakes', 'Kellog Company', (5, 1465), (4, 116), (3, 37), (2, 11), (1, 35)],
    ['Frosted Mini-Wheats', 'Kellogg Company', (5, 883), (4, 95), (3, 18), (2, 6), (1, 26)],
    ['Fruit Loops', 'Kellogg Company', (5, 750), (4, 84), (3, 14), (2, 6), (1, 8)],
    ['Fruity Pebbles', 'Post Consumer Brands', (5, 170), (4, 23), (3, 8), (2, 2), (1, 7)],
    ['Grape-Nuts', 'Post Consumer Brands', (5, 322), (4, 25), (3, 3), (2, 1), (1, 15)],
    ['Honey Bunches of Oats', 'Post Consumer Brands', (5, 95), (4, 7), (3, 3), (2, 1), (1, 2)],
    ['Honey Nut Cheerios', 'General Mills', (5, 814), (4, 64), (3, 22), (2, 8), (1, 22)],
    ['Lucky Charms', 'General Mills', (5, 388), (4, 38), (3, 12), (2, 3), (1, 7)],
    ['Raisin Bran', 'Kellogg Company', (5, 946), (4, 79), (3, 21), (2, 14), (1, 30)],
    ["Reese's Puffs", 'General Mills', (5, 184), (4, 14), (3, 10), (2, 4), (1, 3)],
    ['Rice Krispies', 'Kellogg Company', (5, 429), (4, 31), (3, 11), (2, 5), (1, 13)],
    ['Shredded Wheat', 'Post Consumer Brands', (5, 208), (4, 13), (3, 6), (2, 5), (1, 11)],
    ['Wheaties', 'General Mills', (5, 215), (4, 18), (3, 5), (2, 2), (1, 12)]
]

# 1.0 VARIABLE SCOPE

cereal = ('General Mills', 'Cocoa Puffs', 4.8, 164) # global scope

if cereal: # truth value
    cereal_exists = True # available globally

def format_name(cereal):
    name = f"{cereal[0]} {cereal[1]}" # local scope only
    return name

# TODO Uncomment
# print(f"\n1.0: Cereal exists = {cereal_exists}")

cereal_name = format_name(cereal) # call function

# TODO Uncomment
# print(f"\n1.0: Cereal name = {cereal_name}")

# TODO UNCOMMENT
# print(f"\n1.0: Local variable name = {name}") # NameError: name 'name' is not defined


# 2.0 CHALLENGES

# CHALLENGE 01: GET CEREAL BY NAME

def get_cereal(cereals, name):
    pass # TODO Implement


lucky_charms = None # TODO Call function

# print(f"\nChallenge 01: Lucky Charms = {lucky_charms}")


# CHALLENGE 02: GET CEREAL BY COMPANY

def get_cereal_by_company(cereals, company):
    pass # TODO Implement


post_data = None # TODO Call function

# TODO Uncomment
# print(f"\nChallenge 02: Post data")
# for cereal in post_data:
#     print(cereal)


# CHALLENGE 03: COUNT RATINGS

def count_ratings(ratings):
    pass # TODO Implement


frosted_flakes = None # TODO Call function
ratings_count = None # TODO Call function

# print(f"\nChallenge 03 {frosted_flakes[0]} total ratings = {ratings_count}")


# CHALLENGE 04: INSERT RATINGS COUNT

# TODO Implement for loop with range()

# TODO Uncomment
# print(f"\nChallenge 04 insert ratings count (first 4 cereals)\n")
# for cereal in cereals[:4]:
#     print(cereal)


# CHALLENGE 05 FAVORABLE RATINGS

def get_ratings(cereal):
    pass # TODO Implement

raisin_bran = None # TODO Call function
raisin_bran_ratings = None # TODO Call function
favorable_count = None # TODO Call function

# TODO Uncomment
# print(f"\nChallenge 05 {raisin_bran[0]} favorable count = {favorable_count}")


# CHALLENGE 06 FAVORITE CEREAL

def favorite_cereal(cereals, slice=slice(0, 2)):
    pass # TODO Implement


favorite = None # TODO Call function ( use default slice)

# TODO Uncomment
# print(f"\nChallenge 06: Favorite cereal: {favorite[0]} (n={favorite[1]})")


# CHALLENGE 07 REMOVE EXTREME RATINGS

def exclude_extreme_ratings(cereal):
    pass # TODO Implement


cereals_trimmed = []

# TODO Implement loop

# TODO Uncomment
# print(f"\nChallenge 07: cereal 3-star rankings")
# for cereal in cereals_trimmed:
#     print(cereal)

# TODO Call function
# favorite_trimmed = favorite_cereal(cereals_trimmed, slice(0, 4))

# TODO Uncomment
# print(f"\nChallenge 07: Favorite cereals trimmed: {favorite_trimmed[0]} (n={favorite_trimmed[1]})")


# CHALLENGE 08 (BONUS)

def calculate_weighted_mean(cereal):
    pass # TODO Implement


cereal = None # Call function
weighted_mean = None # Call function

# TODO Uncomment
# print(f"\nChallenge 08: {cereal[0]} rating {weighted_mean} (weighted mean)")

# TODO UNCOMMENT PRINT PLUS LOOP
# Print all weighted means
# print(f"\nChallenge 08: 1-5 star Cereal, Weighted mean, Total ratings\n")

# for cereal in cereals:
#     name = cereal[0]
#     weighted_mean = calculate_weighted_mean(cereal)
#     ratings = get_ratings(cereal)
#     count = count_ratings(ratings)

#     print(f"{name}, {weighted_mean} (n={count})")

# TODO Uncomment
# print(f"\nChallenge 08 1-5 star sorted: Cereal, Weighted mean, Total ratings\n")


# 8.1 LIST COMPREHENSIONS / SORTING WITH LAMBDAS (ANON FUNCTIONS)

# List comprehension
ratings = [
    (cereal[0], calculate_weighted_mean(cereal), count_ratings(get_ratings(cereal)))
    for cereal in cereals
    # for cereal in cereals if count_cereal_reviews(cereal) > 100
    ]


# Sort list using a lambda expression
# TODO Uncomment
# ratings.sort(key=lambda cereal: cereal[1], reverse=True) # sort by rating, reverse order

# TODO Uncomment
# for cereal in ratings:
#     print(f"{cereal[0]}, {cereal[1]} (n={cereal[2]})")


# TODO Uncomment
# print(f"\nChallenge 08 1-3 stars sorted: Cereal, Weighted mean, Total ratings\n")

# Exclude "extreme" ratings
# List comprehension
ratings = [
    (cereal[0], calculate_weighted_mean(cereal), count_ratings(get_ratings(cereal)))
    for cereal in cereals_trimmed
    # for cereal in cereals_trimmed if count_cereal_reviews(cereal) > 100
    ]

# Sort list using a lambda expression
ratings.sort(key=lambda cereal: cereal[1], reverse=True) # sort by rating, reverse order

# TODO Uncomment
# for cereal in ratings:
#     print(f"{cereal[0]}, {cereal[1]} (n={cereal[2]})")
