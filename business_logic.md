# Business Logic
Business logic security must be designed into a system and cannot be added using web application firewalls or other controls after the fact. 
Threat modeling during the design sprints assists greatly in this process.

<details>
  <summary> General </summary>
  
* Ensure business logic flows are sequential, processed in order, and cannot be bypassed.
* Include limits in Business logic to detect and prevent automated attacks.
* For high value business logic flows, create abuse cases.
* Protect against major kinds of attacks, including:
  * Spoofing
  * Tampering
  * Repudiation
  * Information disclosure
  * Denial of service
  * Elevation of privilege
* Process business logic flows for the same user in sequential step order and without allowing skipped steps.
* Process business logic flows with all steps being processed in realistic human time, i.e. transactions are not submitted too quickly.
* Include appropriate limits for specific business actions or transactions appropriately enforced on a per-user basis.
* Use anti-automation controls sufficient to detect and protect against data exfiltration, excessive business logic requests, excessive file uploads, or denial of service attacks.
* Use business logic limits or validation to protect against likely business risks or threats, identified using threat modeling or similar methodologies.
* Test for "time of check to time of use" (TOCTOU) issues or other race conditions for sensitive operations.
* Monitor for unusual events or activity from a business logic perspective (e.g. attempts to perform actions out of order or actions which a legitimate user would never attempt).
* Design in configurable alerting for when automated attacks or unusual activity is detected.
</details>

<details>
  <summary> Example security user stories </summary>
  
* As a user, I want the application to ensure the business logic is processed, monitored, and controlled within its expected use.
</details>
