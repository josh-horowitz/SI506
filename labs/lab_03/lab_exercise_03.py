# Lab Exercise 03
print('Lab Exercise 03 \n')

# Setup
companies = [
    "Domino's, Ann Arbor, 14400, Food",
    "Fisher Investments, Camas, 3500, financial",
    "M&T Bank, Buffalo, 16840, Financial",
    "Dimensional Insight, Burlington, 102, Tech",
    "Bloomingdale's, New York, 6500, Retail",
    "Meijer, Grand Rapids, 70000, Retail",
    "CIL Management Consultants, Chicago, 189, Consulting"
]

# Problem 01 (3 points)

locations = []

for company in companies:
    new_company = company.split(", ")
    locations.append(new_company[1])

print(f"\n1. locations = {locations}")

# Problem 02 (4 points)

financial_co = []

for company in companies:
    new_company = company.split(", ")
    if new_company[-1].lower() == "financial":
        financial_co.append(new_company[0])

print(f"\n2. financial_co = {financial_co}")

# Problem 03 (4 points)

count = 0

for company in companies:
    new_company = company.split(", ")
    if new_company[-1].lower() == 'retail':
        count += 1

print(f"\n3. There are in total of {count} companies in the retail industry")

# PROBLEM 4 (4 Points)
small_companies = []
medium_companies = []
large_companies = []

for company in companies:
    new_company = company.split(", ")
    if int(new_company[2]) < 500:
        small_companies.append(new_company[0])
    elif int(new_company[2]) >= 5000:
        large_companies.append(new_company[0])
    else:
        medium_companies.append(new_company[0])

print(small_companies)
print(medium_companies)
print(large_companies)

# PROBLEM 5 (4 Points)

largest_company = ""
max_employees = 0

for company in companies:
    new_company = company.split(", ")
    if int(new_company[2]) > max_employees:
        max_employees = int(new_company[2])
        largest_company = new_company[0]

print(largest_company)
# END LAB EXERCISE
