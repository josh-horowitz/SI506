# START PROBLEM SET 02
print('Problem Set 02')

# PROBLEM 1 (10 points)
print('\nProblem 1')

gme_prices = [15.84, 35.50, 65.01, 325.00, 63.77]

price_max = max(gme_prices) #TODO: Replace

price_max_index = gme_prices.index(price_max) #TODO: Replace

#TODO: Problem 1.3

gme_prices.append(52.40)

#TODO: Problem 1.4

gme_prices[0] = 17.69

# PROBLEM 2 (10 points)
print('\nProblem 2')

amc_prices = [33.47, 34.41, 40.84, 44.02, 50.16] #TODO: Replace

amc_prices_latest = amc_prices[-1] #TODO: Replace

amc_prices_last_three = amc_prices[-3:] #TODO: Replace

# PROBLEM 3 (10 points)
print('\nProblem 3')

pltr_prices = ' 21.82-24.90-24.01-25.71-26.64-26.28 '

pltr_prices_list = pltr_prices.replace(" ","").split("-") #TODO: Replace

# PROBLEM 4 (20 points)
print('\nProblem 4')

dates = ['September 10th', 'September 3rd', 'August 27th', 'August 20th', 'August 13th', 'August 6th']

dates.reverse()

dates_str = "|".join(dates)

# PROBLEM 5 (20 points)
print('\nProblem 5')

pltr_highest = ""
pltr_highest = (f"In the week ending on {dates[pltr_prices_list.index(max(pltr_prices_list))]}, Palantir closed with a price of ${max(pltr_prices_list)} and AMC closed with a price of ${amc_prices[pltr_prices_list.index(max(pltr_prices_list))-1]}.")
print(pltr_highest)

amc_highest = (f"In the week ending on {dates[amc_prices.index(max(amc_prices))+1]}, Palantir closed with a price of ${pltr_prices_list[amc_prices.index(max(amc_prices))+1]} and AMC closed with a price of ${max(amc_prices)}.")
print(amc_highest)

# PROBLEM 6 (20 points)
print('\nProblem 6')

dates_reversed = dates[::-1]

# PROBLEM 7 (10 points)
print('\nProblem 7')

every_other_date = dates_reversed[::2]
