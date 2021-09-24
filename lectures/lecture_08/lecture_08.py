# SI 506 Lecture 08

# 1.0 BREAK AND CONTINUE

elec_vehicles = [
    ['automaker', 'brand', 'model', 'year', 'range', 'range_hwy', 'range_city', 'highway_08_mpg', 'charge_240v_hrs'],
    ['Ford Motor Company', 'Ford', 'Mustang Mach-E AWD', 2021, 211, 193.7, 225.5, 86, 8.5],
    ['Kandi Technologies Group', 'Kandi', 'K27', 2021, 59, 51.6, 64.3, 102, 7.0],
    ['General Motors Co.', 'Chevrolet', 'Bolt EV', 2021, 259, 235.1, 277.7, 108, 9.3],
    ['Volkswagen AG', 'Audi', 'e-tron', 2021, 222, 221.9408, 222.74, 77, 10.0],
    ['Nissan Motor Co.', 'Nissan', 'Leaf (40 kW-hr battery pack)', 2021, 149, 131.3, 163.2, 99, 8.0],
    ['Tesla, Inc.', 'Tesla', 'Model 3 Performance AWD', 2021, 315, 299.0, 328.7, 107, 10.0],
    ['Volvo Group', 'Volvo', 'XC40 AWD BEV', 2021, 208, 188.0, 223.6, 72, 8.0],
    ['Volkswagen AG', 'Volkswagen', 'ID.4 1st', 2021, 250, 230.1587, 266.7659, 89, 7.5],
    ['Volvo Group', 'Polestar', '2', 2021, 233, 222.1, 241.9, 88, 8.0],
    ['Bayerische Motoren Werke AG', 'BMW', 'i3s', 2021, 153, 136.4, 166.5, 102, 7.0],
    ['Bayerische Motoren Werke AG', 'Mini', 'Cooper SE Hardtop 2 door', 2021, 110, 101.9, 116.9, 100, 4.0],
    ['Tesla, Inc.', 'Tesla','Model S Performance (19in Wheels)', 2021, 387, 373.2, 398.3, 106, 14.7]
]

# Extract the headers
headers = elec_vehicles[0] # column headers


# 1.1 BREAK STATEMENT EXAMPLE

has_kandi = False
for vehicle in elec_vehicles[1:]:
    if vehicle[0].lower() == 'kandi technologies group':
        has_kandi = True
        break # exit loop

# print(f"\n1.1 Has Kandi Technology Group = {has_kandi}")


# 1.2 CHALLENGE BREAK STATEMENT

fast_charge = 3.0 # battery charge (hours)
can_fast_charge = False

# Todo Implement list
for vehicle in elec_vehicles[1:]:
    if vehicle[headers.index('charge_240v_hrs')] <= fast_charge:
        can_fast_charge = True
        break

print(f"\n1.2 has {fast_charge} hr battery charge vehicle = {can_fast_charge}")


# 1.3 CONTINUE STATEMENT EXAMPLE

# TODO UNCOMMENT

outliers = []
for vehicle in elec_vehicles[1:]:
    city_range = vehicle[headers.index('range_city')]
    if 75 < city_range < 275:
        continue # proceed to next iteration (skip)
    outliers.append(vehicle)

print(f"\n1.3 City range outliers\n{outliers}")


# 1.4 CHALLENGE CONTINUE STATEMENT

us_automakers = ('ford motor company', 'general motors co.', 'tesla, inc.') # tuple
non_us_vehicles = []

# TODO Implement list

# Refactor (drop continue statement)
for vehicle in elec_vehicles[1:]:
    if vehicle[0].lower() in us_automakers:
        continue
    non_us_vehicles.append(vehicle)

print(f"\n1.4 Challenge: Asian/European automakers' vehicles (n={len(non_us_vehicles)})\n{non_us_vehicles}")


# 2.0 RANGE() TYPE

seq = range(10)

# print(f"\n2.0.1 seq (type={type(seq)}) = {seq}") # <class 'range'>

seq = list(range(10)) # convert range object to a list

# print(f"\n2.0.2 range seq = {seq}")

seq = list(range(5, 10))

# print(f"\n2.0.3 range seq start/stop = {seq}")

seq = list(range(5, 21, 5))

# print(f"\n2.0.4 range seq start/stop/step = {seq}")

seq = list(range(20, 4, -5))

#print(f"\n2.0.5 range seq start/stop/step reversed = {seq}")


# 2.0.6 FOR LOOP/RANGE()

# TODO UNCOMMENT
# print(f"\n2.0.6 for loop with range()\n")

# for i in range(10):
#     print("I want to own an EV!")


