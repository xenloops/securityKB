# SQL Injection

## What?

A SQL injection attack consists of insertion or "injection" of a SQL query via the input data from the client to the application. A successful SQL injection exploit can read sensitive data from the database, modify database data (Insert/Update/Delete), execute administration operations on the database (such as shutdown the DBMS), recover the content of a given file present on the DBMS file system and in some cases issue commands to the operating system. SQL injection attacks are a type of injection attack, in which SQL commands are injected into data-plane input in order to affect the execution of predefined SQL commands.

SQL injection attacks occur when:

Unintended data enters a program from an untrusted source.
The application uses the data to dynamically construct a SQL query.

The main consequences are:

    Confidentiality: Since SQL databases generally hold sensitive data, loss of confidentiality is a frequent problem with SQL Injection vulnerabilities.
    Authentication: If poor SQL commands are used to check user names and passwords, it may be possible to connect to a system as another user with no previous knowledge of the password.
    Authorization: If authorization information is held in a SQL database, it may be possible to change this information through the successful exploitation of a SQL Injection vulnerability.
    Integrity: Just as it may be possible to read sensitive information, it is also possible to make changes or even delete this information with a SQL Injection attack.

### Example SQL Injection Vulnerability

A basic example SQL-injectible flaw in Java follows: 

```
String query = "SELECT account_balance FROM user_data WHERE user_name = "
             + request.getParameter("customerName");
try {
    Statement statement = connection.createStatement( ... );
    ResultSet results = statement.executeQuery( query );
}
```

What would happen if a user entered ```Nate' or '1'='1``` for their name and the app used their entry as is in the query?

Because the unvalidated "customerName" parameter is simply appended to the query, the example query above becomes:

```SELECT account_balance FROM user_data WHERE user_name = 'Nate' or '1'='1'```

and the query will return all the ```account_balance```s in the ```user_data``` table

an attacker can enter SQL code into that query and the application would take the attacker's code and execute it on the database.


In SQL: select id, firstname, lastname from authors

If one provided: Firstname: evil'ex and Lastname: Newman

the query string becomes:

select id, firstname, lastname from authors where firstname = 'evil'ex' and lastname ='newman'

which the database attempts to run as:

Incorrect syntax near il' as the database tried to execute evil.

A safe version of the above SQL statement could be coded in Java as:

String firstname = req.getParameter("firstname");
String lastname = req.getParameter("lastname");
// FIXME: do your own validation to detect attacks
String query = "SELECT id, firstname, lastname FROM authors WHERE firstname = ? and lastname = ?";
PreparedStatement pstmt = connection.prepareStatement( query );
pstmt.setString( 1, firstname );
pstmt.setString( 2, lastname );
try
{
    ResultSet results = pstmt.execute( );
}
