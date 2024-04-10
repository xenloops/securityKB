# .NET Framework Security

## Updates

* .NET (should) keep itself up-to-date
* Individual frameworks should be updated using NuGet through Visual Studio
* Third-party libraries must be updated separately -- not all use NuGet

## Security announcements

Get notified of security issues by Watching the following Announcement repos (Watch > Custom > check Security alerts):

* [.NET Core Security Announcements](https://github.com/dotnet/announcements)
* [ASP.NET Core & Entity Framework Core Security Announcements](https://github.com/aspnet/Announcements)

## General .NET security controls

* Type-safe code prevents arbitrary memory access
* 

### Anti-patterns

**Do not:**
* Use Code Access Security (CAS), which is deprecated
* 

## .NET controls for the OWASP Top 10

This is a summary. See the [source](https://cheatsheetseries.owasp.org/cheatsheets/DotNet_Security_Cheat_Sheet.html) for example code.

<details>
  <summary> A01 Broken Access Control </summary>

* Set the ```CookieHttpOnly``` flag to protect cookies from client-side scripts
* Set ```ExpireTimeSpan``` to a reasonable session timeout (check for company policy value)
* Set ```SlidingExpiration``` to ```false```
* Set the ```requireSSL``` flag in the config transforms to only send encrypted cookies
* Throttle requests using ```AllowXRequestsEveryXSecondsAttribute``` to thwart brute force attacks during these procdedures:
  * User registration
  * Logon
  * Password reset
* For APIs, authorize users on all externally facing endpoints using ```[Authorize]```  or ```System.Web.Security.Roles.IsUserInRole()```
* Always ensure the logged-in user is intended to have access to a requested resource

## Anti-patterns

**Do not:**
* Write custom authentication or session management code
* Give user feedback on whether the entered username exists on Logon, Registration, or Password reset

</details>


<details>
  <summary> A02 Cryptographic Failures </summary>

## General encryption
* Use a strong hashing algorithm such as AES-512:
  * General hashing: ```System.Security.Cryptography.SHA512```
  * Password hashing: ```Microsoft.AspNetCore.Cryptography.KeyDerivation.Pbkdf2```
* When hashing non-unique inputs such as passwords, salt the value before hashing
* Protect encryption keys more than any other asset (see the [OWASP Key Management Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Key_Management_Cheat_Sheet.html#storage))
* Use TLS 1.2 or later for an entire web site (se the [OWASP Transport Layer Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Security_Cheat_Sheet.html))
* Check a web site's configuration using [SSL Test](https://www.ssllabs.com/ssltest/) or [TestSSL](https://testssl.sh/)
* Ensure headers do not disclose information about the web app
* Make sure the application easily supports a future change of cryptographic algorithms
* Have a cryptography expert review design and code, as even the most trivial error can severely weaken encryption

## Anti-patterns

**Do not:**
* Write custom cryptographic functions
* Write any cryptographic code if possible -- instead use pre-existing secrets management solutions. If that's not possible, use a trusted and well-known library rather than using .NET built-ins (it's easy to make cryptographic errors with them)

## Encryption at rest (local storage)

* Use the [Windows Data Protection API (DPAPI)](https://docs.microsoft.com/en-us/dotnet/standard/security/how-to-use-data-protection) for secure local storage
* Follow the algorithm guidance in the [OWASP Cryptographic Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html#algorithms)

</details>

<details>
  <summary> A03 Injection </summary>

## SQL Injection

* Use an object relational mapper (ORM) or stored procedures
* Use parameterized queries where a direct SQL query must be used
* See the [OWASP Query Parameterization Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Query_Parameterization_Cheat_Sheet.html)
* Practice Least Privilege: connect to the database using an account with the smallest set of permissions required to do its job

## Anti-patterns

**Do not:**
* Concatenate strings anywhere and execute them against the database (known as dynamic SQL)
* It is possible to accidentally write dynamic SQL with ORMs or stored procedures, so check everything
* Connect to the database using the database administrator account

## OS Injection

* Use ```System.Diagnostics.Process.Start``` to call underlying OS functions
* See the [OWASP OS Command Injection Defense Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/OS_Command_Injection_Defense_Cheat_Sheet.html)
* Use allowlist validation on all user-controlled input to prevent improperly formed data from entering the system (see the [OWASP Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html))
* Try to accept only simple alphanumeric characters as user input
* Look at alternatives to passing raw untrusted values via command-line parameters (e.g. encoding using Base64 and decoding in the receiving application)

## Anti-patterns

**Do not:**
* Assume sanitizing special characters without actually removing them is sufficient; combinations of ```\```, ```'```, and ```@``` may have an unexpected impact on sanitization
* Rely on methods without a security guarantee (e.g. ``` ProcessStartInfo.ArgumentList``` warns that it is not safe for untrusted input)

## LDAP injection

* Some characters used in Distinguished Names must be escaped with the backslash
* See the [OWASP LDAP Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)

</details>


<details>
  <summary> A05 Security Misconfiguration </summary>

## Debug and stack traces

* Turn off debug and traces in production using web.config transforms
* Redirect requests made over HTTP to HTTPS

## Anti-patterns

**Do not:**
* Use default passwords

## Cross-Site Request Forgery (CSRF)

See the [OWASP Cross-Site Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html)

### For .NET Framework:
* Send the anti-forgery token with every POST/PUT request
* Then validate the token at the controller level ( or method level if necessary)
* Remove the token completely to invalidate on logout

### For .NET Core 2.0 or later:
* Automatically generate and verify the antiforgery token (see [Microsoft's instructions](https://docs.microsoft.com/en-us/aspnet/core/security/anti-request-forgery?view=aspnetcore-7.0#aspnet-core-antiforgery-configuration))

### For .NET Core/Framework with AJAX:
* Attach the anti-forgery token to AJAX requests

## Anti-patterns

**Do not:**
* Send sensitive data without validating Anti-Forgery-Tokens

</details>


<details>
  <summary> A06 Vulnerable and Outdated Components </summary>

* Keep the .NET Framework updated with the latest patches
* Keep NuGet packages used updated
* Use a Software Composition Analysis tool in the CI/CD pipeline (e.g.  [OWASP Dependency Check](https://owasp.org/www-project-dependency-check)

</details>

<details>
  <summary> A07 Identification and Authentication Failures </summary>

* Use [ASP.NET Core Identity](https://docs.microsoft.com/en-us/aspnet/core/security/authentication/identity?view=aspnetcore-2.2&), which is well configured by default
* Use secure salted password hashes
* Set a secure password policy 
* Set a secure cookie policy (e.g. ```HttpOnly```, expiration)
* Use ```WindowsPrincipal.IsInRole()``` to authenticate a user for specific roles
* 

</details>

<details>
  <summary> A08 Software and Data Integrity Failures </summary>

* Digitally sign assemblies and executable files
* Use Nuget package signing
* Review code and configuration changes to avoid malicious code or dependencies being introduced
* Perform integrity checks or validate digital signatures on serialized objects received from the network
* Use .NET in-box serializers that can handle untrusted data safely, e.g.:
  * ```XmlSerializer``` and ```DataContractSerializer``` to serialize object graphs into and from XML (***not*** ```NetDataContractSerializer```)
  * ```BinaryReader``` and ```BinaryWriter``` for XML and JSON
  * ```System.Text.Json``` APIs to serialize object graphs into JSON

## Anti-patterns

**Do not:**
* Send unsigned or unencrypted serialized objects over the network
* Use the ```BinaryFormatter``` type for data processing

</details>

<details>
  <summary> A09 Security Logging and Monitoring Failures </summary>

* Log all login, access control, and server-side input validation failures with sufficient user context to identify suspicious or malicious accounts
* Establish effective monitoring and alerting
* Log the stack trace, error message, and user ID that caused the error
* See the [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
* Use [Application Insights](https://docs.microsoft.com/en-us/azure/azure-monitor/app/asp-net-core) to add monitoring capabilities

## Anti-patterns

**Do not:**

* Log sensitive data (e.g. passwords)
* Log generic error messages (e.g. ```Log.Error("Error was thrown");```)

</details>

<details>
  <summary> A10 Server-Side Request Forgery (SSRF) </summary>

* Validate and sanitize all user-controlled input before using it in a request
* Use an allowlist of allowed protocols and domains
* Use ```IPAddress.TryParse()``` and ```Uri.CheckHostName()``` to check IP addresses and domain names
* See the [OWASP Server-Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html)


## Anti-patterns

**Do not:**

* Follow HTTP redirects
* Forward raw HTTP responses to the user


</details>



## Sources

* [OWASP DotNet Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DotNet_Security_Cheat_Sheet.html)
* [.NET Key Security Concepts](https://learn.microsoft.com/en-us/dotnet/standard/security/key-security-concepts)
* [.NET Role-Based Security](https://learn.microsoft.com/en-us/dotnet/standard/security/role-based-security)
* 
