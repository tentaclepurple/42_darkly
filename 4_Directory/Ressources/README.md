### where

http://localhost:8080/admin
http://localhost:8080/whatever

### explanation

I used Gobuster to enumerate directories on the web server and discovered several directories. Notably, I found:

    A login page at /admin.
    An htpasswd file in the /whatever directory.
    
The htpasswd file contained an MD5 hash.

I identified that this hash translates to the password qwerty123@ using an MD5 hash decoder. This password is associated with the root user. I used this information to access the system and find a flag, demonstrating a security vulnerability.

To enhance my directory enumeration, I downloaded an updated wordlist for Gobuster using the following wget command:
    wget https://raw.githubusercontent.com/danielmiessler/SecLists/master/Discovery/Web-Content/directory-list-2.3-medium.txt -P /your/download/address


### Solution:

- Protect Sensitive Files:
    - Issue: The htpasswd file was publicly accessible in the /whatever directory.
    - Solution: I should restrict access to sensitive files. Ensure that files containing authentication information or other sensitive data are stored in directories that are not publicly accessible.
- Implement Proper Access Controls:
    - Issue: Sensitive directories and files were exposed without proper access controls.
    - Solution: I need to implement proper access controls to ensure that sensitive areas of the application are only accessible to authorized users. Use web server configurations to restrict access to directories like /admin and files like htpasswd.
