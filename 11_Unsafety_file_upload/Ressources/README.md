## Where

http://localhost:8080/index.php?page=upload


## Explanation

This vulnerability allow attackers to upload malicious files to the server.

We can upload a potentially malicious file with curl modifiying MIME type. In this case we uploaded a php file.

curl -X POST -F "Upload=Upload" -F "uploaded=@file.php;type=image/jpeg" "http://127.0.0.1:8080/index.php?page=upload" | grep 'The flag is :'

This works because in this case the file type checked in backend is the one provided in request, not over the file itself

The response indicated that the file was successfully uploaded, and the flag was retrieved, demonstrating the exploitation of the file upload vulnerability


## How to prevent

- File size limit. Set a maximum file size and number of files that can be uploaded

- Ensure that the MIME type of uploaded files matches expected types for the allowed extensions, adding an additional layer of validation.

- File names can have dangerous characters that may lead to injection attacks so they should be sanitized.

- Implement server-side validation to ensure only files with approved extensions are uploaded.

More resources

https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload#Prevention_Methods_.28Solutions_to_be_more_secure.29