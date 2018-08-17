-- Add a new operative:
-- His name is Kourii Raiko (age 22, 52 kg),
-- he's based in Skywhale Island, OS,
-- and he's been assigned expense accounts 9090 and 9091.

-- ORIGINAL SCHEMA
INSERT INTO Current_Locations(first_name, last_name, location) VALUES ('Kourii', 'Raiko', 'Skywhale Island, OS'); 
i
INSERT INTO Operatives(first_name, last_name, age_years, weight_kg, num_assignments, current_location) VALUES ('Kourii', 'Raiko', 22, 52.0, 0, 'Skywhale Island, OS');

INSERT INTO Expense_Accounts(first_name, last_name, account_id) VALUES ('Kourii', 'Raiko', 9090); 
INSERT INTO Expense_Accounts(first_name, last_name, account_id) VALUES ('Kourii', 'Raiko', 9091);
 
-- MIGRATED SCHEMA
INSERT INTO Operatives(first_name, last_name, age_years, weight_kg, current_location) VALUES ('Kourii', 'Raiko', 22, 52.0, 'Skywhale Island, OS');
SELECT @kourii_id := LAST_INSERT_ID();

INSERT INTO Expense_Account_Users(account_id, operative_id) VALUES (9090, @kourii_id);
INSERT INTO Expense_Account_Users(account_id, operative_id) VALUES (9091, @kourii_id);

-- Update an existing operative:
-- Jinhai has just completed an assignment
-- today on Skywhale Island, OS.
-- He did this assignment with Kourii.

-- ORIGINAL SCHEMA
INSERT INTO Assignments (assignment_date, location, first_name, last_name, was_successful, num_people_on_assignment) VALUES (sysdate(), 'Skywhale Island, OS', 'Kourii', 'Raiko', TRUE, 2);
INSERT INTO Assignments (assignment_date, location, first_name, last_name, was_successful, num_people_on_assignment) VALUES (sysdate(), 'Skywhale Island, OS', 'Jinhai', 'Steakhouse', TRUE, 2);

UPDATE Operatives SET num_assignments = num_assignments + 1 WHERE first_name = 'Kourii' AND last_name = 'Raiko';
UPDATE Operatives SET num_assignments = num_assignments + 1 WHERE first_name = 'Jinhai' AND last_name = 'Steakhouse';

-- MIGRATED SCHEMA
INSERT INTO Assignments(assignment_date, location) VALUES (sysdate(), 'Skywhale Island, OS');

SELECT @kohaii_assignment_id := LAST_INSERT_ID();
SELECT @jinhai_id := operative_id FROM Operatives WHERE first_name = 'Jinhai' AND last_name = 'Steakhouse' LIMIT 1;
SELECT @kourii_id := operative_id FROM Operatives WHERE first_name = 'Kourii' AND last_name = 'Raiko' LIMIT 1;

INSERT INTO Assignment_Members(assignment_id, operative_id) VALUES (@kohaii_assignment_id, @jinhai_id);
INSERT INTO Assignment_Members(assignment_id, operative_id) VALUES (@kohaii_assignment_id, @kourii_id);


-- Get a list of all assignments and the
-- people who've been on them, as well as
-- where they took place and whether they
-- were successful.

-- TODO

-- What are the names of everyone who
-- are able to use expense account 1234?

-- ORIGINAL SCHEMA
SELECT first_name, last_name
FROM Expense_Accounts
WHERE
    account_id = 1234;

-- MIGRATED SCHEMA
SELECT first_name, last_name
FROM Operatives
INNER JOIN Expense_Account_Users
    ON Operatives.operative_id = Expense_Account_Users.operative_id;

-- What are the names of everyone
-- who were on assignment on Skywhale Island, OS
-- on March 12th, 2018?

-- ORIGINAL SCHEMA
SELECT first_name, last_name
FROM Assignments
WHERE 
    location = 'Skywhale Island, OS'
    AND assignment_date = '2018-03-12';

-- MIGRATED SCHEMA
SELECT first_name, last_name
FROM (
    (Operatives RIGHT JOIN Assignment_Members
        ON Operatives.operative_id = Assignment_Members.operative_id)
    INNER JOIN Assignments
        ON Assignment_Members.assignment_id = Assignments.assignment_id
) WHERE
    location = 'Skywhale Island, OS'
    AND assignment_date = '2018-03-12';

-- How many assignments has Jinhai been on?

-- ORIGINAL SCHEMA
-- TODO

-- MIGRATED SCHEMA
-- TODO
