from random import random, randint, randrange
from faker import Faker

mock_generator = Faker()

OUTPUT_FILENAME = 'generated_data_for_start.sql'
CURRENT_LOCATION_INSERT = (
    "INSERT INTO Current_Locations(location, first_name, last_name) "
    "VALUES ('{location}', '{first_name}', '{last_name}');"
)
OPERATIVES_INSERT = (
    "INSERT INTO Operatives(first_name, last_name, age_years, weight_kg, num_assignments, current_location) "
    "VALUES ('{first_name}', '{last_name}', {age_years}, {weight_kg}, {num_assignments}, '{current_location}');"
)
EXPENSE_ACCOUNT_INSERT = (
    "INSERT INTO Expense_Accounts(account_id, first_name, last_name) "
    "VALUES ({account_id}, '{first_name}', '{last_name}');"
)
ASSIGNMENTS_INSERT = (
    "INSERT INTO Assignments (assignment_date, location, first_name, last_name, was_successful, num_people_on_assignment) "
    "VALUES ('{assignment_date}', '{location}', '{first_name}', '{last_name}', {was_successful}, {num_people_on_assignment});"
)

# Generate names
NUM_NAMES = 250

FIRST_NAMES = list(set([mock_generator.name().split()[0] for i in range(NUM_NAMES)]))
LAST_NAMES = list(set([mock_generator.name().split()[1] for i in range(NUM_NAMES*2)]))[0:len(FIRST_NAMES)]
AGES = [randint(20, 45) for i in range(len(FIRST_NAMES))]
WEIGHTS = [(random() + random()) * randint(15, 20) for i in range(NUM_NAMES)]

# Generate locations
NUM_LOCATIONS = 150

LOCATIONS = list(set([' '.join(mock_generator.address().split('\n')[1].split()[:-1]) for i in range(NUM_LOCATIONS)]))

# Generate expense accounts
NUM_EXPENSE_ACCOUNTS = 35

EXPENSE_ACCOUNT_NUMBERS = list(set([randint(1200, 9500) for i in range(NUM_EXPENSE_ACCOUNTS)]))

# Generate assignments
NUM_ASSIGNMENTS = 345

ASSIGNMENT_DATES = [
    (str(randint(2017, 2018)) + str(randint(1, 12)).zfill(2) + '-' + str(randint(1, 25)).zfill(2))
    for i in range(NUM_ASSIGNMENTS)
]

ASSIGNMENT_LOCATIONS = [
    LOCATIONS[randrange(len(LOCATIONS))] for i in range(NUM_ASSIGNMENTS)
]

ASSIGNMENTS = []
for i in range(NUM_ASSIGNMENTS):
    if randint(0, 1):
        # Generate an assignment with multiple people
        num_people_on_assignment = randint(1, 10)

        for j in range(num_people_on_assignment):
            name_index = randrange(len(FIRST_NAMES))

            ASSIGNMENTS.append({
                'assignment_date': ASSIGNMENT_DATES[i],
                'location': ASSIGNMENT_LOCATIONS[i],
                'first_name': FIRST_NAMES[name_index],
                'last_name': LAST_NAMES[name_index],
                'was_successful': 'TRUE' if randint(0, 1) else 'FALSE',
                'num_people_on_assignment': num_people_on_assignment
            })
    else:
        name_index = randrange(len(FIRST_NAMES))

        ASSIGNMENTS.append({
            'assignment_date': ASSIGNMENT_DATES[i],
            'location': ASSIGNMENT_LOCATIONS[i],
            'first_name': FIRST_NAMES[name_index],
            'last_name': LAST_NAMES[name_index],
            'was_successful': 'TRUE' if randint(0, 1) else 'FALSE',
            'num_people_on_assignment': 1
        })


# ^ ASSIGNMENTS OK (1/4)

OPERATIVES = []
for i in range(len(FIRST_NAMES)):
    OPERATIVES.append({
        'first_name': FIRST_NAMES[i],
        'last_name': LAST_NAMES[i],
        'age_years': AGES[i],
        'weight_kg': WEIGHTS[i],
        'num_assignments': len([
            assignment for assignment in ASSIGNMENTS
            if assignment['first_name'] == FIRST_NAMES[i]
            and assignment['last_name'] == LAST_NAMES[i]
        ]),
        'current_location': LOCATIONS[randrange(len(LOCATIONS))]
    })

# ^ OPERATIVES OK (2/4)

LOCATIONS = []
for i in range(len(OPERATIVES)):
    LOCATIONS.append({
        'location': OPERATIVES[i]['current_location'],
        'first_name': OPERATIVES[i]['first_name'],
        'last_name': OPERATIVES[i]['last_name']
    })

# ^ LOCATIONS OK (3/4)

EXPENSE_ACCOUNTS = []
for i in range(NUM_EXPENSE_ACCOUNTS):
    name_index = randrange(len(FIRST_NAMES))

    EXPENSE_ACCOUNTS.append({
        'account_id': EXPENSE_ACCOUNT_NUMBERS[i],
        'first_name': FIRST_NAMES[name_index],
        'last_name': LAST_NAMES[name_index]
    })

# ^ OPERATIVES OK (4/4)

# TODO
print(str(LOCATIONS))
print()
print(str(EXPENSE_ACCOUNTS))
print()
print(str(ASSIGNMENTS))
print()
print(str(OPERATIVES))
print()
