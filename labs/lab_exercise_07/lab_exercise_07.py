# LAB EXERCISE 07
print('Lab Exercise 07 \n')

# SETUP
restaurants = [
    {'Name': 'Frita Batidos', 'Location': '117 W Washington St', 'Rating': 4.5, 'Reviews': 1871, 'Category': 'Burgers'},
    {'Name': "Zingerman's Delicatessen", 'Location': '422 Detroit St', 'Rating': 4.0, 'Reviews': 2224, 'Category': 'Delis'},
    {'Name': "Scorekeepers", 'Location': '310 Maynard St', 'Rating': 2.5, 'Reviews': 59, 'Category': 'Burgers'},
    {'Name': 'Rich Jc Korean Restaurant', 'Location': '1313 S University Ave', 'Rating': 4.0, 'Reviews': 183, 'Category': 'Korean'},
    {'Name': 'Tomukun Noodle Bar', 'Location': '505 E Liberty St Ste 200', 'Rating': 4.0, 'Reviews': 773, 'Category': 'Noodles'},
    {'Name': "Sava's", 'Location': '216 S State St', 'Rating': 4.0, 'Reviews': 1195, 'Category': 'American'},
    {'Name': "Krazy Jim's Blimpy Burger", 'Location': '304 S Ashley St', 'Rating': 3.5, 'Reviews': 231, 'Category': 'Burgers'},
    {'Name': "Joe's Pizza", 'Location': '1107 S University Ave', 'Rating': 4.5, 'Reviews': 107, 'Category': 'Pizza'},
    {'Name': 'Hola Seoul', 'Location': '715 N University Ave', 'Rating': 4.0, 'Reviews': 98, 'Category': 'Korean'},
    {'Name': 'The Chop House', 'Location': '322 S Main St', 'Rating': 4.0, 'Reviews': 448, 'Category': 'Steakhouses'},
    {'Name': 'TK Wu', 'Location': '510 E Liberty St', 'Rating': 3.5, 'Reviews': 236, 'Category': 'Chinese'},
    {'Name': 'HopCat', 'Location': '311 Maynard St', 'Rating': 3.5, 'Reviews': 397, 'Category': 'Burgers'},
    {'Name': 'Lan City Noodle Bar', 'Location': '1235 S University Ave', 'Rating': 4.0, 'Reviews': 5, 'Category': 'Chinese'},
    {'Name': 'First Bite', 'Location': '108 S Main St', 'Rating': 5.0, 'Reviews': 104, 'Category': 'Burgers'}
]

# END SETUP

# Problem 01 (3 points)
def get_restaurants(restaurants,category=None):
    """
    This function takes a list of dictionaries as an argument and returns a list of strings that includes restaurants' names

    Parameters:
        restaurants (list): A list of dictionaries, each representing a restaurant
        category (list): A list of strings containing different categories of restaurants

    Returns:
        restaurants_names (list): A list containing the restaurants' names
    """
    return_value = []
    for restaurant in restaurants:
        if category == None:
            return_value.append(restaurant['Name'])
        else:
            if restaurant['Category'] in category:
                return_value.append(restaurant['Name'])
    return return_value

# Problem 02 (4 points)
def get_most_reviewed_restaurant(restaurants):
    """
    This function takes a list of dictionaries as an argument and returns a dictionary with the restaurant's name as value to the key 'Name' and the number of reviews as value to the key 'Reviews'

    Parameters:
        restaurants (list): A list of dictionaries, each representing a restaurant

    Returns:
        most_reviewed_restaurant (dict): A dictionary containing the restaurant's name and the number of reviews
    """
    most_reviewed = {}
    for restaurant in restaurants:
        if not most_reviewed:
            most_reviewed = restaurant
        else:
            if most_reviewed['Reviews'] < restaurant['Reviews']:
                most_reviewed = restaurant
    return {'Name': most_reviewed['Name'], 'Reviews': most_reviewed['Reviews']}


# Problem 03 (4 points)
def get_high_rating_restaurants(restaurants, category):
    rating_list = {}
    for restaurant in restaurants:
        rating = restaurant['Rating']
        if restaurant['Category'] in category and rating >= 3.5:
            if rating >= 3.5:
                rating_list[restaurant['Name']] = rating
    return rating_list

# Problem 04 (4 points)
def get_avg_rating(high_rating_restaurants):
    values_list = high_rating_restaurants.values()
    print(type(high_rating_restaurants.values()))
    value_total = 0
    for value in values_list:
        value_total += value
    return value_total/len(values_list)

# Problem 05 (5 points)
def write_txt(filepath, dict_list):
   with open(filepath, 'w') as txt_file:
        for item in dict_list:
            item_list = list(item.items())
            txt_file.write(f"{item_list[0:3]}\n")

# Call functions below
def main():
    """
    This function serves as the point of entry and controls the flow of this Python script

    Parameters:
        None

    Returns:
        None
    """

    # Problem 01
    print("Problem 01:\n")
    korean_restaurants = get_restaurants(restaurants, ['Korean'])
    print(korean_restaurants)

    # Problem 02
    print("Problem 02:\n")
    most_reviewed_restaurant = get_most_reviewed_restaurant(restaurants)
    print(most_reviewed_restaurant)

    # Problem 03
    print('Problem 03:\n')
    categories = ['Burgers', 'Chinese']
    high_rating_restaurants = get_high_rating_restaurants(restaurants,categories)
    print(high_rating_restaurants)

    # Problem 04
    print('Problem 04: \n')
    avg_rating = get_avg_rating(high_rating_restaurants)
    print(avg_rating)

    # Problem 05
    write_txt('restaurants_info.txt', restaurants)

if __name__ == "__main__":
    main()