# Configuration

<details>
  <summary>
    Configuration: General
  </summary>
  
  * Maintain a secure, repeatable, automatable build environment.
  * Harden 3rd-party library, dependency, and configuration management (i.e. no out-of-date or insecure components).
  * Create a secure-by-default configuration.
</details>

<details>
  <summary>
    Configuration: Build
  </summary>
  
  * Perform the application build and deployment processes in a secure and repeatable way, 
  using CI / CD automation, automated configuration management, and deployment scripts.
  * Configure compiler flags to enable all available buffer overflow protections and warnings (including stack randomization, data execution prevention). 
  Break the build if unsafe pointer, memory, format string, integer, or string operations are found.
  * Harden server configuration according to the recommendations of the application server and frameworks in use.
  * Verify that the application, configuration, and all dependencies can be re-deployed using automated deployment scripts, built from a documented and tested runbook in a reasonable time, or restored from backups in a timely fashion.
  * Verify that authorized administrators can verify the integrity of all security-relevant configurations to detect tampering.
</details>

<details>
  <summary>
    Configuration: Dependency management
  </summary>
  
  * Use a dependency checker during build or compile time to ensure all components are up to date.
  * Remove all unneeded features, documentation, samples, and configurations (e.g. sample applications, platform documentation, and default/example/test users).
  * Validate for integrity any externally hosted assets (e.g. libraries, stylesheets, or fonts) on a content delivery network (CDN) or external provider using Subresource Integrity.
  * Use third-party components only from pre-defined, vetted, and continually maintained repositories.
  * Maintain an inventory catalog of all third-party libraries in use.
  * Reduce the system's attack surface by sandboxing or encapsulating third-party libraries to expose only the required behavior into the application.
</details>

<details>
  <summary>
    Configuration: Unintended Security Disclosure
  </summary>
  
  * Configure server and framework error messages to deliver actionable, customized responses to eliminate any unintended security disclosures.
  * Disable debug modes in application servers and frameworks in production to eliminate debug features, developer consoles, and unintended security disclosures.
  * Do not expose detailed version information of system components in HTTP headers or any part of the HTTP response.
</details>

<details>
  <summary>
    Configuration: HTTP Security Headers
  </summary>
  
  * Specify the following:
    * A safe content type header character set in every HTTP response (e.g., UTF-8, ISO 8859-1).
    * That all API responses contain Content-Disposition: attachment; filename="api.json" (or other appropriate filename for the content type).
    * A content security policy (CSPv2) that helps mitigate impact for XSS attacks like HTML, DOM, JSON, and JavaScript injection vulnerabilities.
    * All responses contain X-Content-Type-Options: nosniff.
    * HTTP Strict Transport Security headers are included on all responses and for all subdomains, such as Strict-Transport-Security: max-age=15724800; includeSubdomains.
    * A suitable "Referrer-Policy" header is included, such as "no-referrer" or "same-origin".
</details>

<details>
  <summary>
    Configuration: HTTP Request Headers
  </summary>
  
  * Verify that the application server only accepts the HTTP methods in use by the application or API, including pre-flight OPTIONS.
  * Do not use the supplied Origin header for authentication or access control decisions, as the Origin header can be changed by an attacker.
  * Use a strict white-list of trusted domains for the cross-domain resource sharing (CORS) Access-Control-Allow-Origin header, and do not allow the "null" origin.
  * Authenticate that HTTP headers are added by a trusted proxy or SSO devices, such as a bearer token.
  * Accept only the HTTP methods in use by the application or API, including pre-flight OPTIONS.
</details>

