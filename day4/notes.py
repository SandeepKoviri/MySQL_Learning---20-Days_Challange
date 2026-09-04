'''
DML: Data Manipulation Language --> manages data stored within database objects(insert, update, delete)

--------------
INSERT
------
approach
--------
syntax
------
insert into table-name(column-name1, column-name1,.........,column-name-n)
values
(value1,value2,.......,value-n);

example
-------
INSERT INTO EMPLOYEES
(EMPID,FIRSTNAME, LASTNAME, AGE, DOJ, ADDRESS, DEPT)
VALUES
(7, 'SANDEEP','RAJANA', 21, '2026-07-11','VIZAG','TRAINEE')

INSERT INTO EMPLOYEES
(EMPID,FIRSTNAME, LASTNAME, AGE, DOJ, ADDRESS, DEPT)
VALUES
(1, 'RAJ','SANDY', 21, '2026-07-11','VIZAG','TRAINEE');


UPDATE
------
Syntax
------
UPDATE TABLE-NAME SET COLUMN-NAME=VALUE WHERE CONDITION

DELETE
------
Syntax
------
DELETE FROM TABLE-NAME WHERE CONDITION


DDL
___
TRUNCATE
--------
Syntax
------
TRUNCATE TABLE TABLE_NAME;


DROP VS DELETE VS TRUNCATE
__________________________
Delete: based on some condition delete the records

truncate : to delete all present records present in a table

drop: it drops the entire table and structure


DCL
---

GRANT, REVOKE

mysql> CREATE USER 'SANDY' IDENTIFIED BY 'SANDEEP25';
Query OK, 0 rows affected (0.08 sec)

mysql> CREATE USER 'RAJ' IDENTIFIED BY 'RAJANA';
Query OK, 0 rows affected (0.01 sec)


mysql> GRANT SELECT, UPDATE, DELETE ON STUDENTS TO RAJ;
Query OK, 0 rows affected (0.02 sec)

mysql> GRANT INSERT, DROP ON STUDENTS TO SANDY;
Query OK, 0 rows affected (0.01 sec)


'''