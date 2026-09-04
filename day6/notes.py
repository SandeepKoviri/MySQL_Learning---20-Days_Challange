'''
Constraints:
------------
-->Constraints in MySQL are rules applied to columns in a table to control the type of data that can be inserted or updated.
-->They help maintain data accuracy, consistency, and integrity.

Main Constraints in MySQL:

NOT NULL --> Prevents NULL values
UNIQUE --> Prevents duplicate values
PRIMARY KEY -->	Uniquely identifies each record
FOREIGN KEY -->	Creates a relationship between tables
CHECK --> Restricts values based on a condition
DEFAULT --> Provides a default value

1. NOT NULL:
------------
-->Ensures a column must always have a value (cannot be empty).

example:
--------

CREATE TABLE users (
  user_id INT NOT NULL,
  username VARCHAR(50) NOT NULL,
  email VARCHAR(100)
);

-- This works
INSERT INTO users (user_id, username, email) VALUES (1, 'john_doe', 'john@example.com');

-- This will fail - username is NOT NULL
INSERT INTO users (user_id, email) VALUES (2, 'jane@example.com');
---------------------------------------------------------------------------------
2. UNIQUE:
----------
--> Ensures all values in a column are unique (no duplicates).

example:
--------

CREATE TABLE employees (
  emp_id INT NOT NULL UNIQUE,
  email VARCHAR(100) UNIQUE,
  name VARCHAR(50)
);

-- This works
INSERT INTO employees (emp_id, email, name) VALUES (1, 'alice@example.com', 'Alice');

-- This fails - emp_id 1 already exists
INSERT INTO employees (emp_id, email, name) VALUES (1, 'bob@example.com', 'Bob');

-- This fails - email already exists
INSERT INTO employees (emp_id, email, name) VALUES (2, 'alice@example.com', 'Alice2');
-----------------------------------------------------------------------------------------------------
3. PRIMARY KEY:
---------------
--> Uniquely identifies each row in a table. It's a combination of NOT NULL + UNIQUE.

example:
--------

CREATE TABLE products (
  product_id INT PRIMARY KEY,
  product_name VARCHAR(100) NOT NULL,
  price DECIMAL(10, 2)
);

-- This works
INSERT INTO products VALUES (1, 'Laptop', 999.99);

-- This fails - primary key must be unique
INSERT INTO products VALUES (1, 'Mouse', 25.99);

-- This fails - primary key cannot be NULL
INSERT INTO products (product_name, price) VALUES ('Keyboard', 79.99);
----------------------------------------------------------------------------------------------------------
4. FOREIGN KEY:
---------------
--> Ensures referential integrity by linking to a primary key in another table.

example:
--------

CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50) NOT NULL
);

CREATE TABLE employees (
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50) NOT NULL,
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id)
);

-- Insert department first
INSERT INTO departments VALUES (1, 'IT');

-- This works - dept_id 1 exists
INSERT INTO employees VALUES (101, 'John', 1);

-- This fails - dept_id 5 doesn't exist in departments
INSERT INTO employees VALUES (102, 'Sarah', 5);
------------------------------------------------------------------------
5. CHECK:
---------
-->Ensures data meets a specific condition.

example:
--------

CREATE TABLE products (
  product_id INT PRIMARY KEY,
  name VARCHAR(100),
  price DECIMAL(10, 2),
  quantity INT CHECK (quantity >= 0),
  discount INT CHECK (discount BETWEEN 0 AND 100)
);

-- This works
INSERT INTO products VALUES (1, 'Laptop', 1000, 50, 10);

-- This fails - quantity cannot be negative
INSERT INTO products VALUES (2, 'Mouse', 25, -5, 5);

-- This fails - discount must be between 0-100
INSERT INTO products VALUES (3, 'Keyboard', 75, 100, 150);
------------------------------------------------------------------------
6. DEFAULT:
-----------
-->Assigns a default value if no value is provided during insertion.

example:
--------

CREATE TABLE orders (
  order_id INT PRIMARY KEY AUTO_INCREMENT,
  customer_name VARCHAR(50),
  order_date DATE DEFAULT CURDATE(),
  status VARCHAR(20) DEFAULT 'Pending',
  amount DECIMAL(10, 2)
);

-- This works - order_date and status use defaults
INSERT INTO orders (customer_name, amount) VALUES ('Alice', 500);

-- Retrieve the data
SELECT * FROM orders;
-- Result: order_id=1, customer_name='Alice', order_date='2024-12-19', status='Pending', amount=500
-----------------------------------------------------------------------

Benefits of Using Constraints:
-------------------------------
✅ Data Integrity - Ensures only valid data is stored
✅ Data Consistency - Maintains relationships between tables
✅ Error Prevention - Catches invalid data at the database level
✅ Performance - Indexed constraints improve query performance
✅ Security - Prevents invalid or harmful data entry

Constraints are fundamental to building reliable and maintainable databases!
-------------------------------------------------------------------------------------------------------------------
Referential actions:
--------------------
Referential actions define what happens to child records when the referenced parent record is modified or deleted. They are used with FOREIGN KEY constraints and include ON DELETE and ON UPDATE clauses.

ON DELETE CASCADE AND ON UPDATE CASCADE:
----------------------------------------
-->Automatically deletes or updates child records when parent record is deleted or updated.

EXAMPLE:
--------

CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50)
);

CREATE TABLE employees (
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50),
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id) 
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);

-- Insert data
INSERT INTO departments VALUES (1, 'IT'), (2, 'HR');
INSERT INTO employees VALUES (101, 'John', 1), (102, 'Sarah', 1);

-- DELETE CASCADE
DELETE FROM departments WHERE dept_id = 1;
-- Result: All employees in dept_id 1 are automatically deleted

-- UPDATE CASCADE
UPDATE departments SET dept_id = 10 WHERE dept_id = 2;
-- Result: All employees' dept_id is automatically updated to 10
------------------------------------------------------------------------------------------------
ON DELETE SET NULL AND ON UPDATE SET NULL:
------------------------------------------
--> Sets the foreign key column to NULL when parent record is deleted or updated (only works if column allows NULL).

EXAMPLE:
--------
CREATE TABLE departments (
  dept_id INT PRIMARY KEY,
  dept_name VARCHAR(50)
);

CREATE TABLE employees (
  emp_id INT PRIMARY KEY,
  emp_name VARCHAR(50),
  dept_id INT,
  FOREIGN KEY (dept_id) REFERENCES departments(dept_id) 
    ON DELETE SET NULL 
    ON UPDATE SET NULL
);

-- Insert data
INSERT INTO departments VALUES (1, 'IT'), (2, 'Sales');
INSERT INTO employees VALUES (101, 'John', 1), (102, 'Sarah', 2);

-- DELETE with SET NULL
DELETE FROM departments WHERE dept_id = 1;
-- Result: John's dept_id becomes NULL

SELECT * FROM employees;
-- emp_id=101, emp_name='John', dept_id=NULL
-- emp_id=102, emp_name='Sarah', dept_id=2
---------------------------------------------------------------------------------
MySQL Operators:
----------------

'''