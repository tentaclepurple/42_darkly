### where
The Cookie:

    Cookie Name: i_am_admin
    Cookie Value: 68934a3e9455fa72420237eb05902327
    
### explanation
Cookie Name: The name i_am_admin suggests that this cookie might be related to administrative privileges. It indicates whether a user is an admin or not.Cookie Value: The value 68934a3e9455fa72420237eb05902327 appears to be a hash. Specifically, it is an MD5 hash of the word "false".

This suggests that the cookie is being used to determine the user's admin status, with the value "false" indicating they are not an admin.

If you can modify the value of this cookie, you could try changing it to the MD5 hash of "true": 

    MD5 Hash of "true": b326b5062b2f0e69046810717534cb09

Changing the cookie value to b326b5062b2f0e69046810717534cb09 could make the application recognize you as an admin. This indicates a vulnerability related to authorization because the app relies on an easily manipulated cookie for critical security checks.

### How to Prevent This Vulnerability

- Do Not Rely on Cookies for Authorization:
    - Cookies should not store sensitive or critical information like user roles or privileges that can be easily modified by the client.
- Use Secure Tokens:
    - Implement secure tokens, such as signed JWTs (JSON Web Tokens), which include integrity checks to prevent tampering.
- Encrypt Sensitive Data:
    - Avoid using weak hashes like MD5 for sensitive data. Use stronger algorithms like SHA-256 and always combine them with a salt to prevent dictionary attacks.
