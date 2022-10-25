
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
  
Info
</details>

<details>
  <summary>
    Next
  </summary>
  
Info
</details>
