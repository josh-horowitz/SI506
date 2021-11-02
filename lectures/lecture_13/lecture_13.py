# SI 506 Lecture 15

import csv


def calculate_points(club):
    """Returns a club's points total based on the following equation:
    points = 3 points per win + 1 point per draw. A loss nets zero points.

    Parameters:
        club (list): representation of a club

    Returns
        int: league points earned
    """

    return club[5]*3 + club[6]



def clean_data(data, headers):
    """Converts numbers from strings to integers.

    Parameters
        data: list elements to clean

    Returns
        list: cleaned list
    """
    for standing in data:
        for item in standing:
            if standing.index(item) != headers.index('club') and standing.index(item) != headers.index('home'):
                data[data.index(standing)][standing.index(item)] = int(data[data.index(standing)][standing.index(item)])
    return data

def determine_place(standings, headers, club):
    """Updates league standings one club at a time. This function is designed to be called from
    inside a loop. Place is determined by total points. Ties are broken by 1) goals_diff, then if
    still tied by 2) goals scored. If tie remains unbroken, standings are deemed to occupy the same
    place in the standings. Last place club is appended to the standings list not inserted.

    Note: Ties are ignored in this version of the function.

    Parameters:
        standings (list): current standings
        headers (list): list of club attributes used to look up values
        club (dict): club to be inserted/appended to list

    Return:
        list: updated standings
    """

    standings_len = len(standings)
    i = 0
    for place in standings:
        points_idx = headers.index('points')
        if club[points_idx] > place[points_idx]:
            standings.insert(i, club)
            return standings
        elif club[points_idx] == place[points_idx]:
            # Note: goals for/against tie-breaking rules ignored
            standings.insert(i, club)
            return standings
        elif i == standings_len - 1:
            standings.append(club)
            return standings
        else:
            i += 1
            continue

    # Alternative: built-in enumerate function
    # standings_len = len(standings)
    # for i, place in enumerate(standings):
    #     points_idx = headers.index('points')
    #     if club[points_idx] > place[points_idx]:
    #         standings.insert(i, club)
    #         return standings
    #     elif club[points_idx] == place[points_idx]:
    #         # Note: goals for/against tie-breaking rules ignored
    #         standings.insert(i, club)
    #         return standings
    #     elif i == standings_len - 1:
    #         standings.append(club)
    #         return standings
    #     else:
    #         continue


def get_club_standings(standings, club_name):
    """Returns a Premier League club by its common name (e.g., Arsenal).
    The name check is case-insentive. If club is not matched None is
    returned.

    Parameters:
        standings (list): list of football standings
        club_name (str): club's common name

    Returns
        list: representation of a club
    """

    # TODO Implement
    for club in standings:
        if club_name.lower() == club[0].lower():
            return club


def get_region(club_info, club):
    """Return region associated with a club's home location. If match is not obtained
    None is returned.

    Parameters:
        club_info (list): football club general info
        club (list): representation of a football club

    Returns:
        str: English region name
    """

    # TODO Implement


def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list
    of lists, wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line
    of decoded text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read.
        encoding (str): name of encoding used to decode the file.
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences.
        delimiter (str): delimiter that separates the row values

    Returns:
        list: a list of nested "row" lists
    """

    with open(filepath, 'r', encoding=encoding, newline=newline) as file_obj:
        data = []
        reader = csv.reader(file_obj, delimiter=delimiter)
        for row in reader:
            data.append(row)

        return data


def write_csv(filepath, data, headers=None, encoding='utf-8', newline=''):
    """
    Writes data to a target CSV file. Column headers are written as the first
    row of the CSV file if optional headers are specified.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader. On platforms that utilize
    `\r\n` an extra `\r` will be added.

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): content to be written to the target file
        headers (seq): optional header row list or tuple.
        encoding (str): name of encoding used to decode the file.
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences.

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding, newline=newline) as file_obj:
        writer = csv.writer(file_obj)
        if headers:
            writer.writerow(headers)
            for row in data:
                writer.writerow(row)
        else:
            writer.writerows(data)


def main():
    """Program entry point.  Orchestrates program control flow. Generates English Priemer League
    club premier_league list as determined by total points earned. If tied for points break tie by
    comparing goal differential (for - against) and goals scored for the season.

    Parameters:
        None

    Returns:
        None
    """

    # 2.0 DOCSTRINGS

    # TODO uncomment
    # print(f"\n1.0 Print Docstring = {get_club_standings.__doc__}")

    # 3.0 CHALLENGES

    # CHALLENGE 01: SETUP AND CLEAN

    filepath = './english_premier_league-2020_21.csv'
    standings_data = read_csv(filepath, encoding='utf-8-sig') # TODO call function
    # premier_league = read_csv(filepath, encoding='utf-8-sig') # if byte order mark encountered

    # All strings
    # print(f"Challenge 01: raw data\n {standings_data}")

    # Get headers
    headers = standings_data[0] # TODO assign

    # Get cleaned club data
    standings = clean_data(standings_data[1:], headers) # TODO call function

    # Cleaned
    print(f"\nChallenge 01: data cleaned\n {standings}")


    # CHAllENGE 02: COMBINE DATA

    # Get Club info
    filepath = './english_clubs.csv'
    club_info_data = read_csv(filepath, encoding='utf-8-sig') # TODO call function

    # Get headers and info
    club_info_headers = club_info_data[0] # TODO assign
    club_info = club_info_data[1:] # TODO assign

    # Insert headers
    # TODO add header values
    headers.insert(2,'ground')
    headers.insert(3,'capacity')
    # Add values

    # TODO Implement loop
    for club in standings:
        for value in club_info:
            if value[club_info_headers.index('short_name')] == club[headers.index('club')]:
                club.insert(2, value[club_info_headers.index('ground')])
                club.insert(3, value[club_info_headers.index('capacity')])
    print(f"\nChallenge 02: add stadium and capacity\n {standings}")


    # CHALLENGE O3: IMPLEMENT GET_CLUB_STANDINGS

    liverpool = get_club_standings(standings, 'liverpool') # TODO call function

    print(f"\n2.1 Liverpool = {liverpool}")


    # CHALLENGE 04: IMPLEMENT CALCULATE_POINTS

    # Add Points "column" to header

    # TODO add header value
    headers.append('points')

    # Calculate points

    # TODO Implement loop
    for club in standings:
        club.append(calculate_points(club))

    # TEST: check Chelsea's points
    chelsea = get_club_standings(standings, 'chelsea') # TODO call function
    chelsea_points = chelsea[-1] # TODO assign

    print(f"\n3.0 Chelsea points = {chelsea_points}")


    # CHALLENGE 05: GET CLUBS BY REGION

    west_midlands_clubs = []

    # TODO Implement loop

    # print(f"\nChallenge 05: West Midland standings\n{west_midlands_clubs}")


    # 3.6 CHALLENGE 06 SORT standings BY POINTS

    # EPL = English Premier League

    # TODO Uncomment

    # epl_standings = []
    # for club in standings:
    #     if not epl_standings: # if empty (truth value)
    #         epl_standings.append(club) # add first club

    #     if club not in epl_standings: # first club already added so ignore
    #         epl_standings = determine_place(epl_standings, headers, club)

    # print(f"\n3.3 2020-2021 Standings\n")
    # for i, club in enumerate(epl_standings, 1):
    #     print(f"{str(i).zfill(2)}. {club[headers.index('club')]} ({club[headers.index('points')]} pts)")


if __name__ == '__main__':
    main()
