## where

http://localhost:8080/index.php?page=recover


## Explanation

Hidden fields in submit forms vulnerability occurs when sensitive information is included in the HTML code of a form but is not visible to the user. Attackers can exploit this vulnerability to manipulate or submit unauthorized data to the server.

In our case we inspected the password recovery button and found a hidden form with an email address.

I just had to change the email for anythong else but in real life we could change for any other email address and may be receive the password in our own address.


## how to prevent

- Avoid storing sensitive information in hidden form fields. Instead, use server-side session management or secure cookies to maintain user state.

- Implement input validation to ensure that only expected and valid data is submitted through forms.

- Use CSRF tokens to protect against cross-site request forgery attacks, which can exploit hidden form fields.

- Sensitive data encryption. 
