---
title: Operations of the Relational Model
authors: Alessandro Dorigo
tags:
  -
---

## Types of Operations

> [!info]+ **Data Definition Language (DDL)**
>  DDL is a subset of SQL used to define and manage the structure of database objects in a relational database. DDL statements enable database administrators and developers to create, modify, and remove database structures rather than the data itself.
>  It operates at the schema level of the database, providing commands to define the containers (relations/tables, views, etc.) in which data will be stored, and the rules governing that data.

> [!info]+ Data Manipulation Language
> **DML** refers to the component of SQL that enables users to interact with and manipulate data stored in a relational database. DML provides operations for retrieving, inserting, updating, and deleting data within database objects without changing their structure or schema.
>
> Unlike DDL which defines database structure, DML focuses on the content stored within th

> [!info]+ Update operations
> - Update of tuples in the current value of a relation (insert, delete, modify)
> - Update of the schema: create or delete a relation, add or suppress an attribute

> [!tip]+ Remarque
> Options for tuple insertion and tuple suppression can be specified declaratively in the database schema of current RDBMSs
