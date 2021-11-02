# SI 506 Lecture 14

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
        data (list): list elements to clean
        headers (list): "header" values used to look up an index value

    Returns
        list: cleaned list
    """

    # Attempting to recast a string that is not a number will trigger a runtime
    # ValueError exception
    # Example: ValueError: invalid literal for int() with base 10: 'Arsenal'

    # try/except blocks implement the Python EAFP principle
    # Easier to ask for forgiveness than permission

    # This contrasts with the LBYL principle: Look before you leap, a coding style
    # that explicitly tests for pre-conditions (e.g., if x:)

    for row in data:
        for i in range(len(row)):
            try:
                row[i] = int(row[i]) # working with str; assign to element[x] not loop variable
            except ValueError:
                continue

    # Nested loop
    # for row in data:
    #     for i in range(len(row)):
    #         if i == headers.index('club') or i == headers.index('home'):
    #             continue
    #         else:
    #             row[i] = int(row[i])

    # Lookup header values
    # for row in data:
    #     row[headers.index('played')] = int(row[headers.index('played')])
    #     row[headers.index('win')] = int(row[headers.index('win')])
    #     row[headers.index('draw')] = int(row[headers.index('draw')])
    #     row[headers.index('loss')] = int(row[headers.index('loss')])
    #     row[headers.index('goals_for')] = int(row[headers.index('goals_for')])
    #     row[headers.index('goals_against')] = int(row[headers.index('goals_against')])

    # Conventional approach: hard-coded index values
    # for row in data:
    #     row[2] = int(row[2])
    #     row[3] = int(row[3])
    #     row[4] = int(row[4])
    #     row[5] = int(row[5])
    #     row[6] = int(row[6])
    #     row[7] = int(row[7])

    return data


def determine_place(standings, headers, club):
    """Updates league standings one club at a time. This function is designed to be called from
    inside a loop. Place is determined by total points.

    Ties are broken according to the following criteria:
    1. team with higher goals difference (GD) is ranked above team with same points but lower GD.
    2. if GD test fails to break tie then team with higher goals for (GF) is ranked above
       team with lower goals for total.

    If above criteria fail to break the tie, the tied teams are considered to occupy the same
    position in the standings.

    Two additional criteria are employed to break Premier League ties in the standings table.
    3. Points won in head-to-head meetings
    4. Away goals in head-to-head meetings

    Since we don't have meeting data these rules are ignored.

    Parameters:
        standings (list): current standings
        club (dict): club to be inserted/appended to list

    Return:
        list: updated standings
    """

    # Built-in enumerate function
    standings_len = len(standings)
    for i, place in enumerate(standings):
        club_points = calculate_points(club)
        place_points = calculate_points(place)
        goals_for_idx = headers.index('goals_for')
        goals_against_idx = headers.index('goals_against')
        if club_points > place_points:
            standings.insert(i, club)
            return standings
        elif club_points == place_points:
            club_diff = club[goals_for_idx] - club[goals_against_idx]
            place_diff = place[goals_for_idx] - place[goals_against_idx]
            if club_diff > place_diff:
                standings.insert(i, club)
                return standings
            elif club_diff == place_diff and club[goals_for_idx] > place[goals_for_idx]:
                standings.insert(i, club)
                return standings
            else:
                standings.insert(i + 1, club) # insert after
                return standings
        elif i == standings_len - 1:
            standings.append(club)
            return standings
        else:
            continue

    # Alternative (counter)
    # standings_len = len(standings)
    # i = 0
    # for place in standings:
    #     club_points = calculate_points(club)
    #     place_points = calculate_points(place)
    #     goals_for_idx = headers.index('goals_for')
    #     goals_against_idx = headers.index('goals_against')
    #     if club_points > place_points:
    #         standings.insert(i, club)
    #         return standings
    #     elif club_points == place_points:
    #         club_diff = club[goals_for_idx] - club[goals_against_idx]
    #         place_diff = place[goals_for_idx] - place[goals_against_idx]
    #         if club_diff > place_diff:
    #             standings.insert(i, club)
    #             return standings
    #         elif club_diff == place_diff and club[goals_for_idx] > place[goals_for_idx]:
    #             standings.insert(i, club)
    #             return standings
    #         else:
    #             standings.insert(i + 1, club) # insert after
    #             return standings
    #     elif i == standings_len - 1:
    #         standings.append(club)
    #         return standings
    #     else:
    #         i += 1
    #         continue


def get_club_by_nickname(club_info, headers, nickname):
    """Returns a list of clubs known by the passed in nickname. Certain clubs share
    nicknames; typically former nicknames coined during the nineteenth and early
    twentieth centuries.

    Parameters:
        club_info (list): football club general info
        headers (list): "header" values used to look up an index value
        nickname (str): nickname to match on

    Returns:
        list: one or more official club names; if list is empty return None
    """
    club_names = []
    for club in club_info:
        club_nicknames = club[headers.index('nicknames')].split(', ')
        for name in club_nicknames:
            if name.lower() == nickname.lower():
                club_names.append(club[0])

    return club_names


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

    for club in standings:
        if club[0].lower() == club_name.lower():
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

    for item in club_info:
        if item[1] == club[0]:
            return item[4]


def read_csv(filepath, encoding='utf-8', newline='', delimiter=','):
    """
    Reads a CSV file, parsing row values per the provided delimiter. Returns a list
    of lists, wherein each nested list represents a single row from the input file.

    WARN: If a byte order mark (BOM) is encountered at the beginning of the first line
    of decoded text, call < read_csv > and pass 'utf-8-sig' as the < encoding > argument.

    WARN: If newline='' is not specified, newlines '\n' or '\r\n' embedded inside quoted
    fields may not be interpreted correctly by the csv.reader.

    Parameters:
        filepath (str): The location of the file to read
        encoding (str): name of encoding used to decode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences
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


