# Access Control (Authorization)

Authorization is allowing access to resources to only those permitted to use them. 

<details>
  <summary> General </summary>
  
* Ensure that users accessing resources hold valid credentials to do so.
* Associate users with a well-defined set of roles and privileges.
* Protect role and permission metadata from replay or tampering.
* Enforce access control rules on a trusted service layer.
* Ensure users can only access resources for which they possess specific authorization.
* Deny access by default; start new users with no access.
* Ensure that all user and data attributes and policy information used by access controls cannot be manipulated by users unless specifically authorized.
* Verify that access controls fail securely, including when an exception occurs.
* Use MFA at least for administrative interfaces.
* Disable directory browsing ability.
* Disable viewing of directory/file metadata.
* Enforce additional authorization for lower value systems (e.g. step-up or adaptive authorization).
* Enforce separation of duties for high-value functionality.
</details>

<details>
  <summary> Operation Level </summary>
  
* Protect sensitive data and APIs against direct object attacks
* Use a strong anti-CSRF mechanism (preferably built into the framework) to protect authenticated functionality.
</details>


<details>
  <summary> Privileged Access </summary>
  
* Grant temporary permissions to perform privileged tasks. This prevents unauthorized users from gaining access after elevated permissions have expired. Grant access only when users need it, for as short a duration as necessary.
</details>

<details>
  <summary> Example security user stories </summary>
  
* As a user, I want the application to have access controls in place to ensure I can only access what I need to through least-privilege principals.
* As a user, I want APIs to be protected against direct access attack.
* As a user, I want the application's administrative features to use multi-factor authentication.
</details>
