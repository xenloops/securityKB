# Code vulnerabilities

Many vulnerabilities can be remediated where they begin -- in code. 

<details>
  <summary> SQL injection (SQLi) </summary>
  
  **Problem:** A SQL injection attack consists of insertion or "injection" of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data, execute administration operations on the database, recover the content of a given file present on the DBMS file system, and in some cases issue commands to the operating system. [OWASP](https://owasp.org/www-community/attacks/SQL_Injection)

  **Solutions:** Use parameterized queries, use stored procedures, validate input, or escape tainted input. [OWASP SQLi Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

  ### Choice 1: Prepared statements with parameterized queries
  
  Prepared statements with variable binding (parameterized queries) force developers to first define all the SQL code, then pass each parameter to the query. This allows the database to distinguish between code and data, regardless of what user input is supplied. Prepared statements ensure that an attacker is not able to change the intent of a query, even if they insert SQL commands. [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html)

  #### Java
  ```
  String sql = "SELECT * FROM User WHERE userId = ?"; 
  PreparedStatement stmt = con.prepareStatement(sql); 
  stmt.setString(1, userId); 
  ResultSet rs = prepStmt.executeQuery();
  ```

  #### C#

  ```
  String query = "SELECT account_balance FROM user_data WHERE user_name = ?";
  try {
    OleDbCommand command = new OleDbCommand(query, connection);
    command.Parameters.Add(new OleDbParameter("customerName", CustomerName Name.Text));
    OleDbDataReader reader = command.ExecuteReader();
  } catch (OleDbException se) {
    // error handling
  }
  ```

  ### Choice 2: stored procedures 
  
  Not always safe from SQL injection, standard stored procedure programming constructs have the same effect as the use of parameterized queries when implemented safely, which is the norm for most stored procedure languages.

  #### Java
  
  ```
  // After validating tainted input:
  String custname = request.getParameter("customerName");
  try {
    CallableStatement cs = connection.prepareCall("{call sp_getAccountBalance(?)}");
    cs.setString(1, custname);
    ResultSet results = cs.executeQuery();
    // result set handling
  } catch (SQLException se) {
    // error handling
  }
  ```
</details>

<details>
  <summary> Cross-Site Scripting (XSS) </summary>
  
  **Problem:** XSS is a type of code injection in which malicious scripts are inserted into otherwise trusted websites. In an XSS attack an attacker uses a web application to send malicious code, generally in the form of a browser-side script, to a different user. [OWASP](https://owasp.org/www-community/attacks/xss)
  
  Note that there are three types: **reflected** just appears in the browser, **stored** is written to a database, and **DOM-based** modifies the DOM environment in the victim's browser. What matters is that all are bad and can be used in conjunction with other attacks.

  **Solutions:** Use modern web frameworks, sanitize tainted input, encode output. [OWASP XSS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

  ### Use modern web frameworks
  
  Modern frameworks encourage good security practices and help mitigate XSS by using defenses such as templating and auto-escaping. Developers still need to be aware of problems that can occur when using frameworks insecurely, and where gaps in their frameworks exist.
  
  ### Encode output
  
  Use output encoding to safely display user input as entered. Do not interpret variables as code. Use the framework's default output encoding protection. Note that output must be encoded for the context in which it appears, e.g.: 
  
  * HTML body, e.g. ```<div>TAINT</div>``` (validate and encode where needed)
  * HTML entities, e.g. ```<span>TAINT</span>``` (encode: convert & to ```&amp;```, < to ```&lt;```, > to ```&gt;```, " to ```&quot;```, ' to ```&#x27;```, and / to ```&#x2F;```)
  * HTML attributes, e.g. ```<input type="text" name="fname" value="TAINT">``` (replace all characters except alphanumeric with the HTML Entity ```&#xHEX;``` format, including spaces)
  * URLs and URLs in attributes, e.g. ```<a href="URL TAINT ">Click here!</a> <iframe src="URL TAINT " />``` (canonicalize input, validate the URL, use [standard percent encoding](https://www.w3schools.com/tags/ref_urlencode.asp) to encode only parameter values)
  * JavaScript (replace all characters except alphanumeric characters with the \uXXXX [Unicode encoding format](https://www.unicode.org/charts))
  * DOM, e.g. ```<script>document.write("TAINTED INPUT: " + document.location.hash );<script/>``` (see the [DOM based XSS Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html))
  * CSS (use the ```\XX``` or ```\XXXXXX``` formats to encode where needed)

  ### Sanitize tainted input
  
  If a user absolutely needs to write HTML within the application (as for a WYSIWYG editor), use an HTML sanitization utility. Remember to sanitize _after_ making any changes to the input (or sending to a library that modifies it); this may invalidate the security effort.
  
  ### Tools
  
  * [OWASP Java Encoder](https://owasp.org/www-project-java-encoder)
  * [OWASP Java HTML Sanitizer](https://owasp.org/www-project-java-html-sanitizer)
  * [OWASP Enterprise Security API (ESAPI)](https://owasp.org/www-project-enterprise-security-api)
  * [DOMPurify](https://github.com/cure53/DOMPurify)
  * [JSoup Java HTML Parser](https://jsoup.org)
  * [OWASP AntiSamy](https://owasp.org/www-project-antisamy)
  
</details>

<details>
  <summary> Cross-Site Request Forgery (CSRF) </summary>

  **Problem:** A CSRF attack forces a user to execute unwanted actions on a web application in which they're currently authenticated. With some social engineering (e.g. sending a link via email or chat), an attacker may trick the user into doing the attacker's bidding. If the victim is a normal user, this can mean transferring funds, changing the user's email address, etc. If the victim is an administrative user, CSRF can compromise the application. [OWASP](https://owasp.org/www-community/attacks/csrf)
  
  **Solutions:** See the following recommendations. [OWASP CSRF Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

  * Use the framework's CSRF protections if it has any (many modern frameworks do).
    * If it doesn't, add [CSRF tokens](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#token-based-mitigation) to all state changing requests and validate them on the backend.
  * For stateful software, use the [synchronizer token pattern](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#synchronizer-token-pattern).
  * For stateless software, use [double submit cookies](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#double-submit-cookie).
  * Avoid using GET requests for state-changing operations.
  * Do at least one of:
    * Use a [SameSite Cookie Attribute](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#samesite-cookie-attribute) for session cookies (but watch its use with an untrusted domain).
    * Implement [user interaction based protection](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#user-interaction-based-csrf-defense) for highly sensitive operations.
    * Use [custom request headers](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#use-of-custom-request-headers).
    * Verify the origin with [standard headers](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html#verifying-origin-with-standard-headers).
  
</details>
  

<details>
  <summary> Authoritative sources </summary>
  
* Java: [Secure Coding Guidelines for Java SE (Oracle)](https://www.oracle.com/java/technologies/javase/seccodeguide.html)
  
</details>
  
