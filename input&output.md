Input validation is one of the top security functions and routines that should be put into every single application that has user input capabilities. Input validation is one of the top proactive measurers to protect against the top OWASP vulnerabilities. This gap will be called out in any static code analysis every time as a High or Critical finding.
Input validation is performed to ensure only proper formed data is entering the workflow in an application/system to prevent data persisting in a database and triggering to interrupt downstream components. Input validation needs to happen as early as possible in the data flow, preferable as soon as the data is received by an external party.
Input validation is NOT the primary method of preventing the attacks listed below but is a significant contribution to reducing impacts if implemented properly. Review the references for this section to see the detailed documents and cheat sheets.
It is important to note that the concept of input validation to be ‘server side’ is obsolete in today’s cloud computing world. The term ‘trusted service layer’ is used by OWASP to mean any trusted enforcement point, regardless of location, like an API, microservice, Single page application, server side, etc…
The following are the common vulnerabilities that are handled through input validations:
• Cross-site Scripting (XSS) – This allows code to be injected into web pages, typically HTML or JavaScript, by malicious users and results in the execution of that code when it is loaded by other users to steal credentials, exfiltrate data or damage the application.
• Command/SQL Injection – This allows user-supplied input to be interpreted as part of the system command or query.
• Header Injection – This allows the manipulation of HTTP response headers that are dynamically generated based on user inputs. A common attack is the Carriage Return Line Feed (CRLF) which allows an attacker to inject HTTP response headers that control the behavior of the returned webpage. This type of injection is common with XSS or Phishing attacks.
• URL Redirection - This allows input submitted to a redirect function to be manipulated in order to redirect the victim to an alternate page or site of an attacker’s choosing. This is common in Phishing attacks.
• Directory Traversal – This allows an attacker to submit input file names containing characters representing a directory traverse to a parent (e.g. \ ). This attack attempts to access and/or execute files that are not normally accessible.
Input validation should be applied on both syntactical and semantic levels.
• Syntactical – Enforce correct syntax of structured fields. (Ex. SSN, CCD, Dates, Email…)
• Semantic – Enforce the correctness of the values in the specific business context.
o Start data before end date, numbers within expected ranges, email checks…
Whitelisting validation is the appropriate method for all input fields. This approach will force developers to clearly define what IS approved and exclude anything else. On structured input (SSN, CCD, Dates, etc) the format rules can be very strong to the exact input patterns.
When validating free-form input the primary methods of validating are:
• Normalization – Ensure canonical encoding is used across all the text and no invalid characters are present.
• Whitelisting – Unicode allows for whitelisting categories such as ‘decimal digits’ and ‘letters’.
• Individual character whitelisting - If you need to allow an apostrophe for names but not the whole character category.
