# SI 506 Lecture 15

import csv


def read_csv_to_dicts(filepath, encoding='utf-8', newline='', delimiter=','):
    """Accepts a file path, creates a file object, and returns a list of
    dictionaries that represent the row values using the cvs.DictReader().

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
        delimiter (str): delimiter that separates the row values

    Returns:
        list: nested dictionaries representing the file contents
     """

    with open(filepath, 'r', newline=newline, encoding=encoding) as file_obj:
        data = []
        reader = csv.DictReader(file_obj, delimiter=delimiter)
        for line in reader:
            data.append(line) # OrderedDict()
            # data.append(dict(line)) # convert OrderedDict() to dict

        return data


def write_dicts_to_csv(filepath, data, fieldnames, encoding='utf-8', newline=''):
    """
    Writes dictionary data to a target CSV file as row data using the csv.DictWriter().
    The passed in fieldnames list is used by the DictWriter() to determine the order
    in which each dictionary's key-value pairs are written to the row.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): dictionary content to be written to the target file
        fieldnames (seq): sequence specifing order in which key-value pairs are written to each row
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.DictWriter(file_obj, fieldnames=fieldnames)

        writer.writeheader() # first row
        writer.writerows(data)
        # for row in data:
        #     writer.writerow(row)


def main():
    """Program entry point.  Orchestrates program's flow of execution.

    Parameters:
        None

    Returns:
        None
    """

    # 1.0 DICTIONARY

    # A list
    film = [
        'The Wizard of Oz',
        1939,
        2800000,
        26100000,
        'The Wicked Witch of the West',
        'evil spells'
        ]

    # TODO Uncomment
    print(f"\n1.0 The Wizard of Oz list\n{film}")

    # A dictionary
    film = {
        'title': 'The Wizard of Oz',
        'year_released': 1939,
        'budget': 2800000,
        'box_office_receipts': 26100000,
        'scary_character_name': 'The Wicked Witch of the West',
        'scary_character_weapon': 'evil spells'
        }

    # TODO Uncomment
    print(f"\n1.1 The Wizard of Oz dictionary\n{film}")

    # Type
    # TODO Uncomment
    film_type = type(film) # <class 'dict'>

    # TODO Uncomment
    print(f"\n1.1 film obj type = {film_type}")


    # 2.0 CREATING A DICTIONARY

    # 2.1 EMPTY DICTIONARY

    # TODO Uncomment
    film = {} # empty dict
    film['title'] = 'Psycho'
    film['year_released'] = 1960
    film['budget'] = 806947
    film['box_office_receipts'] = 50000000
    film['scary_character'] = {} # nested dict
    film['scary_character']['name'] = 'Norman Bates'
    film['scary_character']['weapon'] = "chef's knife"

    print(f"\n2.1 Psycho = {film}")


    # 2.2 DICTIONARY LITERAL

    # TODO Uncomment
    film = {
        'title': 'Halloween',
        'year_released': 1978,
        'budget': 325000,
        'box_office_receipts': 70000000,
        'scary_character_name': 'Michael Myers',
        'scary_character_weapon': "chef's knife"
        }

    print(f"\n2.2 Halloween = {film}")


    # 2.3 BUILT-IN DICT() FUNCTION

    # TODO Uncomment
    # Pass in keyword arguments (note use of nested dict())
    film = dict(
        title='Friday the 13th',
        year_released=1980,
        budget=5500000,
        box_office_receipts=59800000,
        scary_character=dict(
            name='Jason Vorhees',
            weapon='machete'
        )
    )

    print(f"\n2.3.1 Friday the 13th (keyword args) = {film}")

    # TODO Uncomment
    # Pass in list of tuples (note used of nested dict())
    film = dict(
        [
            ('title', 'Friday the 13th'),
            ('year_released', 1980),
            ('budget', 5500000),
            ('box_office_receipts', 59800000),
            ('scary_character', dict(
                [
                    ('name', 'Jason Vorhees'),
                    ('weapon', 'machete')
                    ]
                )
            )
        ]
    )

    print(f"\n2.3.2 Friday the 13th (tuples) = {film}")


    # 3.0 ACCESSING, ADDING, MODIFYING, AND DELETING KEY-VALUE PAIRS

    # 3.1 ACCESSING VALUES

    film = {
        'title': 'A Nightmare on Elm Street',
        'year_released': 1984,
        'budget': 1800000,
        'box_office_receipts': 25500000,
        'scary_character_name': 'Freddy Krueger',
        'scary_character_weapon': 'clawed glove'
        }

    # Accessing a value
    film_title = film['title'] # TODO Assign value

    # TODO Uncomment (KeyError)
    # film_name = film['name'] # raises KeyError: 'name'

    # TODO Uncomment
    print(f"\n3.1.1 Film title = {film_title}")

    # Nested list of dictionaries
    film = {
        'title': 'A Nightmare on Elm Street',
        'year_released': 1984,
        'budget': 1800000,
        'box_office_receipts': 25500000,
        'scary_character': {
            'name': 'Freddy Krueger',
            'weapon': 'clawed glove'
            }
        }

    # Accessing a nested dictionary value
    scary_character_name = film['scary_character']['name'] # TODO Assign value

    print(f"\n3.1.2 Scary character name = {scary_character_name}")


    # 3.2 ADD, MODIFY, DELETE KEY-VALUE PAIRS

    film = {
        'title': 'The Shining',
        'year_released': 1980,
        'budget': 19000000,
        'box_office_receipts': 46200000,
        'scary_character': {
            'name': 'Jack Torrance',
            'weapon': 'axe'
            }
        }

    # Add key-value pairs
    film['director'] = 'Stanley Kubrick' # TODO assign
    film['screenplay_authors'] = [film['director'], 'Diane Johnson'] # TODO Assign
    film['stars'] = ['Jack Nicholson', 'Shelley Duvall', 'Scatman Crothers', 'Danny Lloyd']

    # TODO Uncomment
    print(f"\n3.2.1 New key-value pairs = {film}")

    # Modify existing key-value pair
    film['box_office_receipts'] = 47000000 # Assign value

    # TODO Uncomment
    print(f"\n3.2.2 Modified key-value pairs = {film}")

    # Delete key-value pair

    # TODO call built-in del() function
    del(film['stars'])

    # TODO Uncomment
    print(f"\n3.2.3 Remove stars = {film}")

    # Add nested key-value pair

    # TODO Add scary character's profession
    film['scary_character']['profession'] = 'writer'
    # TODO Uncomment
    print(f"\n3.2.4 Scary character profession = {film}")


    # 4.0 DICTIONARY METHODS

    # 4.1 DICT.GET()

    film = {
        'title': 'Scream',
        'year_released': 1996,
        'budget': 15000000,
        'box_office_receipts': 173000000,
        'scary_character_name': 'Ghostface',
        'scary_character_weapon': 'knife'
        }

    ghostface = film['scary_character_name'] # returns str

    # TODO Uncomment
    # ghostface = film['scary_character'] # triggers KeyError

    # TODO Uncomment
    # ghostface = film.get('scary_character', 'A scary character') # returns default value

    # ghostface = film.get('scary_character') # returns None

    ghostface = film.get('scary_character_name') # returns str

    print(f"\n4.1 Scary character = {ghostface}")


    # 4.2 DICT.KEYS()

    rating = {
        'title': 'The Wizard of Oz',
        'year_released': 1939,
        'tomatometer_percent_score': .98,
        'tomatometer_avg_rating': 9.50,
        'tomatometer_raters': 160,
        'audience_percent_score': .89,
        'audience_avg_rating': 4.30,
        'audience_raters': 250000
        }

    # TODO Uncomment
    print(f"\n4.2.1 dict_keys object = {type(rating.values())}") # dict_keys object

    # TODO Uncomment
    # Loop over dict_keys object
    # print(f"\n4.2.2 Wizard of Oz rating keys")
    # for key in rating.keys():
    #     print(key)

    # Convert dict_keys to a list
    rating_keys = list(rating.keys()) # TODO convert to a list

    # TODO Uncomment
    print(f"\n4.2.3 Wizard of Oz rating keys list\n{rating_keys}")

    # TODO Uncomment
    # Loop over list of keys; print associated values
    # print(f"\n4.2.4 Wizard of Oz rating values list")
    # for key in rating_keys:
    #     print(rating[key])


    # 4.3 DICT.VALUES()

    rating = {
        'title': 'Psycho',
        'year_released': 1960,
        'tomatometer_percent_score': .96,
        'tomatometer_avg_rating': 9.22,
        'tomatometer_raters': 101,
        'audience_percent_score': .95,
        'audience_avg_rating': 4.46,
        'audience_raters': 240145
        }

    # TODO Uncomment
    # print(f"\n4.3.1 dict_values object = {type(rating.values())}") # dict_values object

    # TODO Uncomment
    # Loop over dict_values object
    # print(f"\n4.3.2 Psycho rating keys")
    # for value in rating.values():
    #     print(value)

    # Convert to a list
    rating_values = list(rating.values()) # TODO convert to a list

    # TODO Uncomment
    print(f"\n4.3.3 Psycho values list\n{rating_values}")

    # TODO Uncomment
    # Print value types
    # print(f"\n4.3.4 Psycho value types")
    # for value in film.values():
    #     print(type(value))


    # 4.4 DICT.ITEMS()

    rating = {
        'title': 'Get Out',
        'year_released': 2017,
        'tomatometer_percent_score': .98,
        'tomatometer_avg_rating': 8.35,
        'tomatometer_raters': 386,
        'audience_percent_score': .86,
        'audience_avg_rating': 4.18,
        'audience_raters': 75450
        }

    # TODO Uncomment
    # print(f"\n4.4.0 dict_items object = {type(film.items())}")


    # Looping over a dictionary's items

    # TODO Loop over dict items


    # FORESHADOWING THE NEXT LECTURE

    filepath = './scary_films.csv'
    films = read_csv_to_dicts(filepath) # returns list of dictionaries

    # TODO Uncomment
    # print(f"\n4.4.1 Scary films (n=({len(films)})\n{films}")

    # dict.items()
    film_names = []

    # TODO Implement loop


    # TODO Uncomment
    # print(f"\n4.4.2 Scary film names (n=({len(film_names)})\n{film_names}")

    # Alternative dict.keys()

    # TODO Implement loop

    # TODO Uncomment
    # print(f"\n4.4.3 Scary film names (n=({len(film_names)})\n{film_names}")


if __name__ == '__main__':
    main()
