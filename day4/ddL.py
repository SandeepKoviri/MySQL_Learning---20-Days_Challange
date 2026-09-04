'''
alter countintation 

rename:
Enter password: ****************
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.42 MySQL Community Server - GPL

Copyright (c) 2000, 2025, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| da5                |
| env1               |
| information_schema |
| mysql              |
| myuser1            |
| performance_schema |
| pfs5               |
| pharmaguard_db     |
| sandeep            |
| sys                |
+--------------------+
10 rows in set (0.01 sec)

mysql> use pfs5;
Database changed
mysql> show tables;
+----------------+
| Tables_in_pfs5 |
+----------------+
| students       |
+----------------+
1 row in set (0.00 sec)

mysql> desc students
    -> desc students;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'desc students' at line 2
mysql> desc students;
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| s_no            | int          | YES  |     | NULL    |       |
| empid           | char(7)      | YES  |     | NULL    |       |
| fname           | varchar(70)  | YES  |     | NULL    |       |
| lname           | varchar(40)  | YES  |     | NULL    |       |
| age             | int          | YES  |     | NULL    |       |
| marks           | int          | YES  |     | NULL    |       |
| percentage      | int          | YES  |     | NULL    |       |
| student_id      | int          | YES  |     | NULL    |       |
| student_address | varchar(100) | YES  |     | NULL    |       |
| dept            | varchar(50)  | YES  |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
10 rows in set (0.00 sec)

mysql> ALTER TABLE students RENAME TO employees;           
Query OK, 0 rows affected (0.04 sec)

mysql> show tables;
+----------------+
| Tables_in_pfs5 |
+----------------+
| employees      |
+----------------+
1 row in set (0.00 sec)

mysql> -- syntex: alter table table_name CHNAGE OLD-COLUMN-NAME NEW-COLUMN-NAME DATATYPE SIZE
mysql> -- CHANGE COLUMN NAME
mysql> ALTER TABLE EMPLOYEES CHANGE FNAME FIRST_NAME VARCHAR(100);
Query OK, 0 rows affected (0.02 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> ALTER TABLE EMPLOYEES CHANGE LNAME SECOND_NAME VARCHAR(100);
Query OK, 0 rows affected (0.10 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DECS EMPLOYEES;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'DECS EMPLOYEES' at line 1
mysql> DESC EMPLOYEES;
+-----------------+--------------+------+-----+---------+-------+
| Field           | Type         | Null | Key | Default | Extra |
+-----------------+--------------+------+-----+---------+-------+
| s_no            | int          | YES  |     | NULL    |       |
| empid           | char(7)      | YES  |     | NULL    |       |
| FIRST_NAME      | varchar(100) | YES  |     | NULL    |       |
| SECOND_NAME     | varchar(100) | YES  |     | NULL    |       |
| age             | int          | YES  |     | NULL    |       |
| marks           | int          | YES  |     | NULL    |       |
| percentage      | int          | YES  |     | NULL    |       |
| student_id      | int          | YES  |     | NULL    |       |
| student_address | varchar(100) | YES  |     | NULL    |       |
| dept            | varchar(50)  | YES  |     | NULL    |       |
+-----------------+--------------+------+-----+---------+-------+
10 rows in set (0.00 sec)

mysql> -- CHANGE TABLE NAME
mysql> -- SYNTEX: ALTER TABLE OLD_TABLE-NAME RENAME TO NEW_TABLE-NAME;
mysql> ALTER TABLE EMPLOYEES RENAME TO CODEGANE_EMP;
Query OK, 0 rows affected (0.04 sec)

mysql> -- NEED TO CHANGE AGAIN TO EMP
mysql> SHOW TABLES;    
+----------------+
| Tables_in_pfs5 |
+----------------+
| codegane_emp   |
+----------------+
1 row in set (0.00 sec)

mysql> ALTER TABLE CODEGANE_EMP RENAME TO EMP;
Query OK, 0 rows affected (0.04 sec)

mysql> SHOW TABLES;
+----------------+
| Tables_in_pfs5 |
+----------------+
| emp            |
+----------------+
1 row in set (0.00 sec)

mysql> CREATE TABLE STUDENTS;
ERROR 4028 (HY000): A table must have at least one visible column.
mysql>     -> create table students(
    ->     -> empid char(7),
    ->     -> fname varchar(50),
    ->     -> lname varchar(40),
    ->     -> age int,
    ->     -> marks int,
    ->     -> percentage int,
    ->     -> student id int,
    ->     -> student address varchar(100),
    ->     -> dept varchar(50),
    ->     -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near '-> create table students(
    -> empid char(7),
    -> fname varchar(50),
    ->' at line 1
mysql> SHOW TABLES;                        
+----------------+
| Tables_in_pfs5 |
+----------------+
| emp            |
+----------------+
1 row in set (0.00 sec)

mysql> CREAT TABLE STUDENTS(
    -> STUID CHAR(7),
    -> FNAME VARCHAR(40),
    -> LNAME VARCHAR(50),
    -> AGE INT,
    -> MARKS INT,
    -> DEPT VARCHAR(50),
    -> STUDENT_ADD VARCHAR(100)
    -> );
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'CREAT TABLE STUDENTS(
STUID CHAR(7),
FNAME VARCHAR(40),
LNAME VARCHAR(50),
AGE I' at line 1
mysql> CREATE TABLE STUDENTS ( 
    -> STUID CHAR(7),          
    -> FNAME VARCHAR(40),                  
    -> LNAME VARCHAR(50),
    -> AGE INT,
    -> MARKS INT,
    -> DEPT VARCHAR(50),
    -> STUDENT_ADD VARCHAR(100)
    -> );
Query OK, 0 rows affected (0.04 sec)

mysql> SHOW TABLES;
+----------------+
| Tables_in_pfs5 |
+----------------+
| emp            |
| students       |
+----------------+
2 rows in set (0.00 sec)

mysql> ALTER TABLE STUDENTS MODIFY STUDENT_ADD TINYTEXT;
Query OK, 0 rows affected (0.09 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> DESC STUDENTS;
+-------------+-------------+------+-----+---------+-------+
| Field       | Type        | Null | Key | Default | Extra |
+-------------+-------------+------+-----+---------+-------+
| STUID       | char(7)     | YES  |     | NULL    |       |
| FNAME       | varchar(40) | YES  |     | NULL    |       |
| LNAME       | varchar(50) | YES  |     | NULL    |       |
| AGE         | int         | YES  |     | NULL    |       |
| MARKS       | int         | YES  |     | NULL    |       |
| DEPT        | varchar(50) | YES  |     | NULL    |       |
| STUDENT_ADD | tinytext    | YES  |     | NULL    |       |
+-------------+-------------+------+-----+---------+-------+
7 rows in set (0.00 sec)

NOTES:
DML(DATA MANIPULATION LANGUAGE):
-------------------------------
INSERT 

approch:        #column_name,field_name both same
-------
syntex: 
INSERT INTO TABLE_NAME(column_NAME,FIELD_NAME,...) VALUES (VALUE,VALUE,...);

example:
--------
mysql> insert into emp(s_no,empid,first_name,second_name,age,dept) values(1001,'emp001','koviri','sandeep',24,'IT');
mysql> insert into emp(s_no,empid,first_name,second_name,age,dept) values(1002,'emp002','jagga','bunny',24,'IT');

Query OK, 1 row affected (0.01 sec)

mysql> select * from emp;
+------+--------+------------+-------------+------+-------+------------+------------+-----------------+------+
| s_no | empid  | FIRST_NAME | SECOND_NAME | age  | marks | percentage | student_id | student_address | dept |
+------+--------+------------+-------------+------+-------+------------+------------+-----------------+------+
| 1001 | emp001 | koviri     | sandeep     |   24 |  NULL |       NULL |       NULL | NULL            | IT   |
| 1002 | emp002 | jagga      | bunny       |   24 |  NULL |       NULL |       NULL | NULL            | IT   |
+------+--------+------------+-------------+------+-------+------------+------------+-----------------+------+
2 rows in set (0.00 sec)

mysql> insert into emp(s_no,empid,fname,second_name,age,dept) values(1003,'emp003','B','nirup',24,'IT');

mysql> create table employees (
    -> s_no int, 
    -> emp_id char(7),   
    -> fname varchar(40),
    -> lname varchar(50),
    -> age int,
    -> DOB date, 
    -> dept varchar(50)
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> insert into employees (s_no,emp_id,fname,lname,age,dob,dept) values(1001,'emp001','koviri','sandeep',24,'2000-01-01','IT');

insert into employees (s_no,emp_id,fname,lname,age,dob,dept) values(1002,'emp002','jagga','bunny',24,'2000-01-01','IT');

insert into employees (s_no,emp_id,fname,lname,age,dob,dept) values(1003,'emp003','K','nirup',24,'2000-01-01','IT'),(1004,'emp004','K','sana',24,'2000-01-01','IT'),(1005,'emp005','K','anusha',24,'2000-01-01','IT');

mysql> select * from employees;
+------+--------+--------+---------+------+------------+------+
| s_no | emp_id | fname  | lname   | age  | DOB        | dept |
+------+--------+--------+---------+------+------------+------+
| 1001 | emp001 | koviri | sandeep |   24 | 2000-01-01 | IT   |
| 1002 | emp002 | jagga  | bunny   |   24 | 2000-01-01 | IT   |
| 1003 | emp003 | K      | nirup   |   24 | 2000-01-01 | IT   |
| 1004 | emp004 | K      | sana    |   24 | 2000-01-01 | IT   |
| 1005 | emp005 | K      | anusha  |   24 | 2000-01-01 | IT   |
+------+--------+--------+---------+------+------------+------+
5 rows in set (0.00 sec)



update:
----------

syntex:
-------
update table_name set column_name = value where condition;

update employees set age = 25 where emp_id = 'emp003';
mysql> update employees set age = 25 where emp_id = 'emp003';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from employees;
+------+--------+--------+---------+------+------------+------+
| s_no | emp_id | fname  | lname   | age  | DOB        | dept |
+------+--------+--------+---------+------+------------+------+
| 1001 | emp001 | koviri | sandeep |   24 | 2000-01-01 | IT   |
| 1002 | emp002 | jagga  | bunny   |   24 | 2000-01-01 | IT   |
| 1003 | emp003 | K      | nirup   |   25 | 2000-01-01 | IT   |
| 1004 | emp004 | K      | sana    |   24 | 2000-01-01 | IT   |
| 1005 | emp005 | K      | anusha  |   24 | 2000-01-01 | IT   |
+------+--------+--------+---------+------+------------+------+
5 rows in set (0.00 sec)


mysql> update employees set address = 'HYD' where emp_id = 'emp003';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update employees set address = 'VSKP' where emp_id = 'emp001';
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> update employees set address = 'VJY' where emp_id = 'emp002'; 
Query OK, 1 row affected (0.01 sec)
Rows matched: 1  Changed: 1  Warnings: 0

mysql> select * from employees;
+------+--------+--------+---------+------+------------+------+---------+
| s_no | emp_id | fname  | lname   | age  | DOB        | dept | address |
+------+--------+--------+---------+------+------------+------+---------+
| 1001 | emp001 | koviri | sandeep |   24 | 2000-01-01 | IT   | VSKP    |
| 1002 | emp002 | jagga  | bunny   |   24 | 2000-01-01 | IT   | VJY     |
| 1003 | emp003 | K      | nirup   |   25 | 2000-01-01 | IT   | HYD     |
| 1004 | emp004 | K      | sana    |   24 | 2000-01-01 | IT   | NULL    |
| 1005 | emp005 | K      | anusha  |   24 | 2000-01-01 | IT   | NULL    |
+------+--------+--------+---------+------+------------+------+---------+
5 rows in set (0.00 sec)


delete
------
syatex:
------
delete from table_name where condition;

delete from employees where emp_id = 'emp004';    


truncate:
-------
syntex:
---------
truncate table table_name;

truncate table employees;

'''

