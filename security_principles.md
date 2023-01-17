# General principles

* Educate all users on security best practices and the organization's security policies, as appropriate to their job duties.
  * Avoid overwhelming users with too many communications or trainings. 
  * Keep trainings short and specific to an issue (e.g. 5-10 minute read/video on SQL Injection). 
  * Make the training materials searchable (e.g. if creating videos, publish their transcripts as well).
* Simplicity 1: If a security feature is too inconvenient or complex to set up, users will opt for the default or a less strict configuration.
* Simplicity 2: Limit the attack surface by disabling any functionality, account, process, system, etc. that is not needed. Better yet, don't install it in the first place (e.g. do not install web, FTP, or Telnet services on employee laptops, and do not install web browsers on servers).
* Least privilege: Permit legitimate users of a system the minimal set of privileges they need to access the functions or information allowed them (e.g. if a user's job requires them to access sensitive customer information, deny their ability to print or save files or take screenshots). [OWASP](https://owasp.org/www-community/Access_Control)
* Separation of privilege 1: Limit what each user can access or which actions they can perform for sensitive data or functions.
* Separation of privilege 2: For extremely sensitive functions or information, require at least two authenticators (e.g. safe-deposit boxes and missile launch systems require two keys). [CISA](https://www.cisa.gov/uscert/bsi/articles/knowledge/principles/separation-of-privilege)
* Defense in depth: Apply overlapping controls throughout a system; if an attacker bypasses one control another may prevent a breach. [NIST](https://csrc.nist.gov/glossary/term/defense_in_depth) [CISA](https://www.cisa.gov/uscert/bsi/articles/knowledge/principles/defense-in-depth)
* Secure by default: Where possible, design default settings to be secure.
* Fail securely (fail-safe): Design security mechanisms so that a failure follows the same path as disallowing the operation (e.g. a malfunction in Active Directory does not allow a user to log in with incorrect credentials). [OWASP](https://owasp.org/www-community/Fail_securely)
* Use standard security frameworks: Trained security people working on widely-used and well-known frameworks put in the time to research and build security in; use the available built-ins to secure your software.
* Trust no one:
  * Validate all inputs from users and external systems.
  * Authenticate users and components/systems on first use.
  * Authenticate users and components/systems before performing critical functionality.
* Document everything: Systems designed without thorough documentation are difficult to maintain. Most important are the security related functions of a system, which must be updated as problems are discovered.

# Anti-patterns
Concepts to avoid in every project. 

* Security through obscurity: Attempting to hide critical information will fail. Anything important enough to hide is essential to hide well. This can include:
  * Database connection strings
  * Configuration files that reveal information about a system an attacker values
  * Credentials
  * Private keys
  * Anything else that could affect the confidentiality, integrity, or availability of your data
* Administer a system from another system with lower security requirements (e.g. an admin interface accessible from a remote computer that can also browse the internet or receive email). [NCSC](https://www.ncsc.gov.uk/whitepaper/security-architecture-anti-patterns)
* Management bypass: A shortcut exists that bypasses layered defenses in the network (e.g. direct admin login to a server that need not go through a WAF). [NCSC](https://www.ncsc.gov.uk/whitepaper/security-architecture-anti-patterns)
* Back-to-back firewalls: At best, doubling up on firewalls in series unnecessarily increases cost. At worst, it adds to administrative complexity and gives a false sense of extra security. There must be a very good technical reason for using this anti-pattern, such as enforcing a contract between two entities connecting to each other. [NCSC](https://www.ncsc.gov.uk/whitepaper/security-architecture-anti-patterns)
* Allow a third party uncontrolled and unobserved access (e.g. contracting a vendor to administer their device in your network without placing tight controls on what they can access). [NCSC](https://www.ncsc.gov.uk/whitepaper/security-architecture-anti-patterns)
* Use unpatchable systems (e.g. an unrealistic 100%-uptime requirement leaves no time for updates and encourages deferring security patches). [NCSC](https://www.ncsc.gov.uk/whitepaper/security-architecture-anti-patterns)

