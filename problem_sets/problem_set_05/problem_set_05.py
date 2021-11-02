# SI 506 Problem Set 05

import csv
import copy

print("Problem 01\n\n")

# Problem 01: Implement read_csv and load the election data.

#declare function
def read_csv(filepath):

    # open filie I need to work with
    with open(filepath, 'r', encoding='utf-8-sig') as input_file:

        csv_data = []
        reader = csv.reader(input_file)
        for row in reader:
            csv_data.append(row)

    return csv_data

raw_election_data_2021 = read_csv('election_data_2021.csv')
raw_election_data_2017 = read_csv('election_data_2017.csv')

print(raw_election_data_2021)
print(raw_election_data_2017)

print("\n\nProblem 02\n\n")

# Problem 02: Implement clean and clean the election data.

def clean(data):
    deepcopy_data = copy.deepcopy(data)

    for element in deepcopy_data:
        index_value = deepcopy_data.index(element)
        for item in element:
            stripped_item = item.strip()
            if index_value == 0:
                insert_value = stripped_item
            else:
                if element.index(item) == deepcopy_data[0].index('Seats'):
                    insert_value = int(stripped_item)
                elif element.index(item) == deepcopy_data[0].index('Affiliation'):
                    insert_value = stripped_item.lower()
                else:
                    insert_value = stripped_item
            element.insert(element.index(item), insert_value)
            element.remove(item)
        deepcopy_data.pop(index_value)
        deepcopy_data.insert(index_value, element)
    return deepcopy_data


clean_election_data_2021 = clean(raw_election_data_2021)
clean_election_data_2017 = clean(raw_election_data_2017)
print(clean_election_data_2021)
print(clean_election_data_2017)

print("\n\nProblem 03\n\n")

# Problem 03: Implement get_party_seat_differences and get the party seat differences for the 2021 election.

def get_seat_differences(current_election, previous_election):

    election_differences = []
    current_election_headers = current_election[0]
    previous_election_headers = previous_election[0]

    for current_result in current_election[1:]:
        for previous_result in previous_election[1:]:
            if previous_result[previous_election_headers.index('Party')] == current_result[current_election_headers.index('Party')]:
                election_differences.append((current_result[current_election_headers.index('Party')], current_result[current_election_headers.index('Seats')]-previous_result[previous_election_headers.index('Seats')]))

    return election_differences

party_seat_differences = get_seat_differences(clean_election_data_2021,clean_election_data_2017)
print(party_seat_differences)

print("\n\nProblem 04\n\n")


# Problem 04: Implement get_leaders and get the leaders for the 2021 election data.
party_leaders_2021 = [
                        ('AfD', 'Joerg Meuthen and Tino Chrupalla'),
                        ('FDP', 'Christian Lindner'),
                        ('CDU/CSU', 'Armin Laschet'),
                        ('SPD', 'Olaf Scholz'),
                        ('Greens', 'Annalena Baerbock and Robert Habeck'),
                        ('Left', 'Janine Wissler and Susanne Hennig-Wellsow')
                    ]

def get_leaders(election_data, party_leaders):
    copy_election_data = copy.deepcopy(election_data)
    copy_election_data[0].append('Party Leader(s)')
    election_data_header = copy_election_data[0]

    for party_tuple in party_leaders:
        party, party_leader = party_tuple
        for data in copy_election_data[1:]:
            if party == data[election_data_header.index('Party')]:
                copy_election_data[copy_election_data.index(data)].append(party_leader)

    return copy_election_data

election_data_2021_with_leaders = get_leaders(clean_election_data_2021, party_leaders_2021)
print(election_data_2021_with_leaders)

print("\n\nProblem 05\n\n")

# Problem 05: Implement get_affiliation_percents and get affiliation percents for the 2021 election data.

def get_seats_percent(election_data):
    left_seats = 0
    right_seats = 0
    center_seats = 0
    far_seats = 0
    seat_total = 0
    election_data_headers = election_data[0]

    for party in election_data[1:]:
        seats = party[election_data_headers.index('Seats')]
        seat_total += seats
        if 'left' in party[election_data_headers.index('Affiliation')]:
            left_seats += seats
        if 'right' in party[election_data_headers.index('Affiliation')]:
            right_seats += seats
        if 'far' in party[election_data_headers.index('Affiliation')]:
            far_seats += seats
        else:
            center_seats += seats

    affiliation_percents = (round((left_seats/seat_total)*100,2),
                            round((right_seats/seat_total)*100,2),
                            round((far_seats/seat_total)*100,2),
                            round((center_seats/seat_total)*100,2))
    return affiliation_percents

print(get_seats_percent(clean_election_data_2021))

print("\n\nProblem 06\n\n")


# Problem 06: Implement write_csv and write election_data_2021_with_leaders to a file called revised_election_data_2021.csv.

def write_csv(filepath, data):

    with open(filepath, 'w', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

write_csv('revised_election_data_2021.csv', election_data_2021_with_leaders)