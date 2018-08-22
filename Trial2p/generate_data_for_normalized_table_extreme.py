from random import random, randint, randrange
from pymysql import connect
from pymysql.cursors import DictCursor
from faker import Faker

mock_generator = Faker()

INSERT_LOCATIONS_SQL = (
    "INSERT IGNORE INTO Locations (location) VALUES ('{location}')"
)

INSERT_EXPENSE_ACCOUNTS_SQL = (
    "INSERT IGNORE INTO Expense_Accounts (account_id) VALUES ({account_id})"
)

INSERT_OPERATIVES_SQL = (
    "INSERT IGNORE INTO Operatives (first_name, last_name, current_location_id, age_years, weight_kg) "
    "VALUES ('{first_name}', '{last_name}', {current_location_id}, {age_years}, {weight_kg})"
)

INSERT_ASSIGNMENTS_SQL = (
    "INSERT IGNORE INTO Assignments (assignment_date, location_id) VALUES ('{assignment_date}', {location_id})"
)

INSERT_ASSIGNMENT_MEMBERS_SQL = (
    "INSERT IGNORE INTO Assignment_Members (assignment_id, operative_id) "
    "VALUES ({assignment_id}, {operative_id})"
)

INSERT_EXPENSE_ACCOUNT_USERS_SQL = (
    "INSERT IGNORE INTO Expense_Account_Users (account_id, operative_id) "
    "VALUES ({account_id}, {operative_id})"
)

# Generate locations
NUM_LOCATIONS = 98260
LOCATION_NAMES = list(set([' '.join(mock_generator.address().split('\n')[1].split()[:-1]) for i in range(NUM_LOCATIONS)]))
LOCATIONS = [{'location': location} for location in range(len(LOCATION_NAMES))]

# Generate expense accounts
NUM_EXPENSE_ACCOUNTS = 550
EXPENSE_ACCOUNT_NUMS = list(set([randint(1200, 9500) for i in range(NUM_EXPENSE_ACCOUNTS)]))
EXPENSE_ACCOUNTS = [{'account_id': account_num} for account_num in range(len(EXPENSE_ACCOUNT_NUMS))]

# Generate operatives
NUM_OPERATIVES = 348670
OPERATIVES = [{
    'first_name': mock_generator.name().split()[0],
    'last_name': mock_generator.name().split()[1],
    'current_location_id': randint(1, len(LOCATIONS)),
    'age_years': randint(20, 45),
    'weight_kg': (random() + random()) * randint(15, 20)
} for i in range(NUM_OPERATIVES)]

# Generate assignments
NUM_ASSIGNMENTS = 185216118
ASSIGNMENTS = [{
    'assignment_date': (str(randint(1993, 2018)) + '-' + str(randint(1, 12)).zfill(2) + '-' + str(randint(1, 25)).zfill(2)),
    'location_id': randint(1, len(LOCATIONS))
} for i in range(NUM_ASSIGNMENTS)]
ASSIGNMENT_MEMBERS = []
for i in range(len(ASSIGNMENTS)):
    if randint(0, 1):
        # Generate an assignment with multiple people
        num_people_on_assignment = randint(1, 10)

        for j in range(num_people_on_assignment):
            ASSIGNMENT_MEMBERS.append({
                'assignment_id': randint(1, len(ASSIGNMENTS)),
                'operative_id': randint(1, len(OPERATIVES))
            })
        
    else:
        ASSIGNMENT_MEMBERS.append({
            'assignment_id': randint(1, len(ASSIGNMENTS)),
            'operative_id': randint(1, len(OPERATIVES))
        })

# Generate expense account users
EXPENSE_ACCOUNT_USERS = [{
    'account_id': randint(1, len(EXPENSE_ACCOUNTS)), 'operative_id': randint(1, len(OPERATIVES))
    } for i in range(len(OPERATIVES))]

# Now insert
conn = connect(
    host='localhost',
    user='trial2p_sol_rw',
    password='kohaii',
    db='Trial2p_solution',
    cursorclass=DictCursor
)

with conn.cursor() as cursor:
    cursor.execute("SET FOREIGN_KEY_CHECKS = 0")
    cursor.execute("TRUNCATE TABLE Locations")
    cursor.execute("TRUNCATE TABLE Expense_Accounts")
    cursor.execute("TRUNCATE TABLE Operatives")
    cursor.execute("TRUNCATE TABLE Assignments")
    cursor.execute("TRUNCATE TABLE Assignment_Members")
    cursor.execute("TRUNCATE TABLE Expense_Account_Users")
    cursor.execute("ALTER TABLE Locations AUTO_INCREMENT = 1")
    cursor.execute("ALTER TABLE Operatives AUTO_INCREMENT = 1")
    cursor.execute("ALTER TABLE Assignments AUTO_INCREMENT = 1")
    cursor.execute("SET FOREIGN_KEY_CHECKS = 1")
    conn.commit()

    for location in LOCATIONS:
        cursor.execute(INSERT_LOCATIONS_SQL.format(**location))
    for expense_account in EXPENSE_ACCOUNTS:
        cursor.execute(INSERT_EXPENSE_ACCOUNTS_SQL.format(**expense_account))
    for operative in OPERATIVES:
        cursor.execute(INSERT_OPERATIVES_SQL.format(**operative))
    for assignment in ASSIGNMENTS:
        cursor.execute(INSERT_ASSIGNMENTS_SQL.format(**assignment))
    for assignment_member in ASSIGNMENT_MEMBERS:
        cursor.execute(INSERT_ASSIGNMENT_MEMBERS_SQL.format(**assignment_member))
    for expense_account_user in EXPENSE_ACCOUNT_USERS:
        cursor.execute(INSERT_EXPENSE_ACCOUNT_USERS_SQL.format(**expense_account_user))
conn.commit()

print("Done.")