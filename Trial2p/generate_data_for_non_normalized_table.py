from random import randint
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

FIRST_NAMES = list(set([mock_generator.name()[0] for i in range(NUM_NAMES)]))
LAST_NAMES = list(set([mock_generator.name()[1] for i in range(NUM_NAMES)]))
AGES = [randint(20, 45) for i in range(NUM_NAMES)]
WEIGHTS = [(random() + random()) * randint(15, 20) for i in range(NUM_NAMES)]

# Generate locations
NUM_LOCATIONS = 150

LOCATIONS = list(set([' '.join(mock_generator.address().split('\n')[1].split()[:-1]) for i in range(NUM_LOCATIONS)]))

# Generate expense accounts
NUM_EXPENSE_ACCOUNTS = 35

EXPENSE_ACCOUNTS = list(set([randint(1200, 9500) for i in range(NUM_EXPENSE_ACCOUNTS)]))

# Generate assignments
NUM_ASSIGNMENTS = 345

ASSIGNMENT_DATES = [(randint(0, 1) * ['2017-', '2018-']) + str(randint(0, 11) * list(range(1, 13))) + '-' + # TODO: day str(randint())]