def read_file(filepath, encoding='utf-8', strip=True):
    """Read text file line by line. Remove whitespace and trailing newline
    escape character.

    Parameters:
        filepath (str): path to file
        encoding (str): name of encoding used to decode the file.
        strip (bool): remove white space, newline escape characters

    Returns
        list: list of lines in file
    """

    with open(filepath, 'r', encoding=encoding) as file_obj:
        if strip:
            data = []
            for line in file_obj:
                # data.append(line) # includes trailing newline '\n'
                data.append(line.strip()) # strip leading/trailing whitespace including '\n'
            return data

            # return [line.strip() for line in file_obj] # list comprehension (single line)
        else:
            return file_obj.readlines() # list


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
        headers (seq): optional header row list or tuple
        encoding (str): name of encoding used to encode the file
        newline (str): specifies replacement value for newline '\n'
                       or '\r\n' (Windows) character sequences

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


def write_file(filepath, data, encoding='utf-8', newline=True):
    """Write content to a target file encoded as UTF-8. If optional newline is specified
    append each line with a newline escape sequence (`\n`).

    Parameters:
        filepath (str): path to target file (if file does not exist it will be created)
        data (list): list of strings comprising the content to be written to the target file
        encoding (str): name of encoding used to encode the file.
        newline (bool): add newline escape sequence to line

    Returns:
        None
    """

    with open(filepath, 'w', encoding=encoding) as file_obj:
        if newline:
            for line in data:
                file_obj.write(f"{line}\n") # add newline
        else:
            file_obj.writelines(data) # write sequence to file