# 2.0.7 FOR LOOP/RANGE()

automakers = [
    'Bayerische Motoren Werke AG',
    'Ford Motor Co.',
    'General Motors Co.',
    'Kandi Technologies Group',
    'Nissan Motor Co.',
    'Volkswagen AG',
    'Volvo Group',
    'Tesla, Inc.'
    ]

# TODO UNCOMMENT

# print(f"\n2.0.7 access automakers with range()\n")

# for i in range(len(automakers)):
#     print(automakers[i])


# 2.1 RANGE() CHALLENGE

select_vehicles = []

# 1. Return all elements
for i in range(len(elec_vehicles)):
    print(elec_vehicles[i])
# TODO Implement

# 2. Skip the header row; add 1 to stop value
for i in range(1, len(elec_vehicles)):
    print(elec_vehicles[i])
# TODO Implement

# 3. Append every other vehicle
for i in list(range(1, len(elec_vehicles),2)):
    select_vehicles.append(elec_vehicles[i])
# TODO Implement

print(f"\n2.0.8 select vehicles\n{select_vehicles}")


# 3.0 WHILE LOOP

# TODO UNCOMMENT

# print(f"\n3.0 while loop")
# i = 0
# while i < 5:
#     print(i)
#     i += 1 # increment

# print(f"\n3.1 while True")
# i = 0
# while True:
#     print(i, 'infinite loop triggered')
#     if i == 5:
#         print(i, 'infinite loop terminated\n')
#         break # exit the loop
#     i += 1 # increment (note indention)

# print(f"\n3.2 while loop with else")
# i = 0
# while i < 5:
#     print('I want an EV.')
#     i += 1 # increment
# else:
#     print('Enough said. We believe you.')

# print(f"\n3.3.1 while loop if-else (increment)")
# i = 0
# while i < 10:
#     if i % 2 == 0:
#         print(f"{i} is an even number.")
#     else:
#         print(f"{i} is an odd number.")
#     i += 1 # increment

# print(f"\n3.3.2 while loop if-else (decrement)")
# i = 10
# while i >= 0:
#     if i % 2 == 0:
#         print(f"{i} is an even number.")
#     else:
#         print(f"{i} is an odd number.")
#     i -= 1 # decrement


# 3.4 CLEANING CHALLENGE

