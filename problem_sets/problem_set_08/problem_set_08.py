import json, requests, copy
from os import write


# Problem 01
def read_json(filepath, encoding='utf-8'):
    """Reads a JSON document, decodes the file content, and returns a list or
    dictionary if provided with a valid filepath.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file

    Returns:
        dict/list: dict or list representations of the decoded JSON document
    """

    with open(filepath, 'r', encoding=encoding) as file:
        return json.load(file)


# Problem 02
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
        return requests.get(url, params=params, timeout=timeout).json()
    else:
        return requests.get(url, timeout=timeout).json()


# Problem 03
def delete_items(dictionary, key_list):
    dict_copy = copy.deepcopy(dictionary)
    for key in key_list:
        if key in dict_copy.keys():
            del(dict_copy[key])
    return dict_copy

# Problem 04
def get_homeworld(person, key_list=None):
    homeworld = get_swapi_resource(person['homeworld'])

    if key_list:
        subset = {}
        for key in key_list:
            if key in homeworld.keys():
                subset[key] = homeworld[key]
        return subset
    else:
        return homeworld

def get_species(person, key_list=None):
    person_species = person['species']
    dictionary = {}
    if person_species:
        species = get_swapi_resource(person_species[0])
        if key_list:
            for key in key_list:
                if key in species.keys():
                    dictionary[key] = species[key]
            return dictionary
        return species
    else:
        return dictionary

# Problem 05
def clean_person_dictionary(person, delete_list, home_list=None, species_list=None):
    updated_person = delete_items(person, delete_list)
    updated_person['homeworld'] = get_homeworld(updated_person, home_list)
    updated_person['species'] = get_species(updated_person, species_list)
    return updated_person

# Problem 06
def board_ship(ship, passengers):
    ship_copy = copy.deepcopy(ship)
    boarding_list = []
    for i in range(len(passengers)):
        for passenger in passengers:
            if passenger['boarding_order'] == i+1:
                boarding_list.append(passenger)
                break
    ship_copy['passengers'] = boarding_list
    return ship_copy

# Problem 07
def write_json(filepath, data, encoding='utf-8', ensure_ascii='False', indent=2):
    with open(filepath, 'w', encoding=encoding) as file:
        json.dump(data, file, ensure_ascii=ensure_ascii, indent=indent)


def main():
    """Program entry point."""

    # Problem 01
    passengers = read_json('passengers.json')['passengers']

    print(f'\nProblem 01:\n{passengers}')

    # Problem 02
    base_url = 'https://swapi.py4e.com/api'
    falcon_params = {'search': 'falcon'}
    falcon = get_swapi_resource(f'{base_url}/starships', falcon_params)['results'][0]

    print(f'\nProblem 02:\n{falcon}')

    # Problem 03
    falcon_keys_delete = list(falcon.keys())[-5:]
    falcon_updated = delete_items(falcon, falcon_keys_delete)
    print(f'Updated Falcon: {falcon_updated}')

    # Problem 04
    bail_home = get_homeworld(get_swapi_resource(f'{base_url}/people', {'search': 'Bail Organa'})['results'][0])
    home_keys_keep = list(bail_home.keys())[:9]
    bail_species = get_species(get_swapi_resource(f'{base_url}/people', {'search': 'Bail Organa'})['results'][0])

    # Problem 05
    for passenger in passengers:
        person = get_swapi_resource(f'{base_url}/people', {'search': passenger['name']})['results'][0]
        passenger.update(clean_person_dictionary(person, ['films', 'vehicles', 'starships', 'created', 'edited', 'url'], home_keys_keep, ['name']))

    # Problem 06
    all_aboard = board_ship(falcon_updated, passengers)
    print(all_aboard)

    # Problem 07
    leaving_tatooine = 'hyperspace_jump.json'
    write_json(data=all_aboard, filepath=leaving_tatooine)


if __name__ == '__main__':
    main()
