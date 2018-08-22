CREATE TABLE Locations (
    location_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    location VARCHAR(255) NOT NULL UNIQUE,

    PRIMARY KEY (location_id)
);

CREATE TABLE Expense_Accounts (
    account_id INTEGER UNSIGNED NOT NULL,

    PRIMARY KEY (account_id),
    CONSTRAINT is_valid_account_id
        CHECK (account_id BETWEEN 1000 AND 9999)
); 

CREATE TABLE Operatives (
    operative_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    current_location_id INTEGER UNSIGNED,
    age_years TINYINT UNSIGNED,
    weight_kg FLOAT UNSIGNED, 

    PRIMARY KEY (operative_id),
    FOREIGN KEY (current_location_id)
        REFERENCES Locations(location_id)
        ON DELETE SET NULL 
);

CREATE TABLE Assignments (
    assignment_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
    assignment_date DATE NOT NULL,
    location_id INTEGER UNSIGNED,

    PRIMARY KEY (assignment_id),
    FOREIGN KEY (location_id)
        REFERENCES Locations(location_id)
        ON DELETE SET NULL
);

CREATE TABLE Assignment_Members (
    assignment_id INTEGER UNSIGNED NOT NULL,
    operative_id INTEGER UNSIGNED NOT NULL,

    PRIMARY KEY (assignment_id, operative_id),
    FOREIGN KEY (assignment_id)
        REFERENCES Assignments(assignment_id)
        ON DELETE CASCADE,
    FOREIGN KEY (operative_id)
        REFERENCES Operatives(operative_id) 
        ON DELETE CASCADE
);

CREATE TABLE Expense_Account_Users (
    account_id INTEGER UNSIGNED NOT NULL,
    operative_id INTEGER UNSIGNED NOT NULL,

    PRIMARY KEY (account_id, operative_id),
    FOREIGN KEY (account_id)
        REFERENCES Expense_Accounts(account_id)
        ON DELETE CASCADE,
    FOREIGN KEY (operative_id)
        REFERENCES Operatives(operative_id) 
        ON DELETE CASCADE
);
