# .NET Framework Security

## Updates

* .NET (should) keep itself up-to-date
* Individual frameworks should be updated using NuGet through Visual Studio
* Third-party libraries must be updated separately -- not all use NuGet

## Security Announcements

Get notified of security issues by Watching the following Announcement repos (Watch > Custom > check Security alerts):

* [.NET Core Security Announcements](https://github.com/dotnet/announcements)
* [ASP.NET Core & Entity Framework Core Security Announcements](https://github.com/aspnet/Announcements)

## .NET Controls for the OWASP Top 10

This is a summary. See the [source](https://cheatsheetseries.owasp.org/cheatsheets/DotNet_Security_Cheat_Sheet.html) for example code.

### Broken Access Control

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

#### Anti-patterns

**Do not:**
* Roll your own authentication or session management code
* Tell user whether the entered username exists on Logon, Registration, or Password reset
* 



<details>
  <summary> A02 Cryptographic Failures </summary>

* Use a strong hashing algorithm such as AES-512:
  * General hashing: ```System.Security.Cryptography.SHA512```
  * Password hashing: ```Microsoft.AspNetCore.Cryptography.KeyDerivation.Pbkdf2```
* When hashing non-unique inputs such as passwords, salt the value before hashing
* 
* Make sure the application easily supports a future change of cryptographic algorithms

Anti-patterns

* Never, ever write your own cryptographic functions
* Where possible, avoid writing any cryptographic code -- instead use pre-existing secrets management solutions
* If that's not possible, use a trusted and well-known library rather than using those built into .NET (it's easy to make cryptographic errors with them)
* 

</details>




<details>
  <summary>  </summary>

</details>












## Sources 

* [OWASP DotNet Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DotNet_Security_Cheat_Sheet.html)
