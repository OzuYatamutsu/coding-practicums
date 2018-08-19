CREATE TABLE Current_Locations (
    location VARCHAR(255) NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,

    PRIMARY KEY (location, first_name, last_name)
);

CREATE TABLE Operatives (
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    age_years TINYINT UNSIGNED,
    weight_kg FLOAT UNSIGNED,
    num_assignments INTEGER UNSIGNED,
    current_location VARCHAR(255),

    PRIMARY KEY (first_name, last_name),
    FOREIGN KEY (current_location)
        REFERENCES Current_Locations(location)
        ON DELETE SET NULL
);

CREATE TABLE Assignments (
    assignment_date DATE NOT NULL,
    location VARCHAR(255),
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    was_successful BOOLEAN,
    num_people_on_assignment TINYINT UNSIGNED,

    PRIMARY KEY (assignment_date, location)
);

CREATE TABLE Expense_Accounts (
    account_id INTEGER UNSIGNED NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,

    PRIMARY KEY (account_id, first_name, last_name),
    CONSTRAINT is_valid_account_id
        CHECK (account_id BETWEEN 1000 AND 9999)
);
