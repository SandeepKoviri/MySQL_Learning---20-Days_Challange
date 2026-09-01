'''
SQL:
----
-->Structured query language is standardized programming language specially designed for managing and manipulating relational databases.it provides declarative syntax that allows users to define data they want retrieve, insert, update or delete without specifying exactly how database should execute these operations.

SQL Commands:
-------------
DDL: Data Definition Language -> Defines and modifies structure of a database objects(tables, schemas, indexes)

DML: Data Manipulation Language -> Manages data stores with in database objects (insert, update, delete)

DQL: Data Query Language -> Used to fetch/retrieve data from database.

TCL: Transaction Control Language -> Manage Transactions to maintain data integrity

DCL: Data Control Language -> Manage permissions and access control on database objects.

DDL Commands:
-------------
1.CREATE: 
---------
--> Used to create N number of things like (database, table, trigger,etc...)

Database --> syntax --> CREATE DATABASE DATABASE_NAME;
Table --> syntax --> CREATE TABLE TABLE_NAME(FIELD_NAME DATATYPE(SIZE),FIELD_NAME DATATYPE(SIZE),....);

2.ALTER:
-------
--> Used to modify the columns in the table.


3.TRUNCATE:
-----------
4.RENAME:
---------

DML Commands:
-------------
INSERT
UPDATE
DELETE

DQL Commands:
-------------
SELECT

today examples input,syntax,outputs
    ===================================================


mysql> student int,
    -> create table students(
    -> empid char(7),
    -> fname varchar(50),
    -> lname varchar(40),
    -> age int,
    -> marks int,
    -> percentage int,
    -> student id int,
    -> student address varchar(100),
    -> dept varchar(50),
    -> );

mysql> to show the table description
    -> ^C
mysql> show columns from students;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| empid   | char(5)      | YES  |     | NULL    |       |
| fname   | varchar(100) | YES  |     | NULL    |       |
| lname   | varchar(30)  | YES  |     | NULL    |       |
| age     | int          | YES  |     | NULL    |       |
| doj     | date         | YES  |     | NULL    |       |
| address | tinytext     | YES  |     | NULL    |       |
| dept    | varchar(20)  | YES  |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+
7 rows in set (0.05 sec)

mysql> -- modify the fname column in employee table to varchar(70)
mysql> -- syntax:- alter table table-name modify colomn-name datatype size;
mysql> alter table students modify fname varchar(70);
Query OK, 0 rows affected (0.19 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc students;
+---------+-------------+------+-----+---------+-------+
| Field   | Type        | Null | Key | Default | Extra |
+---------+-------------+------+-----+---------+-------+
| empid   | char(5)     | YES  |     | NULL    |       |
| fname   | varchar(70) | YES  |     | NULL    |       |
| lname   | varchar(30) | YES  |     | NULL    |       |
| age     | int         | YES  |     | NULL    |       |
| doj     | date        | YES  |     | NULL    |       |
| address | tinytext    | YES  |     | NULL    |       |
| dept    | varchar(20) | YES  |     | NULL    |       |
+---------+-------------+------+-----+---------+-------+
7 rows in set (0.01 sec)

mysql> alter table employee modify lname(40);

mysql> alter table students modify lname varchar(100);
Query OK, 0 rows affected (0.11 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> -- add a new column name named with location of type tinytext to the students table.
mysql> -- syntax:- alter table table-name add colomn-name datatype(size)
mysql> alter table students add location tinytext;
Query OK, 0 rows affected (0.10 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc students;
+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| empid    | char(5)      | YES  |     | NULL    |       |
| fname    | varchar(70)  | YES  |     | NULL    |       |
| lname    | varchar(100) | YES  |     | NULL    |       |
| age      | int          | YES  |     | NULL    |       |
| doj      | date         | YES  |     | NULL    |       |
| address  | tinytext     | YES  |     | NULL    |       |
| dept     | varchar(20)  | YES  |     | NULL    |       |
| location | tinytext     | YES  |     | NULL    |       |
+----------+--------------+------+-----+---------+-------+
8 rows in set (0.00 sec)

mysql> -- to add a column alter a particular column
mysql> alter table table-name add colomn-name after specified-column name(size)
    -> ^C
mysql> -- syntax:- alter table table-name add  column-name after specified-column name
mysql> alter table students add pfid int after address;
Query OK, 0 rows affected (0.09 sec)
Records: 0  Duplicates: 0  Warnings: 0

mysql> desc students;
+----------+--------------+------+-----+---------+-------+
| Field    | Type         | Null | Key | Default | Extra |
+----------+--------------+------+-----+---------+-------+
| empid    | char(5)      | YES  |     | NULL    |       |
| fname    | varchar(70)  | YES  |     | NULL    |       |
| lname    | varchar(100) | YES  |     | NULL    |       |
| age      | int          | YES  |     | NULL    |       |
| doj      | date         | YES  |     | NULL    |       |
| address  | tinytext     | YES  |     | NULL    |       |
| pfid     | int          | YES  |     | NULL    |       |
| dept     | varchar(20)  | YES  |     | NULL    |       |
| location | tinytext     | YES  |     | NULL    |       |
+----------+--------------+------+-----+---------+-------+
9 rows in set (0.00 sec)

mysql> how to add new column in first
    -> ^C
mysql> -- how to add new column in first.
mysql> alter table table-name add  column-name datatype(size)first;
mysql> alter table table-name add  column-name datatypes(size)first;
mysql> -- syntax:- alter table table-name drop column column-name
mysql> alter table students drop column age
    -> ^C
mysql> alter table students drop column location
    -> ^C
mysql> alter table students drop column location;
Query OK, 0 rows affected (0.08 sec)
Records: 0  Duplicates: 0  Warnings: 0

 
mysql> desc students;
+---------+--------------+------+-----+---------+-------+
| Field   | Type         | Null | Key | Default | Extra |
+---------+--------------+------+-----+---------+-------+
| empid   | char(5)      | YES  |     | NULL    |       |
| fname   | varchar(70)  | YES  |     | NULL    |       |
| lname   | varchar(100) | YES  |     | NULL    |       |
| age     | int          | YES  |     | NULL    |       |
| doj     | date         | YES  |     | NULL    |       |
| address | tinytext     | YES  |     | NULL    |       |
| pfid    | int          | YES  |     | NULL    |       |
| dept    | varchar(20)  | YES  |     | NULL    |       |
+---------+--------------+------+-----+---------+-------+
8 rows in set (0.00 sec)

mysql> alter table students drop column location,drop column pfid;
ERROR 1091 (42000): Can't DROP 'location'; check that column/key exists
'''