def main():
    """Program entry point.  Orchestrates program control flow. Generates English Priemer League
    club premier_league list as determined by total points earned. If tied for points break tie by
    comparing goal differential (for - against) and goals scored for the season.

    Parameters:
        None

    Returns:
        None
    """

    # 1.0 TRUTH VALUES

    club_names = [] # falsy
    if club_names: # evaluates to False
        print(f"\nclub_names list has {len(club_names)} elements.") # not called
    else:
        print('\nclub_names list is empty.')

    club_names = ['Arsenal', 'Aston Villa'] # truthy
    if club_names: # evaluates to True
        print(f"\nclub_names list has {len(club_names)} elements.") # called
    else:
        print('\nclub_names list is empty.')

    print('\n') # padding

    # Boolean operation (not)
    # Select favorite "Big Six" club (user-supplied input). Run while loop
    # until condition evaluates to False.
    big_six_clubs = (
        'arsenal',
        'chelsea',
        'liverpool',
        'manchester city',
        'manchester united',
        'tottenham'
        )
    prompt = '\nWhich big six club is your favorite?: '

    # TODO: uncomment to prompt user to enter a big six team name
    # matched = False
    # while not matched:
    #     club = input(prompt)
    #     if club.lower() in big_six_clubs:
    #         print(f"\nThanks. I like {club.capitalize()} too.\n\nFinis.\n")
    #         matched = True

    # 2.0 CHALLENGES

    # SETUP

    filepath = './english_premier_league-2020_21.csv'
    standings_data = read_csv(filepath)
    # premier_league = read_csv(filepath, encoding='utf-8-sig') # if byte order mark encountered

    # All strings
    print(f"Raw data (excerpt)\n{standings_data[:4]}")

    # Get headers
    headers = standings_data[0]

    # Get cleaned club data
    standings = clean_data(standings_data[1:], headers)

    # Cleaned
    print(f"\nData cleaned (excerpt)\n{standings[:3]}")


    # COMBINE DATA

    # Get Club info
    filepath = './english_clubs.csv'
    club_info_data = read_csv(filepath)

    # Get headers and info
    club_info_headers = club_info_data[0]
    club_info = club_info_data[1:]

    # Insert headers
    headers.insert(2, 'ground')
    headers.insert(3, 'capacity')

    # Add values
    for club in standings:
        for info in club_info:
            if club[headers.index('club')].lower() == info[club_info_headers.index('short_name')].lower():
                club.insert(2, info[club_info_headers.index('ground')])
                club.insert(3, int(info[club_info_headers.index('capacity')])) # recast
                break

    print(f"\nAdd stadium and capacity (excerpt)\n{standings[:3]}")


    # IMPLEMENT GET_CLUB_STANDINGS

    liverpool = get_club_standings(standings, 'liverpool')

    print(f"\nLiverpool club record = {liverpool}")

    # CHALLENGES

    # CHALLENGE 01: IMPLEMENT CALCULATE_POINTS

    # Add Points "column" to header

    # TODO append 'points' to headers
    headers.append('points')

    # Calculate points

    for club in standings:
        club.append(calculate_points(club))

    print(f"\nChallenge 01: Add club points (excerpt)\n{standings[:3]}")

    # TEST: check Chelsea's points
    chelsea = get_club_standings(standings, 'Chelsea') # TODO call function
    chelsea_points = chelsea[-1] # TODO lookup points

    print(f"\nChallenge 01: Chelsea points = {chelsea_points}")


    # CHALLENGE 02: GET CLUBS BY REGION

    west_midlands_clubs = []

    for club in standings:
        region = get_region(club_info, club)
        if region == 'West Midlands':
            west_midlands_clubs.append(club[headers.index('club')])

    print(f"\nChallenge 02: West Midland standings\n{west_midlands_clubs}")


    # CHALLENGE 03: GET CLUB BY NICKNAME

    # Get club or clubs known as "The Toffees"
    toffees = get_club_by_nickname(club_info_data, club_info_headers, 'The Toffees') # TODO call function

    print(f"\nChallenge 03: The Toffees = {toffees}")

    # Get club or clubs known as "The Blues"
    blues = get_club_by_nickname(club_info_data,club_info_headers,'The Blues') # TODO call function

    print(f"\nChallenge 03: The Blues = {blues}")


    # CHALLENGE 04: GET CLUB WITH SMALLEST GROUNDS (i.e., STADIUM)

    club_min_capacity = None # TODO assign value
    min_capacity = None # TODO assign value

    # TODO implement loop

    # print(f"\nChallenge 04: Smallest stadium = {club_min_capacity}")


    # CHALLENGE 05: GET REGION CLUB COUNTS

    filepath = './english_regions.txt'
    english_regions = read_file(filepath)

    region_counts = []

    # TODO implement loop

    filepath = './english_regions_club_count.csv'

    # TODO Uncomment
    # write_csv(filepath, region_counts, ['region', 'club_count'])


    # CHALLENGE 06 (BONUS): GET RELEGATED CLUBS (BOTTOM 3 CLUBS)

    # Get the points (do not remove dups, clubs could be tied with low points)

    # TODO Uncomment

    # club_points = []
    # for club in standings:
    #     club_points.append(club[headers.index('points')])

    # club_points = [club[headers.index('points')] for club in standings] # list comprehension

    # Sort ascending

    # TODO Uncomment
    # club_points.sort()

    # Loop over slice of relegated_points to control the order of the relegated clubs

    # TODO Uncomment
    # relegated_clubs = []
    # for num in club_points[:3]:
    #     for club in standings:
    #         if club[headers.index('points')] == num:
    #             relegated_clubs.append(f"{club[headers.index('club')]}, ({club[headers.index('points')]} pts)")


    # print(f"\nChallenge 06: Relegated clubs\n{relegated_clubs}")


    # 3.6 CHALLENGE 07 (BONUS): SORT STANDINGS BY POINTS (BREAK TIES)

    # TODO Uncomment

    # EPL = English Premier League
    # epl_standings = []
    # for club in standings:
    #     if not epl_standings: # if empty (truth value)
    #         epl_standings.append(club) # add first club

    #     if club not in epl_standings: # first club already added so ignore
    #         epl_standings = determine_place(epl_standings, headers, club)

    # print(f"\nChallenge 07: 2020-2021 Standings ordered\n")

    # Format standings
    # pretty_standings = []
    # for i, club in enumerate(epl_standings, 1):
    #     string = f"{str(i).zfill(2)}. {club[headers.index('club')]} ({club[headers.index('points')]} pts)"
    #     print(string)
    #     pretty_standings.append(string)

    # Write to file
    filepath = './english_premier_league_standings-2020_21.txt'
    # TODO Uncomment
    # write_file(filepath, pretty_standings)


if __name__ == '__main__':
    main()
