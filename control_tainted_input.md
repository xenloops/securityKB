# Validation, Sanitization, and Output Encoding

<details>
  <summary>
    Tainted input: General
  </summary>

  * Ensure input validation and output encoding have a common architecture to prevent injection attacks.
  * Verify that input data is strongly typed, validated, range or length checked, and sanitized or filtered.
  * Encode or escape output data for the context of the data as close to the output interpreter as possible.
</details>

<details>
  <summary>
    Tainted input: Input Validation
  </summary>
  
  * Defend against HTTP parameter pollution attacks, particularly if the application framework makes no distinction about the source of request parameters.
  * Protect against mass parameter assignment attacks and against unsafe parameter assignment.
  * Validate all input using positive validation (whitelisting), including HTML form fields, REST requests, URL parameters, HTTP headers, cookies, batch files, RSS feeds, etc.).
  * Strongly type structured data and validate against a defined schema including allowed characters, length and pattern.
  * Allow only whitelisted destinations for URL redirects and forwards, or warn when redirecting to potentially untrusted content.
</details>

<details>
  <summary>
    Tainted input: Sanitization and Sandboxing
  </summary>
  
  * Properly sanitize:
    * All user input.
    * All untrusted HTML input from WYSIWYG editors or similar with a vetted library or framework feature.
    * Unstructured data and enforce safety measures such as allowed characters and length.
  * Avoid the use of dynamic code execution features (e.g. eval() ). When there is no alternative, sanitize or sandbox any user input being included before being executed.
  * Validate or sanitize untrusted data or HTTP file metadata, such as filenames and URL input fields.
  * Use whitelisting of protocols, domains, paths, and ports.
  * Sanitize, disable, or sandbox user-supplied:
    * SVG scriptable content.
    * Scripting or expression template language content (e.g. Markdown, CSS or XSL stylesheets, or BBCode).
</details>

<details>
  <summary>
    Tainted input: Output Encoding
  </summary>
  
  * Use output encoding relevant for the interpreter and context required (e.g. for HTML values, HTML attributes, JavaScript, URL Parameters, 
  HTTP headers, or SMTP).
  * Preserve the user's chosen character set and locale, such that any Unicode character point is valid and safely handled.
  * Use context-aware output escaping.
  * Use parameterized queries, ORMs, or entity frameworks for database queries.
    * Where parameterized queries cannot be used, use context-specific output encoding.
  * Protect against JavaScript and JSON injection attacks:
    * For eval
    * Remote JavaScript includes
    * CSP bypasses
    * DOM XSS
    * JavaScript expression evaluation
  * Protect against LDAP Injection.
  * Protect against OS command injection; use:
    * Parameterized OS queries for operating system calls
    * Contextual command line output encoding
  * Protect against Local File Inclusion (LFI) or Remote File Inclusion (RFI) attacks.
  * Protect against XPath injection or XML injection attacks
</details>

<details>
  <summary>
    Tainted input: Unmanaged Code
  </summary>
  
  * Use memory-safe String functionality.
  * Use safe memory copy and pointer arithmetic functionality.
  * Handle format strings as constant.
  * Use sign, range, and input validation techniques to prevent integer overflows.
</details>

<details>
  <summary>
    Tainted input: Deserialization Prevention
  </summary>
  
  * 
</details>

<details>
  <summary>
    Tainted input: 
  </summary>
  
  * 
</details>

<details>
  <summary>
    Tainted input: 
  </summary>
  
  * 
</details>

