# Malicious Code


<details>
  <summary>
    Malicious Code: General
  </summary>
  
  * Follow these high-level requirements:
    * Handle malicious activity securely and properly to not affect the rest of the application.
    * Verify that source code does not contain:
      * Time-bombs or other time based attacks.
      * Functionality to 'phone home' to unauthorized destinations.
      * Back doors, Easter eggs, rootkits, or unauthorized code, especially code controlled by an attacker.
</details>

<details>
  <summary>
    Malicious Code: Code Integrity
  </summary>
  
  * Use a code analysis tool that can detect potentially malicious code.
  * Verify that the application does not ask for unnecessary or excessive permissions to privacy related features or sensors.
  * Verify that the application source code and third party libraries do not contain:
    * Back doors, such as hard-coded or undocumented accounts or keys, code obfuscation, undocumented binary blobs, rootkits, anti-debugging, or 
    insecure debugging features.
    * Out of date, insecure, or hidden functionality that could be used maliciously if discovered.
    * Time bombs by searching for date and time related functions.
    * Malicious code, such as salami attacks, logic bypasses, or logic bombs.
    * Easter eggs or any other potentially unwanted functionality.
</details>

<details>
  <summary>
    Malicious Code: Application Deployment
  </summary>
  
  * If the application has an auto-update feature, obtain digitally signed updates over secure channels. 
  * Validate the digital signature of the update before installing or executing the update.
  * Employ integrity protections, such as code signing or sub-resource integrity. 
  * Do not load or execute code from untrusted sources, such as loading includes, modules, plugins, code, or libraries from untrusted sources.
  * Protect against sub-domain takeovers or expired domains if the system relies on DNS entries or DNS sub-domains.
</details>

<details>
  <summary>
    Malicious Code: Example security user stories
  </summary>
  
  * As a user, I want the application not to contain malicious capabilities in its source code and third-party libraries.
  * As a user, I want the application to have its source code and components analyzed for malicious capabilities before I use it.
</details>
