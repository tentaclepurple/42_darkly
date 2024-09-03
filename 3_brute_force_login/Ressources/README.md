## where

http://localhost:8080/index.php?page=signin


## Explanation

A brute force attack is a hacking technique used to gain unauthorized access to a system by trying every possible combination of usernames and passwords until the correct one is found. This method relies on the sheer force of computing power to systematically check all possible combinations.

In some cases, attackers may employ techniques to evade detection or bypass security measures, such as slowing down the rate of login attempts to avoid triggering account lockout policies.

In this case we used a list of the most commonly used usernames and passwords and rely on a python script to make http requests,

http://127.0.0.1:8080/?page=signin&username={username}&password={password}&Login=Login#

until we found the correct username and password combination.

- username: admin
- password: shadow


## How to prevent

- Use complex passwords. A mix of uppercase, lowercase, numbers and special characters is preferred

- Implement a number of tries. After a given number of wrong tries the access is blocked.

- Use a CAPTCHA to avoid bots or scripts

- Introduce a 2FA. A two factor authentication on the login stage layer like authentication app, email or mobile code verification gives an extra protection against attacks
