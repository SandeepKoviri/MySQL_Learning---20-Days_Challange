'''
clause 
======
clause is a part of a SQL statement that performs a specific function. 
It can be used to filter, group, or order data in a query. Some common clauses include WHERE, GROUP BY, ORDER BY, and HAVING.

which is used to control how the data is selected , filtered, grouped, and ordered in a query.

where clause
------------
filter records based on a specified condition.
where clause is used to compare operators and logical operators .. etc.
syntax:
SELECT column1, column2, ...
FROM table_name
WHERE condition;

where clause can be used with comparison operators such as =, <>, >, <, >=, <=, and logical operators such as AND, OR, NOT.


group by clause
-----------------
the GROUP BY clause is used to group rows that have the same values in one or more columns. 
it is commonly used with aggregate functions such as COUNT, SUM, AVG, MAX, and MIN to perform calculations on each group of rows.

syntax:
SELECT column1, aggregate_function(column2)
FROM table_name
WHERE condition
GROUP BY column1;

group by clause can be used to group data based on one or more columns and perform calculations on each group.

having clause
-------------
the having clause is used to filter the results of a GROUP BY query based on a specified condition.
it is similar to the WHERE clause, but it is used to filter groups of data rather than individual rows.
syntax:
SELECT column1, aggregate_function(column2)
FROM table_name
WHERE condition
GROUP BY column1
HAVING condition;

order by clause
-----------------
order by clause is used to sort the result set of a query based on one or more columns.
ascending order ASC is the default sorting order, but you can also specify descending order using the DESC keyword.
syntax:
SELECT column1, column2, ...
FROM table_name
WHERE condition
order BY column1 ASC|DESC;

order by clause can be used to sort the result set based on one or more columns in ascending or descending order.
it is used to arrange the result set in a specific order before displaying it.

flow of clauses
-----------------
the flow of clauses in a SQL query is as follows:
select -> from -> where -> group by -> having -> order by



output of clauses
-----------------
mysql> CREATE TABLE STUDENTS (
    ->     StudentID INT AUTO_INCREMENT PRIMARY KEY,
    ->     Name VARCHAR(50),
    ->     Age INT,
    ->     Department VARCHAR(30),
    ->     Marks INT,
    ->     City VARCHAR(30)
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> INSERT INTO STUDENTS (Name, Age, Department, Marks, City) VALUES
    -> ('Anil', 20, 'CSE', 85, 'Hyderabad'),
    -> ('Sneha', 22, 'ECE', 75, 'Mumbai'),
    -> ('Ravi', 20, 'CSE', NULL, 'Hyderabad'),
    -> ('Divya', 23, 'MECH', 65, NULL),
    -> ('Kiran', 22, 'ECE', 75, 'Pune'),
    -> ('Varun', 21, 'CSE', 92, 'Chennai'),
    -> ('Priya', 20, 'EEE', 88, 'Delhi'),
    -> ('John', 22, 'MECH', 55, 'Mumbai'),
    -> ('Rekha', 21, 'ECE', 75, 'Pune'),
    -> ('Ramesh', 23, 'EEE', NULL, 'Delhi');
Query OK, 10 rows affected (0.01 sec)
Records: 10  Duplicates: 0  Warnings: 0

mysql> 
mysql> select*from students;
+-----------+--------+------+------------+-------+-----------+
| StudentID | Name   | Age  | Department | Marks | City      |
+-----------+--------+------+------------+-------+-----------+
|         1 | Anil   |   20 | CSE        |    85 | Hyderabad |
|         2 | Sneha  |   22 | ECE        |    75 | Mumbai    |
|         3 | Ravi   |   20 | CSE        |  NULL | Hyderabad |
|         4 | Divya  |   23 | MECH       |    65 | NULL      |
|         5 | Kiran  |   22 | ECE        |    75 | Pune      |
|         6 | Varun  |   21 | CSE        |    92 | Chennai   |
|         7 | Priya  |   20 | EEE        |    88 | Delhi     |
|         8 | John   |   22 | MECH       |    55 | Mumbai    |
|         9 | Rekha  |   21 | ECE        |    75 | Pune      |
|        10 | Ramesh |   23 | EEE        |  NULL | Delhi     |
+-----------+--------+------+------------+-------+-----------+
10 rows in set (0.00 sec)

mysql> CREATE TABLE sales (
    ->    sale_id INT PRIMARY KEY,
    ->    product VARCHAR(50),
    ->    category VARCHAR(50),
    ->    units_sold INT,
    ->    unit_price INT,
    ->    region VARCHAR(50)
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> 
mysql> INSERT INTO sales (sale_id, product, category, units_sold, unit_price, region) VALUES
    -> (1,  'Keyboard',    'Electronics', 10, 1200,  'North'),
    -> (2,  'Monitor',     'Electronics', 5,  7000,  'South'),
    -> (3,  'Chair',       'Furniture',   15, 2500,  'North'),
    -> (4,  'Desk',        'Furniture',   7,  4500,  'West'),
    -> (5,  'Mouse',       'Electronics', 20, 800,   'East'),
    -> (6,  'Sofa',        'Furniture',   3,  15000, 'South'),
    -> (7,  'Headphones',  'Electronics', 8,  1800,  'North'),
    -> (8,  'Laptop',      'Electronics', 6,  55000, 'West'),
    -> (9,  'Table',       'Furniture',   12, 6000,  'East'),
    -> (10, 'Fan',         'HomeAppliance', 18, 3000, 'South'),
    -> (11, 'AC',          'HomeAppliance', 4, 35000, 'North'),
    -> (12, 'Cupboard',    'Furniture',   5, 12000, 'West'),
    -> (13, 'Printer',     'Electronics', 9, 9000,  'East'),
    -> (14, 'Bed',         'Furniture',   2, 25000, 'South'),
    -> (15, 'Mobile',      'Electronics', 14, 20000, 'North');
Query OK, 15 rows affected (0.02 sec)
Records: 15  Duplicates: 0  Warnings: 0

mysql> select * from students where department = "cse";
+-----------+-------+------+------------+-------+-----------+
| StudentID | Name  | Age  | Department | Marks | City      |
+-----------+-------+------+------------+-------+-----------+
|         1 | Anil  |   20 | CSE        |    85 | Hyderabad |
|         3 | Ravi  |   20 | CSE        |  NULL | Hyderabad |
|         6 | Varun |   21 | CSE        |    92 | Chennai   |
+-----------+-------+------+------------+-------+-----------+
3 rows in set (0.00 sec)

mysql> select * from students where age > 80;          
Empty set (0.00 sec)

mysql> select * from students where marks > 80;
+-----------+-------+------+------------+-------+-----------+
| StudentID | Name  | Age  | Department | Marks | City      |
+-----------+-------+------+------------+-------+-----------+
|         1 | Anil  |   20 | CSE        |    85 | Hyderabad |
|         6 | Varun |   21 | CSE        |    92 | Chennai   |
|         7 | Priya |   20 | EEE        |    88 | Delhi     |
+-----------+-------+------+------------+-------+-----------+
3 rows in set (0.00 sec)

mysql> select * from students where age = 22;  
+-----------+-------+------+------------+-------+--------+
| StudentID | Name  | Age  | Department | Marks | City   |
+-----------+-------+------+------------+-------+--------+
|         2 | Sneha |   22 | ECE        |    75 | Mumbai |
|         5 | Kiran |   22 | ECE        |    75 | Pune   |
|         8 | John  |   22 | MECH       |    55 | Mumbai |
+-----------+-------+------+------------+-------+--------+
3 rows in set (0.00 sec)

mysql> select * from students where city = "mumbai";
+-----------+-------+------+------------+-------+--------+
| StudentID | Name  | Age  | Department | Marks | City   |
+-----------+-------+------+------------+-------+--------+
|         2 | Sneha |   22 | ECE        |    75 | Mumbai |
|         8 | John  |   22 | MECH       |    55 | Mumbai |
+-----------+-------+------+------------+-------+--------+
2 rows in set (0.00 sec)

mysql> select * from students where marks < 70;     
+-----------+-------+------+------------+-------+--------+
| StudentID | Name  | Age  | Department | Marks | City   |
+-----------+-------+------+------------+-------+--------+
|         4 | Divya |   23 | MECH       |    65 | NULL   |
|         8 | John  |   22 | MECH       |    55 | Mumbai |
+-----------+-------+------+------------+-------+--------+
2 rows in set (0.00 sec)

mysql> select * from students;
+-----------+--------+------+------------+-------+-----------+
| StudentID | Name   | Age  | Department | Marks | City      |
+-----------+--------+------+------------+-------+-----------+
|         1 | Anil   |   20 | CSE        |    85 | Hyderabad |
|         2 | Sneha  |   22 | ECE        |    75 | Mumbai    |
|         3 | Ravi   |   20 | CSE        |  NULL | Hyderabad |
|         4 | Divya  |   23 | MECH       |    65 | NULL      |
|         5 | Kiran  |   22 | ECE        |    75 | Pune      |
|         6 | Varun  |   21 | CSE        |    92 | Chennai   |
|         7 | Priya  |   20 | EEE        |    88 | Delhi     |
|         8 | John   |   22 | MECH       |    55 | Mumbai    |
|         9 | Rekha  |   21 | ECE        |    75 | Pune      |
|        10 | Ramesh |   23 | EEE        |  NULL | Delhi     |
+-----------+--------+------+------------+-------+-----------+
10 rows in set (0.00 sec)

mysql> select dept, count(*) as total_stu  
    -> from students
    -> group by department;
ERROR 1054 (42S22): Unknown column 'dept' in 'field list'
mysql> select department, count(*) as total_stu 
    -> from students       
    -> group by department;
+------------+-----------+
| department | total_stu |
+------------+-----------+
| CSE        |         3 |
| ECE        |         3 |
| MECH       |         2 |
| EEE        |         2 |
+------------+-----------+
4 rows in set (0.01 sec)

mysql> select department, avg(marks) as avg_marks
    -> from students
    -> group by department;
+------------+-----------+
| department | avg_marks |
+------------+-----------+
| CSE        |   88.5000 |
| ECE        |   75.0000 |
| MECH       |   60.0000 |
| EEE        |   88.0000 |
+------------+-----------+
4 rows in set (0.00 sec)

mysql> select department, max(marks) as max_marks
    -> from students       
    -> group by department;
+------------+-----------+
| department | max_marks |
+------------+-----------+
| CSE        |        92 |
| ECE        |        75 |
| MECH       |        65 |
| EEE        |        88 |
+------------+-----------+
4 rows in set (0.00 sec)

mysql> select department, min(marks) as lowest_marks
    -> from students       
    -> group by department;
+------------+--------------+
| department | lowest_marks |
+------------+--------------+
| CSE        |           85 |
| ECE        |           75 |
| MECH       |           55 |
| EEE        |           88 |
+------------+--------------+
4 rows in set (0.00 sec)

mysql> select department, sum(marks) as total_marks
    -> from students       
    -> 
    -> group by department;
+------------+-------------+
| department | total_marks |
+------------+-------------+
| CSE        |         177 |
| ECE        |         225 |
| MECH       |         120 |
| EEE        |          88 |
+------------+-------------+
4 rows in set (0.00 sec)

mysql> select city, count(*) as lowest_marks        
    -> from students       
    -> group by city;      
+-----------+--------------+
| city      | lowest_marks |
+-----------+--------------+
| Hyderabad |            2 |
| Mumbai    |            2 |
| NULL      |            1 |
| Pune      |            2 |
| Chennai   |            1 |
| Delhi     |            2 |
+-----------+--------------+
6 rows in set (0.00 sec)

mysql> select department, count(*) as total_stu 
    -> from students       
    -> group by department 
    -> having department > 2;
Empty set, 4 warnings (0.01 sec)

mysql> select department, count(*) as total_stu 
    -> from students
    -> group by department
    -> having count > 2;
ERROR 1054 (42S22): Unknown column 'count' in 'having clause'
mysql> select department, count(*) as total_stu 
    -> from students
    -> group by department
    -> having total_stu > 2;
+------------+-----------+
| department | total_stu |
+------------+-----------+
| CSE        |         3 |
| ECE        |         3 |
+------------+-----------+
2 rows in set (0.00 sec)

mysql> select department, count(*) as total_stu 
    -> from students
    -> group by department
    -> having count(*) > 2; 
+------------+-----------+
| department | total_stu |
+------------+-----------+
| CSE        |         3 |
| ECE        |         3 |
+------------+-----------+
2 rows in set (0.00 sec)

mysql> select department, avg(marks) as avg_m__stu 
    -> from students       
    -> group by department
    -> having avg_m_stu > 75;
ERROR 1054 (42S22): Unknown column 'avg_m_stu' in 'having clause'
mysql> select department, avg(marks) as avg_m__stu 
    -> from students      
    -> group by department
    -> having avg_m__stu > 75;
+------------+------------+
| department | avg_m__stu |
+------------+------------+
| CSE        |    88.5000 |
| EEE        |    88.0000 |
+------------+------------+
2 rows in set (0.00 sec)

mysql> select department, sum(marks) as avg_m__stu 
    -> from students          
    -> group by department
    -> having avg_m__stu > 150;
+------------+------------+
| department | avg_m__stu |
+------------+------------+
| CSE        |        177 |
| ECE        |        225 |
+------------+------------+
2 rows in set (0.00 sec)

mysql> select department, max(marks) as avg_m__stu 
    -> from students           
    -> group by department
    -> having avg_m__stu > 90; 
+------------+------------+
| department | avg_m__stu |
+------------+------------+
| CSE        |         92 |
+------------+------------+
1 row in set (0.00 sec)

mysql> select department, min(marks) as avg_m__stu 
    -> from students          
    -> group by department
    -> having avg_m__stu < 60;
+------------+------------+
| department | avg_m__stu |
+------------+------------+
| MECH       |         55 |
+------------+------------+
1 row in set (0.00 sec)

mysql> select * from students
    -> order by name;
+-----------+--------+------+------------+-------+-----------+
| StudentID | Name   | Age  | Department | Marks | City      |
+-----------+--------+------+------------+-------+-----------+
|         1 | Anil   |   20 | CSE        |    85 | Hyderabad |
|         4 | Divya  |   23 | MECH       |    65 | NULL      |
|         8 | John   |   22 | MECH       |    55 | Mumbai    |
|         5 | Kiran  |   22 | ECE        |    75 | Pune      |
|         7 | Priya  |   20 | EEE        |    88 | Delhi     |
|        10 | Ramesh |   23 | EEE        |  NULL | Delhi     |
|         3 | Ravi   |   20 | CSE        |  NULL | Hyderabad |
|         9 | Rekha  |   21 | ECE        |    75 | Pune      |
|         2 | Sneha  |   22 | ECE        |    75 | Mumbai    |
|         6 | Varun  |   21 | CSE        |    92 | Chennai   |
+-----------+--------+------+------------+-------+-----------+
10 rows in set (0.01 sec)

mysql> select * from students
    -> order by name desc;
+-----------+--------+------+------------+-------+-----------+
| StudentID | Name   | Age  | Department | Marks | City      |
+-----------+--------+------+------------+-------+-----------+
|         6 | Varun  |   21 | CSE        |    92 | Chennai   |
|         2 | Sneha  |   22 | ECE        |    75 | Mumbai    |
|         9 | Rekha  |   21 | ECE        |    75 | Pune      |
|         3 | Ravi   |   20 | CSE        |  NULL | Hyderabad |
|        10 | Ramesh |   23 | EEE        |  NULL | Delhi     |
|         7 | Priya  |   20 | EEE        |    88 | Delhi     |
|         5 | Kiran  |   22 | ECE        |    75 | Pune      |
|         8 | John   |   22 | MECH       |    55 | Mumbai    |
|         4 | Divya  |   23 | MECH       |    65 | NULL      |
|         1 | Anil   |   20 | CSE        |    85 | Hyderabad |
+-----------+--------+------+------------+-------+-----------+
10 rows in set (0.00 sec)

mysql> select * from students
    -> order by marks desc;
+-----------+--------+------+------------+-------+-----------+
| StudentID | Name   | Age  | Department | Marks | City      |
+-----------+--------+------+------------+-------+-----------+
|         6 | Varun  |   21 | CSE        |    92 | Chennai   |
|         7 | Priya  |   20 | EEE        |    88 | Delhi     |
|         1 | Anil   |   20 | CSE        |    85 | Hyderabad |
|         2 | Sneha  |   22 | ECE        |    75 | Mumbai    |
|         5 | Kiran  |   22 | ECE        |    75 | Pune      |
|         9 | Rekha  |   21 | ECE        |    75 | Pune      |
|         4 | Divya  |   23 | MECH       |    65 | NULL      |
|         8 | John   |   22 | MECH       |    55 | Mumbai    |
|         3 | Ravi   |   20 | CSE        |  NULL | Hyderabad |
|        10 | Ramesh |   23 | EEE        |  NULL | Delhi     |
+-----------+--------+------+------------+-------+-----------+
10 rows in set (0.00 sec)

mysql> select depertment, avg(marks) as average_marks
    -> from students
    -> where age > 20
    -> group by depertment
    -> having average_marks > 70
    -> order by average_marks desc;
ERROR 1054 (42S22): Unknown column 'depertment' in 'field list'
mysql> select department, avg(marks) as average_marks
    -> from students
    -> where age > 20
    -> group by department
    -> having average_marks > 70   
    -> order by average_marks desc;
+------------+---------------+
| department | average_marks |
+------------+---------------+
| CSE        |       92.0000 |
| ECE        |       75.0000 |
+------------+---------------+
2 rows in set (0.00 sec)

mysql> select department, sum(marks) as Tot_marks
    -> from students
    -> where 
    -> ^C
mysql> select city, sum(studentid) as Tot_stu    
    -> from students
    -> where marks > 70
    -> group by city
    -> having tot_stu > 1
    -> order by tot_stu asc;
+---------+---------+
| city    | Tot_stu |
+---------+---------+
| Mumbai  |       2 |
| Chennai |       6 |
| Delhi   |       7 |
| Pune    |      14 |
+---------+---------+
4 rows in set (0.00 sec)

mysql> select department, sum(marks) as Tot_marks
    -> from students
    -> where city in ("hyderabad", "puna")
    -> group by department
    -> having tot_marks > 100
    -> order by tot_marks;
Empty set (0.00 sec)

mysql> SELECT department, SUM(marks) AS Tot_marks
    -> FROM students
    -> WHERE city IN ('hyderabad', 'puna')
    -> GROUP BY department
    -> HAVING SUM(marks) > 100
    -> ORDER BY Tot_marks;
Empty set (0.00 sec)

mysql> select * from students;             
+-----------+--------+------+------------+-------+-----------+
| StudentID | Name   | Age  | Department | Marks | City      |
+-----------+--------+------+------------+-------+-----------+
|         1 | Anil   |   20 | CSE        |    85 | Hyderabad |
|         2 | Sneha  |   22 | ECE        |    75 | Mumbai    |
|         3 | Ravi   |   20 | CSE        |  NULL | Hyderabad |
|         4 | Divya  |   23 | MECH       |    65 | NULL      |
|         5 | Kiran  |   22 | ECE        |    75 | Pune      |
|         6 | Varun  |   21 | CSE        |    92 | Chennai   |
|         7 | Priya  |   20 | EEE        |    88 | Delhi     |
|         8 | John   |   22 | MECH       |    55 | Mumbai    |
|         9 | Rekha  |   21 | ECE        |    75 | Pune      |
|        10 | Ramesh |   23 | EEE        |  NULL | Delhi     |
+-----------+--------+------+------------+-------+-----------+
10 rows in set (0.00 sec)

mysql> SELECT department, SUM(marks) AS total
    -> FROM student
    -> WHERE city IN ('Hyderabad', 'Pune')
    -> GROUP BY department
    -> HAVING total > 100
    -> ORDER BY total;
ERROR 1146 (42S02): Table 'pfs5.student' doesn't exist
mysql> SELECT department, SUM(marks) AS total
    -> FROM students
    -> WHERE city IN ('Hyderabad', 'Pune')
    -> GROUP BY department
    -> HAVING total > 100
    -> ORDER BY total;
+------------+-------+
| department | total |
+------------+-------+
| ECE        |   150 |
+------------+-------+
1 row in set (0.00 sec)

mysql> select city, max(marks) as max_score
    -> from students
    -> where department = "ece"
    -> having max(marks) > 70
    -> order by max(marks);
ERROR 1140 (42000): In aggregated query without GROUP BY, expression #1 of SELECT list contains nonaggregated column 'pfs5.students.City'; this is incompatible with sql_mode=only_full_group_by
mysql> select city, max(marks) as max_score
    -> from students
    -> where department = "ece"
    -> group by city
    -> having max(marks) > 70              
    -> order by max(marks);
+--------+-----------+
| city   | max_score |
+--------+-----------+
| Mumbai |        75 |
| Pune   |        75 |
+--------+-----------+
2 rows in set (0.00 sec)

mysql> select department avg(age) as avg_age
    -> from students
    -> where city is not null
    -> group by department   
    -> having avg(age) > 20
    -> order by department;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(age) as avg_age
from students
where city is not null
group by department 
havin' at line 1
mysql> select department avg(age) as avg_age
    -> from students
    -> where city is not null
    -> group by department 
    -> having avg_age > 20 
    -> order by department;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '(age) as avg_age
from students
where city is not null
group by department 
havin' at line 1
mysql> select department,avg(age) as avg_age
    -> from students
    -> where city is not null
    -> group by department 
    -> having avg_age > 20
    -> order by department;
+------------+---------+
| department | avg_age |
+------------+---------+
| CSE        | 20.3333 |
| ECE        | 21.6667 |
| EEE        | 21.5000 |
| MECH       | 22.0000 |
+------------+---------+
4 rows in set (0.00 sec)

mysql> select * from sales;
+---------+------------+---------------+------------+------------+--------+
| sale_id | product    | category      | units_sold | unit_price | region |
+---------+------------+---------------+------------+------------+--------+
|       1 | Keyboard   | Electronics   |         10 |       1200 | North  |
|       2 | Monitor    | Electronics   |          5 |       7000 | South  |
|       3 | Chair      | Furniture     |         15 |       2500 | North  |
|       4 | Desk       | Furniture     |          7 |       4500 | West   |
|       5 | Mouse      | Electronics   |         20 |        800 | East   |
|       6 | Sofa       | Furniture     |          3 |      15000 | South  |
|       7 | Headphones | Electronics   |          8 |       1800 | North  |
|       8 | Laptop     | Electronics   |          6 |      55000 | West   |
|       9 | Table      | Furniture     |         12 |       6000 | East   |
|      10 | Fan        | HomeAppliance |         18 |       3000 | South  |
|      11 | AC         | HomeAppliance |          4 |      35000 | North  |
|      12 | Cupboard   | Furniture     |          5 |      12000 | West   |
|      13 | Printer    | Electronics   |          9 |       9000 | East   |
|      14 | Bed        | Furniture     |          2 |      25000 | South  |
|      15 | Mobile     | Electronics   |         14 |      20000 | North  |
+---------+------------+---------------+------------+------------+--------+
15 rows in set (0.00 sec)

mysql> select category, sum(units_sold) as tot_units
    -> from sales
    -> group by category 
    -> having tot_units > 20;
+---------------+-----------+
| category      | tot_units |
+---------------+-----------+
| Electronics   |        72 |
| Furniture     |        44 |
| HomeAppliance |        22 |
+---------------+-----------+
3 rows in set (0.00 sec)

mysql> select revenue, sum(unit_price) as tot_rev   
    -> from sales
    -> group by revenue
    -> having tot_rev > 50000;
ERROR 1054 (42S22): Unknown column 'revenue' in 'field list'
mysql> select region, sum(unit_price) as tot_rev 
    -> from sales             
    -> group by region 
    -> having tot_rev > 50000;
+--------+---------+
| region | tot_rev |
+--------+---------+
| North  |   60500 |
| West   |   71500 |
+--------+---------+
2 rows in set (0.00 sec)

mysql> select category, count(*) as count_         
    -> from sales                         
    -> group by region^C
mysql> select category, count(product) as count_ 
    -> from sales
    -> group by category                  
    -> having count_ > 2;
+-------------+--------+
| category    | count_ |
+-------------+--------+
| Electronics |      7 |
| Furniture   |      6 |
+-------------+--------+
2 rows in set (0.01 sec)

mysql> select category, avg(unit_price) as price 
    -> from sales
    -> group by category
    -> having price < 5000;
Empty set (0.00 sec)

mysql> select category, avg(unit_price) as price
    -> from sales
    -> group by category
    -> having price > 5000;
+---------------+------------+
| category      | price      |
+---------------+------------+
| Electronics   | 13542.8571 |
| Furniture     | 10833.3333 |
| HomeAppliance | 19000.0000 |
+---------------+------------+
3 rows in set (0.00 sec)

mysql> select region, count(product) as count_p
    -> from sales
    -> group by region
    -> having count_p > 1;
+--------+---------+
| region | count_p |
+--------+---------+
| North  |       5 |
| South  |       4 |
| West   |       3 |
| East   |       3 |
+--------+---------+
4 rows in set (0.00 sec)

mysql> select region, count(product) as count_p
    -> from sales
    -> where product = "electronic" 
    -> group by region    
    -> having count_p > 1;
Empty set (0.00 sec)

mysql> select region, sum(unit_price) as sum_p  
    -> from sales
    -> group by region              
    -> having sum_p > 20000
    -> order by sum_p desc;
+--------+-------+
| region | sum_p |
+--------+-------+
| West   | 71500 |
| North  | 60500 |
| South  | 50000 |
+--------+-------+
3 rows in set (0.00 sec)

mysql> select region, count(product) as count_p
    -> from sales
    -> group by region
    -> having count_p > 1
    -> order by region ;
+--------+---------+
| region | count_p |
+--------+---------+
| East   |       3 |
| North  |       5 |
| South  |       4 |
| West   |       3 |
+--------+---------+
4 rows in set (0.00 sec)

mysql> select category, sum(unit_price) as sum_p  
    -> from sales        
    -> group by category
    -> having sum_p > 10  
    -> order by category;
+---------------+-------+
| category      | sum_p |
+---------------+-------+
| Electronics   | 94800 |
| Furniture     | 65000 |
| HomeAppliance | 38000 |
+---------------+-------+
3 rows in set (0.00 sec)

mysql> select category, avg(unit_price) as avg_p
    -> from sales
    -> group by category
    -> having avg_p < 6000
    -> order by avg_p
    -> ;
Empty set (0.00 sec)

mysql> select category, avg(unit_sold) as avg_s 
    -> from sales         
    -> group by category
    -> having avg_s > 5   
    -> order by avg_s
    -> ;
ERROR 1054 (42S22): Unknown column 'unit_sold' in 'field list'
mysql> select category, avg(units_sold) as avg_s
    -> from sales       
    -> group by category
    -> having avg_s > 5
    -> order by avg_s
    -> ;
+---------------+---------+
| category      | avg_s   |
+---------------+---------+
| Furniture     |  7.3333 |
| Electronics   | 10.2857 |
| HomeAppliance | 11.0000 |
+---------------+---------+
3 rows in set (0.00 sec)

mysql> select category, sum(unit_sold) as sum_s
    -> from sales       
    -> group by category
    -> order by category desc;
ERROR 1054 (42S22): Unknown column 'unit_sold' in 'field list'
mysql> select category, sum(units_sold) as sum_s
    -> from sales             
    -> group by category
    -> order by category desc;
+---------------+-------+
| category      | sum_s |
+---------------+-------+
| HomeAppliance |    22 |
| Furniture     |    44 |
| Electronics   |    72 |
+---------------+-------+
3 rows in set (0.00 sec)

mysql> select region, avg(unit_price) as avg_s 
    -> from sales                             
    -> group by region  
    -> order by region;                       
+--------+------------+
| region | avg_s      |
+--------+------------+
| East   |  5266.6667 |
| North  | 12100.0000 |
| South  | 12500.0000 |
| West   | 23833.3333 |
+--------+------------+
4 rows in set (0.00 sec)

mysql> select category, sum(units_sold * unit_price) as sum_s
    -> from sales
    -> group by category
    -> order by sum_s desc;
+---------------+--------+
| category      | sum_s  |
+---------------+--------+
| Electronics   | 768400 |
| Furniture     | 296000 |
| HomeAppliance | 194000 |
+---------------+--------+
3 rows in set (0.00 sec)

mysql> select region, count(product) as sum_s                
    -> from sales 
    -> group by region     
    -> order by sum_s desc;
+--------+-------+
| region | sum_s |
+--------+-------+
| North  |     5 |
| South  |     4 |
| West   |     3 |
| East   |     3 |
+--------+-------+
4 rows in set (0.00 sec)

mysql> select region, sum(units_sold) as sum_s
    -> from sales          
    -> group by region
    -> order by region ;    
+--------+-------+
| region | sum_s |
+--------+-------+
| East   |    41 |
| North  |    51 |
| South  |    28 |
| West   |    18 |
+--------+-------+
4 rows in set (0.00 sec)

mysql> 
'''