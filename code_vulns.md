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

  **Solutions:** Use modern web frameworks, sanitize tainted input, encode output. [OWASP XSS Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

  ### Use modern web frameworks
  
  Modern frameworks encourage good security practices and help mitigate XSS by using defenses such as templating and auto-escaping. Developers still need to be aware of problems that can occur when using frameworks insecurely, and where gaps in their frameworks exist.
  
  ### Encode output
  
  Use output encoding to safely display user input as entered. Do not interpret variables as code. Use the framework's default output encoding protection. Note that output must be encoded for the context in which it appears, e.g.: 
  
  * HTML entities (convert & to ```&amp;```, < to ```&lt;```, > to ```&gt;```, " to ```&quot;```, ' to ```&#x27;```, and / to ```&#x2F;```)
  * HTML attributes (replace all characters except alphanumeric with the HTML Entity ```&#xHEX;``` format, including spaces)
  * URLs (use [standard percent encoding](https://www.w3schools.com/tags/ref_urlencode.asp) to encode only parameter values)
  * JavaScript (replace all characters except alphanumeric characters with the \uXXXX [Unicode encoding format](https://www.unicode.org/charts))
  * CSS (use the ```\XX``` or ```\XXXXXX``` formats to encode where needed)

  ### Sanitize tainted input
  
  If a user absolutely needs to write HTML within the application (as for a WYSIWYG editor), use an HTML sanitization   utility such as [DOMPurify](https://github.com/cure53/DOMPurify), recommended by OWASP. Remember to sanitize _after_ making any changes to the input (or sending to a library that modifies it); this may invalidate the security effort.

</details>


<details>
  <summary> Authoritative sources </summary>
  
* Java: [Secure Coding Guidelines for Java SE (Oracle)](https://www.oracle.com/java/technologies/javase/seccodeguide.html)
  
</details>
  
