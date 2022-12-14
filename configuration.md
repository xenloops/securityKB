# Configuration security

<details>
  <summary> General </summary>

  Ensure that the configuration provides:
  
* A secure, repeatable, and automatable build environment.
* Hardened 3rd party library, dependency, and configuration management such that out-of-date or insecure components are blocked from inclusion in the application.
* A secure-by-default configuration, such that administrators and users have to weaken the default security posture.
</details>

<details>
  <summary> Build pipeline </summary>
  
Build pipelines provide the ability for repeatable security. When an insecurity is discovered it should be resolved in the source code, build, or deployment scripts and tested automatically.
  
* Perform build and deployment processes in a secure and repeatable way by using CI/CD automation, automated configuration management, and automated deployment scripts.
* Enable all compiler flags that provide buffer overflow protections and warnings (including stack randomization 
and data execution prevention) and break the build if an unsafe pointer, memory, format string, integer, 
or string operation is found.
* Harden the server configuration according to the recommendations of application server and frameworks in use.
* Use automated deployment scripts to ensure the application, configuration, and all dependencies can be re-deployed, 
built from a documented and tested runbook in a reasonable time, or restored from backups in a timely fashion.
* Allow authorized administrators to verify the integrity of all security-relevant configurations to detect tampering.
* When deploying binaries to tainted devices, use binary signatures, trusted connections, and verify endpoints.
* Sandbox/isolate deployments at the network layer, especially during dangerous actions like deserialization.
* Segregate components of different trust levels using vetted security controls.
</details>

<details>
  <summary> Dependencies </summary>
  
* Use a dependency checker during build or compile time to verify that all components are up-to-date.
* Remove all unneeded features, documentation, samples, and configurations (such as sample applications, platform documentation, and default or example users).
* If application assets (such as JavaScript libraries, CSS stylesheets, or web fonts) are hosted externally on a content delivery network 
(CDN) or external provider, use Subresource Integrity (SRI) to validate the integrity of the asset.
* Ensure that third-party components come from pre-defined, trusted and continually maintained repositories.
* Maintain an inventory catalog of all third-party libraries in use.
* Reduce attack surface by sandboxing or encapsulating third-party libraries to expose only the required behavior into the application.
</details>

<details>
  <summary> Unintended security disclosure </summary>
  
* Configure web/application server and framework error messages are configured to deliver user actionable, customized responses to eliminate any unintended security disclosures.
* Disable web/application server and framework debug modes in production to eliminate debug features, developer consoles, 
and unintended security disclosures.
* Avoid exposing detailed version information of system components in HTTP headers or any part of the HTTP response.
</details>

<details>
  <summary> HTTP security headers </summary>
  
* Use a content type header specifying a safe character set in every HTTP response (e.g., UTF-8, ISO 8859-1).
* Use Content-Disposition: attachment; filename="api.json" in all API responses (or other appropriate filenames for the content type).
* Use a content security policy (CSPv2) that mitigates XSS attacks (e.g. HTML, DOM, JSON, and JavaScript injection vulnerabilities).
* Use X-Content-Type-Options: nosniff in all responses.
* Include HTTP Strict Transport Security headers on all responses and for all subdomains, such as Strict-Transport-Security: 
max-age=15724800; includeSubdomains.
* Include a suitable "Referrer-Policy" header, such as "no-referrer" or "same-origin".
</details>

<details>
  <summary> Validate HTTP request header </summary>
  
* Ensure the application server only accepts the HTTP methods in use by the application or API, including pre-flight OPTIONS.
* Do not use the supplied Origin header for authentication or access control decisions, as the Origin header can easily be 
changed by an attacker.
* Use a strict whitelist of trusted domains for the cross-domain resource sharing (CORS) Access-Control-Allow-Origin header 
to match against, and do not support the "null" origin.
* Authenticate HTTP headers added by a trusted proxy or SSO devices, such as a bearer token, by the application.
</details>

<details>
  <summary> Example security user stories </summary>
  
* As a user, I want the application to be built in a secure, repeatable, and automated way.
* As a user, I want the application to maintain a third-party library dependency management process so no security issues are introduced.
* As a user, I want the application to secure the configurations to prevent unauthorized access, modification, or other activities that could expose my data.
</details>