data = [
    ['station_name', 'street_address', 'ev_connector_types', 'ev_network'],
    ['Ann Arbor Downtown Development Authority - Library Parking Structure', '319 S Fifth Ave', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Ann Ashley Parking Structure', '120 W Ann St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Catherine and Fourth Surface Lot', '121 Catherine St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Forrest Parking Structure', '650 Forrest St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - Maynard Parking Structure', '316 Maynard St', 'J1772', 'Non-Networked'],
    ['Ann Arbor Downtown Development Authority - William Street Parking Structure', '115 William St', 'J1772', 'Non-Networked'],
    ['U-M ANN ARBOR ANN STREET #2', '1101-1189 E Ann St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR ICL EDU #1', '1000 Greene St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR WALGREEN #1', '1300 Murfin Ave', 'J1772', 'ChargePoint Network'],
    ['BMW ANN ARBOR STATION 01', '501 Auto Mall Dr', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR WALL STREET #2', '1041 Wall St', 'J1772', 'ChargePoint Network'],
    ["DOMINO'S FARMS DOMINO'S FARMS2", '24 Frank Lloyd Wright Dr', 'J1772', 'ChargePoint Network'],
    ['Ann Arbor Downtown Development Authority - Ashley and Washington Parking Structure', '215 W Washington', 'J1772', 'Non-Networked'],
    ['MEADOWLARK BLDG STATION 2', '3250 W Liberty Rd', 'J1772', 'ChargePoint Network'],
    ['Shell', '2991 S State St', 'CHADEMO, J1772COMBO', 'eVgo Network'],
    ['Meijer - Tesla Supercharger', '3145 Ann Arbor-Saline Rd', 'TESLA', 'Tesla'],
    ['Sheraton Ann Arbor Hotel - Tesla Destination', '3200 Boardwalk Dr', 'J1772, TESLA', 'Tesla Destination'],
    ['MEIJER STORES 064 SALINE RD 1', '3145 Ann Arbor-Saline Rd', 'CHADEMO, J1772COMBO', 'ChargePoint Network'],
    ['U-M ANN ARBOR NCRC STATION 2', 'NCRC', 'J1772', 'ChargePoint Network'],
    ['FLEET SERVICES CITY HALL STA 4', '301 E Huron St', 'J1772', 'ChargePoint Network'],
    ['173 - Ann Arbor', '5645 Jackson Road', 'CHADEMO, J1772COMBO', 'Greenlots'],
    ['Car & Driver - Tesla Destination', '1585 Eisenhower Place', 'TESLA', 'Tesla Destination'],
    ['U-M ANN ARBOR ANN STREET #1', '1101-1189 E Ann St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR ANN STREET #3', '1101-1189 E Ann St', 'J1772', 'ChargePoint Network'],
    ['U-M ANN ARBOR WALL STREET #1', '1041 Wall St', 'J1772', 'ChargePoint Network'],
    ["DOMINO'S FARMS DOMINO'S FARMS", '24 Frank Lloyd Wright Dr', 'J1772', 'ChargePoint Network'],
    ['MEADOWLARK BLDG STATION 1', '3250 W Liberty Rd', 'J1772', 'ChargePoint Network'],
    ['MEIJER STORES 064 SALINE RD 2', '3145 Ann Arbor-Saline Rd', 'CHADEMO, J1772COMBO', 'ChargePoint Network'],
    ['U-M ANN ARBOR NCRC STATION 1', 'NCRC', 'J1772', 'ChargePoint Network'],
    ['FLEET SERVICES POLICE SPACE #5', '301 E Huron St', 'J1772', 'ChargePoint Network'],
    ['BEEKMAN BEEKMAN ST1', '1200 Broadway St', 'J1772', 'ChargePoint Network']
    ]


# 3.4.1 CHALLENGE (COUNTS)

# Example: index chaining

# TODO UNCOMMENT

chargepoint_network_count = 0
i = 0
while i < len(data[1:]):
    if data[i][-1] == 'ChargePoint Network':
        chargepoint_network_count += 1
    i += 1

print(f"\n3.4.1 Chargepoint Network count = {chargepoint_network_count}")


# Copy the data

# Extract headers and charging stations
headers = data[0]
charging_stations = data[1:]

print(f"\n3.4.1 data headers = {headers}")

station_count = len(charging_stations) # exclude header row
umich_station_count = 0 # initialize

# TODO Implement while loop

i = 0
while i in range(len(charging_stations)):
    if charging_stations[i][headers.index('station_name')].startswith('U-M'):
        umich_station_count += 1
    i += 1

print(f"\n3.4.1 UMich charging stations (while) = {umich_station_count} ({umich_station_count*100/station_count:.4}%)")


# TODO UNCOMMENT
# WARN: COMMENT WHILE LOOP ABOVE

# Alternative (so much easier to implement)

# umich_station_count = 0
# for station in charging_stations:
#     if station[0].lower().startswith('u-m'):
#         umich_station_count += 1

# print(f"\n3.4.1 UMich charging stations (for) = {umich_station_count} ({umich_station_count/station_count:.2}%)")


# 3.4.2 CHALLENGE

# TODO IMPLEMENT

i = 1
data_length = len(data)

while i < data_length:
    if data[i][0][:3] == 'U-M' or data[i][0][:3] == 'BMW':
        data[i][0] = data[i][0].replace(data[i][0], data[i][0][:3] + data[i][0][3:].title())
    print(data[i])
    i += 1

# print(f"\n3.4.2 Station mix case (examples) = {charging_stations[-6:]}")


# 3.4.3 CHALLENGE

# Convert string to list

# TODO IMPLEMENT

# print(f"\n3.4.3 Convert str to list (examples) = {charging_stations[-4:-2]}")

# Alternative: for loop

# TODO UNCOMMENT
# WARN: COMMENT OUT 3.4.3 WHILE LOOP ABOVE

# for station in charging_stations:
#     idx = headers.index('ev_connector_types')
#     station[idx] = station[idx].split(', ')

# print(f"\n3.4.3 Convert str to list (for loop) = {charging_stations[-4:-2]}")


# 4.0 WHILE LOOP AND INPUT()

ev_automakers = (
    'Audi',
    'BMW',
    'Ford',
    'GM',
    'Hyundai',
    'Kandi',
    'Kia',
    'Jaguar',
    'Nissan',
    'Tesla',
    'Volkswagen',
    'Volvo'
    )
prompt = '\nWho is your favorite EV automaker?: '

# TODO UNCOMMENT

# while True:
#     automaker = input(prompt)
#     if automaker in ev_automakers:
#         print(f"\nThanks for selecting {automaker}.\n\nFinis.")
#         break # terminate loop
#     print(f"\n'{automaker}' is not listed among the EV manufacturers.")
#     print('Please check spelling and enter again or provide a different automaker.')

# print('\n') # padding
