## where

http://localhost:8080/.hidden/


## Explanation

The `sensitive-directory-disclosure` vulnerability arises when sensitive directories or files are exposed on a web server but are intended to be hidden. Attackers can exploit this by locating and accessing these hidden directories, potentially leading to data leaks or unauthorized access to sensitive information.


It was found exploring the robots.txt file which is a file where the admins usually include urls in the site that should be ignored by the searchers robots.
Then the .hidden/ folder arised.
It had a laberinth of links and a README file in each page.
With a scrapper recursively we explored all links until we found the flag in one README.


## How to prevent

- Delete any paths or URLs leading to sensitive information from the robots.txt file. This file should not be used to hide critical information.

- Implement Authentication: Secure sensitive directories with authentication (e.g., passwords or multi-factor authentication).

- Restrict Access by IP: Consider limiting access to these directories to trusted IPs only.

- Configure Access Permissions: Ensure that only authorized people or processes can access or modify these directories.

- Use HTTPS: Ensure all communication with your site is encrypted using HTTPS.

- Change Control: Keep the robots.txt file in a version control system to monitor any changes.

- Regular Audits: Periodically review the robots.txt file to ensure it does not contain inappropriate information.