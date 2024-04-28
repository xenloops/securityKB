<details>
  <summary> The tl;dr </summary>
  
* Disable network (TCP) access and require all access over a local socket file or named pipe.
* Configure the database to only bind on localhost.
* Restrict access to the network port to specific hosts with firewall rules.
* Place the database server in a separate subnet isolated from the application server.
* For access from an untrusted system (e.g. thick clients) always connect to the backend through an API that enforces appropriate access control. Never make direct connections.
* Implement [TLS encryption](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html):
  * Configure the database to only allow encrypted connections.
  * Install a trusted digital certificate on the server.
  * Force clients to connect using TLSv1.2+ with modern ciphers (e.g, AES-GCM or ChaCha20).
  * Force clients to verify that the digital certificate is correct.
* Configure Secure Authentication:
  * Always require authentication, including connections from the local server.
  * Use strong and unique passwords for each application or service.
  * Configure access with the [minimum permissions required](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html#creating-secure-permissions).
  * For SQL Server, consider the use of [Windows or Integrated Authentication](https://docs.microsoft.com/en-us/dotnet/framework/data/adonet/sql/authentication-in-sql-server).
  * Follow standard account management processes:
    * Review accounts to ensure they are still required.
    * Review permissions regularly.
    * Remove user accounts when an application is decommissioned.
    * Change system passwords when staff leave, or there is reason to believe that they have been compromised.
* Store database credentials securely:
  * Never store credentials in the application source code.
  * Store credentials in a secrets vault or a configuration file that:
    * Is outside of the web root.
    * Can be read only by the required user(s).
    * Is not checked into source code repositories.
  * Where possible store credentials encrypted or otherwise protected using built-in functionality.
* Configure secure user account permissions
  * Employ the principle of least privilege on a granular level as needed.
  * Do not use built-in root, sa or SYS accounts.
  * Do not grant accounts administrative rights over the database instance.
  * Ensure accounts can only connect from allowed hosts (e.g. localhost or the application server).
  * The account should only access the specific database(s) it needs.
  * Use separate databases and accounts for Dev, UAT, and Prod environments.
  * Grant only required permissions on the databases; most applications only need SELECT, UPDATE and DELETE permissions.
  * The account should not be the owner of the database.
  * Avoid using database links or linked servers. Where they are required, use an account that has been granted access to only the minimum databases, tables, and system privileges required.
  * For security-critical applications, apply permissions at more granular levels:
    * Table-level permissions.
    * Column-level permissions.
    * Row-level permissions.
    * Block access to the underlying tables and require access through restricted views.
* Hardening database configurations
  * Harden the underlying operating system by using a secure baseline such as the [Microsoft Security Baselines](https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-security-baselines).
  * Harden the database application:
    * Install required security updates and patches.
    * Configure database services to run under a low privileged user account.
    * Remove default accounts and databases.
    * Store transaction logs on a separate disk from the main database files.
    * Configure regular backups of the database. Ensure that the backups are protected with appropriate permissions and encrypted.

</details>



Database security is essential to the confidentiality, integrity, and availability of data. Understanding the fundamentals of securing databases is crucial to protect sensitive information and mitigate potential risks effectively. The main security controls protecting data are:

* Authentication
* Access control/authorization
* Encryption
* Logging and monitoring
* Audit
* Backup and recovery
* Continuous education

Authentication and authorization mechanisms play a vital role in database security. Enforce strong authentication practices, such as complex passwords and/or multi-factor authentication (MFA), to verify users' identities. 

Access control is a cornerstone of database security; authorization ensures that the correct users and systems can access only the data and functionality they are authorized for. Database Administrators (DBAs) must implement strict access controls by defining roles, permissions, and privileges based on the security Principle of Least Privilege. This means granting users and applications only the minimum level of access necessary to perform their functions.

Encryption is another fundamental control for securing data. Encryption mechanisms should be used to protect data both at rest (on disk) and in transit (over the network). [Transparent Data Encryption (TDE)](https://en.wikipedia.org/wiki/Transparent_data_encryption) encrypts data files to prevent unauthorized access to data at rest. Using [Transport Layer Security (TLS)](https://en.wikipedia.org/wiki/Transport_Layer_Security) encrypts data moving between the database server and client applications, safeguarding data from interception and/or manipulation by attackers.

Regular monitoring and auditing are essential for detecting and responding to security threats promptly. DBAs should implement [Database Activity Monitoring (DAM)](https://en.wikipedia.org/wiki/Database_activity_monitoring) tools to track database access, queries, and changes to data. Auditing database activities helps maintain accountability, identify suspicious behavior, and comply with regulatory requirements by generating audit trails and access logs.

Backup and recovery procedures are critical components of database security. DBAs should regularly back up database files and store backups securely to ensure data security and availability in case of disasters, data corruption, or ransomware attacks. Establishing comprehensive disaster recovery plans with defined recovery objectives and procedures enables quick restoration of databases in the event of data loss or system failures.

Lastly, DBAs should stay informed about the latest security vulnerabilities, patches, and best practices in database security. Regularly updating the database system and related software helps mitigate known vulnerabilities and strengthens overall security posture.

Securing databases requires a comprehensive approach that includes authentication, authorization/access control, encryption, logging and monitoring, auditing, backup and recovery, and training. By mastering these fundamentals, DBAs can effectively protect databases and sensitive data from security threats and ensure the integrity and availability of critical information assets.

Some useful resources for securely administering databases:

* [OWASP Database Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Database_Security_Cheat_Sheet.html#database-configuration-and-hardening)
* OWASP Proactive Controls:
  * [C3: Secure Database Access](https://owasp.org/www-project-proactive-controls/v3/en/c3-secure-database) - [Microsoft article for SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/getting-started-with-database-engine-permissions)
  * [C6: Implement Digital Identity](https://owasp.org/www-project-proactive-controls/v3/en/c6-digital-identity.html)
  * [C7: Enforce Access Controls](https://owasp.org/www-project-proactive-controls/v3/en/c7-enforce-access-controls.html) - Microsoft articles for SQL Server: [Getting started](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/getting-started-with-database-engine-permissions) - [Effective permissions](https://learn.microsoft.com/en-us/sql/relational-databases/security/authentication-access/determining-effective-database-engine-permissions) - [SQL Server 2017 permissions (PDF)](https://raw.githubusercontent.com/Microsoft/sql-server-samples/master/samples/features/security/permissions-posters/Microsoft_SQL_Server_2017_and_Azure_SQL_Database_permissions_infographic.pdf)
  * [C8: Protect Data Everywhere](https://owasp.org/www-project-proactive-controls/v3/en/c8-protect-data-everywhere.html) - [Microsoft article for SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/security/encryption/sql-server-encryption)
  * [C9: Implement Security Logging and Monitoring](https://owasp.org/www-project-proactive-controls/v3/en/c9-security-logging.html) - [Microsoft article for SQL Server](https://learn.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-database-engine)
* [Microsoft: SQL Server security best practices](https://learn.microsoft.com/en-us/sql/relational-databases/security/sql-server-security-best-practices?view=sql-server-ver16)

 
