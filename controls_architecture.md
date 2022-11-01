# Architecture, Design, and Threat Modeling

<details>
  <summary>
    Architecture: Secure SDLC
  </summary>
  
  * Verify you're using a secure SDLC that bakes security practices into each development stage.
  * Use threat modeling for every major design change to identify threats, countermeasures, and risk responses.
  * Use functional security constraints in all user stories.
  * Document all trust boundaries, components, and data flows.
  * Verify the system's high-level architecture and remote services.
  * Verify that security controls are:
    * Centralized
    * Vetted
    * Simple to understand, implement, and use
  * Verify that all personnel have access to the following:
    * Secure coding checklists and guidelines
    * Security requirements
    * Security policies
</details>

<details>
  <summary>
    Architecture: Authentication
  </summary>
  
  * Use unique and least-privilege required service accounts for all nonhuman components.
  * Authenticate connections between application components.
  * Use a single vetted authentication mechanism.
  * Log authentication events.
  * Verify consistent strength of all authentication paths.
  * Avoid sharing unsynchronized state between authentication logic flows.
  * Use thread-safe functions for authentication.
</details>

<details>
  <summary>
    Architecture: Access Control
  </summary>
  
  * Never enforce access controls on the client.
  * Verify that trusted points in the system enforce access controls.
  * Enforce least privilege for all functionality and resources.
  * Use a single vetted access control mechanism.
  * Allocate permissions using role-based access control (RBAC).
  * Use feature- or attribute-based access control (FBAC or ABAC) to check authorization.
  * Avoid sharing unsynchronized state between access control logic flows.
  * Use thread-safe functions for access control.
</details>

<details>
  <summary>
    Architecture: Session Management
  </summary>
  
  * Avoid sharing unsynchronized state between session management logic flows.
  * Use thread-safe functions for session management.
</details>

<details>
  <summary>
    Architecture: Input/Output
  </summary>
  
  This is a complex topic, covered more completely [in its own page](input&output.md).
  * Verify that I/O requirements define how to process data based on content, laws, regulations, and policy.
  * Never use serialization with untrusted clients (or at least adequately protect the serialized data).
  * Verify that all inputs using a trusted and vetted service.
  * Verify that output encoding is done by or close to the interpreter that requires it.
</details>

<details>
  <summary>
    Architecture: Cryptography
  </summary>
  
  * Protect data according to their classifications. 
  * Follow established cryptographic key management standards (e.g. NIST SP 800-57).
  * Verify use of key vaults to protect key material or use alternatives to keys.
  * Verify that all key data can be easily replaced.
  * Use shared keys only for low-risk secrets and treat such secrets architecturally as in the clear.
</details>

<details>
  <summary>
    Architecture: Error Handling and Logging
  </summary>
  
  * Use a single, vetted logging approach/framework system-wide.
  * Send logs securely to a remote system for analysis and escalation.
</details>

<details>
  <summary>
    Architecture: Data Protection
  </summary>
  
  * Categorize all data processed, transmitted, or stored properly.
  * Protect sensitive data in transit and at rest as appropriate.
  * Apply each data category's protection requirements in the architecture, including:
    * Encryption
    * Integrity
    * Confidentiality
    * Secure retention
</details>

<details>
  <summary>
    Architecture: Communications
  </summary>
  
  * Encrypt communication channels between components.
  * Components must verify the authenticity of connections.
</details>

<details>
  <summary>
    Architecture (?): Supply Chain
  </summary>
  
  * Use a vetted source code control system.
  * Verify that check-ins are bound to change orders or issue tickets.
  * Enforce access control and traceability/auditing.
  * Understand the security posture of all components, including those from third parties.
  * Never use unsupported, insecure, or deprecated client-side technologies, e.g.:
    * NSAPI plugins
    * Flash
    * Shockwave
    * ActiveX
    * Silverlight
    * NACL
    * Client-side Java applets
</details>

<details>
  <summary>
    Architecture: Secure File Uploads
  </summary>
  
  * Store uploaded files outside the web root.
  * If they need to be displayed or downloaded by the system, ensure uploaded files are served:
    * By octet stream downloads
    * From an unrelated domain (e.g. cloud storage)
  * Use an appropriate content security policy (CSP). [OWASP](https://owasp.org/www-community/controls/Content_Security_Policy)
</details>

<details>
  <summary>
    Architecture: Configuration
  </summary>
  
  * Segregate components of differing trust levels with vetted controls, e.g.:
    * Firewalls
    * API gateways
    * Reverse proxies
    * Cloud-based security groups
  * 
</details>

<details>
  <summary>
    Architecture (?): Build Pipeline
  </summary>
  
  * When deploying binaries to tainted devices, use binary signatures, trusted connections, and verify endpoints.
  * Use a tool in the pipeline that automatically reports obsolete or insecure components used in the build.
  * Sandbox/isolate deployments at the network layer, especially during dangerous actions like deserialization.
  * Segregate components of different trust levels using vetted security controls.
</details>

<details>
  <summary>
    Architecture: Sample User Stories
  </summary>
  
  * As a user, I want to the application to be built using a secure development lifecycle process.
  * As a user, I want the application built using threat models.
  * As a user, I want the application's security to be verified before I use it.
  * As a user, I want the application to only use secure and authenticated communications.
  * As a user, I want the application to follow least privilege principals.
  * As a user, I want all user input to be validated to prevent injection attacks.
  * As a user, I want the application to use current cryptographic processes and secured properly.
  * As a user, I want the application to log appropriate data for records and analysis.
  * As a user, I want my sensitive data identified, classified, and protected to the appropriate levels.
  * As a user, I want the application's source code to be controlled.
  * As a user, I want the application to isolate and protect uploaded files.
  * As a user, I want the application's configuration to be controlled, consistent and protected.
</details>

