-- Add a new operative:
-- His name is Kourii (age 22, 52 kg)
-- and he's based in Skywhale Island, OS.

-- ORIGINAL SCHEMA
-- TODO

-- MIGRATED SCHEMA
-- TODO

-- Update an existing operative:
-- Jinhai has just completed an assignment
-- today on Skywhale Island, OS.
-- He did this assignment with Kourii.

-- ORIGINAL SCHEMA
-- TODO

-- MIGRATED SCHEMA
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
