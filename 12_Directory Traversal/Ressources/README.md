### where
http://localhost:8080/?page=../../../../../../../etc/passwd

### explanation

It is a vulnerability that allows an attacker to access files and directories outside the web server's root directory. This is achieved by manipulating variables that reference files with character sequences such as ../ (meaning ‘up one directory level’).

By accessing ?page=../../../../../etc/passwd, you are trying to read the /etc/passwd file, which is a system file on UNIX/Linux systems that contains information about users.

### How to Prevent This Vulnerability

1. Validation and Input Restriction
 - Validate the content of variables: Make sure that parameters used to access files are strictly validated. For example, if you expect a filename, verify that the parameter matches an allowed set of files and does not contain characters such as ../ or /.
 - Use whitelisting: Defines a list of allowed files or paths that can be accessed. If the value does not match a file in the list, the request must be rejected.
 - Validate file extension: If only certain types of files should be allowed (e.g. .html or .txt), verify that the requested file has the correct extension.

2. Input Sanitisation
 - Remove or encode special characters: Sanitise user input to remove or encode character sequences such as ../, ../, or %2e%2e (its URL-encoded equivalent). This prevents users from being able to upload directories.
 - Normalise paths: Converts all paths to canonical form before use, which helps eliminate relative paths such as ../ and allows for safer path comparison.

3. Use of Secure Functions
 - Avoid dynamic file inclusion: Avoid using file inclusion based on user input such as include() or require() without strict validation.
 - Control file access: Use functions that limit access to specific files or directories, such as realpath() in PHP, which resolves the absolute path and can be used to verify that the path is within an allowed directory.

4. Secure Server Configuration
 - Set correct permissions: Ensure that the server has correct read/write permissions on files and directories, limiting access to only what is necessary for the application.
 - Jail or chroot: Run the application within a restricted environment (such as a chroot jail) where it can only access a limited set of files and directories.
 - Disable directory listings: Configures the web server not to list directories. This reduces the exposure of files that could be manipulated by Path Traversal.