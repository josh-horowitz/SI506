# SI 506 Lecture 19

import json
import requests

class Person:
    """Representation of a person.

    Attributes:
        url (str): uniform resource locator
        name (str): person name
        birth_year (str): person's birth_year
        force_sensitive (bool): ability to harness the power of the Force
        homeworld (Planet): person's home planet

    Methods:
        get_homeworld: retrieve home planet
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, birth_year, force_sensitive=False):
        """Initialize Person instance.

        Parameters:
            url (str): uniform resource locator
            name (str): person name
            birth_year (str): person's birth_year
            force_sensitive (bool): ability to harness the power of the Force

        Returns:
           Person: person instance
        """

        pass # TODO Implement

    def __str__(self):
        """Return a string representation of the object."""

        pass # TODO implement


    def get_age(self, current_era, current_year):
        """Returns age of person in relation to the passed in current era
        (BBY or ABY only) and year. The BBY era (Before the Battle of Yavin) is
        a retrospective calendar and the integer values denoting the
        years are listed continuously in reverse order from largest to smallest
        as each relates to battle (0 BBY). The ABY era (After the Battle of Yavin)
        commences in the year following the battle and the integer values
        denoting the years are ordered continuously from smallest to largest.

        Parameters:
            current_era (str): the era which is considered current
            current_year (int): the year which is consider current

        Returns:
            int: age of person measured in years. If age cannot be determined
                 None is returned

        """

        birth_era = self.birth_year[-3:]
        birth_year = int(self.birth_year[:-3]) # cast to int

        if current_era == 'ABY' and birth_era == 'ABY' and current_year >= birth_year:
            return current_year - birth_year # ABY era only
        elif current_era == 'ABY' and birth_era == 'BBY':
            return current_year + birth_year # spans both eras
        elif current_era == 'BBY' and birth_era == 'BBY' and birth_year >= current_year:
            return birth_year - current_year # BBY era only
        else:
            return None # Treat as unknown rather than trigger ValueError


    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal
        rather than built-in dict() to avoid built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and mutated, adding,
        modifying or removing instance attributes as a result.

        return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        pass # TODO implment


class Planet:
    """Representation of a planet.

    Attributes:
        url: uniform resource locator
        name: planet name
        gravity: gravity level
        climate: climate description
        terrain: terrain description
        population: population size

    Methods:
        jsonable: return JSON-friendly dict representation of the object
    """

    def __init__(self, url, name, gravity, climate, terrain, population):
        """Initialize Planet instance."""

        self.url = url
        self.name = name
        self.gravity = gravity
        self.climate = climate
        self.terrain = terrain
        self.population = population

    def __str__(self):
        """Return a string representation of the object."""

        return self.name

    def jsonable(self):
        """Return a JSON-friendly representation of the object. Use a dictionary literal
        rather than built-in dict() to avoid built-in lookup costs.

        Do not simply return self.__dict__. It can be intercepted and mutated, adding,
        modifying or removing instance attributes as a result.

        return self.__dict__ # DANGEROUS
        # return copy.deepcopy(self.__dict__) # safe but slow

        Parameters:
            None

        Returns:
            dict: dictionary of the object's instance variables
        """

        return {
                'url': self.url,
                'name': self.name,
                'gravity': self.gravity,
                'climate': self.climate,
                'terrain': self.terrain,
                'population': self.population
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
    """Entry point for program. Orchestrates workflow involving
    reading in local data, issuing GET requests to retrieve remote data,
    instantiating class instances, and writing out data as JSON to a file.

    Parameters:
        None

    Returns:
        None
    """

    endpoint = 'https://swapi.py4e.com/api'

    # 3.0 CLASS INSTANTIATION

    # Get Yoda data
    swapi_yoda = None # TODO Get Yoda representation from SWAPI

    # Instantiate Person
    yoda = None # TODO instantiate Person object

    # TODO uncomment
    # print(f"\nYoda instance = {yoda}") # reads yoda.__str__

    # Get first 10 people from SWAPI
    people = []
    swapi_people = None # Get first 10 people records from SWAPI

    # Append Person instances to list

    # TODO Implement loop

    # TODO Uncomment
    # print(f"\n3.1 People (obj identifiers)\n{people}") # list of opaque object identifiers printed to screen


    # 4.0 DUNDER __STR__

    # TODO Uncomment
    # print(f"\n4.0 Person instance human-friendly (str) = {yoda}")

    # print(f"\n4.0 People instances human-friendly (str)\n")
    # for person in people:
    #     print(person) # person.__str__ printed


    # 5.0 ACCESS INSTANCE VARIABLE VALUES

    birth_year = None # TODO get value
    is_force_sensitive = None # TODO get value

    # print(f"\n5.0 Yoda's birth year = {birth_year}")
    # print(f"\n5.0 Yoda Force-sensitive? = {is_force_sensitive}")


    # 6.0 INSTANCE METHODS (GET_AGE)

    date = '19BBY' # Year of Luke Skywalker's birth
    age = None # TODO Get Yoda's age

    # TODO uncomment
    # print(f"\n6.1 Yoda's age (at Luke Skywalker's birth) = {age}")

    # Year of Yoda's "death" at his home on the planet Dabogah
    # Source: https://starwars.fandom.com/wiki/Yoda

    date = '4ABY'
    age = None # TODO Get Yoda's age

    # TODO uncomment
    # print(f"\n6.1 Yoda's age (at 'death') = {age}")


    # 7.0 CONVERT INSTANCE TO A JSON-FRIENDLY DICTIONARY

    # TRIGGER TYPE_ERROR EXCEPTION
    # TypeError: Object of type Person is not JSON serializable
    # write_json('yoda.json', yoda)

    # TODO REPLACE None
    # write_json('yoda.json', None)

    # 8.0 COMPOSITION

    swapi_dagobah = None # TODO get Dagobah

    # TODO Uncomment
    # Assign Planet instance
    # yoda.homeworld = Planet(
    #     swapi_dagobah.get('url'),
    #     swapi_dagobah.get('name'),
    #     swapi_dagobah.get('gravity'),
    #     swapi_dagobah.get('climate'),
    #     swapi_dagobah.get('terrain'),
    #     swapi_dagobah.get('population')
    # )

    # TODO Uncomment
    # TRIGGER TYPE ERROR EXCEPTION
    # TypeError: Object of type Planet is not JSON serializable
    # write_json('yoda.json', yoda.jsonable())

    # TODO Uncomment
    # REFACTOR PERSON.JSONABLE()
    # write_json('yoda.json', yoda.jsonable())


if __name__ == '__main__':
    main()
