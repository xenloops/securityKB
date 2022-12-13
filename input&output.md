# Input and Output

_Also see the [Tainted Input](tainted_input.md) section._

User controlled input (a.k.a. **taint** or **untrusted input**) is one of the top security concerns that must be addressed in every application that has user input capabilities. It is the primary cause of several vulnerabilities that consistently appear in the OWASP Top 10 vunerability lists, like Command Injection and Cross-Site Scripting (XSS). 

Input validation is the top proactive measure to protect against untrusted input. Input validation is performed to ensure only properly formed data is entering the workflow in an application/system to prevent data persisting in a database and tainting downstream components. Input validation needs to happen as early as possible in the data flow, preferably as soon as data are received from an external party.

Static code analysis (SAST) and dynamic analysis (DAST) tools will call this out as a Critical or High finding. 

Input validation is not the only method necessary to prevent attacks such as those listed below, but is a significant contribution to reducing risk when implemented properly. Note that the concept of input validation to be 'server side' is obsolete in today’s cloud computing world. The term 'trusted service layer' is used by OWASP to mean any trusted enforcement point, regardless of location (e.g. an API, microservice, single page application, or on a server).

The following are the common vulnerabilities that are mitigated through input validation:

  * **Cross-site Scripting (XSS)** allows code to be injected into web pages (typically HTML or JavaScript) and is executed when loaded by other users to steal credentials, exfiltrate data, or damage the application.
  * **Command/SQL Injection** allows tainted input to be interpreted as part of a system command or database query.
  * **Header Injection** allows the manipulation of HTTP response headers that are dynamically generated based on user input. For example, in the Carriage Return Line Feed (CRLF) attack an attacker injects HTTP response headers that control the behavior of the returned webpage. This type of injection is common with XSS or phishing attacks.
  * **URL Redirection** allows input submitted to a redirect function to be manipulated to redirect the victim to an attacker's site. This is common in phishing attacks.
  * **Directory Traversal** allows an attacker to submit input file names containing characters representing a directory that traverses to a parent. This attack attempts to access files and/or execute binaries that are not normally accessible.

Input validation should be applied on both syntactical and semantic levels.

  * **Syntactical** controls enforce correct syntax of structured fields (e.g. SSN, CCD, dates, email).
  * **Semantic** controls enforce the correctness of the values in the specific business context (e.g. start date before end date, numbers within expected ranges, email address format).

For free-form input, the primary methods of validation are:

  * **Normalization** ensures canonical encoding is used across all input and no invalid characters are present.
  * **Whitelisting** ensures only specified characters are allowed. 
    * Unicode allows for whitelisting categories such as 'decimal digits' and 'letters'.
    * Whitelisting should be context-driven (e.g. allow an apostrophe for names, but not for all text entry fields).
    * Whitelisting validation is the appropriate method for all input fields. This approach will force developers to clearly define what is allowed and exclude anything else. On structured input (SSN, CCD, Dates, etc) the format rules should be precisely defined.
    * "Blacklisting" should be avoided, as a list of disallowed characters would need to be maintained when new attacks or character sets are devised.


