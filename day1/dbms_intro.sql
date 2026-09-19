'''
-----day1-----
---26/08/26---

Sysytem Over view

Full Stack --> Front End + Back End

Front End
_________
Front end is the visual and interactive layer of a website or application that users see directly and interact with through a wen browser or mobile app.

Responsibilities of frontend
----------------------------
1.display webpages and user interface(UI)
2.accept user input(forms, buttons, search boxes)
3.validates user input before sending to the server
4.call back end APIs to fetch and send data
5.display the response received from the backend
6.provides animations and interactive effects

Back End
________
Back End is the server-side part of an application, user can't see directly, but it performs all business logic, security, data processing and database operations 
It acts as brain of application

Responsibilities of Back End
---------------------------
Process client request
Implements business logic
Connects with databases
Performs CRUD operations
Authenticates and authorise users
Encrypts Passwords and sensitive data 
generate reports
send emails and notifications
handles file upload and downloads
returns response to the client

API(Application Programming Interface)
______________________________________
An API is a set of rules and protocol that allows two different applications or system to communicate and data exchange without exposing their internal implementation

It act as a bridge between the frontend and backend or two different software systems


Storage Areas
_____________
As a part of our application we required to store some data like customers information, billing information, calls information etc to store this data we required storage areas

there are 2 types of storage areas such as
1.temporary storage areas 
2.permanent storage areas

Temporary storage areas
-----------------------
these are the memory areas where the data will be stored temporarily
eg: All JVM Memory areas(HEAP, stack) once JVM is shutdown all the memory areas will be cleared automatically

Permanent Storage Areas
-----------------------
also known as Persistent Storage Areas, here we can store data Permanently
eg: file systems, databases, data warehouse, big data etc

File Management System(FMS)
___________________________
A file management system is a system where data is stored in files on the operating systems, each application program must handle its own storage data retrival and updating. File system can be provided by the local operating system.

File systems are best suitable for to store very less amount of information(like KB).

example: a library management system storing books in separate text file likes, books.txt, members.txt

Limitations of FMS
------------------
1.Data Redundancy: same data stored in multiple files
2.Data Inconsistency: updates in one file may not be reflected in another
3.Poor Data Security : no proper accessed control
4.Difficult Data Retrieval: searching requires custom programs
5.Intergrity Issues: No contains (eg: roll number is uniqueness)
6.Scalability Issues: hard to manage as data grows

to overcome the above problems of file systems we should go for database

-----DBMS-----
Intro for DBMS
===============

DBMS(Database Management System)
________________________________
A DBMS is a collection of program that enables users to create , manage, and manipulate databases

Advantages
----------
1.We can store huge amount of information in databases
2.Query Language support is available for every databases hence we can perform database operations easily
3.To access data present in the database, compulsory username and password must be required hence data is secured

drawbacks
---------
1.Databases cannot store huge amount of information like(100gb) data
2.database can provide support for only structured data(tabular data or relational data) and cannot provide support for semi structured data like(xml files) and audios and videos

FMS VS DBMS (IMP Q)
___________________
1. data is stored in separate files
   data is stored in structured database

2. high data redundancy(duplicate data)
   reduces data redundancy

3. difficult to maintain and update
   easy to maintain and update

4. security is limited
   providing strong security mechanism

5. data sharing is difficult
   multiple uses can accesses data simultaneously

6. no relationships between tables
   support relationships between tables

7. backup and recovery is difficult
   provides backup and recovery features

8. suitable for small applications
   suitable for small, medium and large applications

Q: what is the difference between a file system and a DBMS?
------------------------------------------------------------
A file system stores data in separate data in separate files and may lead to data redundancy, and security issues, a DBMS stores data in structured manner using tables, reduces redundancy, provides security, supports multiple users, and ensures 


What is data, field, record, database?
---------------------------------------
data: raw facts or figures without context
example: 7, yash

field: smallest unit of data in a database(column/attribute)
example: eno, ename

record: collection of related fields(rows/tuple)
example: (101, 'yash')

Database: organized collection of related records stored together
example: an employee database containing all employee record





'''