import csv
import copy
from os import write


#Problem 01
def read_csv(filepath, encoding='utf-8'):
    """
    This function reads in a csv and returns its contents as a list

    Parameters:
        filepath (str): A str representing the filepath for the file to be read
        encoding (str): A str representing the character encoding of the file

    Returns:
        (list): A list with the content of the file
    """
    with open(filepath, 'r', encoding=encoding) as file:
        data = []
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    return data

#Problem 02
def add_ratings(shows, ratings):
    """
    This function makes a copy of a show list and adds the shows IMDb rating to it

    Parameters:
        shows (list): A list of shows
        ratings (list): A list of IMDb ratings for the shows

    Returns:
        (list): A list of shows with the ratings added
    """
    shows_copy = copy.deepcopy(shows)
    shows_copy[0].append('IMDb Rating')
    for show in shows_copy[1:]:
        for rating in ratings[1:]:
            if show[shows[0].index('Title')].lower() == rating[ratings[0].index('Title')].lower():
                show.append(rating[1])

    return shows_copy

#Problem 03
def clean_show_data(shows):
    """
    This function cleans the data of a list of shows

    Parameters:
        shows (list): A list of shows

    Returns:
        (list): The list of shows with clean data
    """
    shows_copy = copy.deepcopy(shows)
    for show in shows_copy[1:]:
        for data in show:
            if show.index(data) == shows_copy[0].index('Creator(s)'):
                show.insert(show.index(data),data.split('/'))
                show.remove(data)
            elif show.index(data) == shows_copy[0].index('Genre(s)'):
                show.insert(show.index(data),data.split('/'))
                show.remove(data)
            elif show.index(data) == shows_copy[0].index('IMDb Rating'):
                show.insert(show.index(data), float(data))
                show.remove(data)
    return shows_copy
#Problem 04
def get_highest_rated_show(shows):
    highest_rated_show = []
    highest_rating = 0
    for show in shows[1:]:
        if show[shows[0].index('IMDb Rating')] > highest_rating:
            highest_rated_show = show
            highest_rating = show[shows[0].index('IMDb Rating')]

    return (highest_rated_show[shows[0].index('Title')],highest_rated_show[shows[0].index('Creator(s)')])
#Problem 05
def filter_by_genre(shows, genre):
    show_genre = []
    for show in shows:
        for data in show[shows[0].index('Genre(s)')]:
            if genre.lower() == data.lower():
                show_genre.append(show)
    return show_genre
#Problem 06
def stringify(shows):
    stringified_shows = copy.deepcopy(shows)
    for show in stringified_shows[1:]:
        for data in show:
            #print(data)
            if show.index(data) == stringified_shows[0].index('Creator(s)') or show.index(data) == stringified_shows[0].index('Genre(s)'):
                show.insert(show.index(data),"/".join(data))
                show.remove(data)
    return stringified_shows
#Problem 07
def write_csv(filepath, data):
    with open(filepath, 'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)
#Main function
def main():
    """
    This function serves as the main point of entry point of the program
    """
    #Problem 01
    netflix_data = read_csv('netflix_data.csv') #TODO: Replace
    disney_data = read_csv('disney_data.csv') #TODO: Replace
    netflix_ratings = read_csv('netflix_ratings.csv') #TODO: Replace
    disney_ratings = read_csv('disney_ratings.csv') #TODO: Replace

    #Problem 02
    netflix_data_with_ratings = add_ratings(netflix_data, netflix_ratings) #TODO: Replace
    disney_data_with_ratings = add_ratings(disney_data, disney_ratings) #TODO: Replace

    #Problem 03
    clean_netflix_data = clean_show_data(netflix_data_with_ratings)
    print(clean_netflix_data)
    clean_disney_data = clean_show_data(disney_data_with_ratings)
    #print(clean_disney_data)
    #Problem 04
    best_netflix_show = get_highest_rated_show(clean_netflix_data) #TODO: Replace
    best_disney_show = get_highest_rated_show(clean_disney_data) #TODO: Replace

    #Problem 05
    sci_fi_shows = []
    sci_fi_shows.append(clean_disney_data[0])
    sci_fi_shows.extend(filter_by_genre(clean_disney_data, 'Science Fiction'))
    sci_fi_shows.extend(filter_by_genre(clean_netflix_data, 'Science Fiction'))

    #Problem 06
    stringified_sci_fi_shows = stringify(sci_fi_shows)

    #Problem 07
    write_csv('sci_fi_shows.csv',stringified_sci_fi_shows)
    # WARN: if variables in the tuple below are not yet defined, initialize them to zero (0)
    return (netflix_data, disney_data, netflix_ratings, disney_ratings, netflix_data_with_ratings,
    disney_data_with_ratings, clean_netflix_data, clean_disney_data, best_netflix_show, best_disney_show
    )

#Do not delete
if __name__ == '__main__':
    main()
