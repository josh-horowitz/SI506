import json
import requests


class Film:
    """TODO"""

    franchise = 'Star Wars' # class variable

    def __init__(self):
        """TODO"""

        pass # TODO Implement (including parameter list)

    def __str__(self):
        """TODO"""

        pass # TODO Implement

    def get_audience_positive_rating(self):
        """TODO"""

        pass # TODO Implement

    def jsonable(self):
        """TODO"""

        pass # TODO Implement


class AudienceRating:
    """TODO"""

    def __init__(self, title, positive_rating, five_star_avg_rating, num_ratings):
        """TODO"""

        self.title = title
        self.positive_rating = positive_rating
        self.five_star_avg_rating = five_star_avg_rating
        self.num_ratings = num_ratings

    def __str__(self):
        """TODO"""

        return f"{self.title} ({self.positive_rating} rating)"

    def jsonable(self):
        """TODO"""

        return {
            'title': self.title,
            'positive_rating': self.positive_rating,
            'five_star_avg_rating': self.five_star_avg_rating,
            'num_ratings': self.num_ratings
        }


def get_swapi_resource(url, params=None, timeout=10):
    """Returns a response object decoded into a dictionary. If query string < params > are
    provided the response object body is returned in the form on an "envelope" with the data
    payload of one or more SWAPI entities to be found in ['results'] list; otherwise, response
    object body is returned as a single dictionary representation of the SWAPI entity.

    Parameters:
        url (str): a url that specifies the resource.
        params (dict): optional dictionary of querystring arguments.
        timeout (int): timeout value in seconds

    Returns:
        dict: dictionary representation of the decoded JSON.
    """

    if params:
        return requests.get(url, params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        return json.load(file_obj)


def write_json(filepath, data, encoding='utf-8', ensure_ascii=False, indent=2):
    """Serializes object as JSON. Writes content to the provided filepath.

    Parameters:
        filepath (str): the path to the file
        data (dict)/(list): the data to be encoded as JSON and written to the file
        encoding (str): name of encoding used to encode the file
        ensure_ascii (str): if False non-ASCII characters are printed as is; otherwise
                            non-ASCII characters are escaped.
        indent (int): number of "pretty printed" indention spaces applied to encoded JSON

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        json.dump(data, file_obj, ensure_ascii=ensure_ascii, indent=indent)


def main():
    """TODO"""

    # Get films (ignore today)
    # endpoint = 'https://swapi.py4e.com/api'
    # films_data = get_swapi_resource(f"{endpoint}/films/")['results']


    # CHALLENGE 02

    # Get films (read file instead - quicker)
    films_data = None # TODO read file

    films = {}

    # TODO Implement loop

    # TODO Uncomment
    # print(f"\nChallenge 02: Films\n{films}")


    # CHALLENGE 03

    # Get ratings
    ratings_data = None # TODO read file

    audience_ratings = {}

    # TODO Implement loop

    # TODO Uncomment
    # print(f"\nAudience ratings\n{audience_ratings}")


    # CHALLENGE 04

    # Blend (add AudienceRating instances to each Film instance)

    # TODO Implement loop

    # Check
    # write_json('star_wars_audience_ratings.json', films['A New Hope'].jsonable())

    # JSON-friendly list
    writeable = []

    # TODO Implement loop

    # TODO Uncomment
    # Write to file
    # write_json('films_ratings.json', writeable)


    # CHALLENGE 05

    film_rankings = None # TODO convert dictionary values to list

    # BONUS: sort films by positive rating (descending)
    # film_rankings.sort(key=lambda film: film.audience_rating.positive_rating, reverse=True)

    # Alternative (built-in sorted() function)
    # film_rankings = sorted(
    #     film_rankings,
    #     key=lambda film: film.audience_rating.positive_rating,
    #     reverse=True
    #     )

    # TODO Uncomment
    # print(f"Audience ranking\n")
    # for film in film_rankings:
    #     print(f"{film.title} ({film.audience_rating.positive_rating} rating)")

    # Write to file
    writeable = []

    # TODO Implement loop

    # TODO Uncomment
    # Write to file
    # write_json('films_ranked.json', writeable)


if __name__ == '__main__':
    main()
