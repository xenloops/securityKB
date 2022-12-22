# Code vulnerabilities

Many vulnerabilities can be remediated where they begin -- in code. 

<details>
  <summary> SQL injection (SQLi) </summary>
  
  **Problem:** A SQL injection attack consists of insertion or "injection" of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data, execute administration operations on the database, recover the content of a given file present on the DBMS file system, and in some cases issue commands to the operating system. [OWASP](https://owasp.org/www-community/attacks/SQL_Injection)

  **Solutions:** Use parameterized queries, use stored procedures, validate input, or escape tainted input. [OWASP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)

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
  <summary> Authoritative sources </summary>
  
* Java: [Secure Coding Guidelines for Java SE (Oracle)](https://www.oracle.com/java/technologies/javase/seccodeguide.html)
  
</details>
  
