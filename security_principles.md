# General principles

* Simplicity 1: If a secure feature is too complex to set up, users will opt for the default or a more lax configuration. Remember the KISS philosophy.
* Simplicity 2: Limit the attack surface by disabling (or not installing in the first place) any functionality, account, process, system, etc. that is not needed.
* Least privilege: 
* Defense in depth: 
* Failsafe by default (fail securely):
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


