# SI 506 Lecture 18

import csv
import json
import requests


def drop_data(entity, keys):
    """Deletes < entity > dictionary key-values pairs if a key matches a key
    in the passed in keys tuple.

    Parameters:
        entity (dict): dictionary with key-value pairs to drop (i.e., delete)

    Returns:
        dict: dictionary with matching key-value pairs removed
    """

    pass # TODO Implement


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
    """Program entry point."""

    endpoint = 'https://swapi.py4e.com/api'

    # 4.1 CHALLENGE 01: GET CHEWIE PLUS HOMEWORLD AND SPECIES DATA

    response = None # TODO call function

    # print(f"\nChallenge 01: Response\n{response}")

    chewie = None # TODO get first element

    # print(f"\nChallenge 01: Chewbacca\n{chewie}")

    # Write to file
    # TODO Uncomment
    # write_json('chewie.json', chewie)

    # Add homeworld
    # chewie['homeworld'] = None # TODO call function

    # Add species

    # TODO check truth value; get species

    # print(f"\nChallenge 01: Chewbacca enriched\n{chewie}")

    # Write to file
    # TODO Uncomment
    # write_json('chewie_enriched.json', chewie)


    # 4.2 CHALLENGE 02 DROP_DATA()

    drop_keys = ('films', 'created', 'edited', 'people', 'residents', 'starships', 'vehicles')

    x_wing = None # TODO get T-65 X-wing
    x_wing = None # TODO call function, delete key-value pairs

    # print(f"\nChallenge 02: T-65 X-wing\n{x_wing}")

    # Write to file
    # TODO Uncomment
    # write_json('x_wing.json', x_wing)


    # 4.3 CHALLENGE 03 COMBINE DATA

    wookiee_starships = None # read file
    wookiee_x_wing = None # TODO access T-65 X-wing

    # Combine data

    # TODO update x_wing with wookiee_x_wing

    # TODO Uncomment
    # write_json('x_wing_enriched.json', x_wing)


    # 4.4 CHALLENGE 04

    # TODO Implment loop

    # WARN: elements are not updated using a simple for loop
    # for element in x_wing['pilots']:
    #     pilot = get_swapi_resource(element)
    #     element = drop_data(pilot, drop_keys) # does not update value

    # Write to file
    # TODO Uncomment
    # write_json('x_wing_pilots.json', x_wing)


    # 4.5 CHALLENGE 05

    x_wing = None # TODO call function, one-item tuple

    # Get Luke Skywalker
    luke = None # TODO call function
    luke = None # TODO call function

    homeworld = None # TODO call function

    # TODO call function, assign value to luke dict

    # TODO check species, assign value to luke dict

    # Get R2-D2 (Astromech droid)

    # Repeat above for R2-D2
    r2 = None
    r2 = None

    # TODO create crew members dictionary; assign to x-wing


    # Write to file
    # TODO Uncomment
    # write_json('x_wing_crew.json', x_wing)


if __name__ == '__main__':
    main()
