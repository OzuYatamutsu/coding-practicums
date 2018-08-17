CREATE TABLE Current_Location (
    location VARCHAR2(255) NOT NULL,
    first_name VARCHAR2(255) NOT NULL,
    last_name VARCHAR2(255) NOT NULL,

    PRIMARY KEY (location)
);

CREATE TABLE Operatives (
    first_name VARCHAR2(255) NOT NULL,
    last_name VARCHAR2(255) NOT NULL,
    age_years TINYINT UNSIGNED NOT NULL,
    weight_kg FLOAT UNSIGNED NOT NULL,
    num_assignments INTEGER UNSIGNED,
    current_location VARCHAR2(255),

    PRIMARY KEY (first_name, last_name),
    FOREIGN KEY (current_location)
        REFERENCES Current_Location(location)
        ON DELETE SET NULL
);

CREATE TABLE Assignments (
    assignment_date DATE NOT NULL,
    location VARCHAR2(255) NOT NULL,
    first_name VARCHAR2(255) NOT NULL,
    last_name VARCHAR2(255) NOT NULL,
    was_successful BOOLEAN,
    num_people_on_assignment TINYINT UNSIGNED,

    PRIMARY KEY (assignment_date, location),
    FOREIGN KEY (location)
        REFERENCES Current_Location(location)
        ON DELETE SET NULL
);

CREATE TABLE Expense_Accounts (
    account_id INTEGER UNSIGNED NOT NULL,
    first_name VARCHAR2(255) NOT NULL,
    last_name VARCHAR2(255) NOT NULL,

    PRIMARY KEY (account_id, first_name, last_name)
);
