# SI 506 Lecture 07

# 2.0 DEFINITE ITERATION

# https://www.fueleconomy.gov/feg/ws/index.shtml#ft7

elec_vehicles = [
    'Ford Mustang Mach-E AWD',
    'Kandi K27',
    'Chevrolet (GM) Bolt EV',
    'Audi (Volkswagen) e-tron',
    'Nissan Leaf (40 kW-hr battery pack)',
    'Tesla Model 3 Performance AWD',
    'Volvo XC40 AWD BEV',
    'Volkswagen ID.4 1st',
    'Polestar (Volvo) 2',
    'BMW i3s',
    'Mini (BMW) Cooper SE Hardtop 2 door',
    'Tesla Model S Performance (19in Wheels)'
]

# 2.0 CREATE LIST OF TESLA VEHICLES
tesla_vehicles = []
tesla_vehicles.append(elec_vehicles[5])
tesla_vehicles.append(elec_vehicles[-1])

# TODO Append Tesla vehicles

# TODO Uncomment
print(f"\n2.0 Tesla vehicles (n={len(elec_vehicles)}) = {tesla_vehicles}")


# 2.1 FOR LOOP

# TODO Uncomment
print(f"\n2.1 elec_vehicles (loop)")

# TODO Implement "Electric vehicles" loop; print each vehicle

for vehicle in elec_vehicles:
    print(vehicle)

# 2.2 IF STATEMENT

# TODO Uncomment
print(f"\n2.2.1 Volo vehicles")

# Find "volvo" string

for vehicle in elec_vehicles:
    if vehicle.lower().find('volvo') > -1:
        print(vehicle)

# TODO implement "Volvo" loop

# Filter on "tesla"; append element to accumulator list
tesla_vehicles = [] # accumulator

# TODO implement "Tesla" loop

# TODO Uncomment
print(f"\n2.2.2 Tesla vehicles (loop) = {tesla_vehicles}")
for vehicle in elec_vehicles:
    if vehicle.lower().startswith('tesla'):
        tesla_vehicles.append(vehicle)

print(tesla_vehicles)

# 3.0 THE ACCUMULATOR PATTERN

elec_vehicles = [
    ['Ford', 'Mustang Mach-E AWD', 2021, 211],
    ['Kandi', 'K27', 2021, 59],
    ['Chevrolet (GM)', 'Bolt EV', 2021, 259],
    ['Audi (Volkswagen)', 'e-tron', 2021, 222],
    ['Nissan', 'Leaf (40 kW-hr battery pack)', 2021, 149],
    ['Tesla', 'Model 3 Performance AWD', 2021, 315],
    ['Volvo', 'XC40 AWD BEV', 2021, 208],
    ['Volkswagen', 'ID.4 1st', 2021, 250],
    ['Polestar (Volvo)', '2', 2021, 233],
    ['BMW', 'i3s', 2021, 153],
    ['Mini (BMW)', 'Cooper SE Hardtop 2 door', 2021, 110],
    ['Tesla','Model S Performance (19in Wheels)', 2021, 387]
]

vehicle_max_range = None
num = 0

# TODO Implement "max range" loop

for vehicle in elec_vehicles:
    if vehicle[-1] > num:
        vehicle_max_range = vehicle
        num = vehicle[-1]

# TODO Uncomment
print(f"\n3.0 Max range (max={num} mi) = {vehicle_max_range}")


# 3.1 CHALLENGE

# TODO Implement accumulator pattern

vehicle_min_range = None
# num = vehicle_max_range
num = float('inf')

for vehicle in elec_vehicles:
    if vehicle[-1] < num:
        vehicle_min_range = vehicle
        num = vehicle[-1]

# TODO Uncomment
print(f"\n3.1 Challenge: min range (min={num} mi) = {vehicle_min_range}")


# 4.0 LOOPING AND SLICING

elec_vehicles = [
    ['automaker', 'brand', 'model', 'year', 'range', 'range_hwy', 'range_city', 'highway_08_mpg', 'charge_240v_hrs'],
    ['Ford Motor Co.', 'Ford', 'Mustang Mach-E AWD', 2021, 211, 193.7, 225.5, 86, 8.5],
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

headers = elec_vehicles[0] # column headers
vehicles_range = [] # accumulator

# TODO Implement loop

for vehicle in elec_vehicles[1:]:
    if vehicle[headers.index('range')] > 250:
        vehicles_range.append(vehicle)

# TODO Uncomment
print(f"\n4.0 Accumulator pattern (range > 250 mi) = {vehicles_range}")


# 5.0 COUNTING

volvo_count = 0

# TODO Implement "Volvo Group" loop

for vehicle in elec_vehicles[1:]:
    if vehicle[headers.index('automaker')] == 'Volvo Group':
        volvo_count += 1

# TODO Uncomment
print(f"\n5.0 Volvo count = {volvo_count}")


# 5.1 CHALLENGE COUNTING

# TODO Implement
mpg_count = 0

for vehicle in elec_vehicles[1:]:
    if vehicle[headers.index('highway_08_mpg')] > 100:
        mpg_count += 1

# TODO Uncomment
print(f"\n5.1 Challenge mpg > 100 mi = {mpg_count}")


# 6.0 IF-ELSE

short_charge = []
long_charge = []

# TODO Implement loop

for vehicle in elec_vehicles[1:]:
    if vehicle[-1] < 8:
        short_charge.append(vehicle)
    else:
        long_charge.append(vehicle)

# TODO Uncomment
print(f"\n6.0.1 short charge = {short_charge}")
print(f"\n6.0.2 long charge = {long_charge}")


# 7.0 IF-ELIF-ELSE

range_city_high = [] # 300+ mpg (city)
range_city_med = [] # 150-299 mpg (city)
range_city_low = [] # 0 - 149 mpg (city)

# TODO Implement loop

for vehicle in elec_vehicles[1:]:
    if vehicle[headers.index('range_city')] < 150:
        range_city_low.append(vehicle)
    elif vehicle[headers.index('range_city')] < 300:
        range_city_med.append(vehicle)
    else:
        range_city_high.append(vehicle)


# TODO Uncomment
print(f"\n7.0.1 range city high = {range_city_high}")
print(f"\n7.0.2 range city medium = {range_city_med}")
print(f"\n7.0.3 range city low = {range_city_low}")
