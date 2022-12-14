# Files and Resources

<details>
  <summary> General </summary>
  
* Handle tainted file data in a secure manner.
* Store tainted file data obtained from untrusted sources outside the web root and with limited permissions.
</details>

<details>
  <summary> Uploads </summary>
  
* Use an appropriate content security policy (CSP). [OWASP](https://owasp.org/www-community/controls/Content_Security_Policy)
* Place limits on the files such that large files cannot fill up storage and cause a denial of service attack.
* Check compressed files for "zip bombs" -- small input files that decompress into huge files, thus exhausting file storage limits.
* Enforce file size and maximum number of files per user quotas to ensure that a single user cannot fill up the storage with too many files or excessively large files.
</details>

<details>
  <summary> Integrity </summary>
  
* Validate files obtained from untrusted sources to be of an expected type based on the file's content, not just its extension or magic number.
</details>

<details>
  <summary> Execution </summary>
  
* Do not use user-submitted filenames directly with system or framework files and URLs to protect against path traversal.
* Validate or ignore user-submitted filenames to prevent the disclosure, creation, updating, or removal of local or remote files.
* Protect against reflective file download by validating or ignoring user-submitted filenames in a JSON, JSONP, or URL parameter; 
set the response Content-Type header to text/plain, and the Content-Disposition header to a fixed filename.
* Do not use user-submitted filenames directly with system APIs or libraries to protect against OS command injection.
* Do not include and execute functionality from untrusted sources, such as unverified content distribution networks, JavaScript libraries, 
node npm libraries, or server-side DLLs.
</details>

<details>
  <summary> Storage </summary>
  
* Store files from untrusted sources outside the web root, with limited permissions, and with strong validation.
* Scan files obtained from untrusted sources by antivirus scanners to prevent upload of known malicious content.
</details>

<details>
  <summary> Downloads </summary>
  
* If they need to be displayed or downloaded by the system, ensure uploaded files are served:
  * By octet stream downloads
  * From an unrelated domain (e.g. cloud storage)
* Configure the web tier to serve only files with specific file extensions to prevent unintentional information and source code leakage 
(e.g. backup files, temporary working files, compressed files, and other extensions commonly used by editors).
* Never execute direct requests to uploaded files (especially as HTML/JavaScript content).
</details>

<details>
  <summary> Server-Side Request Forgery (SSRF) </summary>
  
* Configure the web or application server with a whitelist of resources or systems to which the server can send requests or load data/files from.
</details>

<details>
  <summary> Example security user stories </summary>
  
* As a user, I want the application to validate that any files or data uploaded do not cause any adverse impact to functionality, data, or access.
</details>
