### where

http://localhost:8080/?page=media&src=nsa

### explanation
When using the URL http://localhost:8080/?page=media&src=data:text/html;base64,PHNjcmlwdD5hbGVydCgiNDIgVXJkdWxpeiIpPC9zY3JpcHQ+

Use the terminal "echo -n '<script>alert(“42 Urduliz”)</script>' | base64"  to get the base64 translation of the script.

- Base64 Handling:
    - The src parameter accepts base64 encoded data with the MIME type text/html, which the application decodes and processes as HTML.
- Execution of JavaScript:
    - Because the HTML included JavaScript (<script>alert("42 Urduliz")</script>), the browser executed this script, leading to the discovery of the flag.

### How to Prevent This Vulnerability:

- Sanitize Input:
    - Ensure that all HTML content passed through URL parameters is sanitized to remove any potential script tags or JavaScript code.
- Implement Content Security Policy (CSP):
    - Use CSP headers to restrict the sources from which scripts can be loaded and executed, reducing the risk of XSS attacks.
- Validate and Restrict Content Types:
    - Allow only specific, expected content types. If only images are expected, restrict the src parameter to image data only, not HTML.
- Security Headers:
    - Use headers like X-Content-Type-Options: nosniff to prevent browsers from interpreting content types incorrectly.
