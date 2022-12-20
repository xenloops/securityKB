# General principles

* Simplicity 1: If a security feature is too inconvenient or complex to set up, users will opt for the default or a less strict configuration.
* Simplicity 2: Limit the attack surface by disabling any functionality, account, process, system, etc. that is not needed. Better yet, don't install it in the first place (e.g. do not install web, FTP, or Telnet services on employee laptops, and do not install web browsers on servers).
* Least privilege: Permit legitimate users of a system the minimal set of privileges they need to access the functions or information allowed them (e.g. if a user's job requires them to access sensitive customer information, deny their ability to print or save files or take screenshots). [OWASP](https://owasp.org/www-community/Access_Control)
* Defense in depth: Apply overlapping controls throughout a system; if an attacker bypasses one control another may prevent a breach.
* Fail securely by default (fail-safe): Design security mechanisms so that a failure follows the same path as disallowing the operation (e.g. a malfunction in Active Directory does not allow a user to log in with incorrect credentials). [OWASP](https://owasp.org/www-community/Fail_securely)
* Secure by default: 
* Compartmentalize: 
* Use standard security frameworks: Trained security people working on widely-used and well-known frameworks put in the time to research and build security in; use the available built-ins to secure your software.
* Trust no one:
  * Validate all inputs from users and external systems.
  * Authenticate users and components/systems on first use.
  * Authenticate users and components/systems before performing critical functionality.
* Document everything

# Anti-patterns
Concepts to avoid in every project.

* Security through obscurity: Attempting to hide critical information will fail. Anything important enough to hide is essential to hide well. This can include:
  * Database connection strings
  * Configuration files that reveal information about a system an attacker values
  * Credentials
  * Private keys
  * Anything else that could affect the confidentiality, integrity, or availability of your data


